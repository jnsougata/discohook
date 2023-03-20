import aiohttp
from .command import *
from .modal import Modal
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import AppCmdType
from .user import ClientUser
from .permissions import Permissions
from .command import ApplicationCommand
from .view import Button, SelectMenu
from fastapi.requests import Request
from .dash import dashboard
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Union, Callable


async def delete_cmd(request: Request, command_id: str):
    resp = await request.app.delete_command(command_id)
    if resp.status == 204:
        return JSONResponse({"success": True}, status_code=resp.status)
    return JSONResponse({"error": "Failed to delete command"}, status_code=resp.status)


async def sync(request: Request, secret: str = None):
    if secret == request.app.token:
        return JSONResponse(await request.app.sync())
    return JSONResponse({"error": "Unauthorized"}, status_code=401)


class Client(FastAPI):
    """
    The main client class for Discohook.

    Parameters
    ----------
    application_id: Union[int, str]
        The application ID of your bot.
    public_key: str
        The public key of your bot.
    token: str
        The bot token of your bot.
    route: str
        The route to listen for interactions on. Defaults to `/interactions`.
    **kwargs
        Any additional kwargs to pass to the FastAPI instance.

    """
    def __init__(
        self,
        application_id: Union[int, str],
        public_key: str,
        token: str,
        *,
        route: str = "/interactions",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.redoc_url = None
        self.docs_url = None
        self.token = token
        self.public_key = public_key
        self.application_id = application_id
        self.session: Optional[aiohttp.ClientSession] = aiohttp.ClientSession(
            base_url="https://discord.com",
            headers={"Authorization": f"Bot {self.token}", "Content-Type": "application/json"}
        )
        self.active_components: Optional[Dict[str, Union[Button, Modal, SelectMenu]]] = {}
        self._sync_queue: List[ApplicationCommand] = []
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self.cached_inter_tokens: Dict[str, str] = {}
        self.add_route(route, handler, methods=["POST"], include_in_schema=False)
        self.add_api_route(
            "/dh/sync/{secret}", sync, methods=["GET"], include_in_schema=False
        )
        self.add_api_route(
            "/dh/dash/{secret}", dashboard, methods=["GET"], include_in_schema=False
        )
        self.add_api_route(
            "/dh/delete/{command_id}", delete_cmd, methods=["GET"], include_in_schema=False
        )
        self._global_error_handler: Optional[Callable] = None

    def load_component(self, component: Union[Button, Modal, SelectMenu]):
        """
        Load a component into the client.

        Do not use this method unless you know what you are doing.

        Parameters
        ----------
        component: Union[Button, Modal, SelectMenu]
            The component to load into the client.
        """
        self.active_components[component.custom_id] = component

    def store_inter_token(self, interaction_id: str, token: str):
        self.cached_inter_tokens[interaction_id] = token

    def command(
        self,
        name: str,
        description: Optional[str] = None,
        *,
        id: str = None,  # noqa
        options: Optional[List[Option]] = None,
        permissions: Optional[List[Permissions]] = None,
        dm_access: bool = True,
        category: AppCmdType = AppCmdType.slash,
    ):
        """
        A decorator to register a command.

        Parameters
        ----------
        name: str
            The name of the command.
        description: Optional[str]
            The description of the command. Does not apply to user & message commands.
        id: Optional[str]
            The ID of the command. If not provided, the command will not be synced.
        options: Optional[List[Option]]
            The options of the command. Does not apply to user & message commands.
        permissions: Optional[List[Permissions]]
            The default permissions of the command.
        dm_access: bool
            Whether the command can be used in DMs. Defaults to True.
        category: AppCmdType
            The category of the command. Defaults to slash commands.
        """
        command = ApplicationCommand(
            name=name,
            description=description,
            options=options,
            permissions=permissions,
            dm_access=dm_access,
            category=category,
            id=id,
        )

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*_, **__):
                if asyncio.iscoroutinefunction(coro):
                    command._callback = coro
                    if command.id:
                        self.application_commands[command.id] = command
                    self._sync_queue.append(command)
                    return command

            return wrapper()

        return decorator

    def add_commands(self, *commands: ApplicationCommand):
        """
        Add commands to the client.

        Parameters
        ----------
        *commands: ApplicationCommand
            The commands to add to the client.
        """
        self.application_commands.update({command.id: command for command in commands if command.id})
        self._sync_queue.extend(commands)

    async def delete_command(self, command_id: str):
        """
        Delete a command from the client.

        Parameters
        ----------
        command_id: str
        """
        return await self.session.delete(f"/api/v10/applications/{self.application_id}/commands/{command_id}")

    def load_scripts(self, *scripts: str):
        """
        Load scripts into the client.

        Scripts are modules that contain commands and a setup function.
        """
        import importlib

        scripts = [script.replace(".py", "") for script in scripts if script.endswith(".py")]
        for path in scripts:
            importlib.import_module(path).setup(self)

    def on_error(self, coro: Callable):
        """
        A decorator to register a global error handler.

        Parameters
        ----------
        coro: Callable
            The coroutine to register as the global error handler. Must take 2 parameters:`error` and `data`.
        """
        self._global_error_handler = coro

    async def send_message(self, channel_id: int, payload: Dict[str, Any]):
        """
        Send a message to a channel.

        This method is used internally by the client. You should not use this method unless you know what you are doing.

        Parameters
        ----------
        channel_id: int
            The ID of the channel to send the message to.
        payload: Dict[str, Any]
            The payload to send to the channel.
        """
        url = f"/api/v10/channels/{channel_id}/messages"
        await self.session.post(url, json=payload)

    async def as_user(self) -> ClientUser:
        """
        Get the client as partial user.

        Returns
        -------
        ClientUser
            The client as partial user.
        """
        data = await (
            await self.session.get(f"/api/v10/oauth2/applications/@me")
        ).json()
        return ClientUser(data)

    async def sync(self):
        """
        Sync the commands to the client.

        This method is used internally by the client. You should not use this method.
        """
        url = f"/api/v10/applications/{self.application_id}/commands"
        resp = await self.session.put(url, json=[command.to_dict() for command in self._sync_queue])
        return await resp.json()

import aiohttp
from .command import *
from .modal import Modal
from .embed import Embed
from .file import File
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import ApplicationCommandType
from .user import ClientUser
from .permissions import Permissions
from .command import ApplicationCommand
from .view import Button, SelectMenu
from fastapi.requests import Request
from .dash import dashboard
from .params import handle_send_params, merge_fields
from fastapi.responses import JSONResponse
from .multipart import create_form
from .https import multipart_request
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
    The main client class for discohook.
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
        category: ApplicationCommandType = ApplicationCommandType.slash,
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

    async def send_message(
            self, 
            channel_id: int, 
            content: Optional[str] = None,
            *,
            tts: bool = False,
            embed: Optional[Embed] = None,
            embeds: Optional[List[Embed]] = None,
            file: Optional[File] = None,
            files: Optional[List[File]] = None,
        ):
        """
        Send a message to a channel using the ID of the channel.

        Parameters
        ----------
        channel_id: int
            The ID of the channel to send the message to.
        content: Optional[str]
            The content of the message.
        tts: bool
            Whether the message should be sent using text-to-speech. Defaults to False.
        embed: Optional[Embed]
            The embed to send with the message.
        embeds: Optional[List[Embed]]
            A list of embeds to send with the message. Maximum of 10.
        """
        payload = handle_send_params(content, tts=tts, embed=embed, embeds=embeds, file=file, files=files)
        files = merge_fields(file, files)
        form = create_form(payload, files)
        return await multipart_request(path=f"/channels/{channel_id}/messages", session=self.session, form=form)

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

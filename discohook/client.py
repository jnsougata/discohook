import asyncio
import atexit
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import aiohttp
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse

from .base import Component
from .channel import Channel, PartialChannel
from .command import ApplicationCommand
from .dash import dashboard
from .embed import Embed
from .file import File
from .guild import Guild
from .handler import _handler
from .help import _help
from .https import HTTPClient
from .interaction import Interaction
from .message import Message
from .poll import Poll
from .user import User
from .utils import compare_password
from .view import View
from .webhook import Webhook


async def delete_cmd(request: Request):
    if not request.app.password:
        return JSONResponse(
            {"error": "Password not set inside the application"}, status_code=500
        )
    data = await request.json()
    password = data.get("password")
    command_id = data.get("id")
    guild_id = data.get("guild_id")
    if not compare_password(request.app.password, password):
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    resp = await request.app.delete_command(command_id, guild_id=guild_id)
    if resp.status == 204:
        return JSONResponse({"success": True}, status_code=resp.status)
    return JSONResponse({"error": "Failed to delete command"}, status_code=resp.status)


async def sync(request: Request):
    if not request.app.password:
        return JSONResponse(
            {"error": "Password not set inside the application"}, status_code=500
        )
    data = await request.json()
    password = data.get("password")
    if not compare_password(request.app.password, password):
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    responses, raw = await request.app._sync()  # noqa
    if not any([resp.status == 200 for resp in responses]):
        erred_first_response = next(
            (resp for resp in responses if resp.status != 200), None
        )
        data = await erred_first_response.json()
        data["raw_payload"] = raw
        return JSONResponse(data, status_code=500)
    commands = []
    for resp in responses:
        commands.extend(await resp.json())
    return JSONResponse(commands, status_code=200)


async def authenticate(request: Request):
    if not request.app.password:
        return JSONResponse(
            {"error": "Password not set inside the application"}, status_code=500
        )
    data = await request.json()
    password = data.get("password")
    if not compare_password(request.app.password, password):
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    return JSONResponse({"success": True}, status_code=200)


class Client(Starlette):
    """
    The base client class for discohook.

    Parameters
    ----------
    application_id: int | str
        The application ID of the bot.
    public_key: str
        The public key of the bot.
    token: str
        The token of the bot.
    route: str
        The route to listen for interactions on.
    password: str | None
        The password to use for the dashboard.
    default_help_command: bool
        Whether to use the default help command or not. Defaults to False.
    **kwargs
        Keyword arguments to pass to the FastAPI instance.
    """

    def __init__(
        self,
        *,
        application_id: Union[int, str],
        public_key: str,
        token: str,
        route: str = "/interactions",
        password: Optional[str] = None,
        default_help_command: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.token = token
        self.public_key = public_key
        self.application_id = application_id
        self.password = password
        session = aiohttp.ClientSession("https://discord.com")

        @atexit.register
        def close_session():
            asyncio.get_event_loop().run_until_complete(session.close())

        self.http = HTTPClient(self, token, session)
        self.active_components: Dict[str, Component] = {}
        self._sync_queue: List[ApplicationCommand] = []
        self.commands: Dict[str, ApplicationCommand] = {}
        self.add_route(route, _handler, methods=["POST"], include_in_schema=False)
        self.add_route("/api/sync", sync, methods=["POST"], include_in_schema=False)
        self.add_route("/api/dash", dashboard, methods=["GET"], include_in_schema=False)
        self.add_route(
            "/api/verify", authenticate, methods=["POST"], include_in_schema=False
        )
        self.add_route(
            "/api/commands", delete_cmd, methods=["DELETE"], include_in_schema=False
        )
        self._custom_id_parser: Optional[Callable[[Interaction, str], str]] = None
        if default_help_command:
            self.add_commands(_help)
        self._interaction_error_handler: Optional[
            Callable[[Interaction, Exception], Any]
        ] = None

    def on_error(self):
        """
        A decorator to add an error handler for any server errors.
        """

        def decorator(coro: Callable[[Request, Exception], Any]):
            self.add_exception_handler(Exception, coro)
            return coro

        return decorator

    def load_view(self, view: View):
        """
        Loads multiple components into the client.
        Do not use this method unless you know what you are doing.

        Parameters
        ----------
        view: View
            The view to load components from.
        """
        for component in view.children:
            self.active_components[component.custom_id] = component

    def preload(self, custom_id: str):
        """
        This decorator is used to load a component into the client.
        This method will help you to use persistent components with static custom ids.

        Parameters
        ----------
        custom_id: str
            The unique custom id of the component.

        Raises
        ------
        ValueError
            If the custom id is not a not empty string or is not provided.
        """

        def decorator(component: Component):
            if not custom_id or not isinstance(custom_id, str):
                raise ValueError("Invalid custom id provided.")
            component.custom_id = custom_id
            self.active_components[custom_id] = component
            return component

        return decorator

    def load(self, cmd: ApplicationCommand) -> ApplicationCommand:
        """
        A decorator to load a command into the client.
        """
        self.commands[cmd.key] = cmd
        self._sync_queue.append(cmd)
        return cmd

    def add_commands(self, *commands: Union[ApplicationCommand, Any]):
        """
        Add commands to the client.

        Parameters
        ----------
        *commands: ApplicationCommand
            The commands to add to the client.
        """
        for command in commands:
            self.commands[command.key] = command
        self._sync_queue.extend(commands)

    async def delete_command(self, command_id: str, *, guild_id: Optional[str] = None):
        """
        Delete a command from the client.

        Parameters
        ----------
        command_id: str
            The id of the command to delete.
        guild_id: str | None
            The id of the guild to delete the command from. Defaults to None.
        """
        return await self.http.delete_command(
            str(self.application_id), command_id, guild_id
        )

    # def load_modules(self, directory: str):
    #     """
    #     Loads multiple command from modules within directory by walking through it.
    #
    #     Parameters
    #     ----------
    #     directory: str
    #         The directory to load the modules from.
    #     """
    #     import importlib
    #     import pathlib
    #     from os import sep
    #
    #     globs = pathlib.Path(directory).glob(f"**{sep}*.py")
    #     modules = [str(path).replace(sep, ".")[:-3] for path in globs]
    #     for module in modules:
    #         importlib.import_module(module).setup(self)

    def on_interaction_error(self):
        """
        A decorator to register a global interaction error handler.
        """

        def decorator(coro: Callable[[Interaction, Exception], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Exception handler must be a coroutine.")
            self._interaction_error_handler = coro
            return coro

        return decorator

    def custom_id_parser(self):
        """
        A decorator to register a dev defined custom id parser.
        """

        def decorator(coro: Callable[[Interaction, str], str]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Custom id parser must be a coroutine.")
            self._custom_id_parser = coro

        return decorator

    async def send(
        self,
        channel_id: str,
        content: Optional[str] = None,
        *,
        tts: bool = False,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
        view: Optional[View] = None,
        poll: Optional[Poll] = None,
    ) -> Message:
        """
        Send a message to a channel using the ID of the channel.

        Parameters
        ----------
        channel_id: str
            The ID of the channel to send the message to.
        content: Optional[str]
            The content of the message.
        tts: bool
            Whether the message should be sent using text-to-speech. Defaults to False.
        embed: Optional[Embed]
            The embed to send with the message.
        embeds: Optional[List[Embed]]
            A list of embeds to send with the message. Maximum of 10.
        file: Optional[File]
            A file to be sent with the message
        files: Optional[List[File]]
            A list of files to be sent with message.
        view: Optional[View]
            The view to send with the message.
        poll: Optional[Poll]
            The poll to send with the message.

        Returns
        -------
        Message
            The message that was sent.
        """
        if not channel_id.isdigit():
            raise TypeError("Channel ID must be a snowflake.")
        channel = PartialChannel(self, channel_id)
        return await channel.send(
            content=content,
            tts=tts,
            embed=embed,
            embeds=embeds,
            file=file,
            files=files,
            view=view,
            poll=poll,
        )

    async def me(self) -> User:
        """
        Get the client as a discord user.

        Returns
        -------
        User
            The client as a user.
        """
        resp = await self.http.fetch_user(self.application_id)
        return User(self, await resp.json())

    async def edit(self, username: str, *, avatar: Optional[str] = None):
        """
        Edits the client user.

        Parameters
        ----------
        username: :class:`str`
            The new username of the client user.
        avatar: Optional[:class:`str`]
            The new avatar of the client user in base64 data URI scheme.
        """
        payload = {"username": username}
        if avatar:
            payload["avatar"] = avatar
        await self.http.edit_client(payload)

    async def _sync(self) -> Tuple[List[aiohttp.ClientResponse], List[Dict[str, Any]]]:
        """
        Sync the commands to the client.

        This method is used internally by the client. You should not use this method.
        """
        responses = []
        guild_commands = {}
        for cmd in self._sync_queue:
            if cmd.guild_id:
                guild_commands.setdefault(cmd.guild_id, []).append(cmd)
        if guild_commands:
            tasks = []
            for guild_id, commands in guild_commands.items():
                tasks.append(
                    self.http.sync_guild_commands(
                        str(self.application_id),
                        guild_id,
                        [cmd.to_dict() for cmd in commands],
                    )
                )
            responses.extend(await asyncio.gather(*tasks))
            self._sync_queue = [cmd for cmd in self._sync_queue if not cmd.guild_id]
        if self._sync_queue:
            responses.append(
                await self.http.sync_global_commands(
                    str(self.application_id),
                    [cmd.to_dict() for cmd in self._sync_queue],
                )
            )
        return responses, [cmd.to_dict() for cmd in self._sync_queue]

    async def create_webhook(
        self, channel_id: str, *, name: str, image_base64: Optional[str] = None
    ):
        """
        Create a webhook in a channel.

        Parameters
        ----------
        channel_id: str
            The ID of the channel to create the webhook in.
        name:
            The name of the webhook.
        image_base64:
            The base64 encoded image of the webhook.
        Returns
        -------
        Webhook

        """
        resp = await self.http.create_webhook(
            channel_id, {"name": name, "avatar": image_base64}
        )
        data = await resp.json()
        return Webhook(self, data)

    async def fetch_webhook(
        self, webhook_id: str, *, webhook_token: Optional[str] = None
    ):
        """
        Fetch a webhook from the client.
        Parameters
        ----------
        webhook_id: str
            The ID of the webhook to fetch.
        webhook_token: Optional[str]
            The token of the webhook to fetch.
        Returns
        -------
        Webhook
        """
        resp = await self.http.fetch_webhook(webhook_id, webhook_token=webhook_token)
        data = await resp.json()
        return Webhook(self, data)

    async def fetch_guild(self, guild_id: str) -> Optional[Guild]:
        """
        Fetches the guild of given id.

        Returns
        -------
        Guild
        """
        resp = await self.http.fetch_guild(guild_id)
        data = await resp.json()
        if not data.get("id"):
            return
        return Guild(self, data)

    async def fetch_user(self, user_id: str) -> Optional[User]:
        """
        Fetches the user of given id.

        Returns
        -------
        User
        """
        resp = await self.http.fetch_user(user_id)
        data = await resp.json()
        if not data.get("id"):
            return
        return User(self, data)

    async def fetch_channel(self, channel_id: str) -> Optional[Channel]:
        """
        Fetches the channel of given id.

        Returns
        -------
        Channel
        """
        resp = await self.http.fetch_channel(channel_id)
        data = await resp.json()
        if not data.get("id"):
            return
        return Channel(self, data)

    async def fetch_commands(self):
        """
        Fetches the commands of the client.

        Returns
        -------
        List[Dict[str, Any]]
        """
        resp = await self.http.fetch_global_application_commands(
            str(self.application_id)
        )
        return await resp.json()

    async def fetch_info(self) -> Dict[str, Any]:
        """
        Returns the application object associated with the requesting client user.

        Returns
        -------
        Dict[str, Any]
        """
        resp = await self.http.fetch_application()
        return await resp.json()

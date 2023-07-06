import asyncio
from typing import Any, Callable, Dict, List, Optional, Union

import aiohttp
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .channel import PartialChannel
from .command import ApplicationCommand, Option
from .dash import dashboard
from .embed import Embed
from .enums import ApplicationCommandType
from .file import File
from .guild import Guild
from .handler import handler
from .https import HTTPClient
from .message import Message
from .permissions import Permissions
from .user import ClientUser
from .view import Component, View
from .webhook import Webhook


async def delete_cmd(request: Request, command_id: str, token: str):
    if token != request.app.token:
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    resp = await request.app.delete_command(command_id)
    if resp.status == 204:
        return JSONResponse({"success": True}, status_code=resp.status)
    return JSONResponse({"error": "Failed to delete command"}, status_code=resp.status)


async def sync(request: Request, token: str):
    if token != request.app.token:
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    resp = await request.app.sync()
    return JSONResponse(await resp.json(), status_code=resp.status)


class Client(FastAPI):
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
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.token = token
        self.docs_url = None
        self.redoc_url = None
        self.public_key = public_key
        self.application_id = application_id
        self.http = HTTPClient(self, token, aiohttp.ClientSession("https://discord.com"))
        self.active_components: Dict[str, Component] = {}
        self._sync_queue: List[ApplicationCommand] = []
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self.cached_inter_tokens: Dict[str, str] = {}
        self.add_route(route, handler, methods=["POST"], include_in_schema=False)
        self.add_api_route("/api/sync/{token}", sync, methods=["GET"], include_in_schema=False)
        self.add_api_route("/api/dash/{token}", dashboard, methods=["GET"], include_in_schema=False)
        self.add_api_route(
            "/api/commands/{command_id}/{token}", delete_cmd, methods=["DELETE"], include_in_schema=False
        )
        self.error_handler: Optional[Callable] = None
        self._custom_id_parser: Optional[Callable] = None

    def load_components(self, view: View):
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

    def preload(self, component: Component) -> Component:
        """
        This decorator is used to load a component into the client.
        This method will help you to use persistent components with static custom ids.

        Parameters
        ----------
        component: Component
            The component to load.

        Returns
        -------
        Component
            The component that was loaded.

        Raises
        ------
        ValueError
            If the component does not have a static custom id.
        """
        if not component.has_static_custom_id:
            raise ValueError("Component must have a static custom id to be preloaded.")
        self.active_components[component.custom_id] = component
        return component

    def store_inter_token(self, interaction_id: str, token: str):
        self.cached_inter_tokens[interaction_id] = token

    def command(
        self,
        name: str,
        description: Optional[str] = None,
        *,
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
        options: Optional[List[Option]]
            The options of the command. Does not apply to user & message commands.
        permissions: Optional[List[Permissions]]
            The default permissions of the command.
        dm_access: bool
            Whether the command can be used in DMs. Defaults to True.
        category: AppCmdType
            The category of the command. Defaults to slash commands.
        """
        cmd = ApplicationCommand(
            name=name,
            description=description,
            options=options,
            permissions=permissions,
            dm_access=dm_access,
            category=category,
        )

        def decorator(coro: Callable):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Callback must be a coroutine.")
            cmd.callback = coro
            self.application_commands[cmd._id] = cmd  # noqa
            self._sync_queue.append(cmd)
            return cmd

        return decorator

    def add_commands(self, *commands: Union[ApplicationCommand, Any]):
        """
        Add commands to the client.

        Parameters
        ----------
        *commands: ApplicationCommand
            The commands to add to the client.
        """
        self.application_commands.update({command._id: command for command in commands})  # noqa
        self._sync_queue.extend(commands)

    async def delete_command(self, command_id: str):
        """
        Delete a command from the client.

        Parameters
        ----------
        command_id: str
        """
        return await self.http.delete_command(str(self.application_id), command_id)

    def load_modules(self, directory: str):
        """
        Loads multiple command form modules in a directory.

        Parameters
        ----------
        directory: str
            The directory to load the modules from.
        """
        import importlib
        import os

        scripts = os.listdir(directory)
        scripts = [f"{directory}.{script[:-3]}" for script in scripts if script.endswith(".py")]
        for script in scripts:
            importlib.import_module(script).setup(self)

    def on_error(self, coro: Callable):
        """
        A decorator to register a global error handler.

        Parameters
        ----------
        coro: Callable
            The coroutine to register as the global error handler. Must take 2 parameters:`error` and `data`.
        """
        self.error_handler = coro

    def custom_id_parser(self, coro: Callable):
        """
        A decorator to register a dev defined custom id parser.
        Parameters
        ----------
        coro: Callable
        """
        self._custom_id_parser = coro

    async def send_message(
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

        )

    async def as_user(self) -> ClientUser:
        """
        Get the client as partial user.

        Returns
        -------
        ClientUser
            The client as partial user.
        """
        resp = await self.http.fetch_client_info()
        return ClientUser(self, await resp.json())

    async def sync(self):
        """
        Sync the commands to the client.

        This method is used internally by the client. You should not use this method.
        """
        return await self.http.sync_commands(str(self.application_id), [cmd.to_dict() for cmd in self._sync_queue])

    async def create_webhook(self, channel_id: str, *, name: str, image_base64: Optional[str] = None):
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
        resp = await self.http.create_webhook(channel_id, {"name": name, "avatar": image_base64})
        data = await resp.json()
        return Webhook(data, self)

    async def fetch_webhook(self, webhook_id: str, *, webhook_token: Optional[str] = None):
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
        return Webhook(data, self)

    async def fetch_guild(self, guild_id: str) -> Optional[Guild]:
        """
        Fetches the guild of given id.

        Returns
        -------
        Guild
        """
        resp = await self.http.fetch_guild(guild_id)
        data = await resp.json()
        try:
            return Guild(data, self)
        except KeyError:
            return None

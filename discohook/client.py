import asyncio
import base64
from typing import Any, Callable, Dict, List, Literal, Optional, Tuple, Union

import aiohttp
from starlette.applications import Starlette
from starlette.requests import Request

from .channel import Channel, PartialChannel
from .command import ApplicationCommand
from .components import (ActionRow, Container, File, MediaGallery, Section,
                         Separator, TextDisplay)
from .dashboard import (authenticate_route, delete_cmd_route, homepage_route,
                        sync_route)
from .emoji import PartialEmoji
from .engine import _engine
from .guild import Guild
from .handler import Handler
from .help import _help
from .https import HTTPClient
from .interaction import Interaction
from .message import Message
from .ratelimit import RatelimitMux
from .user import User
from .webhook import Webhook


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
    ratelimit_mux: RatelimitMux | None
        Whether to use a custom ratelimit mux or not. Defaults to None.
    **kwargs
        Keyword arguments to pass to the Starlette instance.
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
        ratelimit_mux: Optional[RatelimitMux] = None,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
            routes=[
                sync_route,
                homepage_route,
                authenticate_route,
                delete_cmd_route,
            ],
        )
        self.token = token
        self.public_key = public_key
        self.application_id = application_id
        self.password = password
        self.http = HTTPClient(
            token=token, application_id=str(application_id), rate_limiter=ratelimit_mux
        )
        self.active_handlers: Dict[str, Optional[Handler]] = {}
        self._sync_queue: List[ApplicationCommand] = []
        self.active_commands: Dict[str, ApplicationCommand] = {}
        self.add_route(route, _engine, methods=["POST"], include_in_schema=False)
        # self.add_route("/api/sync", sync, methods=["POST"], include_in_schema=False)
        # self.add_route("/api/dash", homepage, methods=["GET"], include_in_schema=False)
        # self.add_route(
        #     "/api/verify", authenticate, methods=["POST"], include_in_schema=False
        # )
        # self.add_route(
        #     "/api/commands", delete_cmd, methods=["DELETE"], include_in_schema=False
        # )
        self._custom_id_parser: Optional[Callable[[Interaction, str], str]] = None
        if default_help_command:
            self.commands(_help)
        self._interaction_error_handler: Optional[Callable[[Interaction], Any]] = None

    @classmethod
    def from_env(
        cls,
        path: str = ".env",
        *,
        default_help_command: bool = False,
        ratelimit_mux: Optional[RatelimitMux] = None,
        **kwargs,
    ) -> "Client":
        """
        Creates a client from environment variables.
        The environment variables must be set in the following format:
            - APPLICATION_ID: The application ID of the bot.
            - PUBLIC_KEY: The public key of the bot.
            - BOT_TOKEN: The token of the bot.
            - APPLICATION_PASSWORD: The password to use for the dashboard (OPTIONAL).
                The password is used to authenticate the dashboard and the sync route.
                The password is not required if you are not using the dashboard or the sync route.

        Parameters
        ----------
        path: str
            Path to the .env file. Defaults to ".env".
        default_help_command: bool
            Whether to use the default help command or not. Defaults to False.
        ratelimit_mux: RatelimitMux | None
            Whether to use a custom ratelimit mux or not. Defaults to None.
        **kwargs
            Keyword arguments to pass to the Starlette instance.

        Returns
        -------
        Client
            The client instance.
        """
        import os

        from dotenv import load_dotenv

        load_dotenv(path)

        application_id = os.environ["APPLICATION_ID"]
        public_key = os.environ["PUBLIC_KEY"]
        token = os.environ["BOT_TOKEN"]
        password = os.getenv("APPLICATION_PASSWORD")

        return cls(
            application_id=str(application_id),
            public_key=public_key,
            token=token,
            password=password,
            default_help_command=default_help_command,
            ratelimit_mux=ratelimit_mux,
            **kwargs,
        )

    def on_error(self):
        """
        A decorator to add an error handler for any server errors.
        """

        def decorator(coro: Callable[[Request, Exception], Any]):
            self.add_exception_handler(Exception, coro)
            return coro

        return decorator

    def register(
        self, item: Union[Handler, ApplicationCommand]
    ) -> Union[Handler, ApplicationCommand]:
        """
        Registers a handler or command to the client.

        Parameters
        ----------
        item: Union[Handler, ApplicationCommand]
            The handler or command to register.
        """
        if isinstance(item, ApplicationCommand):
            self.active_commands[item.handler.id] = item
            self._sync_queue.append(item)
        else:
            self.active_handlers[item.id] = item
        return item

    def commands(self, *commands: Union[ApplicationCommand, Any]):
        """
        Add commands to the client.

        Parameters
        ----------
        *commands:
            The commands to add to the client.
        """
        for command in commands:
            self.active_commands[command.handler.id] = command
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
        return await self.http.delete_application_command(
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

        def decorator(coro: Callable[[Interaction], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Exception handler must be a coroutine.")
            self._interaction_error_handler = coro
            return coro

        return decorator

    def custom_id_parser(self, coro: Callable[[Interaction, str], str]):
        """
        A decorator to register a dev defined custom id parser.
        """
        self._custom_id_parser = coro

    async def send(
        self,
        channel_id: str,
        *components: Union[
            TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container
        ],
    ) -> Message:
        """
        Send a message to a channel using the ID of the channel.

        Parameters
        ----------
        channel_id: str
            The ID of the channel to send the message to.
        *components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]
            The components to send in the message.

        Returns
        -------
        Message
            The message that was sent.
        """
        if not channel_id.isdigit():
            raise TypeError("Channel ID must be a snowflake.")
        channel = PartialChannel(self, channel_id)
        return await channel.send(*components)

    async def me(self) -> User:
        """
        Get the client as a discord user.

        Returns
        -------
        User
            The client as a user.
        """
        resp = await self.http.get_user(str(self.application_id))
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
        await self.http.modify_current_user(payload)

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
                    self.http.bulk_overwrite_guild_application_commands(
                        str(self.application_id),
                        guild_id,
                        [cmd.to_dict() for cmd in commands],
                    )
                )
            responses.extend(await asyncio.gather(*tasks))
            self._sync_queue = [cmd for cmd in self._sync_queue if not cmd.guild_id]
        if self._sync_queue:
            responses.append(
                (
                    await self.http.bulk_overwrite_global_application_commands(
                        str(self.application_id),
                        [cmd.to_dict() for cmd in self._sync_queue],
                    )
                )
            )
        return responses, [cmd.to_dict() for cmd in self._sync_queue]

    async def create_webhook(
        self,
        channel_id: str,
        *,
        name: str,
        image_base64: Optional[str] = None,
        reason: Optional[str] = None,
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
        reason:
            The reason for creating the webhook. This will be shown in the audit log.
            This is optional and can be None.
        Returns
        -------
        Webhook

        """
        resp = await self.http.create_webhook(
            channel_id, {"name": name, "avatar": image_base64}, reason=reason
        )
        data = await resp.json()
        return Webhook(data, self)

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
        resp = await self.http.get_webhook(webhook_id, webhook_token)
        return Webhook(await resp.json(), self)

    async def fetch_guild(
        self, guild_id: str, *, with_counts: Optional[str] = False
    ) -> Optional[Guild]:
        """
        Fetches the guild of given id.

        Returns
        -------
        Guild
        """
        resp = await self.http.get_guild(
            guild_id, with_counts="true" if with_counts else "false"
        )
        data = await resp.json()
        if not data.get("id"):
            return None
        return Guild(self, data)

    async def fetch_user(self, user_id: str) -> Optional[User]:
        """
        Fetches the user of given id.

        Returns
        -------
        User
        """
        resp = await self.http.get_user(user_id)
        data = await resp.json()
        if not data.get("id"):
            return None
        return User(self, data)

    async def fetch_channel(self, channel_id: str) -> Optional[Channel]:
        """
        Fetches the channel of given id.

        Returns
        -------
        Channel
        """
        resp = await self.http.get_channel(channel_id)
        data = await resp.json()
        if not data.get("id"):
            return None
        return Channel(self, data)

    async def fetch_commands(self):
        """
        Fetches the commands of the client.

        Returns
        -------
        List[Dict[str, Any]]
        """
        resp = await self.http.get_global_application_commands(str(self.application_id))
        return await resp.json()

    async def fetch_info(self) -> Dict[str, Any]:
        """
        Returns the application object associated with the requesting client user.

        Returns
        -------
        Dict[str, Any]
        """
        resp = await self.http.get_current_application()
        return await resp.json()

    async def fetch_application_emojis(self):
        """
        Fetch all emojis from the client.
        """
        resp = await self.http.list_application_emojis()
        return await resp.json()

    async def fetch_application_emoji(self, emoji_id: str):
        """
        Fetch an emoji from the client.

        Parameters
        ----------
        emoji_id: str
            The ID of the emoji to fetch.
        """
        resp = await self.http.get_application_emoji(emoji_id)
        return await resp.json()

    async def create_application_emoji(
        self, *, name: str, image: bytes, image_type: Literal["png", "jpeg", "gif"]
    ) -> PartialEmoji:
        """
        Create a new emoji in a guild.

        Parameters
        ----------
        name: str
            The name of the emoji.
        image: bytes
            The image of the emoji in bytes.
        image_type: str
            The image type of the emoji. (e.g. "png", "jpeg", "gif")

        Returns
        -------
        PartialEmoji
        """
        data_uri = f"data:image/{image_type};base64,{base64.b64encode(image).decode()}"
        resp = await self.http.create_application_emoji(
            {"name": name, "image": data_uri}
        )
        emoji_data = await resp.json()
        return PartialEmoji(
            name=emoji_data["name"],
            id=emoji_data["id"],
            animated=emoji_data.get("animated", False),
        )

    async def edit_application_emoji(self, emoji_id: str, name: str):
        """
        Edit an existing emoji in a guild.

        Parameters
        ----------
        emoji_id: str
            The ID of the emoji.
        name: str
            The name of the emoji.
        """
        await self.http.modify_application_emoji(emoji_id, name)

    async def delete_application_emoji(self, emoji_id: str):
        """
        Delete an existing emoji in a guild.

        Parameters
        ----------
        emoji_id: str
            The ID of the emoji.
        """
        await self.http.delete_application_emoji(emoji_id)

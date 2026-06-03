import traceback
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from .adapter import ResponseAdapter
from .channel import PartialChannel
from .enums import InteractionContextType, InteractionType, try_enum
from .guild import PartialGuild
from .member import Member
from .message import Message
from .user import User
from .utils import snowflake_time, unwrap_user

if TYPE_CHECKING:
    from .client import Client


class Interaction:
    """
    Represents a discord interaction.
    """

    def __init__(self, client: "Client", data: Dict[str, Any]):
        self.payload = data
        self._responded = False
        self.client: "Client" = client
        self._parsed_options = None
        self.focused_option_name: Optional[str] = None
        self._error = None
        self.custom_id: Optional[str] = None

    @property
    def error(self) -> Optional[Exception]:
        """
        Error that occurred during the interaction

        Returns:
            Exception | None: Exception object.
        """
        return self._error

    @property
    def traceback(self) -> Optional[str]:
        """
        Traceback of the error that occurred during the interaction

        Returns:
            str | None: Traceback string.
        """
        if not self._error:
            return None
        return "".join(
            traceback.format_exception(
                type(self.error), self.error, self.error.__traceback__
            )
        )

    @property
    def data(self) -> Dict[str, Any]:
        """
        Command data payload (if the interaction is a command).

        Returns:
            Dict[str, Any]: Command data payload.
        """
        return self.payload.get("data", {})

    @property
    def parsed_command_options(self) -> Optional[Dict[str, Any]]:
        """
        Resolved command options payload (if the interaction is a command).
        """
        return self._parsed_options

    @property
    def responded(self) -> bool:
        """
        Whether the interaction has been responded to.

        Returns:
            bool: Whether the interaction has been responded to.
        """
        return self._responded

    @property
    def id(self) -> str:
        """
        Unique id of the interaction

        Returns:
            str: Interaction id.
        """
        return self.payload["id"]

    @property
    def type(self) -> Optional[InteractionType]:
        """
        The type of the interaction

        Returns
        -------
        Optional[InteractionType]
        """
        return try_enum(InteractionType, self.payload["type"])

    @property
    def token(self) -> str:
        """
        The token of the interaction

        Returns
        -------
        str
        """
        return self.payload["token"]

    @property
    def version(self) -> int:
        """
        The version of the interaction

        Returns
        -------
        int
        """
        return self.payload["version"]

    @property
    def application_id(self) -> str:
        """
        The id of the application that the interaction was triggered for

        Returns
        -------
        str
        """
        return self.payload["application_id"]

    @property
    def guild_id(self) -> Optional[str]:
        """
        The guild id of the interaction

        Returns
        -------
        Optional[str]
        """
        return self.payload.get("guild_id")

    @property
    def channel_id(self) -> str:
        """
        The channel id of the interaction

        Returns
        -------
        Optional[str]
        """
        return self.payload["channel_id"]

    @property
    def app_permissions(self) -> Optional[int]:
        """
        The permissions of the application

        Returns
        -------
        Optional[int]
        """
        return self.payload.get("app_permissions")

    @property
    def locale(self) -> Optional[str]:
        """
        The locale of the interaction

        Returns
        -------
        Optional[str]
        """
        return self.payload.get("locale")

    @property
    def guild_locale(self) -> Optional[str]:
        """
        The guild locale of the interaction

        Returns
        -------
        Optional[str]
        """
        return self.payload.get("guild_locale")

    @property
    def created_at(self) -> float:
        """
        The timestamp when the interaction was created

        Returns
        -------
        float
        """
        return snowflake_time(self.id)

    @property
    def context(self) -> Optional[InteractionContextType]:
        """
        Context where the interaction was triggered from.

        Returns
        -------
        InteractionContextType | None
        """
        ctx = self.payload.get("context")
        if ctx is None:
            return None
        return InteractionContextType(int(ctx))

    @property
    def channel(self) -> PartialChannel:
        """
        The channel where the interaction was triggered

        Returns
        -------
        PartialChannel
        """
        return PartialChannel(self.client, self.channel_id, self.guild_id)

    @property
    def author(self) -> Union[User, Member]:
        """
        The author of the interaction
        If the interaction was triggered in a guild, this will return a member object else it will return user object.

        Returns
        -------
        Union[User, Member]
        """
        if not self.guild_id:
            return User(self.client, self.payload["user"])
        return Member(self.client, unwrap_user(self.payload["member"], self.guild_id))

    @property
    def guild(self) -> Optional[PartialGuild]:
        if not self.guild_id:
            return None
        return PartialGuild(self.client, self.guild_id) if self.guild_id else None

    @property
    def message(self) -> Optional[Message]:
        """
        The message from which the component interaction was triggered

        Returns
        -------
        Message
        """
        payload = self.payload.get("message")
        if not payload:
            return None
        return Message(self.client, payload)

    @property
    def response(self):
        """
        The response adapter for the interaction

        Returns
        -------
        ResponseAdapter
        """
        return ResponseAdapter(self)

    @property
    def from_originator(self) -> bool:
        """
        Whether the interaction was triggered by the same user who triggered the message

        Returns
        -------
        bool
        """
        if not self.message:
            return True
        return self.message.interaction.user == self.author

    async def original_response(self) -> Optional[Message]:
        """
        Gets the original response message of the interaction if the interaction has been responded to.

        Returns
        -------
        InteractionResponse
            The original response message
        """
        if not self._responded:
            return None
        resp = await self.client.http.get_original_interaction_response(
            self.application_id, self.token
        )
        data = await resp.json()
        return Message(self.client, data)

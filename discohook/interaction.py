from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from .channel import PartialChannel
from .enums import InteractionType, try_enum, InteractionContextType
from .guild import PartialGuild
from .member import Member
from .message import Message
from .adapter import ResponseAdapter
from .user import User
from .utils import snowflake_time

if TYPE_CHECKING:
    from .client import Client


class Interaction:
    """
    Base interaction class for all interactions

    Properties
    ----------
    id: str
        The unique id of the interaction
    type: int
        The type of the interaction
    token: str
        The token of the interaction
    version: int
        The version of the interaction
    application_id: str
        The id of the application that the interaction was triggered for
    data: Optional[Dict[str, Any]]
        The command data payload (if the interaction is a command)
    guild_id: Optional[str]
        The guild id of the interaction
    channel_id: Optional[str]
        The channel id of the interaction
    app_permissions: Optional[int]
        The permissions of the application
    locale: Optional[str]
        The locale of the interaction
    guild_locale: Optional[str]
        The guild locale of the interaction
    created_at: int
        The timestamp when the interaction was created

    Parameters
    ----------
    data: Dict[str, Any]
        The interaction data payload
    client: Client
        The stateful client
    """

    def __init__(self, client: "Client", data: Dict[str, Any]):
        self.payload = data
        self._responded = False
        self.client: "Client" = client
        self._parsed_options = None
        self.focused_option_name: Optional[str] = None

    @property
    def data(self) -> Dict[str, Any]:
        """
        The command data payload (if the interaction is a command)

        Returns
        -------
        Dict[str, Any]
        """
        return self.payload.get("data", {})

    @property
    def parsed_command_options(self) -> Optional[Dict[str, Any]]:
        """
        The resolved command options payload (if the interaction is a command)
        """
        return self._parsed_options

    @property
    def responded(self) -> bool:
        """
        Whether the interaction has been responded to

        Returns
        -------
        bool
        """
        return self._responded

    @property
    def id(self) -> str:
        """
        The unique id of the interaction

        Returns
        -------
        str
        """
        return self.payload["id"]

    @property
    def kind(self) -> Optional[InteractionType]:
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
            return
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
        self.payload["member"]["guild_id"] = self.guild_id
        return Member(self.client, self.payload["member"])

    @property
    def guild(self) -> Optional[PartialGuild]:
        if not self.guild_id:
            return
        return PartialGuild(self.client, self.guild_id)

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
            return
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
            return
        resp = await self.client.http.fetch_original_webhook_message(self.application_id, self.token)
        data = await resp.json()
        return Message(self.client, data)

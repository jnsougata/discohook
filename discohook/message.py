from .user import User
from .role import Role
from .embed import Embed
from .view import View
from .file import File
from .multipart import create_form
from typing import Optional, List, Dict, Any, TYPE_CHECKING
from .params import handle_edit_params, MISSING, merge_fields, handle_send_params

if TYPE_CHECKING:
    from .client import Client
    from .interaction import Interaction


class Message:
    """
    Represents a Discord message.

    Properties
    ----------
    id: :class:`str`
        The id of the message.
    channel_id: :class:`str`
        The id of the channel the message was sent in.
    author: :class:`User`
        The author of the message.
    content: :class:`str`
        The content of the message.
    timestamp: :class:`str`
        The timestamp of the message.
    edited_timestamp: Optional[:class:`str`]
        The timestamp of when the message was last edited.
    tts: :class:`bool`
        Whether the message was sent using text-to-speech.
    mention_everyone: :class:`bool`
        Whether the message mentions everyone.
    mentions: List[:class:`User`]
        The users mentioned in the message.
    mention_roles: List[:class:`Role`]
        The roles mentioned in the message.
    mention_channels: Optional[:class:`dict`]
        The channels mentioned in the message.
    attachments: :class:`dict`
        The attachments in the message.
    embeds: :class:`list`
        The embeds in the message.
    reactions: Optional[:class:`list`]
        The reactions in the message.
        ...
    """
    def __init__(self, payload: Dict[str, Any], client: "Client") -> None:
        self.client = client
        self.data = payload

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def type(self) -> int:
        return self.data["type"]

    @property
    def channel_id(self) -> str:
        return self.data["channel_id"]

    @property
    def author(self) -> User:
        return User(self.data["author"], self.client)

    @property
    def content(self) -> Optional[str]:
        return self.data["content"]

    @property
    def timestamp(self) -> str:
        return self.data["timestamp"]

    @property
    def edited_timestamp(self) -> Optional[str]:
        return self.data.get("edited_timestamp")

    @property
    def tts(self) -> bool:
        return self.data.get("tts", False)

    @property
    def mention_everyone(self) -> bool:
        return self.data.get("mention_everyone", False)

    @property
    def mentions(self) -> List[User]:
        return [User(x, self.client) for x in self.data.get("mentions", [])]

    @property
    def mention_roles(self) -> List[Role]:
        return [Role(x, self.client) for x in self.data.get("mention_roles", [])]

    @property
    def mention_channels(self) -> Optional[dict]:
        return self.data.get("mention_channels")

    @property
    def attachments(self) -> Optional[dict]:
        return self.data.get("attachments")

    @property
    def embeds(self) -> Optional[List[dict]]:
        return self.data.get("embeds")

    @property
    def reactions(self) -> Optional[List[dict]]:
        return self.data.get("reactions")

    @property
    def nonce(self) -> Optional[str]:
        return self.data.get("nonce")

    @property
    def pinned(self) -> bool:
        return self.data.get("pinned", False)

    @property
    def webhook_id(self) -> Optional[str]:
        return self.data.get("webhook_id")

    @property
    def activity(self) -> Optional[dict]:
        return self.data.get("activity")

    @property
    def application(self) -> Optional[dict]:
        return self.data.get("application")

    @property
    def application_id(self) -> Optional[str]:
        return self.data.get("application_id")

    @property
    def message_reference(self) -> Optional[dict]:
        return self.data.get("message_reference")

    @property
    def flags(self) -> Optional[int]:
        return self.data.get("flags")

    @property
    def referenced_message(self) -> Optional[dict]:
        return self.data.get("referenced_message")

    @property
    def interaction_data(self) -> Optional[dict]:
        return self.data.get("interaction")

    @property
    def thread(self) -> Optional[dict]:
        return self.data.get("thread")

    @property
    def components(self) -> Optional[List[dict]]:
        return self.data.get("components")

    @property
    def sticker_items(self) -> Optional[List[dict]]:
        return self.data.get("sticker_items")

    @property
    def stickers(self) -> Optional[List[dict]]:
        return self.data.get("stickers")

    @property
    def position(self) -> Optional[int]:
        return self.data.get("position")

    async def delete(self):
        """
        Deletes the message.
        """
        return await self.client.http.delete_message(self.channel_id, self.id)

    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[File] = MISSING,
        files: Optional[List[File]] = MISSING,
        suppress_embeds: Optional[bool] = MISSING,
    ):
        """
        Edits the message.

        Parameters
        ----------
        content: Optional[str]
            The new content of the message.
        embed: Optional[Embed]
            The new embed of the message.
        embeds: Optional[List[Embed]]
            The new embeds of the message.
        view: Optional[View]
            The new view of the message.
        tts: Optional[bool]
            Whether the message should be sent with text-to-speech.
        file: Optional[File]
            A file to send with the message.
        files: Optional[List[File]]
            A list of files to send with the message.
        suppress_embeds: Optional[bool]
            Whether the embeds should be suppressed.
        """
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )
        if view is not MISSING:
            self.client.load_components(view)
        resp = await self.client.http.edit_channel_message(
            self.channel_id, self.id, create_form(data, merge_fields(file, files))
        )
        data = await resp.json()
        return Message(data, self.client)


class FollowupResponse:
    """
    Represents a followup message sent by an interaction, subclassed from :class:`Message`.
    """
    def __init__(self, payload: Dict[str, Any], interaction: "Interaction") -> None:
        self.message = Message(payload, interaction.client)
        self.interaction = interaction

    async def delete(self):
        """
        Deletes the followup message.
        """
        return await self.interaction.client.http.delete_webhook_message(
            self.interaction.application_id,
            self.interaction.token,
            self.message.id,
        )

    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[File] = MISSING,
        files: Optional[List[File]] = MISSING,
        suppress_embeds: Optional[bool] = MISSING,
    ) -> Message:
        """
        Edits the followup message.

        Parameters
        ----------
        same as :meth:`Message.edit`
        """
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )
        if view is not MISSING and view:
            self.interaction.client.load_components(view)
        self.interaction.client.store_inter_token(self.interaction.id, self.interaction.token)
        resp = await self.interaction.client.http.edit_webhook_message(
            self.interaction.application_id,
            self.interaction.token,
            self.message.id,
            create_form(data, merge_fields(file, files))
        )
        data = await resp.json()
        return Message(data, self.interaction.client)


class InteractionResponse:
    """
    Represents a response message sent by an interaction
    """
    def __init__(self, interaction: "Interaction") -> None:
        self.interaction = interaction

    async def delete(self):
        """
        Deletes the response message.
        """
        await self.interaction.client.http.delete_webhook_message(
            self.interaction.application_id, self.interaction.token, "@original"
        )

    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[File] = MISSING,
        files: Optional[List[File]] = MISSING,
        suppress_embeds: Optional[bool] = MISSING,
    ) -> Message:
        """
        Edits the response message.

        Parameters
        ----------
        same as :meth:`Message.edit`
        """
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )
        if view is not MISSING and view:
            self.interaction.client.load_components(view)
        self.interaction.client.store_inter_token(self.interaction.id, self.interaction.token)
        resp = await self.interaction.client.http.edit_webhook_message(
            self.interaction.application_id, self.interaction.token, "@original",
            create_form(data, merge_fields(file, files))
        )
        data = await resp.json()
        return Message(data, self.interaction.client)

    async def followup(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[View] = None,
        tts: Optional[bool] = False,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
        ephemeral: Optional[bool] = False,
        suppress_embeds: Optional[bool] = False,
    ) -> FollowupResponse:
        """
        Sends a follow-up message to a deferred interaction

        Parameters
        ----------
        content: Optional[str]
            The content of the message to send
        embed: Optional[Embed]
            The embed to send with the message
        embeds: Optional[List[Embed]]
            The list of embeds to send with the message (max 10)
        view: Optional[View]
            The view to send with the message
        tts: Optional[bool]
            Whether the message should be sent as tts or not
        file: Optional[File]
            The file to send with the message
        files: Optional[List[File]]
            The list of files to send with the message
        ephemeral: Optional[bool]
            Whether the message should be ephemeral or not
        suppress_embeds: Optional[bool]
            Whether the message should suppress embeds or not
        """
        payload = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            suppress_embeds=suppress_embeds,
        )
        if view:
            self.interaction.client.store_inter_token(self.interaction.id, self.interaction.token)
            self.interaction.client.load_components(view)
        resp = await self.interaction.client.http.send_webhook_message(
            self.interaction.application_id, self.interaction.token, create_form(payload, merge_fields(file, files))
        )
        data = await resp.json()
        return FollowupResponse(data, self.interaction)
    
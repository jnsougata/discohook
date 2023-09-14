from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from .attachment import Attachment
from .embed import Embed
from .emoji import PartialEmoji
from .file import File
from .models import AllowedMentions, MessageReference
from .multipart import create_form
from .params import MISSING, handle_edit_params, merge_fields, handle_send_params
from .role import Role
from .user import User
from .view import View

if TYPE_CHECKING:
    from .client import Client


class MessageInteraction:
    """
    Represents a partial interaction received with message.
    """

    def __init__(self, client: "Client", payload: Dict[str, Any]) -> None:
        self.client = client
        self.data = payload

    @property
    def id(self) -> str:
        """
        The id of the interaction.
        """
        return self.data["id"]

    @property
    def token(self) -> str:
        """
        The token of the interaction.
        """
        return self.data["token"]

    @property
    def type(self) -> int:
        """
        The type of interaction.
        """
        return self.data["type"]

    @property
    def user(self) -> User:
        """
        The user who invoked the interaction.
        """
        return User(self.client, self.data["user"])


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

    def __init__(self, client: "Client", payload: Dict[str, Any]) -> None:
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
        return User(self.client, self.data["author"])

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
        return [User(self.client, x) for x in self.data.get("mentions", [])]

    @property
    def mention_roles(self) -> List[Role]:
        return [Role(self.client, x) for x in self.data.get("mention_roles", [])]

    @property
    def mention_channels(self) -> Optional[dict]:
        return self.data.get("mention_channels")

    @property
    def attachments(self) -> Optional[List[Attachment]]:
        attachments = self.data.get("attachments")
        if not attachments:
            return
        return [Attachment(x) for x in attachments]

    @property
    def embeds(self) -> Optional[List[Embed]]:
        embeds = self.data.get("embeds")
        if not embeds:
            return
        return [Embed.from_dict(x) for x in embeds]

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
    def interaction(self) -> Optional[MessageInteraction]:
        data = self.data.get("interaction")
        if not data:
            return
        return MessageInteraction(self.client, data)

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
        return await self.client.http.delete_channel_message(self.channel_id, self.id)

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
        if view and view is not MISSING:
            self.client.load_components(view)
        resp = await self.client.http.edit_channel_message(
            self.channel_id, self.id, create_form(data, merge_fields(file, files))
        )
        data = await resp.json()
        return Message(self.client, data)

    async def pin(self):
        """
        Pins the message to the channel.
        """
        return await self.client.http.pin_channel_message(self.channel_id, self.id)

    async def unpin(self):
        """
        Unpins the message from the channel.
        """
        return await self.client.http.unpin_channel_message(self.channel_id, self.id)

    async def reply(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[View] = None,
        tts: Optional[bool] = False,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
        allowed_mentions: Optional[AllowedMentions] = None,
        mention_author: Optional[bool] = None,
    ):
        """
        Replies to the message.

        Parameters
        ----------
        content: Optional[str]
            The content of the message.
        embed: Optional[Embed]
            The embed of the message.
        embeds: Optional[List[Embed]]
            The embeds of the message.
        view: Optional[View]
            The view of the message.
        tts: Optional[bool]
            Whether the message should be sent with text-to-speech.
        file: Optional[File]
            A file to send with the message.
        files: Optional[List[File]]
            A list of files to send with the message.
        allowed_mentions: Optional[AllowedMentions]
            The allowed mentions for the message.
        mention_author: Optional[bool]
            Whether the author should be mentioned.

        Returns
        -------
        Message
        """
        if mention_author is not None:
            if not allowed_mentions:
                allowed_mentions = AllowedMentions(replied_user=True)
            allowed_mentions["replied_user"] = True
        data = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            allowed_mentions=allowed_mentions,
            message_reference=MessageReference(message_id=self.id, channel_id=self.channel_id)
        )
        if view and view is not MISSING:
            self.client.load_components(view)
        resp = await self.client.http.send_message(self.channel_id, create_form(data, merge_fields(file, files)))
        data = await resp.json()
        return Message(self.client, data)

    async def add_reaction(self, emoji: Union[PartialEmoji, str]):
        """
        Creates a reaction on the message.

        Parameters
        ----------
        emoji: Union[Emoji, str]
            The emoji to react with.
        """

        if isinstance(emoji, PartialEmoji):
            encoded = f'{emoji.name}:{emoji.id}'
        else:
            encoded = "".join(f"%{byte:02x}" for byte in emoji.encode("utf-8"))
        return await self.client.http.create_message_reaction(self.channel_id, self.id, encoded)

    async def remove_reaction(self, emoji: Union[PartialEmoji, str], user_id: Optional[str] = None):
        """
        Removes a reaction on the message.

        Parameters
        ----------
        emoji: Union[Emoji, str]
            The emoji to delete.
        user_id: Optional[str]
            The user to delete the reaction of.
        """

        if isinstance(emoji, PartialEmoji):
            encoded = f'{emoji.name}:{emoji.id}'
        else:
            encoded = "".join(f"%{byte:02x}" for byte in emoji.encode("utf-8"))
        return await self.client.http.delete_message_reaction(self.channel_id, self.id, encoded, user_id or "@me")

    async def remove_reactions(self, emoji: Optional[Union[PartialEmoji, str]] = None):
        """
        Removes all reactions on the message.

        Parameters
        ----------
        emoji: Union[Emoji, str, None]
            The emoji to remove reactions of.
        """
        if isinstance(emoji, PartialEmoji):
            encoded = f'{emoji.name}:{emoji.id}'
        else:
            encoded = "".join(f"%{byte:02x}" for byte in emoji.encode("utf-8"))
        return await self.client.http.delete_all_message_reactions(self.id, self.channel_id, encoded)

from typing import TYPE_CHECKING, List, Optional

from .asset import Asset
from .channel import PartialChannel
from .embed import Embed
from .file import File
from .guild import PartialGuild
from .message import Message
from .multipart import create_form
from .params import MISSING, handle_edit_params, handle_send_params, merge_fields
from .user import User
from .view import View

if TYPE_CHECKING:
    from .client import Client


class Webhook:
    """
    Represents a Discord Application Owned Webhook.

    Properties
    ----------
    id: :class:`str`
        The id of the webhook.
    type: :class:`int`
        The type of the webhook.
    guild_id: Optional[:class:`str`]
        The id of the guild the webhook is in.
    channel_id: Optional[:class:`str`]
        The id of the channel the webhook is in.
    name: Optional[:class:`str`]
        The name of the webhook.
    avatar: Optional[:class:`Asset`]
        The avatar of the webhook.
    token: Optional[:class:`str`]
        The token of the webhook.
    application_id: Optional[:class:`str`]
        The id of the application the webhook belongs to.
    source_guild: Optional[:class:`PartialGuild`]
        The source guild of the webhook.
    source_channel: Optional[:class:`PartialChannel`]
        The source channel of the webhook.
    url: :class:`str`
        The url of the webhook.
    """

    def __init__(self, data: dict, client: "Client"):
        self.data = data
        self.client = client

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def type(self) -> int:
        return self.data["type"]

    @property
    def guild_id(self) -> Optional[str]:
        return self.data.get("guild_id")

    @property
    def channel_id(self) -> Optional[str]:
        return self.data.get("channel_id")

    @property
    def name(self) -> Optional[str]:
        return self.data.get("name")

    @property
    def avatar(self) -> Optional[Asset]:
        _hash = self.data.get("avatar")
        if _hash:
            return Asset(hash=_hash, fragment=f"avatars/{self.id}/")
        return None

    @property
    def token(self) -> Optional[str]:
        return self.data.get("token")

    @property
    def application_id(self) -> Optional[str]:
        return self.data.get("application_id")

    @property
    def source_guild(self) -> Optional[PartialGuild]:
        data = self.data.get("source_guild")
        if data:
            return PartialGuild(self.client, data["id"])
        return None

    @property
    def source_channel(self) -> Optional[PartialChannel]:
        data = self.data.get("source_channel")
        if data:
            return PartialChannel(self.client, data["id"])
        return None

    @property
    def url(self) -> Optional[str]:
        return self.data.get("url")

    @property
    def user(self) -> Optional[User]:
        data = self.data.get("user")
        if data:
            return User(self.client, data)

    async def delete(self):
        """
        Deletes the webhook.
        Returns
        -------
        None
        """
        await self.client.http.delete_webhook(self.id)

    async def edit(
        self,
        name: Optional[str] = None,
        image_base64: Optional[str] = None,
        channel_id: Optional[str] = None,
    ) -> "Webhook":
        """
        Edits the webhook.

        Parameters
        ----------
        name: Optional[:class:`str`]
            The new name of the webhook.
        image_base64: Optional[:class:`str`]
            The new avatar of the webhook.
        channel_id: Optional[:class:`str`]
            The new channel id of the webhook.
        Returns
        -------
        :class:`Webhook`

        Notes
        -----
        The image must be a base64 encoded string.
        All parameters are optional.
        """
        payload = {}
        if name:
            payload["name"] = name
        if image_base64:
            payload["avatar"] = image_base64
        if channel_id:
            payload["channel_id"] = channel_id
        resp = await self.client.http.edit_webhook(self.id, payload)
        data = await resp.json()
        return Webhook(data, self.client)

    async def send_message(
        self,
        content: Optional[str] = None,
        *,
        username: Optional[str] = None,
        avatar_url: Optional[str] = None,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
        tts: bool = False,
        view: Optional[View] = None,
        thread_name: Optional[str] = None,
    ) -> None:
        """
        Sends a message to the webhook.
        Parameters
        ----------
        content: Optional[:class:`str`]
            The content of the message.
        username:
            The username of the webhook.
        avatar_url:
            The avatar url of the webhook. (Overrides the webhook's avatar)
        embed: Optional[:class:`Embed`]
            The embed of the message.
        embeds: Optional[List[:class:`Embed`]]
            The embeds of the message.
        file: Optional[:class:`File`]
            The file of the message.
        files:
            The files of the message.
        tts: :class:`bool`
            Whether the message should be sent with text-to-speech.
        view: Optional[:class:`View`]
            The view to be sent with the message.
        thread_name: Optional[:class:`str`]
            The name of the thread to create.

        Returns
        -------
        None
        """
        payload = handle_send_params(content, tts=tts, embed=embed, embeds=embeds, file=file, files=files, view=view)
        if username:
            payload["username"] = username
        if avatar_url:
            payload["avatar_url"] = avatar_url
        if thread_name:
            payload["thread_name"] = thread_name
        if view:
            self.client.load_components(view)
        form = create_form(payload, merge_fields(file, files))
        await self.client.http.send_webhook_message(self.id, self.token, form)

    async def edit_message(
        self,
        message_id: str,
        *,
        content: Optional[str] = MISSING,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        file: Optional[File] = MISSING,
        files: Optional[List[File]] = MISSING,
        view: Optional[View] = MISSING,
    ) -> Message:
        """
        Edits a message from the webhook.

        Parameters
        ----------
        message_id: :class:`str`
            The id of the message to edit.
        content: Optional[:class:`str`]
            The new content of the message.
        embed: Optional[:class:`Embed`]
            The new embed to be sent with the message.
        embeds: Optional[List[:class:`Embed`]]
            The new embeds to be sent with the message.
        file: Optional[:class:`File`]
            The new file to be sent with the message.
        files: Optional[List[:class:`File`]]
            The new files to be sent with the message.
        view: Optional[:class:`View`]
            The new view to be sent with the message.

        Returns
        -------
        :class:`Message`
        """
        payload = handle_edit_params(content, embed=embed, embeds=embeds, file=file, files=files, view=view)
        if view:
            self.client.load_components(view)
        form = create_form(payload, merge_fields(file, files))
        resp = await self.client.http.edit_webhook_message(self.id, self.token, message_id, form)
        data = await resp.json()
        return Message(self.client, data)

    async def delete_message(self, message_id: str) -> None:
        """
        Deletes a message from the webhook.
        Parameters
        ----------
        message_id: :class:`str`
            The id of the message to delete.

        Returns
        -------
        None
        """
        await self.client.http.delete_webhook_message(self.id, self.token, message_id)

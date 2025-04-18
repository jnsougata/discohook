from typing import TYPE_CHECKING, List, Optional

import aiohttp

from .asset import Asset
from .channel import PartialChannel
from .embed import Embed
from .file import File
from .guild import PartialGuild
from .https import HTTPClient
from .message import Message
from .params import UNSPECIFIED, _prepare_editing_payload, _prepare_sending_payload
from .user import User
from .view import View

if TYPE_CHECKING:
    from .client import Client


# noinspection PyShadowingBuiltins
class PartialWebhook:

    def __init__(self, id: str, token: str):
        self.id = id
        self.token = token
        self.http = HTTPClient()

    async def send(
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
        thread_name: Optional[str] = None,
        wait: bool = False,
        thread_id: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
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
        thread_name: Optional[:class:`str`]
            The name of the thread to create.
        wait: :class:`bool`
            Waits for server confirmation of the message.
        thread_id: Optional[:class:`str`]
            Whether to send to a specified thread within the webhook's channel.

        Returns
        -------
        aiohttp.ClientResponse
        """

        extras = {
            "username": username,
            "avatar_url": avatar_url,
            "thread_name": thread_name,
        }
        params = {"wait": int(wait)}
        if thread_id:
            params["thread_id"] = thread_id
        payload = _prepare_sending_payload(
            content=content,
            tts=tts,
            embed=embed,
            embeds=embeds,
            file=file,
            files=files,
            **extras,
        )
        resp = await self.http.execute_webhook(self.id, self.token, payload, params)
        return resp

    @classmethod
    def from_url(cls, url: str) -> "PartialWebhook":
        return cls(*url.split("/")[-2:])


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

    def __init__(self, client: "Client", data: dict):
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

    async def delete(self, *, reason: Optional[str] = None):
        """
        Deletes the webhook.
        Returns
        -------
        None
        """
        await self.client.http.delete_webhook(self.id, reason=reason)

    async def edit(
        self,
        name: Optional[str] = None,
        image_base64: Optional[str] = None,
        channel_id: Optional[str] = None,
        reason: Optional[str] = None,
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
        resp = await self.client.http.modify_webhook(self.id, payload, reason=reason)
        data = await resp.json()
        return Webhook(self.client, data)

    async def send(
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
    ):
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
        extras = {
            "username": username,
            "avatar_url": avatar_url,
            "thread_name": thread_name,
        }

        payload = _prepare_sending_payload(
            content=content,
            tts=tts,
            embed=embed,
            embeds=embeds,
            file=file,
            files=files,
            view=view,
            **extras,
        )
        if view:
            self.client.load_view(view)
        return await self.client.http.send_webhook_message(self.id, self.token, payload)

    async def edit_message(
        self,
        message_id: str,
        *,
        content: Optional[str] = UNSPECIFIED,
        embed: Optional[Embed] = UNSPECIFIED,
        embeds: Optional[List[Embed]] = UNSPECIFIED,
        file: Optional[File] = UNSPECIFIED,
        files: Optional[List[File]] = UNSPECIFIED,
        view: Optional[View] = UNSPECIFIED,
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
        payload = _prepare_editing_payload(
            content=content,
            embed=embed,
            embeds=embeds,
            file=file,
            files=files,
            view=view,
        )
        if view:
            self.client.load_view(view)
        resp = await self.client.http.edit_webhook_message(
            self.id, self.token, message_id, payload
        )
        data = await resp.json()
        return Message(self.client, data)

    async def delete_message(self, message_id: str) -> aiohttp.ClientResponse:
        """
        Deletes a message from the webhook.

        Parameters
        ----------
        message_id: :class:`str`
            The id of the message to delete.

        Returns
        -------
        aiohttp.ClientResponse
        """
        return await self.client.http.delete_webhook_message(
            self.id, self.token, message_id
        )

    async def fetch_message(self, message_id: str, *, thread_id: Optional[str] = None):
        """
        Fetches a message sent by the webhook.

        Parameters
        ----------
        message_id: :class:`str`
            The id of the message to edit.
        thread_id: Optional[:class:`str`]
            The thread id the message is in.

        Returns
        -------
        :class:`Message`
        """
        params = {}
        if thread_id:
            params["thread_id"] = thread_id
        resp = await self.client.http.get_webhook_message(self.id, self.token, message_id, **params)
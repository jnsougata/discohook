from typing import TYPE_CHECKING, Optional, Union, Dict, Any

import aiohttp

from .asset import Asset
from .channel import PartialChannel
from .components import TextDisplay, MediaGallery, File, ActionRow, Section, Separator, Container
from .guild import PartialGuild
from .https import HTTPClient
from .message import Message
from .params import _prepare_payload
from .user import User
from .view import View

if TYPE_CHECKING:
    from .client import Client


# noinspection PyShadowingBuiltins
class Webhook:

    def __init__(
        self,
        data: Union[Dict[str, Any], str],
        client: Optional["Client"] = None,
    ):
        self.data = data
        self.client = client

    @classmethod
    def from_url(cls, url: str, *, client: Optional["Client"] = None) -> "Webhook":
        id, token = url.split("/")[-2:]
        data = {"id": id, "token": token, "type": 1}
        return cls(data, client=client)

    @classmethod
    async def fetch(cls, id: str, *, token: Optional[str] = None, client: Optional["Client"] = None):
        """
        Fetches the webhook from Discord.

        Returns
        -------
        :class:`Webhook`
            The fetched webhook.
        """
        if not client and token:
            resp = HTTPClient().get_webhook(id, token)
        elif client and not token:
            resp = await client.http.get_webhook(id)
        else:
            raise ValueError("Either client or token must be provided to fetch a webhook.")
        data = await resp.json()
        return cls(client=client, data=data)

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
    def token(self) -> str:
        return self.data.get("token", "")

    @property
    def application_id(self) -> Optional[str]:
        return self.data.get("application_id")

    @property
    def source_guild(self) -> Optional[Union[PartialGuild, Dict[str, Any]]]:
        data = self.data.get("source_guild")
        if data and self.client:
            return PartialGuild(self.client, data["id"])
        else:
            return data

    @property
    def source_channel(self) -> Optional[Union[PartialChannel, Dict[str, Any]]]:
        data = self.data.get("source_channel")
        if data and self.client:
            return PartialChannel(self.client, data["id"])
        else:
            return data

    @property
    def url(self) -> Optional[str]:
        return self.data.get("url")

    @property
    def user(self) -> Optional[Union[User, Dict[str, Any]]]:
        data = self.data.get("user")
        if data and self.client:
            return User(self.client, data)
        else:
            return data

    async def delete(self, *, reason: Optional[str] = None):
        """
        Deletes the webhook.
        Returns
        -------
        None
        """
        await self.client.http.delete_webhook(self.id, reason=reason)

    async def modify(
        self,
        name: Optional[str] = None,
        image_base64: Optional[str] = None,
        channel_id: Optional[str] = None,
        reason: Optional[str] = None
    ):
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
        reason: Optional[:class:`str`]
            The reason for editing the webhook to be logged.

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
        resp = await self.client.http.modify_webhook(self.id, payload, token=self.token, reason=reason)
        self.data = await resp.json()
        return self

    async def send(
        self,
        *components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container],
        username: Optional[str] = None,
        avatar_url: Optional[str] = None,
        thread_name: Optional[str] = None,
        wait: bool = False,
        thread_id: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
        """
        Sends a message to the webhook.

        Parameters
        ----------
        *components:
            Components to be sent with the message.
        username:
            The username of the webhook.
        avatar_url:
            The avatar url of the webhook. (Overrides the webhook's avatar)
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
        params = {
            "wait": "true" if wait else "false",
            "with_components": "true"
        }
        if thread_id:
            params["thread_id"] = thread_id
        payload = _prepare_payload(View.from_children(*components), **extras)
        http = HTTPClient()
        resp = await http.execute_webhook(self.id, self.token, payload, **params)
        await http.session.close()
        return resp

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
        return await self.client.http.get_webhook_message(
            self.id, self.token, message_id, **params
        )

    async def edit_message(
        self,
        message_id: str,
        *components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container],
        thread_id: Optional[str] = None
    ) -> Message:
        """
        Edits a message from the webhook.

        Parameters
        ----------
        message_id: :class:`str`
            The id of the message to edit.
        *components:
            Components to be sent with the message.
        thread_id: Optional[:class:`str`]
            The thread id the message is in.

        Returns
        -------
        :class:`Message`
        """
        payload = _prepare_payload(View.from_children(*components))
        resp = await self.client.http.edit_webhook_message(
            self.id, self.token, message_id, payload, thread_id=thread_id, with_components="true"
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

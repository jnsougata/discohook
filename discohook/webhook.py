from typing import TYPE_CHECKING, Optional

import aiohttp

from .components import TopLevelComponent
from .https import HTTPClient
from .message import Message
from .params import _prepare_payload
from .poll import Poll
from .view import View

if TYPE_CHECKING:
    from .client import Client


# noinspection PyShadowingBuiltins
class PartialWebhook:
    """
    Represents a Discord webhook with no authentication.

    Attributes:
        id (str): Discord webhook id.
        token (str): Discord webhook token.
        type (int): Discord webhook type.
        guild_id (str): Discord webhook guild id.
        channel_id (str): Discord webhook channel id.
        name (str): Discord webhook name.
        avatar (str): Discord webhook avatar hash.
        application_id (str): ID of the application that created it.
        source_guild (str): Guild of the channel that this webhook is following
            (returned for Channel Follower Webhooks).
        source_channel (str): Channel that this webhook is following
            (returned for Channel Follower Webhooks).
    """
    def __init__(self, *, id: str, token: str):
        self.id = id
        self.token = token
        self.type = 0
        self.guild_id = None
        self.channel_id = None
        self.name = None
        self.avatar = None
        self.application_id = None
        self.source_guild = None
        self.source_channel = None
        self.url = None
        self._http = HTTPClient()

    @classmethod
    def from_url(cls, url: str) -> "PartialWebhook":
        """
        Creates a webhook from a Discord webhook URL.

        Args:
            url (str): Discord webhook URL.

        Returns:
            PartialWebhook: Webhook object.
        """
        id, token = url.split("/")[-2:]
        return cls(id=id, token=token)

    @classmethod
    def from_data(cls, data: dict) -> "PartialWebhook":
        """
        Creates a webhook from a Discord webhook data.

        Args:
            data (dict): Discord webhook data.

        Returns:
            PartialWebhook: Webhook object.
        """
        webhook = cls(id=data["id"], token=data.get("token", ""))
        for key, value in data.items():
            setattr(webhook, key, value)
        return webhook

    async def resolve(self):
        """
        Populates the webhook attributes.
        """
        resp = await self._http.get_webhook_with_token(id=self.id, token=self.token)
        data = await resp.json()
        for k, v in data.items():
            setattr(self, k, v)

    async def delete(self):
        """
        Deletes the webhook.
        """
        await self._http.delete_webhook_with_token(id=self.id, token=self.token)

    async def modify(
        self,
        *,
        name: Optional[str] = None,
        image_base64: Optional[str] = None,
        channel_id: Optional[str] = None
    ):
        """
        Edits the webhook.

        Args:
            name (str | None): Name of the webhook.
            image_base64 (str | None): Avatar of the webhook as a base64 encoded string.
            channel_id (str | None): Channel id of the webhook.
        """
        payload = {}
        if name:
            payload["name"] = name
        if image_base64:
            payload["avatar"] = image_base64
        if channel_id:
            payload["channel_id"] = channel_id
        await self._http.modify_webhook_with_token(id=self.id, token=self.token, payload=payload)

    async def execute(
        self,
        *components: TopLevelComponent,
        poll: Optional[Poll] = None,
        username: Optional[str] = None,
        avatar_url: Optional[str] = None,
        thread_name: Optional[str] = None,
        wait: bool = False,
        thread_id: Optional[str] = None,
    ) -> aiohttp.ClientResponse:
        """
        Executes the webhook.

        Args:
            components (Tuple[TopLevelComponent]): Components to be sent with the message.
            poll (Poll | None): Poll to be sent with the message.
            username (str | None): Name of the webhook. (Overrides the default username)
            avatar_url (str | None): Avatar of the webhook. (Overrides the default avatar)
            thread_name (str | None): Name of the thread to create.
                (Requires the webhook channel to be a forum or media channel)
            wait (bool): Whether to wait for server confirmation of the message before responding.
            thread_id (str): Whether to send to a specified thread within the webhook's channel.

        Returns:
            aiohttp.ClientResponse: Response from the webhook.

        Raises:
            ValueError: If the webhook token is not set or resolved.
        """

        if not self.token:
            raise ValueError(
                "Webhook token is required. Set or resolve the webhook token.")
        extras = {
            "username": username,
            "avatar_url": avatar_url,
            "thread_name": thread_name,
        }
        params = {"wait": "true" if wait else "false", "with_components": "true"}
        if thread_id:
            params["thread_id"] = thread_id
        payload = _prepare_payload(View.from_children(*components), poll=poll, **extras)
        resp = await self._http.execute_webhook(id=self.id, token=self.token, data=payload, **params)
        return resp

    async def fetch_message(self, message_id: str, *, thread_id: Optional[str] = None):
        """
        Fetches a message sent by the webhook.

        Args:
            message_id (str): Message id to fetch.
            thread_id (str | None): ID of the thread the message is in.

        Returns:
            aiohttp.ClientResponse: Response from the webhook.

        Raises:
            ValueError: If the webhook token is not set or resolved.
        """
        if not self.token:
            raise ValueError(
                "Webhook token is required. Set or resolve the webhook token.")
        params = {}
        if thread_id:
            params["thread_id"] = thread_id
        return await self._http.get_webhook_message(
            id=self.id, token=self.token, message_id=message_id, **params
        )

    async def edit_message(
        self,
        message_id: str,
        *components: TopLevelComponent,
        thread_id: Optional[str] = None,
    ) -> Message:
        """
        Edits a message from the webhook.

        Args:
            message_id (str): Message id to edit.
            components (Tuple[TopLevelComponent]): Components to be sent with the message.
            thread_id (str | None): ID of the thread the message is in.

        Returns:
            aiohttp.ClientResponse: Response from the webhook.
        """
        payload = _prepare_payload(View.from_children(*components))
        params = {"with_components": "true"}
        if thread_id:
            params["thread_id"] = thread_id
        return await self._http.edit_webhook_message(
            id=self.id,
            token=self.token,
            message_id=message_id,
            data=payload,
            **params
        )

    async def delete_message(self, message_id: str) -> aiohttp.ClientResponse:
        """
        Deletes a message from the webhook.

        Args:
            message_id (str): Message id to delete.

        Returns:
            aiohttp.ClientResponse: Response from the webhook.
        """
        return await self._http.delete_webhook_message(
            id=self.id, token=self.token, message_id=message_id
        )


# noinspection PyShadowingBuiltins
class Webhook(PartialWebhook):
    """
    Represents a Discord webhook.
    """

    def __init__(self, client: "Client", *, id: str):
        super().__init__(id=id, token="")
        self.user = None
        self.client = client

    @classmethod
    async def from_data(cls, client: "Client", *, data: dict) -> "Webhook":
        webhook = Webhook(client=client, id=data["id"])
        for key, value in data.items():
            setattr(webhook, key, value)
        return webhook

    async def resolve(self):
        """
        Populates the webhook attributes.
        """
        resp = await self.client.http.get_webhook(id=self.id)
        data = await resp.json()
        for key, value in data.items():
            setattr(self, key, value)

    async def delete(self, *, reason: Optional[str] = None):
        """
        Deletes the webhook.

        Args:
            reason (str | None): Reason to delete the webhook. Shows up in audit log.
        """
        await self.client.http.delete_webhook(self.id, reason=reason)

    async def modify(
        self,
        name: Optional[str] = None,
        image_base64: Optional[str] = None,
        channel_id: Optional[str] = None,
        reason: Optional[str] = None,
    ):
        """
        Edits the webhook.

        Args:
            name (str | None): Name of the webhook.
            image_base64 (str | None): Avatar of the webhook as a base64 encoded string.
            channel_id (str | None): Channel id of the webhook.
            reason (str | None): Reason to edit the webhook. Shows up in audit log.

        Returns:
            Webhook: Modified webhook object.
        """
        payload = {}
        if name:
            payload["name"] = name
        if image_base64:
            payload["avatar"] = image_base64
        if channel_id:
            payload["channel_id"] = channel_id
        resp = await self.client.http.modify_webhook(
            self.id, payload, token=self.token, reason=reason
        )
        data = await resp.json()
        self.channel_id = data.get("channel_id")
        self.name = data.get("name")
        self.avatar = data.get("avatar")
        return self
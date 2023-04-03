from .user import User
from .embed import Embed
from .file import File
from .view import View
from .asset import Asset
from .guild import PartialGuild
from .channel import PartialChannel
from .multipart import create_form
from .message import Message
from typing import TYPE_CHECKING, Optional, List
from .params import handle_send_params, merge_fields, handle_edit_params, MISSING

if TYPE_CHECKING:
    from .client import Client


class Webhook:
    
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
        h = self.data.get("avatar")
        if h:
            return Asset(hash=h, fragment=f"avatars/{self.id}/")

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
            return PartialGuild(data["id"], self.client)

    @property
    def source_channel(self) -> Optional[PartialChannel]:
        data = self.data.get("source_channel")
        if data:
            return PartialChannel(data, self.client)

    @property
    def url(self) -> Optional[str]:
        return self.data.get("url")

    @property
    def user(self) -> Optional[User]:
        data = self.data.get("user")
        if data:
            return User(data, self.client)

    async def delete(self):
        await self.client.http.delete_webhook(self.id)

    async def edit(
        self,
        name: Optional[str] = None,
        image_base64: Optional[str] = None,
        channel_id: Optional[str] = None,
    ) -> "Webhook":
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
        payload = handle_edit_params(content, embed=embed, embeds=embeds, file=file, files=files, view=view)
        if view:
            self.client.load_components(view)
        form = create_form(payload, merge_fields(file, files))
        resp = await self.client.http.edit_webhook_message(self.id, self.token, message_id, form)
        data = await resp.json()
        return Message(data, self.client)

    async def delete_message(self, message_id: str) -> None:
        await self.client.http.delete_webhook_message(self.id, self.token, message_id)

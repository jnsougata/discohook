from .user import User
from .role import Role
from .https import request
from .embed import Embed
from .view import View
from typing import Optional, List, Dict, Any
from typing import TYPE_CHECKING
from .params import handle_edit_params, MISSING
if TYPE_CHECKING:
    from .client import Client
    from .interaction import Interaction


class Message:

    def __init__(self, payload: Dict[str, Any], client: "Client") -> None:
        self._client = client
        self.data = payload
        self.id = payload["id"]
        self.channel_id = payload["channel_id"]
        self.author = User(payload["author"])
        self.content = payload["content"]
        self.timestamp = payload["timestamp"]
        self.edited_timestamp = payload.get("edited_timestamp")
        self.tts = payload["tts"]
        self.mention_everyone = payload["mention_everyone"]
        self.mentions = [User(x) for x in payload["mentions"]]
        self.mention_roles = [Role(x) for x in payload["mention_roles"]]
        self.mention_channels = payload.get("mention_channels")
        self.attachments = payload["attachments"]
        self.embeds = payload["embeds"]
        self.reactions = payload.get("reactions")
        self.nonce = payload.get("nonce")
        self.pinned = payload["pinned"]
        self.webhook_id = payload.get("webhook_id")
        self.type = payload["type"]
        self.activity = payload.get("activity")
        self.application = payload.get("application")
        self.application_id = payload.get("application_id")
        self.message_reference = payload.get("message_reference")
        self.flags = payload.get("flags")
        self.referenced_message = payload.get("referenced_message")
        self.interaction = payload.get("interaction")
        self.thread = payload.get("thread")
        self.components = payload.get("components")
        self.sticker_items = payload.get("sticker_items")
        self.stickers = payload.get("stickers")
        self.position = payload.get("position")
    
    async def delete(self):
        await request(
            "DELETE",
            path=f"/channels/{self.channel_id}/messages/{self.id}",
            session=self._client.session,
        )
    
    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[Dict[str, Any]] = MISSING,
        files: Optional[List[Dict[str, Any]]] = MISSING,
        supress_embeds: Optional[bool] = MISSING,
    ) -> "Message":
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            supress_embeds=supress_embeds,
        )
        if view:
            for component in view.children:
                self._client.load_component(component)
        return Message(
            await request(
                "PATCH",
                path=f"/channels/{self.channel_id}/messages/{self.id}",
                session=self._client.session,
                json=data,
            ), self._client)


class FollowupMessage(Message):
    def __init__(self, payload: dict, interaction: "Interaction") -> None:
        super().__init__(payload, interaction.client)
        self.interaction = interaction

    async def delete(self):
        await request(
            "DELETE",
            path=f"/webhooks/{self.interaction.application_id}/{self.interaction.token}/messages/{self.id}",
            session=self.interaction.client.session,  # noqa
        )

    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[Dict[str, Any]] = MISSING,
        files: Optional[List[Dict[str, Any]]] = MISSING,
        supress_embeds: Optional[bool] = MISSING,
    ) -> Message:
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            supress_embeds=supress_embeds,
        )
        if view is not MISSING and view:
            for component in view.children:
                self.interaction.client.load_component(component)
        self.interaction.client.store_inter_token(self.interaction.id, self.interaction.token)
        resp = await request(
            "PATCH",
            path=f"/webhooks/{self.interaction.application_id}/{self.interaction.token}/messages/{self.id}",
            session=self.interaction.client.session,
            json=data,
        )
        return Message(resp, self.interaction.client)


class ResponseMessage(Message):
    def __init__(self, payload: dict, interaction: "Interaction") -> None:
        super().__init__(payload, interaction.client)
        self.interaction = interaction

    async def delete(self):
        await request(
            "DELETE",
            path=f"/webhooks/{self.interaction.application_id}/{self.interaction.token}/messages/@original",
            session=self.interaction.client.session,
        )

    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[Dict[str, Any]] = MISSING,
        files: Optional[List[Dict[str, Any]]] = MISSING,
        supress_embeds: Optional[bool] = MISSING,
    ) -> Message:
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            supress_embeds=supress_embeds,
        )
        if view is not MISSING and view:
            for component in view.children:
                self.interaction.client.load_component(component)
        self.interaction.client.store_inter_token(self.interaction.id, self.interaction.token)
        resp = await request(
            "PATCH",
            path=f"/webhooks/{self.interaction.application_id}/{self.interaction.token}/messages/@original",
            session=self.interaction.client.session,
            json=data,
        )
        return Message(resp, self.interaction.client)

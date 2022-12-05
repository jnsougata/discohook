from .enums import InteractionType, InteractionCallbackType
from typing import Any, Dict, Optional, List, Union, TYPE_CHECKING
from fastapi.responses import JSONResponse
from .embed import Embed
from .user import User
from .member import Member
from .component import View
from .modal import Modal
from .https import request
from .option import Choice
from fastapi.requests import Request
from .messgae import Message, ResponseMessage, FollowupMessage
from .param_handler import handle_edit_params, handle_send_params, MISSING
if TYPE_CHECKING:
    from .client import Client


class CommandData:
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data['id']
        self.name: str = data['name']
        self.type: int = data['type']
        self.guild_id: Optional[str] = data.get('guild_id')
        self.target_id: Optional[str] = data.get('target_id')
        self.resolved: Optional[Dict[str, Any]] = data.get('resolved')
        self.options: Optional[List[Dict[str, Any]]] = data.get('options')


class Interaction:

    def __init__(self, data: Dict[str, Any], request: Request):
        self._payload = data
        self.request: Request = request
        self.client: 'Client' = request.app
        self.id: str = data['id']
        self.type: int = data['type']
        self.token: str = data['token']
        self.version: int = data['version']
        self.application_id: str = data['application_id']
        self.data: Optional[Dict[str, Any]] = data.get('data')
        self.guild_id: Optional[str] = data.get('guild_id')
        self.channel_id: Optional[str] = data.get('channel_id')
        self.member: Optional[Dict[str, Any]] = data.get('member')
        self.user: Optional[Dict[str, Any]] = data.get('user')
        self.message: Optional[Dict[str, Any]] = data.get('message')
        self.app_permissions: Optional[int] = data.get('app_permissions')
        self.locale: Optional[str] = data.get('locale')
        self.guild_locale: Optional[str] = data.get('guild_locale')

    @property
    def owner(self) -> Optional[User]:
        if not self.message:
            return None
        return User(self.message["interaction"]["user"])

    @property
    def from_owner(self) -> bool:
        if not self.message:
            return True
        return self.owner == self.author

    @property
    def author(self) -> Optional[Union[User, Member]]:
        if self.guild_id:
            self.member.update(self.member.pop("user", {}))
            return Member(self.member)
        return User(self.user)

    @property
    def command_data(self) -> Optional[CommandData]:
        if self.type == InteractionType.app_command.value:
            return CommandData(self.data)
        return None

    async def send_modal(self, modal: Modal):
        self.client.ui_factory[modal.custom_id] = modal
        payload = {
            "data": modal.json(),
            "type": InteractionCallbackType.modal.value,
        }
        await request(
            method="POST",
            path=f"/interactions/{self.id}/{self.token}/callback",
            session=self.client._session, json=payload,
        )

    async def send_autocomplete(self, choices: List[Choice]):
        payload = {
            "type": InteractionCallbackType.autocomplete_result.value,
            "data": {"choices": [choice.json() for choice in choices]}
        }
        await request(
            method="POST",
            path=f"/interactions/{self.id}/{self.token}/callback",
            session=self.client._session,
            json=payload
        )

    async def defer(self, ephemeral: bool = False):
        payload = {
            "type": InteractionCallbackType.deferred_channel_message_with_source.value,
        }
        if ephemeral:
            payload["data"] = {"flags": 64}
        await request(
            method="POST", 
            path=f"/interactions/{self.id}/{self.token}/callback", 
            session=self.client._session, 
            json=payload
        )
    
    async def response(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[View] = None,
        tts: Optional[bool] = False,
        file: Optional[Dict[str, Any]] = None,
        files: Optional[List[Dict[str, Any]]] = None,
        ephemeral: Optional[bool] = False,
        supress_embeds: Optional[bool] = False,
    ) -> None:
        data = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            components=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            supress_embeds=supress_embeds
        )
        if view:
            for component in view._children:  # noqa
                self.client._load_component(component)  # noqa
        self.client._load_inter_token(self.id, self.token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        await request(
            "POST",
            path=f"/interactions/{self.id}/{self.token}/callback",
            session=self.client._session,
            json=payload,
        )

    
    async def follow_up(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        components: Optional[View] = None,
        tts: Optional[bool] = False,
        file: Optional[Dict[str, Any]] = None,
        files: Optional[List[Dict[str, Any]]] = None,
        ephemeral: Optional[bool] = False,
        supress_embeds: Optional[bool] = False,
    ) -> FollowupMessage:
        payload = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            components=components,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            supress_embeds=supress_embeds
        )
        if components:
            for component in components._children:
                self.client._load_component(component)
        self.client._load_inter_token(self.id, self.token)
        data  = await request(
            method="POST",
            path=f"/webhooks/{self.application_id}/{self.token}",
            session=self.client._session,
            json=payload,
        )
        return FollowupMessage(data, self)
    
    async def original_response(self) -> ResponseMessage:
        resp = await request(
            path=f"/webhooks/{self.application_id}/{self.token}/messages/@original",
            session=self.client._session
        )
        return ResponseMessage(resp, self)


class ComponetInteraction(Interaction):

    def __init__(self, data: Dict[str, Any], request: Request):
        super().__init__(data, request)

    async def follow_up(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[View] = None,
        tts: Optional[bool] = False,
        file: Optional[Dict[str, Any]] = None,
        files: Optional[List[Dict[str, Any]]] = None,
        ephemeral: Optional[bool] = False,
        supress_embeds: Optional[bool] = False,
    ) -> FollowupMessage:
        data = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            components=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            supress_embeds=supress_embeds
        )
        if view:
            for component in view._children:  # noqa
                self.client._load_component(component)  # noqa
        self.client._load_inter_token(self.id, self.token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        resp = await request(
            "POST",
            path=f"/interactions/{self.id}/{self.token}/callback",
            session=self.client._session, json=payload,
        )
        return FollowupMessage(resp, self)

    async def edit_original(
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
            components=view,
            tts=tts,
            file=file,
            files=files,
            supress_embeds=supress_embeds
        )
        if view is not MISSING and view:
            for component in view._children:  # noqa
                self.client._load_component(component)  # noqa
        self.client._load_inter_token(self.id, self.token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.update_message.value,
        }
        resp = await request(
            "POST",
            path=f"/interactions/{self.id}/{self.token}/callback",
            session=self.client._session, json=payload,
        )
        return Message(resp)

    @property
    def origin(self) -> Optional[str]:
        if not self.message:
            return
        parent_id = self.message["interaction"]["id"]
        return self.client.cached_inter_tokens.get(parent_id, '')

    async def original_message(self) -> Message:
        if not self.origin:
            return
        resp = await request(
            path=f"/webhooks/{self.application_id}/{self.origin}/messages/@original",
            session=self.client._session
        )
        return Message(resp)

    async def delete_original(self):
        if not self.origin:
            return
        self.client.cached_inter_tokens.pop(self.id, None)
        await request(
            method="DELETE",
            path=f"/webhooks/{self.application_id}/{self.origin}/messages/@original",
            session=self.client._session, 
        )
    
    
class CommandInteraction(Interaction):

    def __init__(self, data: Dict[str, Any], request: Request):
        super().__init__(data, request)

    async def response(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[View] = None,
        tts: Optional[bool] = False,
        file: Optional[Dict[str, Any]] = None,
        files: Optional[List[Dict[str, Any]]] = None,
        ephemeral: Optional[bool] = False,
        supress_embeds: Optional[bool] = False,
    ) -> None:
        data = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            components=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            supress_embeds=supress_embeds
        )
        if view:
            for component in view._children:  # noqa
                self.client._load_component(component)  # noqa
        self.client._load_inter_token(self.id, self.token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        await request(
            "POST",
            path=f"/interactions/{self.id}/{self.token}/callback",
            session=self.client._session,
            json=payload,
        )
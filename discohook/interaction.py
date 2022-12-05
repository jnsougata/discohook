from .enums import InteractionType, InteractionCallbackType
from typing import Any, Dict, Optional, List, Union, TYPE_CHECKING
from fastapi.responses import JSONResponse
from .embed import Embed
from .user import User
from .member import Member
from .component import View
from .modal import Modal
from .https import request, HTTPClient
from .option import Choice
from fastapi.requests import Request
if TYPE_CHECKING:
    from .client import Client

MISSING = object()
NO_AUTH_HEADER = {"Content-Type": "application/json"}

def handle_send_params(
    content: Optional[str] = None,
    *,
    embed: Optional[Embed] = None,
    embeds: Optional[List[Embed]] = None,
    components: Optional[View] = None,
    tts: Optional[bool] = False,
    file: Optional[Dict[str, Any]] = None,
    files: Optional[List[Dict[str, Any]]] = None,
    ephemeral: Optional[bool] = False,
    supress_embeds: Optional[bool] = False
):
    payload = {}
    flag_value = 0
    if embed:
        if not embeds:
            embeds = []
        embeds.append(embed)
    if file:
        if not files:
            files = []
        files.append(file)
    if ephemeral:
        flag_value |= 1 << 6
    if supress_embeds:
        flag_value |= 1 << 2
    if content:
        payload["content"] = str(content)
    if tts:
        payload["tts"] = True
    if embeds:
        payload["embeds"] = [embed.json() for embed in embeds]
    if components:
        payload["components"] = components.json()
    if files:
        payload["attachments"] = files
    if flag_value:
        payload["flags"] = flag_value

    return payload


def handle_edit_params(
    content: Optional[str] = MISSING,
    *,
    embed: Optional[Embed] = MISSING,
    embeds: Optional[List[Embed]] = MISSING,
    components: Optional[View] = MISSING,
    tts: Optional[bool] = MISSING,
    file: Optional[Dict[str, Any]] = MISSING,
    files: Optional[List[Dict[str, Any]]] = MISSING,
    supress_embeds: Optional[bool] = MISSING,
):
    payload = {}
    if embed is None:
        embeds = []
    if file is None:
        files = []
    if components is None:
        components = []
    if content is not MISSING:
        payload["content"] = str(content)
    if tts is not MISSING:
        payload["tts"] = tts
    if embeds is not MISSING:
        payload["embeds"] = [embed.json() for embed in embeds]
    if components is not MISSING:
        payload["components"] = components.json() if components else []
    if files is not MISSING:
        payload["attachments"] = files
    if supress_embeds is not MISSING:
        payload["flags"] = 1 << 2

    return payload


class CommandData:
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data['id']
        self.name: str = data['name']
        self.type: int = data['type']
        self.guild_id: Optional[str] = data.get('guild_id')
        self.target_id: Optional[str] = data.get('target_id')
        self.resolved: Optional[Dict[str, Any]] = data.get('resolved')
        self.options: Optional[List[Dict[str, Any]]] = data.get('options')


class CommandInteraction:
    def __init__(self, client: "Client", data: Dict[str, Any]):
        self.client = client
        self.interaction_id = data["id"]
        self.interaction_token = data["token"]
            
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
        self.client._load_inter_token(self.interaction_id, self.interaction_token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        await request(
            "POST",
            path=f"/interactions/{self.interaction_id}/{self.interaction_token}/callback",
            session=self.client._session,
            json=payload,
        )



class ComponentInteraction:
    def __init__(self, client: "Client", data: Dict[str, Any]):
        self.client = client
        self.interaction_id = data["id"]
        self.interaction_token = data["token"]
        self.application_id = data["application_id"]
        self.message = data.get("message")

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
    ):
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
        self.client._load_inter_token(self.interaction_id, self.interaction_token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        return await request(
            "POST",
            path=f"/interactions/{self.interaction_id}/{self.interaction_token}/callback",
            session=self.client._session, json=payload,
        )

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
    ):
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
        self.client._load_inter_token(self.interaction_id, self.interaction_token)  # noqa
        payload = {
            "data": data,
            "type": InteractionCallbackType.update_message.value,
        }
        return await request(
            "POST",
            path=f"/interactions/{self.interaction_id}/{self.interaction_token}/callback",
            session=self.client._session, json=payload,
        )

    @property
    def origin(self) -> str:
        if self.message:
            parent_id = self.message["interaction"]["id"]
            return self.client.cached_inter_tokens.get(parent_id, '')
        return ''

    async def fetch_original(self):
        if not self.origin:
            return
        self.client._populated_return = None
        return await request(
            path=f"/webhooks/{self.application_id}/{self.origin}/messages/@original",
            headers=NO_AUTH_HEADER,
            session=self.client._session
        )

    async def delete_original(self):
        if not self.origin:
            return
        self.client.cached_inter_tokens.pop(self.interaction_id, None)
        self.client._populated_return = None
        await request(
            method="DELETE",
            path=f"/webhooks/{self.application_id}/{self.origin}/messages/@original",
            session=self.client._session, 
            headers=NO_AUTH_HEADER,
        )



class Interaction:

    def __init__(self, data: Dict[str, Any]):
        self._payload = data
        self.request: Optional[Request] = None
        self.client: Optional['Client'] = None
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

    @property
    def component(self) -> ComponentInteraction:
        return ComponentInteraction(self.client, self._payload)

    @property
    def command(self) -> CommandInteraction:
        return CommandInteraction(self.client, self._payload)

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
    ) -> JSONResponse:
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
        # TODO: parse the response as a message
        return await request(
            method="POST",
            path=f"/webhooks/{self.application_id}/{self.token}",
            session=self.client._session,
            json=payload,
        )
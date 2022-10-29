from .enums import InteractionType, InteractionCallbackType
from typing import Any, Dict, Optional, List, Union, TYPE_CHECKING
from fastapi.responses import JSONResponse
from .embed import Embed
from .models import User, Member
from .component import ActionRows
from .modal import Modal
from .https import request
if TYPE_CHECKING:
    from .client import Client

MISSING = object()


def handle_send_params(
    content: Optional[str] = None,
    *,
    embed: Optional[Embed] = None,
    embeds: Optional[List[Embed]] = None,
    components: Optional[ActionRows] = None,
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
            components: Optional[ActionRows] = MISSING,
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
    def __init__(self, app: "Client", data: Dict[str, Any]):
        self._app = app
        self._id = data["id"]
        self._token = data["token"]

    async def response(
            self,
            content: Optional[str] = None,
            *,
            embed: Optional[Embed] = None,
            embeds: Optional[List[Embed]] = None,
            components: Optional[ActionRows] = None,
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
            for component in components._children:  # noqa
                self._app._load_component(component)  # noqa
        self._app._load_inter_token(self._id, self._token)  # noqa
        return JSONResponse(
            {
                "data": payload,
                "type": InteractionCallbackType.channel_message_with_source.value,
            },
            status_code=200
        )


class ComponentInteraction:
    def __init__(self, app: "Client", data: Dict[str, Any]):
        self._app = app
        self._id = data["id"]
        self._token = data["token"]
        self._application_id = data["application_id"]
        self._message = data.get("message")

    async def follow_up(
            self,
            content: Optional[str] = None,
            *,
            embed: Optional[Embed] = None,
            embeds: Optional[List[Embed]] = None,
            components: Optional[ActionRows] = None,
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
            for component in components._children:  # noqa
                self._app._load_component(component)  # noqa
        self._app._load_inter_token(self._id, self._token)  # noqa
        return JSONResponse(
            {
                "data": payload,
                "type": InteractionCallbackType.channel_message_with_source.value,
            },
            status_code=200
        )

    def edit(
            self,
            content: Optional[str] = MISSING,
            *,
            embed: Optional[Embed] = MISSING,
            embeds: Optional[List[Embed]] = MISSING,
            components: Optional[ActionRows] = MISSING,
            tts: Optional[bool] = MISSING,
            file: Optional[Dict[str, Any]] = MISSING,
            files: Optional[List[Dict[str, Any]]] = MISSING,
            supress_embeds: Optional[bool] = MISSING,
    ):
        payload = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            components=components,
            tts=tts,
            file=file,
            files=files,
            supress_embeds=supress_embeds
        )
        if components is not MISSING and components:
            for component in components._children:  # noqa
                self._app._load_component(component)  # noqa
        self._app._load_inter_token(self._id, self._token)  # noqa
        return JSONResponse(
            {
                "data": payload,
                "type": InteractionCallbackType.update_message.value,
            },
            status_code=200
        )

    @property
    def _origin_token(self):
        if self._message:
            parent_id = self._message["interaction"]["id"]
            return self._app.cached_inter_tokens.get(parent_id, '')
        return ''

    async def fetch_original(self):
        if not self._origin_token:
            return
        return await request("GET", f"/webhooks/{self._application_id}/{self._origin_token}/messages/@original")

    async def delete_original(self):
        if not self._origin_token:
            return
        self._app.cached_inter_tokens.pop(self._id, None)
        await request("DELETE", f"/webhooks/{self._application_id}/{self._origin_token}/messages/@original")

    async def edit_original(
            self,
            content: Optional[str] = MISSING,
            *,
            embed: Optional[Embed] = MISSING,
            embeds: Optional[List[Embed]] = MISSING,
            components: Optional[ActionRows] = MISSING,
            tts: Optional[bool] = MISSING,
            file: Optional[Dict[str, Any]] = MISSING,
            files: Optional[List[Dict[str, Any]]] = MISSING,
            supress_embeds: Optional[bool] = MISSING,
    ):
        payload = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            components=components,
            tts=tts,
            file=file,
            files=files,
            supress_embeds=supress_embeds
        )
        if components is not MISSING and components:
            for component in components._children:  # noqa
                self._app._load_component(component)  # noqa
        self._app._load_inter_token(self._id, self._token)  # noqa
        if not self._origin_token:
            return
        return await request(
            "PATCH", f'/webhooks/{self._application_id}/{self._origin_token}/messages/@original', json=payload)


class Interaction:

    def __init__(self, data: Dict[str, Any]):
        self._raw_data = data
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
    def original_author(self) -> Optional[User]:
        if not self.message:
            return None
        return User(self.message["interaction"]["user"])

    @property
    def from_original_author(self) -> bool:
        if not self.message:
            return True
        return self.original_author.id == self.author.id

    @property
    def author(self) -> Optional[Union[User, Member]]:
        if self.guild_id:
            self.member.update(self.member.pop("user"))
            return Member(self.member)
        return User(self.user)

    @property
    def _app_command_data(self) -> Optional[CommandData]:
        if self.type == InteractionType.app_command.value:
            return CommandData(self.data)
        return None

    @property
    def component(self) -> ComponentInteraction:
        return ComponentInteraction(self.client, self._raw_data)

    @property
    def command(self) -> CommandInteraction:
        return CommandInteraction(self.client, self._raw_data)

    async def send_modal(self, modal: Modal):
        self.client.ui_factory[modal.custom_id] = modal
        return JSONResponse(
            {
                "data": modal.json(),
                "type": InteractionCallbackType.modal.value,
            },
            status_code=200
        )

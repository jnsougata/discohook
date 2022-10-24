from .enums import interaction_types, callback_types
from typing import Any, Dict, Optional, List
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from .embed import Embed
from .component import Components
import aiohttp

MISSING = object()


class CommandData(BaseModel):
    id: str
    name: str
    type: int
    guild_id: Optional[str] = None
    target_id: Optional[str] = None
    resolved: Optional[Dict[str, Any]] = None
    options: Optional[List[Dict[str, Any]]] = None


class Interaction(BaseModel):
    app: Any
    id: str
    type: int
    token: str
    version: int
    application_id: str
    data: Optional[Dict[str, Any]] = None
    guild_id: Optional[str] = None
    channel_id: Optional[str] = None
    member: Optional[Dict[str, Any]] = None
    user: Optional[Dict[str, Any]] = None
    message: Optional[Dict[str, Any]] = None
    app_permissions: Optional[int] = None
    locale: Optional[str] = None
    guild_locale: Optional[str] = None

    @property
    def app_command_data(self) -> Optional[CommandData]:
        if self.type == interaction_types.app_command.value:
            return CommandData(**self.data)
        return None

    def response(
            self,
            content: Optional[str] = None,
            *,
            embed: Optional[Embed] = None,
            embeds: Optional[List[Embed]] = None,
            components: Optional[Components] = None,
            tts: Optional[bool] = False,
            file: Optional[Dict[str, Any]] = None,
            files: Optional[List[Dict[str, Any]]] = None,
            ephemeral: Optional[bool] = False,
            supress_embeds: Optional[bool] = False,
    ) -> JSONResponse:
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
            payload["embeds"] = [embed.to_json() for embed in embeds]
        if components:
            payload["components"] = components.to_json()
            for component in components._items:  # noqa
                self.app.ui_factory[component.custom_id] = component
        if files:
            payload["attachments"] = files
        if flag_value:
            payload["flags"] = flag_value

        return JSONResponse(
            {
                "data": payload, "type": callback_types.channel_message_with_source.value,
            },
            status_code=200
        )

    def edit(
            self,
            content: Optional[str] = MISSING,
            *,
            embed: Optional[Embed] = MISSING,
            embeds: Optional[List[Embed]] = MISSING,
            components: Optional[Components] = MISSING,
            tts: Optional[bool] = MISSING,
            file: Optional[Dict[str, Any]] = MISSING,
            files: Optional[List[Dict[str, Any]]] = MISSING,
            supress_embeds: Optional[bool] = MISSING,
    ):
        data = {}
        if embed is None:
            embeds = []
        if file is None:
            files = []
        if components is None:
            components = []
        if content is not MISSING:
            data["content"] = str(content)
        if tts is not MISSING:
            data["tts"] = tts
        if embeds is not MISSING:
            data["embeds"] = [embed.to_json() for embed in embeds]
        if components is not MISSING:
            data["components"] = components.to_json() if components else []
            if components:
                for component in components._items: # noqa
                    self.app.ui_factory[component.custom_id] = component
        if files is not MISSING:
            data["attachments"] = files
        if supress_embeds is not MISSING:
            data["flags"] = 1 << 2
        return JSONResponse(
            {
                "data": data, "type": callback_types.update_message.value,
            },
            status_code=200
        )

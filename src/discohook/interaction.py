from .enums import interaction_types, callback_types
from typing import Any, Dict, Optional, List
from pydantic import BaseModel
from fastapi.responses import JSONResponse


class CommandData(BaseModel):
    id: str
    name: str
    type: int
    guild_id: Optional[str] = None
    target_id: Optional[str] = None
    resolved: Optional[Dict[str, Any]] = None
    options: Optional[List[Dict[str, Any]]] = None


class Interaction(BaseModel):
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

    @staticmethod
    def response(
            content: Optional[str] = None,
            *,
            embed: Optional[Dict[str, Any]] = None,
            embeds: Optional[List[Dict[str, Any]]] = None,
            component: Optional[Dict[str, Any]] = None,
            components: Optional[List[Dict[str, Any]]] = None,
            tts: Optional[bool] = False,
            file: Optional[Dict[str, Any]] = None,
            files: Optional[List[Dict[str, Any]]] = None,
            ephemeral: Optional[bool] = False,
            supress_embeds: Optional[bool] = False,
    ) -> JSONResponse:
        payload = {}
        embeds_container = []
        components_container = []
        attachments_container = []
        flag_value = 0
        if embed:
            embeds_container.append(embed)
        if embeds:
            embeds_container.extend(embeds)
        if component:
            components_container.append(component)
        if components:
            components_container.extend(components)
        if file:
            attachments_container.append(file)
        if files:
            attachments_container.extend(files)
        if ephemeral:
            flag_value |= 1 << 6
        if supress_embeds:
            flag_value |= 1 << 2
        if content:
            payload["content"] = str(content)
        if tts:
            payload["tts"] = True
        if embeds_container:
            payload["embeds"] = embeds_container
        if components_container:
            payload["components"] = components_container
        if attachments_container:
            payload["attachments"] = attachments_container
        if flag_value:
            payload["flags"] = flag_value

        return JSONResponse(
            {
                "type": callback_types.channel_message_with_source.value,
                "data": payload
            },
            status_code=200
        )


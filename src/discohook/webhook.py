from .enums import interaction_types, try_enum
from typing import Any, Dict, Optional, List
from dataclasses import dataclass
from fastapi.responses import JSONResponse
from .utils import MISSING


@dataclass
class Webhook:
    id: str
    type: int
    token: str
    application_id: str
    guild_id: Optional[str] = None
    channel_id: Optional[str] = None

    @staticmethod
    def send(
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Dict[str, Any]] = MISSING,
        embeds: Optional[List[Dict[str, Any]]] = MISSING,
        component: Optional[Dict[str, Any]] = MISSING,
        components: Optional[List[Dict[str, Any]]] = MISSING,
        tts: Optional[bool] = False,
        file: Optional[Dict[str, Any]] = MISSING,
        files: Optional[List[Dict[str, Any]]] = MISSING,
        ephemeral: Optional[bool] = MISSING,
        supress_embeds: Optional[bool] = MISSING,
    ) -> JSONResponse:
        payload = {}
        if content is not MISSING:
            payload["content"] = str(content)
        payload["embeds"] = []
        payload["components"] = []
        payload["attachments"] = []
        payload["flags"] = 0
        if embed is not MISSING:
            payload["embeds"].append(embed)
        if embeds is not MISSING:
            payload["embeds"].extend(embeds)
        if component is not MISSING:
            payload["components"].append(component)
        if components is not MISSING:
            payload["components"].extend(components)
        if ephemeral is not MISSING:
            payload["flags"] |= 1 << 6
        if supress_embeds is not MISSING:
            payload["flags"] |= 1 << 2
        if tts:
            payload["tts"] = True
        if file is not MISSING:
            payload["attachments"].append(file)
        if files is not MISSING:
            payload["attachments"].extend(files)
        return JSONResponse(content=payload, status_code=200)


from typing import Optional, List, Dict, Any
from .embed import Embed
from .view import View


MISSING = object()


def handle_send_params(
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
        payload["embeds"] = [embed.to_dict() for embed in embeds]
    if view:
        payload["components"] = view.components
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
    view: Optional[View] = MISSING,
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
    if view is None:
        view = []
    if content is not MISSING:
        payload["content"] = str(content)
    if tts is not MISSING:
        payload["tts"] = tts
    if embeds is not MISSING:
        payload["embeds"] = [embed.to_dict() for embed in embeds]
    if view is not MISSING:
        payload["components"] = view.components if view else []
    if files is not MISSING:
        payload["attachments"] = files
    if supress_embeds is not MISSING:
        payload["flags"] = 1 << 2

    return payload

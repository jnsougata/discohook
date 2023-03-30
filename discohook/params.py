from .file import File
from .view import View
from .embed import Embed
from typing import Optional, List, Dict, Any


MISSING = object()

def merge_fields(filed: Optional[Any] , fileds: Optional[List[Any]]) -> List[Any]:
    tmp = []
    if filed:
        tmp.append(filed)
    if fileds:
        tmp.extend(fileds)
    return tmp

def handle_send_params(
    content: Optional[str] = None,
    *,
    embed: Optional[Embed] = None,
    embeds: Optional[List[Embed]] = None,
    view: Optional[View] = None,
    tts: Optional[bool] = False,
    file: Optional[File] = None,
    files: Optional[List[File]] = None,
    ephemeral: Optional[bool] = False,
    supress_embeds: Optional[bool] = False,
):
    payload = {}
    flag_value = 0
    embeds = merge_fields(embed, embeds)
    files = merge_fields(file, files)
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
        payload["attachments"] = [
            {
                "id": i,
                "filename": file.name,
                "ephemeral": file.spoiler,
                "description": file.description,
            }
            for i, file in enumerate(files)
        ]
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
    file: Optional[File] = MISSING,
    files: Optional[List[File]] = MISSING,
    supress_embeds: Optional[bool] = MISSING,
):
    payload = {}
    embeds = merge_fields(embed, embeds)
    files = merge_fields(file, files)
    if content is not MISSING:
        payload["content"] = str(content)
    if tts is not MISSING:
        payload["tts"] = tts
    if embeds is not MISSING:
        payload["embeds"] = [embed.to_dict() for embed in embeds]
    if view is not MISSING:
        payload["components"] = view.components if view else []
    if files is not MISSING:
        payload["attachments"] = [
            {
                "id": i,
                "filename": file.name,
                "ephemeral": file.spoiler,
                "description": file.description,
            }
            for i, file in enumerate(files)
        ] if files else []
    if supress_embeds is not MISSING:
        payload["flags"] = 1 << 2

    return payload

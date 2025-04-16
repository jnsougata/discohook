import json
import mimetypes
from enum import Enum, IntEnum
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

import aiohttp

from .embed import Embed
from .file import File
from .models import AllowedMentions, MessageReference
from .view import View

if TYPE_CHECKING:
    from .poll import Poll

MISSING = Any


def _prepare_sending_payload(
    *,
    content: Optional[str] = None,
    embed: Optional[Embed] = None,
    embeds: Optional[List[Embed]] = None,
    view: Optional[View] = None,
    tts: Optional[bool] = False,
    file: Optional[File] = None,
    files: Optional[List[File]] = None,
    ephemeral: Optional[bool] = False,
    allowed_mentions: Optional[AllowedMentions] = None,
    message_reference: Optional[MessageReference] = None,
    sticker_ids: Optional[List[str]] = None,
    suppress_embeds: Optional[bool] = False,
    supress_notifications: Optional[bool] = False,
    poll: Optional["Poll"] = None,
    payload_type: Optional[Enum] = None,
    **kwargs: Any,
) -> Union[Dict[str, Any], aiohttp.MultipartWriter]:
    merged_files = []
    if file:
        merged_files.append(file)
    if files:
        merged_files.extend(files)
    merged_embeds = []
    if embed:
        merged_embeds.append(embed)
    if embeds:
        merged_embeds.extend(embeds)
    for e in merged_embeds:
        merged_files.extend(e.attachments)

    payload: Dict[str, Any] = {}
    flags = 0
    if ephemeral:
        flags |= 1 << 6
    if suppress_embeds:
        flags |= 1 << 2
    if supress_notifications:
        flags |= 1 << 12

    if content:
        payload["content"] = content
    if tts:
        payload["tts"] = True
    if merged_embeds:
        payload["embeds"] = [e.to_dict() for e in merged_embeds]
    if view:
        payload["components"] = view.components
    if allowed_mentions:
        payload["allowed_mentions"] = allowed_mentions.to_dict()
    if message_reference:
        payload["message_reference"] = message_reference.to_dict()
    if sticker_ids:
        payload["sticker_ids"] = sticker_ids
    if poll:
        payload["poll"] = poll.to_dict()
    if merged_files:
        payload["attachments"] = [
            {
                "id": i,
                "filename": f.name,
                "ephemeral": f.spoiler,
                "description": f.description,
            }
            for i, f in enumerate(merged_files)
        ]
    if flags:
        payload["flags"] = flags
    payload.update(kwargs)
    payload_json = (
        payload
        if payload_type is None
        else {"type": payload_type.value, "data": payload}
    )
    if merged_files:
        form = aiohttp.MultipartWriter("form-data")
        form.append(
            json.dumps(payload_json),
            headers={
                "Content-Disposition": 'form-data; name="payload_json"',
                "Content-Type": "application/json",
            },
        )
        for i, f in enumerate(merged_files):
            mime, _ = mimetypes.guess_type(f.name)
            form.append(
                f.content,
                headers={
                    "Content-Disposition": f'form-data; name="files[{i}]"; filename="{f.name}"',
                    "Content-Type": mime or "application/octet-stream",
                },
            )
        return form
    return payload_json


def _prepare_editing_payload(
    *,
    content: Optional[str] = MISSING,
    embed: Optional[Embed] = MISSING,
    embeds: Optional[List[Embed]] = MISSING,
    view: Optional[View] = MISSING,
    tts: Optional[bool] = MISSING,
    file: Optional[File] = MISSING,
    files: Optional[List[File]] = MISSING,
    suppress_embeds: Optional[bool] = MISSING,
    payload_type: Optional[Enum] = None,
    **kwargs: Any,
):
    payload: Dict[str, Any] = {}
    if embed is None:
        payload["embeds"] = []
    if embeds is None:
        payload["embeds"] = []
    if view is None:
        payload["components"] = []
    if file is None:
        payload["attachments"] = []
    if files is None:
        payload["attachments"] = []
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
        ]
    if suppress_embeds is not MISSING:
        payload["flags"] = 1 << 2
    payload.update(kwargs)
    payload_json = (
        payload
        if payload_type is None
        else {"type": payload_type.value, "data": payload}
    )
    if files is not MISSING:
        form = aiohttp.MultipartWriter("form-data")
        form.append(
            json.dumps(payload_json),
            headers={
                "Content-Disposition": 'form-data; name="payload_json"',
                "Content-Type": "application/json",
            },
        )
        for i, f in enumerate(files):
            mime, _ = mimetypes.guess_type(f.name)
            form.append(
                f.content,
                headers={
                    "Content-Disposition": f'form-data; name="files[{i}]"; filename="{f.name}"',
                    "Content-Type": mime or "application/octet-stream",
                },
            )
        return form
    return payload_json

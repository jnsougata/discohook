import json
import mimetypes
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

import aiohttp

from .embed import Embed
from .enums import InteractionCallbackType
from .file import File
from .models import AllowedMentions, MessageReference
from .view import LegacyView, View

if TYPE_CHECKING:
    from .poll import Poll

UNSPECIFIED = Any


def _append_file(form: aiohttp.MultipartWriter, index: int, file: File) -> None:
    mime, _ = mimetypes.guess_type(file.name)
    form.append(
        file.content,
        headers={
            "Content-Disposition": f'form-data; name="files[{index}]"; filename="{file.name}"',
            "Content-Type": mime or "application/octet-stream",
        },
    )


def _prepare_sending_payload(
    *,
    component: Optional[View] = None,
    content: Optional[str] = None,
    embed: Optional[Embed] = None,
    embeds: Optional[List[Embed]] = None,
    view: Optional[LegacyView] = None,
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
    payload_type: Optional[InteractionCallbackType] = None,
    **kwargs: Any,
) -> Union[Dict[str, Any], aiohttp.MultipartWriter]:

    # Patch to support components v2
    if component:
        payload = {}
        flags = 1 << 15
        if payload_type:
            payload["type"] = payload_type.value
            payload["data"] = {
                "flags": flags,
                "components": [child.to_dict() for child in component.children],
            }
        else:
            payload["flags"] = flags
            payload["components"] = [child.to_dict() for child in component.children]

        if len(component.attachments):
            form = aiohttp.MultipartWriter("form-data")
            form.append_json(
                payload,
                headers={
                    "Content-Disposition": 'form-data; name="payload_json"',
                    "Content-Type": "application/json",
                },
            )
            for i, f in enumerate(component.attachments):
                _append_file(form, i, f)
            return form
        return payload

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
        form.append_json(
            payload_json,
            headers={
                "Content-Disposition": 'form-data; name="payload_json"',
                "Content-Type": "application/json",
            },
        )
        for i, file in enumerate(merged_files):
            _append_file(form, i, file)
        return form
    return payload_json


def _prepare_editing_payload(
    *,
    content: Optional[str] = UNSPECIFIED,
    embed: Optional[Embed] = UNSPECIFIED,
    embeds: Optional[List[Embed]] = UNSPECIFIED,
    view: Optional[LegacyView] = UNSPECIFIED,
    tts: Optional[bool] = UNSPECIFIED,
    file: Optional[File] = UNSPECIFIED,
    files: Optional[List[File]] = UNSPECIFIED,
    suppress_embeds: Optional[bool] = UNSPECIFIED,
    payload_type: Optional[InteractionCallbackType] = None,
    **kwargs: Any,
):
    payload: Dict[str, Any] = {}
    if content is not UNSPECIFIED and content is not None:
        payload["content"] = str(content)
    if content is None:
        payload["content"] = None
    if embed is None or embeds is None:
        payload["embeds"] = None
    elif embed is not UNSPECIFIED or embeds is not UNSPECIFIED:
        payload["embeds"] = []
        if embed is not UNSPECIFIED:
            payload["embeds"].append(embed.to_dict())
        if embeds is not UNSPECIFIED:
            payload["embeds"].extend([e.to_dict() for e in embeds])
    if tts is not UNSPECIFIED:
        payload["tts"] = tts
    if suppress_embeds is not UNSPECIFIED:
        payload["flags"] = 1 << 2
    if view is None:
        payload["components"] = []
    elif view is not UNSPECIFIED:
        payload["components"] = view.components
    if file is None or files is None:
        payload["attachments"] = []
    elif files is not UNSPECIFIED and file is not UNSPECIFIED:
        payload["attachments"] = []
        if file is not UNSPECIFIED:
            payload["attachments"].append(
                {
                    "id": 0,
                    "filename": file.name,
                    "ephemeral": file.spoiler,
                    "description": file.description,
                }
            )
        if files is not UNSPECIFIED:
            payload["attachments"].extend(
                [
                    {
                        "id": i,
                        "filename": f.name,
                        "ephemeral": f.spoiler,
                        "description": f.description,
                    }
                    for i, f in enumerate(files)
                ]
            )
    payload.update(kwargs)
    payload_json = (
        payload
        if payload_type is None
        else {"type": payload_type.value, "data": payload}
    )
    if files is not UNSPECIFIED or file is not UNSPECIFIED:
        form = aiohttp.MultipartWriter("form-data")
        form.append_json(
            payload_json,
            headers={
                "Content-Disposition": 'form-data; name="payload_json"',
                "Content-Type": "application/json",
            },
        )
        merged_files = []
        if file is not UNSPECIFIED and file is not None:
            merged_files.append(file)
        if files is not UNSPECIFIED and files is not None:
            merged_files.extend(files)
        for i, f in enumerate(merged_files):
            _append_file(form, i, f)
        return form
    return payload_json

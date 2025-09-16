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


def _prepare_payload(
    view: View,
    *,
    ephemeral: Optional[bool] = False,
    allowed_mentions: Optional[AllowedMentions] = None,
    message_reference: Optional[MessageReference] = None,
    suppress_embeds: Optional[bool] = False,
    supress_notifications: Optional[bool] = False,
    payload_type: Optional[InteractionCallbackType] = None,
    **kwargs: Any,
) -> Union[Dict[str, Any], aiohttp.MultipartWriter]:
    payload = {}
    flags = 1 << 15
    if ephemeral:
        flags |= 1 << 6
    if suppress_embeds:
        flags |= 1 << 2
    if supress_notifications:
        flags |= 1 << 12
    payload["flags"] = flags
    if message_reference:
        payload["message_reference"] = message_reference.to_dict()
    if allowed_mentions:
        payload["allowed_mentions"] = allowed_mentions.to_dict()
    payload["components"] = [child.to_dict() for child in view.children]
    if kwargs:
        payload.update(kwargs)
    if payload_type:
        payload = {"type": payload_type.value, "data": payload}
    if len(view.attachments):
        form = aiohttp.MultipartWriter("form-data")
        form.append_json(
            payload,
            headers={
                "Content-Disposition": 'form-data; name="payload_json"',
                "Content-Type": "application/json",
            },
        )
        for i, f in enumerate(view.attachments):
            _append_file(form, i, f)
        return form
    return payload

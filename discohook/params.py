import json
import mimetypes
from typing import Any, List, Optional, Dict

import aiohttp

from .embed import Embed
from .file import File
from .models import AllowedMentions, MessageReference
from .view import View

MISSING = Any


def _merge_fields(field: Optional[Any], fields: Optional[List[Any]]) -> List[Any]:
    tmp = []
    if field and field is not MISSING:
        tmp.append(field)
    if fields and fields is not MISSING:
        tmp.extend(fields)
    return tmp


# noinspection PyTypeChecker
def _create_form(
    payload: Dict[str, Any],
    files: Optional[List[File]] = None,
    embeds: Optional[List[Embed]] = None,
) -> aiohttp.MultipartWriter:
    form = aiohttp.MultipartWriter("form-data")
    form.append(
        json.dumps(payload),
        headers={
            "Content-Disposition": 'form-data; name="payload_json"',
            "Content-Type": "application/json",
        }
    )
    if not files:
        files = []
    if embeds:
        for embed in embeds:
            files.extend(embed.attachments)
    for i, file in enumerate(files):
        mime, _ = mimetypes.guess_type(file.name)
        form.append(
            file.content,
            headers={
                "Content-Disposition": f'form-data; name="files[{i}]"; filename="{file.name}"',
                "Content-Type": mime or "application/octet-stream",
            }
        )
    return form


class _SendingPayload:
    def __init__(
        self,
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
    ):
        self.content = content
        self.embed = embed
        self.embeds = embeds
        self.view = view
        self.tts = tts
        self.file = file
        self.files = files
        self.ephemeral = ephemeral
        self.allowed_mentions = allowed_mentions
        self.message_reference = message_reference
        self.sticker_ids = sticker_ids
        self.suppress_embeds = suppress_embeds
        self.supress_notifications = supress_notifications

    def _handle_send_params(self):
        payload = {}
        flag_value = 0
        embeds = _merge_fields(self.embed, self.embeds)
        files = _merge_fields(self.file, self.files)
        for embed in embeds:
            if embed.attachments:
                files.extend(embed.attachments)
        if self.ephemeral:
            flag_value |= 1 << 6
        if self.suppress_embeds:
            flag_value |= 1 << 2
        if self.supress_notifications:
            flag_value |= 1 << 12
        if self.content:
            payload["content"] = str(self.content)
        if self.tts:
            payload["tts"] = True
        if embeds:
            payload["embeds"] = [embed.to_dict() for embed in embeds]
        if self.view:
            payload["components"] = self.view.components
        if self.allowed_mentions:
            payload["allowed_mentions"] = self.allowed_mentions.to_dict()
        if self.message_reference:
            payload["message_reference"] = self.message_reference.to_dict()
        if self.sticker_ids:
            payload["sticker_ids"] = self.sticker_ids
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

    def to_dict(self) -> Dict[str, Any]:
        return self._handle_send_params()

    def to_form(self) -> aiohttp.MultipartWriter:
        data = self._handle_send_params()
        return _create_form(data, self.files, self.embeds)

    @staticmethod
    def form_with_data(
        data: Dict[str, Any],
        *,
        embed: Optional[Embed] = None,
        file: Optional[File] = None,
        embeds: Optional[List[Embed]] = None,
        files: Optional[List[File]] = None,
    ) -> aiohttp.MultipartWriter:
        embeds = _merge_fields(embed, embeds)
        files = _merge_fields(file, files)
        for embed in embeds:
            files.extend(embed.attachments)
        return _create_form(data, files, embeds)


class _EditingPayload(_SendingPayload):
    def __init__(
        self,
        *,
        content: Optional[str] = MISSING,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[File] = MISSING,
        files: Optional[List[File]] = MISSING,
        suppress_embeds: Optional[bool] = MISSING,
    ):
        super().__init__(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )

    def _handle_edit_params(self):
        payload = {}
        if self.embed is None:
            payload["embeds"] = []
        if self.embeds is None:
            payload["embeds"] = []
        if self.view is None:
            payload["components"] = []
        if self.file is None:
            payload["attachments"] = []
        if self.files is None:
            payload["attachments"] = []
        embeds = _merge_fields(self.embed, self.embeds)
        files = _merge_fields(self.file, self.files)
        for embed in embeds:
            if embed.attachments:
                files.extend(embed.attachments)
        if self.content is not MISSING:
            payload["content"] = str(self.content)
        if self.tts is not MISSING:
            payload["tts"] = self.tts
        if embeds:
            payload["embeds"] = [embed.to_dict() for embed in embeds]
        if self.view is not MISSING:
            payload["components"] = self.view.components if self.view else []
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
        if self.suppress_embeds is not MISSING:
            payload["flags"] = 1 << 2

        return payload

    def to_dict(self) -> Dict[str, Any]:
        return self._handle_edit_params()

    def to_form(self) -> aiohttp.MultipartWriter:
        data = self._handle_edit_params()
        return _create_form(data, self.files, self.embeds)

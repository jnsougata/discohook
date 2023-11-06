from enum import Enum
import json
import mimetypes
from typing import Any, List, Optional, Dict

import aiohttp

from .embed import Embed
from .file import File
from .models import AllowedMentions, MessageReference
from .view import View

MISSING = Any


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

    def _merge_fields(self):
        if not self.files or self.files is MISSING:
            self.files = []
        if self.file:
            self.files.append(self.file)
        if not self.embeds or self.embeds is MISSING:
            self.embeds = []
        if self.embed:
            self.embeds.append(self.embed)
        for embed in self.embeds:
            if embed.attachments:
                self.files.extend(embed.attachments)

    @staticmethod
    def _create_form(
        payload: Dict[str, Any],
        files: Optional[List[File]] = None
    ) -> aiohttp.MultipartWriter:
        form = aiohttp.MultipartWriter("form-data")
        # noinspection PyTypeChecker
        form.append(
            json.dumps(payload),
            headers={
                "Content-Disposition": 'form-data; name="payload_json"',
                "Content-Type": "application/json",
            }
        )
        if not files:
            files = []
        for i, file in enumerate(files):
            mime, _ = mimetypes.guess_type(file.name)
            # noinspection PyTypeChecker
            form.append(
                file.content,
                headers={
                    "Content-Disposition": f'form-data; name="files[{i}]"; filename="{file.name}"',
                    "Content-Type": mime or "application/octet-stream",
                }
            )
        return form

    def _handle_send_params(self):
        self._merge_fields()
        payload = {}
        flag_value = 0
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
        if self.embeds:
            payload["embeds"] = [embed.to_dict() for embed in self.embeds]
        if self.view:
            payload["components"] = self.view.components
        if self.allowed_mentions:
            payload["allowed_mentions"] = self.allowed_mentions.to_dict()
        if self.message_reference:
            payload["message_reference"] = self.message_reference.to_dict()
        if self.sticker_ids:
            payload["sticker_ids"] = self.sticker_ids
        if self.files:
            payload["attachments"] = [
                {
                    "id": i,
                    "filename": file.name,
                    "ephemeral": file.spoiler,
                    "description": file.description,
                }
                for i, file in enumerate(self.files)
            ]
        if flag_value:
            payload["flags"] = flag_value
        return payload

    def to_dict(self, payload_type: Optional[Enum] = None, **kwargs) -> Dict[str, Any]:
        data = self._handle_send_params()
        data.update(kwargs)
        if payload_type is None:
            return data
        return {"data": data, "type": int(payload_type)}

    def to_form(self, payload_type: Optional[Enum] = None, **kwargs) -> aiohttp.MultipartWriter:
        return self._create_form(self.to_dict(payload_type, **kwargs), self.files)


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
        self._merge_fields()
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
        if self.content is not MISSING:
            payload["content"] = str(self.content)
        if self.tts is not MISSING:
            payload["tts"] = self.tts
        if self.embeds:
            payload["embeds"] = [embed.to_dict() for embed in self.embeds]
        if self.view is not MISSING:
            payload["components"] = self.view.components if self.view else []
        if self.files:
            payload["attachments"] = [
                {
                    "id": i,
                    "filename": file.name,
                    "ephemeral": file.spoiler,
                    "description": file.description,
                }
                for i, file in enumerate(self.files)
            ]
        if self.suppress_embeds is not MISSING:
            payload["flags"] = 1 << 2

        return payload

    def to_dict(self, payload_type: Optional[Enum] = None, **kwargs) -> Dict[str, Any]:
        data = self._handle_edit_params()
        data.update(kwargs)
        if payload_type is None:
            return data
        return {"data": data, "type": int(payload_type)}

    def to_form(self, payload_type: Optional[Enum] = None, **kwargs) -> aiohttp.MultipartWriter:
        return self._create_form(self.to_dict(payload_type, **kwargs), self.files)

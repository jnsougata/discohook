import json
import mimetypes
from typing import Any, Dict, List, Optional

import aiohttp

from .file import File
from .embed import Embed


# noinspection PyTypeChecker
def create_form(
    payload: Dict[str, Any],
    files: Optional[List[File]],
    embeds: Optional[List[Embed]]
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

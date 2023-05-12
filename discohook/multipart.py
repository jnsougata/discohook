import json
from typing import Any, Dict, List, Optional

import aiohttp

from .file import File


# noinspection PyTypeChecker
def create_form(payload: Dict[str, Any], files: Optional[List[File]] = None) -> aiohttp.MultipartWriter:
    form = aiohttp.MultipartWriter("form-data")
    form.append(
        json.dumps(payload), 
        headers={
            "Content-Disposition": 'form-data; name="payload_json"',
            "Content-Type": "application/json"
        }
    )
    if not files:
        return form
    for i, file in enumerate(files):
        form.append(
            file.content.read(),
            headers={
                "Content-Disposition": f'form-data; name="files[{i}]"; filename="{file.name}"',
                "Content-Type": "application/octet-stream",
            }
        )
    return form

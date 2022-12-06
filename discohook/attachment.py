import aiohttp
from typing import Optional


class Attachment:

    def __init__(self, data: dict) -> None:
        self.id: str = data["id"]
        self.filename: str = data["filename"]
        self.description: Optional[str] = data.get("description")
        self.content_type: Optional[str] = data.get("content_type")
        self.size: int = data["size"]
        self.url: str = data["url"]
        self.proxy_url: str = data["proxy_url"]
        self.height: Optional[int] = data.get("height")
        self.width: Optional[int] = data.get("width")
        self.ephemeral: bool = data.get("ephemeral", False)

    async def read(self) -> bytes:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(self.url)
            return await resp.content.read()
    
    async def iter(self) -> aiohttp.StreamReader:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(self.url)
            return resp.content

from typing import Optional

import aiohttp


class Attachment:
    """
    Represents a discord file attachment.

    Attributes:
        id (str): ID of attachment.
        filename (str): Filename of attachment.
        description (str): Description of attachment.
        content_type (str): Content type of attachment.
        size (int): Size of attachment.
        url (str): URL of attachment.
        proxy_url (str): Proxy URL of attachment.
        height (int): Height of attachment.
        width (int): Width of attachment.
        ephemeral (bool): Whether attachment is ephemeral.
        duration_secs (int): Duration of attachment.
        waveform (str): Waveform of attachment.
        flags (int): Flags of attachment.
        placeholder (str): Placeholder of attachment.
        placeholder_version (int): Placeholder version of attachment.
    """

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
        self.duration_secs: Optional[int] = data.get("duration_secs")
        self.waveform: Optional[str] = data.get("waveform")
        self.flags: Optional[int] = data.get("flags")
        self.placeholder: Optional[str] = data.get("placeholder")
        self.placeholder_version: Optional[int] = data.get("placeholder_version")

    async def read(self) -> bytes:
        """
        Reads content of attachment.

        Returns:
            bytes: Content of attachment in bytes.
        """
        async with aiohttp.ClientSession() as session:
            resp = await session.get(self.url)
            return await resp.content.read()

    async def iter(self) -> aiohttp.StreamReader:
        """
        Creates an asynchronous generator.

        Returns:
            aiohttp.StreamReader: Asynchronous generator.
        """
        async with aiohttp.ClientSession() as session:
            resp = await session.get(self.url)
            return resp.content

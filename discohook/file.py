import io
from typing import Optional


class File:
    """
    Represents a file to send to Discord.

    Parameters
    ----------
    name: str
        The name of the file.
    content: io.BytesIO
        The content of the file.
    description: str | None
        The description of the file.
    spoiler: bool
        Whether the file is a spoiler.
    """

    def __init__(self, name: str, *, content: io.BytesIO, description: Optional[str] = None, spoiler: bool = False):
        self.name = name
        self.content = content
        self.description = description
        self.spoiler = spoiler

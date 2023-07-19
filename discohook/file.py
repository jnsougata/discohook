from typing import Optional


class File:
    """
    Represents a file to send to Discord.

    Parameters
    ----------
    name: str
        The name of the file.
    content: bytes
        The content of the file in bytes.
    description: str | None
        The description of the file.
    spoiler: bool
        Whether the file is a spoiler.
    """

    def __init__(
        self,
        name: str,
        *,
        content: bytes,
        spoiler: bool = False,
        description: Optional[str] = None
    ):
        self.name = name
        self.content = content
        self.spoiler = spoiler
        self.description = description

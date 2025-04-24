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

    @classmethod
    def from_path(cls, path: str, *, spoiler: bool = False, description: Optional[str] = None):
        """
        Creates a File object from a file path.

        Parameters
        ----------
        path: str
            The path to the file.
        spoiler: bool
            Whether the file is a spoiler.
        description: str | None
            The description of the file to be sent.
        """
        with open(path, "rb") as f:
            content = f.read()
        name = path.split("/")[-1]
        return cls(name, content=content, spoiler=spoiler, description=description)
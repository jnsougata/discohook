from typing import Any, Dict, Optional

from .enums import ComponentType


# noinspection PyShadowingBuiltins
class File:
    """
    Represents a file to send to Discord.

    Args:
        name (str | None): Name of the file.
        content (bytes | None): Content of the file in bytes.
        description (str | None): Description of the file.
        spoiler (bool): Whether the file is a spoiler.
        id (int | None): ID of the file used to identify the file.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        content: Optional[bytes] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        spoiler: bool = False,
        id: Optional[int] = None,
    ):
        self.name = name
        self.content = content
        self.spoiler = spoiler
        self.description = description
        self.type = ComponentType.file
        self.url = url
        self.id = id

    @classmethod
    def from_path(
        cls,
        path: str,
        *,
        spoiler: bool = False,
        description: Optional[str] = None,
        id: Optional[int] = None,
    ):
        """
        Creates a File object from a file path.

        Args:
            path (str): Path to the file.
            spoiler (bool): Whether the file is a spoiler.
            description (str | None): Description of the file to be sent.
            id (int | None): ID of the file used to identify the file.

        Returns:
            File: File object.
        """
        with open(path, "rb") as f:
            content = f.read()
            name = path.split("/")[-1]
            url = f"attachment://{name}"
            return cls(
                name,
                content=content,
                spoiler=spoiler,
                description=description,
                url=url,
                id=id,
            )

    @classmethod
    def from_url(
        cls,
        url: str,
        *,
        description: Optional[str] = None,
        spoiler: bool = False,
        id: Optional[int] = None,
    ):
        """
        Creates a File object from a file URL.

        Args:
            url (str): URL to the file.
            description (str | None): Description of the file to be sent.
            spoiler (bool): Whether the file is a spoiler.
            id (int | None): ID of the file used to identify the file.

        Returns:
            File: File object.
        """
        return cls(url=url, description=description, spoiler=spoiler, id=id)

    def to_dict(self) -> Dict[str, Any]:
        data = {"type": self.type, "file": {"url": self.url}, "spoiler": self.spoiler}
        if self.id:
            data["id"] = self.id
        if self.description:
            data["description"] = self.description
        return data

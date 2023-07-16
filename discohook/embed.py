from typing import Any, Dict, List, Optional

from .file import File


class Embed:
    """
    Represents a discord Embed object.

    Parameters
    ----------
    title: str | None
        The title of the embed.
    description: str | None
        The description of the embed.
    url: str | None
        The url of the embed.
    color: int | None
        The color of the embed.
    timestamp: str | None
        The timestamp of the embed.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        *,
        description: Optional[str] = None,
        url: Optional[str] = None,
        color: Optional[int] = None,
        timestamp: Optional[str] = None,
    ):
        self.title = title
        self.description = description
        self.url = url
        self.color = color
        self.timestamp = timestamp
        self.data: Dict[str, Any] = {}
        self.fields: List[Dict[str, Any]] = []

    def author(self, *, name: str, url: Optional[str] = None, icon_url: Optional[str] = None):
        """
        Sets the author of the embed.

        Parameters
        ----------
        name: :class:`str`
            The name of the author.
        url: Optional[:class:`str`]
            The url of the author.
        icon_url: Optional[:class:`str`]
            The icon url of the author.
        """
        self.data["author"] = {"name": name}
        if url:
            self.data["author"]["url"] = url
        if icon_url:
            self.data["author"]["icon_url"] = icon_url

    def footer(self, text: str, *, icon_url: Optional[str] = None):
        """
        Sets the footer of the embed.

        Parameters
        ----------
        text: :class:`str`
            The text of the footer.
        icon_url: Optional[:class:`str`]
            The icon url of the footer.
        """
        self.data["footer"] = {"text": text}
        if icon_url:
            self.data["footer"]["icon_url"] = icon_url

    def image(self, url: str):
        """
        Sets the image of the embed.

        Parameters
        ----------
        url: :class:`str`
            The url of the image.
        """
        self.data["image"] = {"url": url}

    def image_from_attachment(self, file: File):
        """
        Sets the image of the embed from a file attachment.

        Parameters
        ----------
        file: :class:`File`
            The file attachment.
        """
        self.data["image"] = {"url": f"attachment://{file.name}"}

    def thumbnail(self, url: str):
        """
        Sets the thumbnail of the embed.

        Parameters
        ----------
        url: :class:`str`
            The url of the thumbnail.
        """
        self.data["thumbnail"] = {"url": url}

    def thumbnail_from_attachment(self, file: File):
        """
        Sets the thumbnail of the embed from a file attachment.

        Parameters
        ----------
        file: :class:`File`
            The file attachment.
        """
        self.data["thumbnail"] = {"url": f"attachment://{file.name}"}

    def add_field(self, name: str, value: str, *, inline: bool = False):
        """
        Adds a field to the embed.

        Parameters
        ----------
        name: :class:`str`
            The name of the field.
        value: :class:`str`
            The value of the field.
        inline: :class:`bool`
            Whether the field is inline.
        """
        self.fields.append({"name": name, "value": value, "inline": inline})

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns the embed as a dictionary.

        This method is used internally by the library. You will rarely need to use it.

        Returns
        -------
        :class:`dict`
            The embed as a dictionary.
        """
        if self.title:
            self.data["title"] = str(self.title)
        if self.description:
            self.data["description"] = str(self.description)
        if self.url:
            self.data["url"] = self.url
        if self.color is not None:
            self.data["color"] = self.color
        if self.timestamp:
            self.data["timestamp"] = self.timestamp
        if self.fields:
            self.data["fields"] = self.fields
        return self.data

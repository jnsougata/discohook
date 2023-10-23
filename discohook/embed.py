from typing import Any, Dict, List, Optional, Union

from .file import File
from .utils import color_parser


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
    color: int | str | None
        The color of the embed in hex or int.
    timestamp: str | None
        The timestamp of the embed.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        *,
        description: Optional[str] = None,
        url: Optional[str] = None,
        color: Optional[Union[int, str]] = None,
        timestamp: Optional[str] = None,
    ):
        self.title = title
        self.description = description
        self.url = url
        self.color = color
        self.timestamp = timestamp
        self.data: Dict[str, Any] = {}
        self.fields: List[Dict[str, Any]] = []
        self.__attachments: List[File] = []

    @property
    def attachments(self) -> List[File]:
        """
        Returns the attachments of the embed.
        """
        return self.__attachments

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Embed":
        """
        Creates an embed from a dictionary.
        This method is handy when you want to create an embed manually.

        Parameters
        ----------
        data: :class:`dict`
            The dictionary to create the embed from.

        Returns
        -------
        :class:`Embed`
            The created embed.
        """
        embed = cls(**data)
        embed.data = data
        embed.fields = data.pop("fields", [])
        return embed

    def set_author(self, *, name: str, url: Optional[str] = None, icon_url: Optional[str] = None):
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

    def set_footer(self, text: str, *, icon_url: Optional[str] = None):
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

    def set_image(self, img: Union[str, File]):
        """
        Sets the image of the embed from a file attachment or url.

        Parameters
        ----------
        img: :class:`str` | :class:`File`
            The url or file attachment of the image.
        """
        if isinstance(img, str):
            self.data["image"] = {"url": img}
        elif isinstance(img, File):
            self.__attachments.append(img)
            self.data["image"] = {"url": f"attachment://{img.name}"}
        else:
            raise TypeError("img must be str or File")

    def set_thumbnail(self, img: Union[str, File]):
        """
        Sets the thumbnail of the embed.

        Parameters
        ----------
        img: :class:`str` | :class:`File`
            The url or file attachment of the thumbnail.
        """
        if isinstance(img, str):
            self.data["thumbnail"] = {"url": img}
        elif isinstance(img, File):
            self.__attachments.append(img)
            self.data["thumbnail"] = {"url": f"attachment://{img.name}"}
        else:
            raise TypeError("img must be str or File")

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
            self.data["color"] = color_parser(self.color)
        if self.timestamp:
            self.data["timestamp"] = self.timestamp
        if self.fields:
            self.data["fields"] = self.fields
        return self.data

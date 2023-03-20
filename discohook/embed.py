from typing import Any, Dict, Optional, List


class Embed:
    """
    Represents a discord Embed object.

    Parameters
    ----------
    title: Optional[:class:`str`]
        The title of the embed.
    description: Optional[:class:`str`]
        The description of the embed.
    url: Optional[:class:`str`]
        The url of the embed.
    color: Optional[:class:`int`]
        The color of the embed.
    timestamp: Optional[:class:`str`]
        The timestamp of the embed.
    """
    def __init__(
        self,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[str] = None,
        color: Optional[int] = None,
        timestamp: Optional[str] = None
    ):
        self.data: Dict[str, Any] = {}
        if title:
            self.data["title"] = str(title)
        if description:
            self.data["description"] = str(description)
        if url:
            self.data["url"] = url
        if color:
            self.data["color"] = color
        if timestamp:
            self.data["timestamp"] = timestamp

        self._fields_container: List[Dict[str, Any]] = []

    def author(
        self, *, name: str, url: Optional[str] = None, icon_url: Optional[str] = None
    ):
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

    def thumbnail(self, url: str):
        """
        Sets the thumbnail of the embed.

        Parameters
        ----------
        url: :class:`str`
            The url of the thumbnail.
        """
        self.data["thumbnail"] = {"url": url}

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
        self._fields_container.append({"name": name, "value": value, "inline": inline})

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns the embed as a dictionary.

        This method is used internally by the library. You will rarely need to use it.

        Returns
        -------
        """
        if self._fields_container:
            self.data["fields"] = self._fields_container
        return self.data

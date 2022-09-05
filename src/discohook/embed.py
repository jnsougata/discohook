from typing import Any, Dict, Optional


class Embed:
    def __init__(
            self,
            *,
            title: Optional[str] = None,
            description: Optional[str] = None,
            url: Optional[str] = None,
            color: Optional[int] = None,
            timestamp: Optional[str] = None
    ):
        self._data: Dict[str, Any] = {}
        if title:
            self._data["title"] = str(title)
        if description:
            self._data["description"] = str(description)
        if url:
            self._data["url"] = url
        if color:
            self._data["color"] = color
        if timestamp:
            self._data["timestamp"] = timestamp

        self._fields_container: List[Dict[str, Any]] = []

    def author(self, *, name: str, url: Optional[str] = None, icon_url: Optional[str] = None):
        self._data["author"] = {"name": name}
        if url:
            self._data["author"]["url"] = url
        if icon_url:
            self._data["author"]["icon_url"] = icon_url

    def footer(self, text: str, *, icon_url: Optional[str] = None):
        self._data["footer"] = {"text": text}
        if icon_url:
            self._data["footer"]["icon_url"] = icon_url

    def image(self, url: str):
        self._data["image"] = {"url": url}

    def thumbnail(self, url: str):
        self._data["thumbnail"] = {"url": url}

    def add_field(self, *, name: str, value: str, inline: bool = False):
        self._fields_container.append({"name": name, "value": value, "inline": inline})

    def to_json(self) -> Dict[str, Any]:
        if self._fields_container:
            self._data["fields"] = self._fields_container
        return self._data

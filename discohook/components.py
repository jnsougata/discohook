from typing import Any, Dict, Optional, Union

from .button import Button
from .enums import ComponentType
from .file import File
from .select import Select

__all__ = [
    "ActionRow",
    "File",
    "Media",
    "MediaGallery",
    "TextDisplay",
    "Thumbnail",
    "Section",
    "Separator",
    "Container",
]


# noinspection PyShadowingBuiltins
class ActionRow:

    def __init__(
        self, *components: Union[Button, Select, Any], id: Optional[int] = None
    ):
        self.id = id
        self.type = ComponentType.action_row
        self.components = components
        assert (
            1 <= len(components) <= 5
        ), "ActionRow must have between 1 and 5 components."

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "components": [component.to_dict() for component in self.components],
        }
        if self.id:
            data["id"] = self.id
        return data


class Media:

    def __init__(
        self, media: str, description: Optional[str] = None, spoiler: bool = False
    ):
        self.media = media
        self.description = description
        self.spoiler = spoiler

    def to_dict(self) -> Dict[str, Any]:
        data = {"media": self.media, "spoiler": self.spoiler}
        if self.description:
            data["description"] = self.description
        return data


# noinspection PyShadowingBuiltins
class MediaGallery:

    def __init__(self, *media: Media, id: Optional[int] = None):
        self.id = id
        self.type = ComponentType.media_gallery
        self.items = media
        assert 1 <= len(media) <= 10, "MediaGallery must have between 1 and 10 items."

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "items": [media.to_dict() for media in self.items],
        }
        if self.id:
            data["id"] = self.id
        return data


# noinspection PyShadowingBuiltins
class TextDisplay:

    def __init__(self, markdown: str, *, id: Optional[int] = None):
        self.id = id
        self.type = ComponentType.text_display
        self.content = markdown

    def to_dict(self) -> Dict[str, Any]:
        data = {"type": self.type, "content": self.content}
        if self.id:
            data["id"] = self.id
        return data


# noinspection PyShadowingBuiltins
class Thumbnail:
    def __init__(
        self,
        media: str,
        *,
        description: Optional[str] = None,
        spoiler: bool = False,
        id: Optional[int] = None,
    ):
        self.id = id
        self.type = ComponentType.thumbnail
        self.media = media
        self.description = description
        self.spoiler = spoiler

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "media": {"url": self.media},
            "spoiler": self.spoiler,
        }
        if self.id:
            data["id"] = self.id
        if self.description:
            data["description"] = self.description
        return data


# noinspection PyShadowingBuiltins
class Section:
    def __init__(
        self,
        *components: TextDisplay,
        accessory: Union[Button, Thumbnail],
        id: Optional[int] = None,
    ):
        self.type = ComponentType.section
        self.components = components
        self.accessory = accessory
        self.id = id

    def to_dict(self):
        data = {
            "type": self.type,
            "components": [component.to_dict() for component in self.components],
            "accessory": self.accessory.to_dict(),
        }
        if self.id:
            data["id"] = self.id
        return data


# noinspection PyShadowingBuiltins
class Separator:

    def __init__(self, *, id: Optional[int] = None, spacing: int = 1):
        self.id = id
        self.type = ComponentType.separator
        self.divider = True
        self.spacing = spacing
        assert spacing in [1, 2], "Spacing must be either 1 or 2."

    def to_dict(self) -> Dict[str, Any]:
        data = {"type": self.type, "divider": self.divider, "spacing": self.spacing}
        if self.id:
            data["id"] = self.id
        return data


# noinspection PyShadowingBuiltins
class Container:

    def __init__(
        self,
        *components: Union[
            ActionRow, TextDisplay, Section, MediaGallery, Separator, File
        ],
        accent_color: Optional[int] = None,
        id: Optional[int] = None,
    ):
        self.id = id
        self.type = ComponentType.container
        self.components = components
        self.accent_color = accent_color
        self.attachments = [c for c in components if isinstance(c, File) if c.content]
        assert (
            1 <= len(components) <= 10
        ), "Container must have between 1 and 10 components."

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "components": [component.to_dict() for component in self.components],
        }
        if self.id:
            data["id"] = self.id
        if self.accent_color is not None:
            data["accent_color"] = self.accent_color
        return data

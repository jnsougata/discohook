from typing import Any, Dict, List, Optional, Union

from .button import Button
from .enums import ComponentType, TextInputFieldLength
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
    "TextInput",
    "FileUpload",
    "Label",
    "Checkbox",
    "CheckboxGroup",
    "CheckboxGroupOption",
    "RadioGroup",
    "RadioGroupOption",
    "TopLevelComponent",
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
            data["id"] = self.id  # noqa
        return data


class Media:

    def __init__(
        self,
        *,
        media: Union[str, File],
        description: Optional[str] = None,
        spoiler: bool = False,
    ):
        self.attachment = None
        if isinstance(media, File):
            self.media = {"url": f"attachment://{media.name}"}
            self.attachment = media
        else:
            self.media = {"url": media}
        self.description = description
        self.spoiler = spoiler

    def to_dict(self) -> Dict[str, Any]:
        data = {"media": self.media, "spoiler": self.spoiler}
        if self.description:
            data["description"] = self.description  # type: ignore
        return data


# noinspection PyShadowingBuiltins
class MediaGallery:

    def __init__(self, *media: Media, id: Optional[int] = None):
        self.id = id
        self.type = ComponentType.media_gallery
        self.items = media
        self.attachments = [m.attachment for m in media if m.attachment]
        assert 1 <= len(media) <= 10, "MediaGallery must have between 1 and 10 items."

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "items": [media.to_dict() for media in self.items],
        }
        if self.id:
            data["id"] = self.id  # noqa
        return data


# noinspection PyShadowingBuiltins
class TextDisplay:

    def __init__(self, *, markdown: str, id: Optional[int] = None):
        self.id = id
        self.type = ComponentType.text_display
        self.content = markdown

    def to_dict(self) -> Dict[str, Any]:
        data = {"type": self.type, "content": self.content}
        if self.id:
            data["id"] = self.id  # noqa
        return data


# noinspection PyShadowingBuiltins
class Thumbnail:
    def __init__(
        self,
        *,
        media: Union[str, File],
        description: Optional[str] = None,
        spoiler: bool = False,
        id: Optional[int] = None,
    ):
        self.id = id
        self.type = ComponentType.thumbnail
        self.media = media
        self.description = description
        self.spoiler = spoiler
        self.attachment = media if isinstance(media, File) else None

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "media": {
                "url": (
                    self.media
                    if isinstance(self.media, str)
                    else f"attachment://{self.media.name}"
                )
            },
            "spoiler": self.spoiler,
        }
        if self.id:
            data["id"] = self.id  # noqa
        if self.description:
            data["description"] = self.description  # noqa
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
        self.attachment = (
            accessory.attachment if isinstance(accessory, Thumbnail) else None
        )

    def to_dict(self):
        data = {
            "type": self.type,
            "components": [component.to_dict() for component in self.components],
            "accessory": self.accessory.to_dict(),
        }
        if self.id:
            data["id"] = self.id  # noqa
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
        self.attachments = []
        for c in components:
            if isinstance(c, MediaGallery):
                self.attachments.extend(c.attachments)
            elif isinstance(c, File) and c.content:
                self.attachments.append(c)
        assert (
            1 <= len(components) <= 10
        ), "Container must have between 1 and 10 components."

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "components": [component.to_dict() for component in self.components],
        }
        if self.id:
            data["id"] = self.id  # noqa
        if self.accent_color is not None:
            data["accent_color"] = self.accent_color  # noqa
        return data


class TextInput:
    """
    Represents a text input field in a modal.

    Parameters
    ----------
    custom_id: :class:`str`
        The label of the text input field.
    id: :class:`int`
        A unique id of the text input field. Must be valid python identifier.
    required: :class:`bool`
        Whether this component is required to be filled (defaults to true).
    placeholder: :class:`str`
        Custom placeholder text if the input is empty; max 100 characters.
    value: :class:`str`
        Pre-filled value for this component; max 4000 characters.
    min_length: :class:`int`
        The minimum length of the text input field.
    max_length: :class:`int`
        The maximum length of the text input field.
    style: :class:`TextInputFieldLength`
        The style of the text input field.
    """

    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        required: bool = True,
        placeholder: Optional[str] = None,
        value: Optional[str] = None,
        min_length: int = 0,
        max_length: int = 4000,
        style: TextInputFieldLength = TextInputFieldLength.short,
    ):
        self.custom_id = custom_id
        assert custom_id.isidentifier(), "field_id must be a valid python identifier"
        self.id = id
        self.required = required
        self.placeholder = placeholder
        self.value = value
        self.min_length = min_length
        self.max_length = max_length
        self.style = style

    def to_dict(self):
        return {
            "id": self.id,
            "type": ComponentType.text_input.value,
            "style": self.style.value,
            "value": self.value,
            "custom_id": self.custom_id,
            "min_length": self.min_length,
            "max_length": self.max_length,
            "placeholder": self.placeholder,
            "required": self.required,
        }


class FileUpload:
    """
    Represents a file upload component in a modal.

    Parameters
    ----------
    custom_id: :class:`str`
        The label of the file upload field.
    id: :class:`int`
        A unique id of the file upload field. Must be valid python identifier.
    min_values: :class:`int`
        Minimum number of items that must be uploaded (defaults to 1); min 0, max 10
    max_values: :class:`int`
        Maximum number of items that can be uploaded (defaults to 1); max 10
    required: :class:`bool`
        Whether this component is required to be filled (defaults to true).
    """

    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
    ):
        self.custom_id = custom_id
        assert custom_id.isidentifier(), "field_id must be a valid python identifier"
        self.id = id
        self.min_values = min_values
        self.max_values = max_values
        self.required = required

    def to_dict(self):
        return {
            "id": self.id,
            "type": ComponentType.file_upload.value,
            "custom_id": self.custom_id,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "required": self.required,
        }


class Checkbox:
    def __init__(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        default: bool = False,
    ):
        self.id = id
        self.custom_id = custom_id
        self.default = default

    def to_dict(self):
        return {
            "type": ComponentType.checkbox.value,
            "id": self.id,
            "custom_id": self.custom_id,
            "default": self.default,
        }


class CheckboxGroupOption:
    def __init__(
        self,
        *,
        label: str,
        value: str,
        description: Optional[str] = None,
        default: bool = False,
    ):
        self.label = label
        self.value = value
        self.description = description
        self.default = default

    def to_dict(self):
        return {
            "label": self.label,
            "value": self.value,
            "description": self.description,
            "default": self.default,
        }


class CheckboxGroup:
    def __init__(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        options: List[CheckboxGroupOption],
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        required: bool = True,
    ):
        self.id = id
        self.custom_id = custom_id
        self.options = options
        self.min_values = min_values
        self.max_values = max_values
        self.required = required

    def to_dict(self):
        data = {
            "type": ComponentType.checkbox_group.value,
            "id": self.id,
            "custom_id": self.custom_id,
            "options": [option.to_dict() for option in self.options],
            "required": self.required,
        }
        if self.min_values is not None:
            data["min_values"] = self.min_values
        if self.max_values is not None:
            data["max_values"] = self.max_values
        return data


class RadioGroupOption:
    def __init__(
        self,
        label: str,
        value: str,
        description: Optional[str] = None,
        default: bool = False,
    ):
        self.label = label
        self.value = value
        self.description = description
        self.default = default

    def to_dict(self):
        return {
            "label": self.label,
            "value": self.value,
            "description": self.description,
            "default": self.default,
        }


class RadioGroup:
    def __init__(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        options: List[RadioGroupOption],
        required: bool = True,
    ):
        self.id = id
        self.custom_id = custom_id
        self.options = options
        self.required = required

    def to_dict(self):
        return {
            "type": ComponentType.radio_group.value,
            "id": self.id,
            "custom_id": self.custom_id,
            "options": [option.to_dict() for option in self.options],
            "required": self.required,
        }


# noinspection PyShadowingBuiltins
class Label:
    def __init__(
        self,
        label: str,
        child: Union[
            Select, TextInput, FileUpload, Checkbox, CheckboxGroup, RadioGroup
        ],
        *,
        id: Optional[int] = None,
        description: Optional[str] = None,
    ):
        self.label = label
        self.id = id
        self.description = description
        self.child = child

    def to_dict(self):
        return {
            "type": ComponentType.label.value,
            "label": self.label,
            "id": self.id,
            "description": self.description,
            "component": self.child.to_dict(),
        }


TopLevelComponent = Union[str, TextDisplay, ActionRow, Section, Container, Separator, File, MediaGallery]

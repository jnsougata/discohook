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
    """
    Action row component.

    Args:
        components (Tuple[Button | Select]): Components to include in the action row. Must be between 1 and 5 components.
        id (int | None): Unique id for the action row.

    Attributes:
        id (int): Action row id.
        type (ComponentType): Action row type.
        components (List[Component]): Action row components.
    """

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
    """
    Media component.

    Args:
        media (str | File): Media to include in the media component.
        description (str | None): Media description.
        spoiler (bool): Whether the media should be spoiler or not.

    """

    def __init__(
        self,
        *,
        media: Union[str, File],
        description: Optional[str] = None,
        spoiler: bool = False,
    ):
        self.attachment = None
        if isinstance(media, File):
            self.media = {"url": f"attachment://{media.name}"}  # noqa
            self.attachment = media
        else:
            self.media = {"url": media}  # noqa
        self.description = description
        self.spoiler = spoiler

    def to_dict(self) -> Dict[str, Any]:
        data = {"media": self.media, "spoiler": self.spoiler}
        if self.description:
            data["description"] = self.description  # type: ignore
        return data


# noinspection PyShadowingBuiltins
class MediaGallery:
    """
    Media gallery component.

    Args:
        *media (Media): Media items to include in the gallery.
        id (int | None): Unique id for the media gallery.

    Attributes:
        id (int): Media gallery id.
        type (ComponentType): Media gallery type.
        items (Tuple[Media]): Media items in the gallery.
        attachments (List[File]): Attachments for the media items.
    """
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
    """
    Text display component.

    Args:
        markdown (str): Markdown content to display.
        id (int | None): Unique id for the text display.

    Attributes:
        id (int | None): Optional text display id.
        type (ComponentType): Text display type.
        content (str): Markdown content to display.
    """
    def __init__(self, markdown: str, *, id: Optional[int] = None):
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
    """
    Thumbnail component.

    Args:
        media (str | File): Media to include in the thumbnail.
        description (str | None): Thumbnail description.
        spoiler (bool): Whether the thumbnail should be spoiler or not.
        id (int | None): Unique id for the thumbnail.

    Attributes:
        attachment (File | None): Attachment for the thumbnail if media is a File.
    """
    def __init__(
        self,
        media: Union[str, File],
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
    """
    Section component.

    Args:
        *components (Tuple[TextDisplay]): Text display components to include in the section.
        accessory (Button | Thumbnail): Accessory component for the section.
        id (int | None): Unique id for the section.

    Attributes:
        attachment (File | None): Attachment for the accessory if it is a File.
    """
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
    """
    Separator component.

    Args:
        id (int | None): Optional separator id.
        spacing (int): The spacing of the separator. Must be either 1 or 2.

    Raises:
        AssertionError: If spacing is not 1 or 2.
    """
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
    """
    Container component.

    Args:
        *components (Tuple[ActionRow | TextDisplay | Section | MediaGallery | Separator | File]): Components to include in the container. Must be between 1 and 10 components.
        accent_color (int | None): Optional accent color for the container.
        id (int | None): Unique id for the container.

    Attributes:
        attachments (List[File]): List of attachments in the container.
    """
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
            elif isinstance(c, Section):
                if c.attachment:
                    self.attachments.append(c.attachment)
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

    Args:
        custom_id (str): Custom id of the text input field. Must be a valid python identifier.
        id (int | None): Optional unique id of the text input field.
        required (bool): Whether this component is required to be filled (defaults to true).
        placeholder (str | None): Custom placeholder text if the input is empty; max 100 characters.
        value (str | None): Pre-filled value for this component; max 4000 characters.
        min_length (int): Minimum length of the text input field.
        max_length (int): Maximum length of the text input field.
        style (TextInputFieldLength): The style of the text input field.
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

# noinspection PyShadowingBuiltins
class FileUpload:
    """
    Represents a file upload component in a modal.

    Args:
        id (int): A unique id of the file upload field. Must be a valid python identifier.
        min_values (int): Minimum number of items that must be uploaded (defaults to 1)
        max_values (int): Maximum number of items that must be uploaded (defaults to 1)
        required (bool): Whether this component is required to be filled (defaults to true).
    """
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
        self.id = id  # noqa
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

# noinspection shadowing-builtins
class Checkbox:
    """
    Represents a checkbox component in a modal.

    Args:
        custom_id (str): A unique id of the checkbox field. Must be a valid python identifier.
        id (int | None): A unique id of the checkbox field. Must be a valid python identifier.
        default (bool): Whether this checkbox is checked by default (defaults to false).
    """
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
    """
    Represents an option in a checkbox group.

    Args:
        label (str): The label of the checkbox option.
        value (str): The value of the checkbox option.
        description (str | None): The description of the checkbox option.
        default (bool): Whether this checkbox option is checked by default (defaults to false).
    """
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


# noinspection shadowing-builtins
class CheckboxGroup:
    """
    Represents a group of checkboxes in a modal.

    Args:
        custom_id (str): A unique id of the checkbox group. Must be a valid python identifier.
        options (List[CheckboxGroupOption]): A list of checkbox options in the group.
        min_values (int | None): Minimum number of checkboxes that must be checked (defaults to None).
        max_values (int | None): Maximum number of checkboxes that can be checked (defaults to None).
        required (bool): Whether this component is required to be filled (defaults to true).
    """
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
    """
    Represents an option in a radio group.

    Args:
        label (str): Label of the radio option.
        value (str): Value of the radio option.
        description (str | None): Description of the radio option.
        default (bool): Whether this radio option is selected by default (defaults to false).
    """
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

# noinspection shadowing-builtins
class RadioGroup:
    """
    Represents a group of radio buttons in a modal.

    Args:
        custom_id (str): A unique id of the radio group. Must be a valid python identifier.
        options (List[RadioGroupOption]): A list of radio options in the group.
        required (bool): Whether this component is required to be filled (defaults to true).
    """
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
    """
    Represents a label component in a modal.

    Args:
        label (str): The text of the label.
        child (Select | TextInput | FileUpload | Checkbox | CheckboxGroup | RadioGroup): Child component for the label.
        id (int | None): Optional unique id of the label.
        description (str | None): The description of the label.
    """
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


TopLevelComponent = Union[
    str, TextDisplay, ActionRow, Section, Container, Separator, File, MediaGallery
]

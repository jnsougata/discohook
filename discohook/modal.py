from typing import Any, Callable, Dict, List, Optional

from .enums import MessageComponentType, TextInputFieldLength
from .view import Component


class TextInput:
    """
    Represents a text input field in a modal.

    Parameters
    ----------
    label: :class:`str`
        The label of the text input field.
    field_id: :class:`str`
        A unique id of the text input field. Must be valid python identifier.
    required: :class:`bool`
        Whether the text input field is required.
    hint: :class:`str`
        The hint of the text input field.
    default_text: :class:`str`
        The default text of the text input field.
    min_length: :class:`int`
        The minimum length of the text input field.
    max_length: :class:`int`
        The maximum length of the text input field.
    style: :class:`TextInputFieldLength`
        The style of the text input field.
    """

    def __init__(
        self,
        label: str,
        field_id: str,
        *,
        required: bool = False,
        hint: Optional[str] = None,
        default_text: Optional[str] = None,
        min_length: int = 0,
        max_length: int = 4000,
        style: TextInputFieldLength = TextInputFieldLength.short,
    ):
        self.label = label
        self.field_id = field_id
        self.required = required
        self.hint = hint
        self.default_text = default_text
        self.min_length = min_length
        self.max_length = max_length
        self.style = style

    def to_dict(self):
        return {
            "type": MessageComponentType.action_row.value,
            "components": [
                {
                    "type": 4,
                    "label": self.label,
                    "style": self.style.value,
                    "value": self.default_text,
                    "custom_id": self.field_id,
                    "min_length": self.min_length,
                    "max_length": self.max_length,
                    "placeholder": self.hint or "",
                    "required": self.required,
                }
            ],
        }


class Modal(Component):
    """
    A modal for discord.

    Parameters
    ----------
    title: :class:`str`
        The title of the modal.
    custom_id: :class:`str`
        The unique id of the modal.
    """

    def __init__(self, title: str, *, custom_id: Optional[str] = None):
        super().__init__(custom_id=custom_id)
        self.title = title
        # self.components: List[Component] = []
        self.rows: List[Dict[str, Any]] = []

    # def add_select_menu(self, menu: SelectMenu):
    #     self.components.append(menu)
    #     self.rows.append(menu.to_dict())

    def add_field(
        self,
        label: str,
        field_id: str,
        *,
        required: bool = False,
        hint: Optional[str] = None,
        default_text: Optional[str] = None,
        min_length: int = 0,
        max_length: int = 4000,
        style: TextInputFieldLength = TextInputFieldLength.short,
    ):
        """
        Add a text input field to the modal.

        Parameters
        ----------
        label: str
            The label of the field.
        field_id: str
            A unique id of the text input field. Must be valid python identifier.
        required: bool
            Whether the field is required or not.
        hint: str
            The hint to be displayed on the field.
        default_text: str
            The default text to be displayed on the field.
        min_length: int
            The minimum length of the field.
        max_length: int
            The maximum length of the field.
        style: TextInputFieldLength
            The style of the field.
        """
        self.rows.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [
                    {
                        "type": 4,
                        "label": label,
                        "style": style.value,
                        "value": default_text,
                        "custom_id": field_id,
                        "min_length": min_length,
                        "max_length": max_length,
                        "placeholder": hint or "",
                        "required": required,
                    }
                ],
            }
        )

    def to_dict(self):
        """
        Convert the modal to a dict to be sent to discord. For internal use only.
        """
        data = {"title": self.title, "custom_id": self.custom_id, "components": []}
        if self.rows:
            data["components"].extend(self.rows)
        return data


def modal(
    title: str,
    fields: List[TextInput],
    *,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a modal and registers a callback.

    Parameters
    ----------
    title: str
        The title of the modal.
    fields: List[TextInput]
        The fields to be added to the modal.
    custom_id: Optional[str]
        The custom id of the modal. If not provided, it will be generated automatically.

    Returns
    -------
    :class:`Modal`
    """
    def decorator(coro: Callable):
        m = Modal(title, custom_id=custom_id)
        for field in fields:
            m.rows.append(field.to_dict())
        m.callback = coro
        return m
    return decorator

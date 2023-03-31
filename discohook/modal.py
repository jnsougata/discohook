import secrets
from typing import Callable
# from .component import Button, SelectMenu
from .enums import MessageComponentType, TextInputFieldLength


class Modal:
    """
    A modal for discord.
    """
    def __init__(self, title: str):
        self.title = title
        self._callback = None
        self.custom_id = secrets.token_urlsafe(16)
        self._row = {"type": MessageComponentType.action_row.value, "components": []}
        self._data = {"title": title, "custom_id": self.custom_id, "components": []}

    # def add_select(self, select: SelectMenu):
    #   self._data["components"].append(
    #        {
    #            "type": component_types.action_row.value,
    #            "components": [select.json()]
    #        }
    #    )

    def add_field(
        self,
        label: str,
        field_id: str,
        *,
        required: bool = False,
        hint: str = None,
        default_text: str = None,
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
            The dev defined ID of the field to be used in the callback.
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
        self._data["components"].append(
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
        if self._row["components"]:
            self._data["components"].append(self._row)
        return self._data

    def onsubmit(self, coro: Callable):
        """
        A decorator to register a callback for the modal.
        """
        self._callback = coro

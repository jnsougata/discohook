from typing import Dict, Any, List
from .view import Component
from .enums import MessageComponentType, TextInputFieldLength


class Modal(Component):
    """
    A modal for discord.
    """
    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.rows: List[Dict[str, Any]] = []

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

import secrets
from functools import wraps
from typing import Callable
from typing import Optional, Union, Any, Sequence, List, Dict
from .enums import component_types
from .component import Button, SelectMenu


class Modal:

    def __init__(self, title: str):
        self.title = title
        self._callback = None
        self.custom_id = secrets.token_urlsafe(16)
        self._action_row = {"type": component_types.action_row.value, "components": []}
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
            custom_id: str,
            *,
            required: bool = False,
            hint: str = None,
            default_text: str = None,
            min_length: int = 0,
            max_length: int = 4000,
            style: int = 1,
    ):
        self._data["components"].append(
            {
                "type": component_types.action_row.value,
                "components": [
                    {
                        "type": 4,
                        "label": label,
                        "style": style,
                        "value": default_text,
                        "custom_id": custom_id,
                        "min_length": min_length,
                        "max_length": max_length,
                        "placeholder": hint or "",
                        "required": required,
                    }
                ]
            }
        )

    def json(self):
        if self._action_row["components"]:
            self._data['components'].append(self._action_row)
        return self._data

    def on_submit(self, coro: Callable):
        self._callback = coro

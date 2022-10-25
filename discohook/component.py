import secrets
from fastapi import FastAPI
from functools import wraps
from .emoji import PartialEmoji
from .enums import button_styles, component_types
from typing import Optional, Union, List, Dict, Any, Callable


class Button:
    def __init__(
            self,
            label: str,
            *,
            url: Optional[str] = None,
            style: button_styles = button_styles.blurple,
            disabled: Optional[bool] = False,
            emoji: Optional[PartialEmoji] = None,
    ):
        self.label = label
        self.url = url
        self.style = style
        self.disabled = disabled
        self.custom_id = secrets.token_urlsafe(16)
        self.emoji = emoji
        self._handler: Optional[Callable] = None

    def on_click(self, coro: Callable):
        self._handler = coro

    def to_json(self) -> Dict[str, Any]:
        payload = {
            "type": component_types.button.value,
            "style": self.style.value,
            "label": self.label,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.emoji:
            payload["emoji"] = self.emoji.to_json()
        if self.url and self.style is button_styles.url:
            payload["url"] = self.url
        return payload


class Components:
    def __init__(self):
        self._structure: List[Dict[str, Any]] = []
        self._items = []

    def add_buttons(self, *buttons: Button):
        self._structure.append({
            "type": component_types.action_row.value,
            "components": [button.to_json() for button in buttons[:5]],
        })
        self._items.extend(buttons[:5])

    def add_select_menu(self):
        raise NotImplementedError

    def to_json(self) -> List[Dict[str, Any]]:
        return self._structure

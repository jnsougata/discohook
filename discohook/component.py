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
        self._callback: Optional[Callable] = None

    def on_click(self, coro: Callable):
        self._callback = coro

    def json(self) -> Dict[str, Any]:
        payload = {
            "type": component_types.button.value,
            "style": self.style.value,
            "label": self.label,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.emoji:
            payload["emoji"] = self.emoji.json()
        if self.url and self.style is button_styles.url:
            payload["url"] = self.url
        return payload


class SelectOption:
    def __init__(
            self,
            label: str,
            value: str,
            *,
            description: Optional[str] = None,
            emoji: Optional[PartialEmoji] = None,
            default: Optional[bool] = False,
    ):
        self.label = label
        self.value = value
        self.description = description
        self.emoji = emoji
        self.default = default

    def json(self) -> Dict[str, Any]:
        payload = {
            "label": self.label,
            "value": self.value,
            "description": self.description,
            "default": self.default,
        }
        if self.emoji:
            payload["emoji"] = self.emoji.json()
        return payload


class SelectMenu:
    def __init__(
            self,
            options: List[SelectOption],
            *,
            placeholder: Optional[str] = None,
            min_values: Optional[int] = None,
            max_values: Optional[int] = None,
            disabled: Optional[bool] = False,
    ):
        self._callback: Optional[Callable] = None
        self.custom_id = secrets.token_urlsafe(16)
        self.data = {
            "type": 3,
            "custom_id": self.custom_id,
            "options": [option.json() for option in options],
        }
        if placeholder:
            self.data["placeholder"] = placeholder
        if min_values:
            self.data["min_values"] = min_values
        if max_values:
            self.data["max_values"] = max_values
        if disabled:
            self.data["disabled"] = disabled

    def on_selection(self, coro: Callable):
        self._callback = coro

    def json(self) -> Dict[str, Any]:
        return self.data


class Components:
    def __init__(self):
        self.children = []
        self._structure: List[Dict[str, Any]] = []

    def add_buttons(self, *buttons: Button):
        self._structure.append({
            "type": component_types.action_row.value,
            "components": [button.json() for button in buttons[:5]],
        })
        self.children.extend(buttons[:5])

    def add_select_menu(self, select_menu: SelectMenu):
        self._structure.append({
            "type": component_types.action_row.value,
            "components": [select_menu.json()],
        })
        self.children.append(select_menu)

    def json(self) -> List[Dict[str, Any]]:
        return self._structure

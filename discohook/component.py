import secrets
from fastapi import FastAPI
from functools import wraps
from .emoji import PartialEmoji
from .enums import ButtonStyle, MessageComponentType, SelectMenuType, ChannelType
from typing import Optional, Union, List, Dict, Any, Callable


class Button:
    def __init__(
            self,
            label: str,
            *,
            url: Optional[str] = None,
            style: ButtonStyle = ButtonStyle.blurple,
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
            "type": MessageComponentType.button.value,
            "style": self.style.value,
            "label": self.label,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.emoji:
            payload["emoji"] = self.emoji.json()
        if self.url and self.style is ButtonStyle.url:
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
            menu_type: SelectMenuType,
            options: Optional[List[SelectOption]] = None,
            *,
            channel_types: Optional[List[ChannelType]] = None,
            placeholder: Optional[str] = None,
            min_values: Optional[int] = None,
            max_values: Optional[int] = None,
            disabled: Optional[bool] = False,
    ):
        self._callback: Optional[Callable] = None
        self.custom_id = secrets.token_urlsafe(16)
        self.data = {
            "type": menu_type.value,
            "custom_id": self.custom_id,
        }
        if (menu_type == SelectMenuType.text) and (options is not None):
            self.data["options"] = [option.json() for option in options]
        if (menu_type == SelectMenuType.channel) and (channel_types is not None):
            self.data["channel_types"] = [channel_type.value for channel_type in channel_types]
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


class ActionRows:
    def __init__(self, buttons: Optional[List[Button]] = None, select_menus: Optional[List[SelectMenu]] = None):
        self._children = []
        self._structure: List[Dict[str, Any]] = []
        if buttons:
            self.append_button_row(*buttons)
        if select_menus:
            for select_menu in select_menus:
                self.append_select_menu(select_menu)

    def append_button_row(self, *buttons: Button):
        self._structure.append({
            "type": MessageComponentType.action_row.value,
            "components": [button.json() for button in buttons[:5]],
        })
        self._children.extend(buttons[:5])

    def append_select_menu(self, select_menu: SelectMenu):
        self._structure.append({
            "type": MessageComponentType.action_row.value,
            "components": [select_menu.json()],
        })
        self._children.append(select_menu)

    def json(self) -> List[Dict[str, Any]]:
        return self._structure

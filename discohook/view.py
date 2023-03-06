import secrets
from .emoji import PartialEmoji
from typing import Optional, List, Dict, Any, Callable, Union
from .enums import ButtonStyle, MessageComponentType, SelectMenuType, ChannelType


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
        self.url = url
        self.label = label
        self.emoji = emoji
        self.style = style
        self.disabled = disabled
        self.custom_id = secrets.token_urlsafe(16)
        self._callback: Optional[Callable] = None

    def onclick(self, coro: Callable):
        self._callback = coro

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "type": MessageComponentType.button.value,
            "style": self.style.value,
            "label": self.label,
        }
        if not self.style == ButtonStyle.link:
            payload["custom_id"] = self.custom_id
            payload["disabled"] = self.disabled
        if self.emoji:
            payload["emoji"] = self.emoji.to_dict()
        if self.url and self.style == ButtonStyle.link:
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

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "label": self.label,
            "value": self.value,
            "description": self.description,
            "default": self.default,
        }
        if self.emoji:
            payload["emoji"] = self.emoji.to_dict()
        return payload


class SelectMenu:
    def __init__(
        self,
        options: Optional[List[SelectOption]] = None,
        *,
        channel_types: Optional[List[ChannelType]] = None,
        placeholder: Optional[str] = None,
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        disabled: Optional[bool] = False,
        type: SelectMenuType = SelectMenuType.text,  # noqa
    ):
        self._callback: Optional[Callable] = None
        self.custom_id = secrets.token_urlsafe(16)
        self.data = {
            "type": type.value,
            "custom_id": self.custom_id,
        }
        if (type == SelectMenuType.text) and (options is not None):
            self.data["options"] = [option.to_dict() for option in options]
        if (type == SelectMenuType.channel) and (channel_types is not None):
            self.data["channel_types"] = [
                channel_type.value for channel_type in channel_types
            ]
        if placeholder:
            self.data["placeholder"] = placeholder
        if min_values:
            self.data["min_values"] = min_values
        if max_values:
            self.data["max_values"] = max_values
        if disabled:
            self.data["disabled"] = disabled

    def onselection(self, coro: Callable):
        self._callback = coro

    def to_dict(self) -> Dict[str, Any]:
        return self.data


class View:
    def __init__(self):
        self.components: List[Dict[str, Any]] = []
        self.children: List[Union[Button, SelectMenu]] = []

    def add_button_row(self, *buttons: Button):
        self.components.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [button.to_dict() for button in buttons[:5]],
            }
        )
        self.children.extend(buttons[:5])

    def add_select_menu(self, select_menu: SelectMenu):
        self.components.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [select_menu.to_dict()],
            }
        )
        self.children.append(select_menu)

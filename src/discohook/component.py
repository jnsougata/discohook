import secrets
from .enums import button_styles, component_types
from .emoji import PartialEmoji
from typing import Optional, Union, List, Dict, Any


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
        self.custom_id = secrets.token_hex(8)
        self.emoji = emoji

    def to_json(self) -> Dict[str, Any]:
        payload = dict()
        payload["type"] = component_types.button.value
        payload["style"] = self.style.value
        payload["label"] = self.label
        payload["disabled"] = self.disabled
        payload["custom_id"] = self.custom_id
        if self.emoji:
            payload["emoji"] = self.emoji.to_json()
        if self.url and self.style is button_styles.url:
            payload["url"] = self.url
        return payload


class Component:
    def __init__(self):
        self._structure: List[Dict[str, Any]] = list()

    def add_buttons(self, *buttons: Button):
        self._structure.append({
            "type": component_types.action_row.value,
            "components": [button.to_json() for button in buttons[:5]],
        })

    def add_select_menu(self):
        raise NotImplementedError

    def to_json(self) -> List[Dict[str, Any]]:
        return self._structure

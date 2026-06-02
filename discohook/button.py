from typing import Any, Dict, Optional, Union

from .emoji import PartialEmoji
from .enums import ButtonStyle, ComponentType
from .handler import Handler


class Button:
    """
    Represents a discord button type component.

    Attributes:
        label (str): Label of the button.
        url (str | None): Url to be opened for `ButtonStyle.link`.
        style (ButtonStyle): Style of the button.
        disabled (bool): Whether the button is disabled or not.
        emoji (PartialEmoji): Emoji object for the button.
        handler (Handler): Handler for the button.
    """

    def __init__(
        self,
        label: Optional[str] = None,
        *,
        url: Optional[str] = None,
        style: ButtonStyle = ButtonStyle.blurple,
        disabled: bool = False,
        emoji: Optional[Union[str, PartialEmoji]] = None,
        handler: Optional[Handler] = None,
    ):
        """
        Initialize the button.

        Args:
            label (str | None): Label of the button.
            url (str | None): Url to be opened for `ButtonStyle.link`.
            style (ButtonStyle): Style of the button.
            disabled (bool): Whether the button is disabled or not.
            emoji (str | PartialEmoji | None): Emoji to be displayed on the button.

        """
        self.handler = handler
        self.url = url
        self.label = label
        self.style = style
        self.disabled = disabled
        self.emoji = PartialEmoji(name=emoji) if isinstance(emoji, str) else emoji

    def to_dict(self) -> Dict[str, Any]:
        """
        Builds a dictionary representation of the button.

        This is used internally by the library. It is rarely required for general purpose use cases.

        Returns:
            dict: Dictionary representation of the button.
        """
        assert self.label or self.emoji, "label or emoji must be provided"
        payload = {
            "type": ComponentType.button,
            "style": self.style,
            "disabled": self.disabled,
        }
        if self.label:
            payload["label"] = self.label
        if self.emoji:
            payload["emoji"] = self.emoji.to_dict()
        if self.style != ButtonStyle.link:
            payload["custom_id"] = self.handler.id
        if self.url and self.style == ButtonStyle.link:
            payload["url"] = self.url
        return payload

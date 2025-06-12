from typing import Any, Dict, Optional, Union

from .emoji import PartialEmoji
from .enums import ButtonStyle, ComponentType
from .handler import Handler


class Button:
    """
    Represents a discord button type component.

    Parameters
    ----------
    label: str | None
        The text to be displayed on the button.
    url: str | None
        The url to be opened when the button is clicked if the style is set to :attr:`ButtonStyle.link`.
    style: :class:`ButtonStyle`
        The style of the button.
    disabled: :class:`bool`
        Whether the button is disabled or not.
    emoji: :class:`str` | :class:`PartialEmoji` | None
        The emoji to be displayed on the button.
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
        self.handler = handler
        self.url = url
        self.label = label
        self.style = style
        self.disabled = disabled
        self.emoji = PartialEmoji(name=emoji) if isinstance(emoji, str) else emoji

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
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

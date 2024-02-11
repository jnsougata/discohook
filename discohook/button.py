import asyncio
from typing import Any, Callable, Dict, Optional, Union, TYPE_CHECKING

from .abc import Component
from .emoji import PartialEmoji
from .enums import ComponentType, ButtonStyle


if TYPE_CHECKING:
    from .interaction import Interaction


class Button(Component):
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
        custom_id: Optional[str] = None,
    ):
        super().__init__(ComponentType.button, custom_id)
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
            "type": self.type,
            "style": self.style,
            "disabled": self.disabled,
        }
        if self.label:
            payload["label"] = self.label
        if self.emoji:
            payload["emoji"] = self.emoji.to_dict()
        if self.style != ButtonStyle.link:
            payload["custom_id"] = self.custom_id
        if self.url and self.style == ButtonStyle.link:
            payload["url"] = self.url
        return payload


def new(
    label: Optional[str] = None,
    *,
    style: ButtonStyle = ButtonStyle.blurple,
    disabled: bool = False,
    emoji: Optional[Union[str, PartialEmoji]] = None,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a button and registers a callback.

    Parameters
    ----------
    label: str | None
        The text to be displayed on the button.
    style: :class:`ButtonStyle`
        The style of the button.
    disabled: :class:`bool`
        Whether the button is disabled or not.
    emoji: :class:`str` | :class:`PartialEmoji` | None
        The emoji to be displayed on the button.
    custom_id: Optional[:class:`str`]
        The custom id of the button.
    """
    def decorator(coro: Callable[["Interaction"], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Button(
            label=label,
            style=style,
            disabled=disabled,
            emoji=emoji,
            custom_id=custom_id,
        )
        self.callback = coro
        return self

    return decorator


def link(label: Optional[str], *, url: str, emoji: Optional[Union[str, PartialEmoji]] = None):
    """
    A decorator that creates a link button.

    Parameters
    ----------
    label: str | None
        The text to be displayed on the button.
    url: str
        The url to be opened when the button is clicked.
    emoji: :class:`str` | :class:`PartialEmoji` | None
        The emoji to be displayed on the button.
    """
    return Button(label=label, url=url, style=ButtonStyle.link, emoji=emoji)

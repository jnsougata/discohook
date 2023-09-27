import asyncio
from typing import Any, Dict, List, Optional, Callable, TYPE_CHECKING, Union

from .abc import Component
from .emoji import PartialEmoji
from .enums import ComponentType, SelectType, ChannelType


if TYPE_CHECKING:
    from .interaction import Interaction
    from .channel import PartialChannel
    from .role import PartialRole
    from .user import User


class SelectOption:
    """
    Represents a discord select menu option object.

    Parameters
    ----------
    label: :class:`str`
        The text to be displayed on the option.
    value: :class:`str`
        The value to be sent to the bot when the option is selected.
    description: str | None
        The description to be displayed on the option.
    emoji: :class:`str` | :class:`PartialEmoji` | None
        The emoji to be displayed on the option.
    default: :class:`bool`
        Whether the option is selected by default or not.
    """

    def __init__(
        self,
        label: str,
        value: str,
        *,
        description: Optional[str] = None,
        emoji: Optional[Union[PartialEmoji, str]] = None,
        default: bool = False,
    ):
        self.label = label
        self.value = value
        self.description = description
        self.emoji = emoji
        self.default = default

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
        """
        payload = {
            "label": self.label,
            "value": self.value,
            "description": self.description,
            "default": self.default,
        }
        if self.emoji:
            self.emoji = self.emoji if isinstance(self.emoji, PartialEmoji) else PartialEmoji(name=self.emoji)
            payload["emoji"] = self.emoji.to_dict()
        return payload


class Select(Component):
    """
    Represents a discord select menu component.

    Parameters
    ----------
    placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    kind: :class:`SelectType`
        The type of the select menu.
    """

    def __init__(
        self,
        kind: SelectType,
        *,
        placeholder: Optional[str] = None,
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        disabled: Optional[bool] = False,
        custom_id: Optional[str] = None,
    ):
        kind = ComponentType(kind.value)
        super().__init__(kind, custom_id)
        self.placeholder: Optional[str] = placeholder
        self.min_values: Optional[int] = min_values
        self.max_values: Optional[int] = max_values
        self.disabled: Optional[bool] = disabled
        self.options: Optional[List[SelectOption]] = None
        self.channel_types: Optional[List[ChannelType]] = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
        """
        payload = {
            "type": self.kind,
            "custom_id": self.custom_id
        }
        if self.kind == ComponentType.select_text:
            if not self.options:
                raise ValueError("options must be provided for text select menus")
            payload["options"] = [option.to_dict() for option in self.options]
        if self.kind == ComponentType.select_channel and self.channel_types:
            payload["channel_types"] = [x.value for x in self.channel_types]
        if self.placeholder:
            payload["placeholder"] = self.placeholder
        if self.min_values:
            payload["min_values"] = self.min_values
        if self.max_values:
            payload["max_values"] = self.max_values
        if self.disabled:
            payload["disabled"] = self.disabled
        return payload


def channel(
    types: Optional[List[ChannelType]] = None,
    *,
    placeholder: Optional[str] = None,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a channel select menu and registers a callback.

    Parameters
    ----------
    types: Optional[List[:class:`ChannelType`]]
        The channel types to be displayed on the select menu.
    placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """
    def decorator(coro: Callable[["Interaction", List["PartialChannel"]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            kind=SelectType.channel,
            custom_id=custom_id,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
        )
        self.channel_types = types
        self.callback = coro
        return self

    return decorator


def text(
    options: List[SelectOption],
    *,
    placeholder: Optional[str] = None,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a text select menu and registers a callback.

    Parameters
    ----------
    options: List[:class:`SelectOption`]
        The options to be displayed on the select menu.
    placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """
    def decorator(coro: Callable[["Interaction", List[str]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            kind=SelectType.text,
            custom_id=custom_id,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
        )
        self.options = options
        self.callback = coro
        return self

    return decorator


def role(
    placeholder: Optional[str] = None,
    *,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a select menu and registers a callback.

    For text select menus, use :meth:`text` and for channel select menus, use :meth:`channel`.

    Parameters
    ----------
    placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.

    Raises
    ------
    TypeError
        If the callback is not a coroutine.
    """

    def decorator(coro: Callable[["Interaction", List["PartialRole"]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            kind=SelectType.role,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            custom_id=custom_id,
        )
        self.callback = coro
        return self

    return decorator


def user(
    placeholder: Optional[str] = None,
    *,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a user select menu and registers a callback.

    Parameters
    ----------
    placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """
    def decorator(coro: Callable[["Interaction", List["User"]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            kind=SelectType.user,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            custom_id=custom_id,
        )
        self.callback = coro
        return self

    return decorator


def mentionable(
    placeholder: Optional[str] = None,
    *,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a mentionable select menu and registers a callback.

    Parameters
    ----------
     placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """
    def decorator(coro: Callable[["Interaction", List[Union["User", "PartialRole"]]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            kind=SelectType.mentionable,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            custom_id=custom_id,
        )
        self.callback = coro
        return self

    return decorator

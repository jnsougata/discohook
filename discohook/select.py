import asyncio
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union

from .component import Component
from .emoji import PartialEmoji
from .enums import ChannelType, ComponentType, SelectDefaultValueType, SelectType

if TYPE_CHECKING:
    from .channel import PartialChannel
    from .interaction import Interaction
    from .role import PartialRole
    from .user import User


# noinspection PyShadowingBuiltins
class SelectDefaultValue:
    """
    Represents a discord select menu default option object.
    Only applicable for non string select menus.

    Parameters
    ----------
    id: :class:`str`
        The id of the user, role or channel.
    type: :class:`SelectDefaultValueType`
        The type of the default value.
    """

    def __init__(self, id: str, type: SelectDefaultValueType):
        self.id = id
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
        """
        payload = {"id": self.id, "type": self.type}
        return payload


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
        self.emoji = PartialEmoji(name=emoji) if isinstance(emoji, str) else emoji
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
            payload["emoji"] = self.emoji.to_dict()
        return payload


# noinspection PyShadowingBuiltins
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
    type: :class:`SelectType`
        The type of the select menu.
    """

    def __init__(
        self,
        type: SelectType,
        *,
        placeholder: Optional[str] = None,
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        disabled: Optional[bool] = False,
        custom_id: Optional[str] = None,
    ):
        super().__init__(ComponentType(type.value), custom_id)
        self.placeholder: Optional[str] = placeholder
        self.min_values: Optional[int] = min_values
        self.max_values: Optional[int] = max_values
        self.disabled: Optional[bool] = disabled
        self.options: Optional[List[SelectOption]] = None
        self.channel_types: Optional[List[ChannelType]] = None
        self.default_values: Optional[List[SelectDefaultValue]] = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
        """
        payload = {"type": self.type, "custom_id": self.custom_id}
        if self.type == ComponentType.select_text:
            if not self.options:
                raise ValueError("options must be provided for text select menus")
            payload["options"] = [option.to_dict() for option in self.options]
        elif self.type != ComponentType.select_text and self.default_values:
            payload["default_values"] = [
                value.to_dict() for value in self.default_values
            ]
        if self.type == ComponentType.select_channel and self.channel_types:
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
    default_values: Optional[List[SelectDefaultValue]] = None,
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
    default_values: Optional[List[:class:`SelectDefaultValue`]]
        The default values of the select menu.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """

    def decorator(coro: Callable[["Interaction", List["PartialChannel"]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            type=SelectType.channel,
            custom_id=custom_id,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
        )
        self.channel_types = types
        self.default_values = default_values
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
            type=SelectType.text,
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
    default_values: Optional[List[SelectDefaultValue]] = None,
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
    default_values: Optional[List[:class:`SelectDefaultValue`]]
        The default values of the select menu.
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
            type=SelectType.role,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            custom_id=custom_id,
        )
        self.default_values = default_values
        self.callback = coro
        return self

    return decorator


def user(
    placeholder: Optional[str] = None,
    *,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    default_values: Optional[List[SelectDefaultValue]] = None,
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
    default_values: Optional[List[:class:`SelectDefaultValue`]]
        The default values of the select menu.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """

    def decorator(coro: Callable[["Interaction", List["User"]], Any]):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            type=SelectType.user,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            custom_id=custom_id,
        )
        self.default_values = default_values
        self.callback = coro
        return self

    return decorator


def mentionable(
    placeholder: Optional[str] = None,
    *,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    disabled: Optional[bool] = False,
    default_values: Optional[List[SelectDefaultValue]] = None,
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
    default_values: Optional[List[:class:`SelectDefaultValue`]]
        The default values of the select menu.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.
    """

    def decorator(
        coro: Callable[["Interaction", List[Union["User", "PartialRole"]]], Any]
    ):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self = Select(
            type=SelectType.mentionable,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            custom_id=custom_id,
        )
        self.default_values = default_values
        self.callback = coro
        return self

    return decorator

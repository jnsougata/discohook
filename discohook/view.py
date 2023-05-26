import asyncio
import secrets
from typing import Any, Callable, Dict, List, Optional, Union

from .emoji import PartialEmoji
from .enums import ButtonStyle, ChannelType, MessageComponentType, SelectType


class Component:
    """
    Represents a discord component.

    Parameters
    ----------
    type: :class:`MessageComponentType`
        The type of the component.
    """

    def __init__(self, type: Optional[MessageComponentType] = None, custom_id: Optional[str] = None):
        self.type = type
        self.callback: Optional[Callable] = None
        self.custom_id = custom_id or secrets.token_urlsafe(16)
        self.checks: List[Callable] = []

    def on_interaction(self, coro: Callable):
        """
        Decorator that registers a callback to be called when the component is interacted with.

        Parameters
        ----------
        coro: Callable
            The coroutine to be called when the component is interacted with.

        Raises
        ------
        TypeError
            If the callback is not a coroutine.
        """
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        self.callback = coro

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning("No callback registered for this component.")
        return self.callback(*args, **kwargs)


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
        super().__init__(MessageComponentType.button, custom_id)
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
        payload = {
            "type": self.type.value,
            "style": self.style.value,
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
        emoji: Optional[PartialEmoji] = None,
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
            payload["emoji"] = self.emoji.to_dict()
        return payload


class Select(Component):
    """
    Represents a discord select menu component.

    Parameters
    ----------
    options: Optional[List[:class:`SelectOption`]]
        The options to be displayed on the select menu.
    channel_types: Optional[List[:class:`ChannelType`]]
        The channel types to be displayed on the select menu if the type is set to :attr:`SelectMenuType.channel`.
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
        options: Optional[List[SelectOption]] = None,
        *,
        placeholder: Optional[str] = None,
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        channel_types: Optional[List[ChannelType]] = None,
        type: Union[MessageComponentType, SelectType] = MessageComponentType.text_select,
        disabled: Optional[bool] = False,
        custom_id: Optional[str] = None,
    ):
        super().__init__(type, custom_id)
        self.data = {"type": type.value, "custom_id": self.custom_id}
        self.options: Optional[List[SelectOption]] = options
        self.channel_types: Optional[List[ChannelType]] = channel_types
        self.placeholder: Optional[str] = placeholder
        self.min_values: Optional[int] = min_values
        self.max_values: Optional[int] = max_values
        self.disabled: Optional[bool] = disabled

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
        """
        if self.options:
            if self.type == MessageComponentType.text_select:
                self.data["options"] = [option.to_dict() for option in self.options]  # type: ignore
            if self.type == MessageComponentType.channel_select and self.channel_types:
                self.data["channel_types"] = [channel_type.value for channel_type in self.channel_types]
        if self.placeholder:
            self.data["placeholder"] = self.placeholder
        if self.min_values:
            self.data["min_values"] = self.min_values
        if self.max_values:
            self.data["max_values"] = self.max_values
        if self.disabled:
            self.data["disabled"] = self.disabled
        return self.data


class View:
    """
    Represents a discord message component tree.

    This is used to create actions rows and add buttons and select menus to them without having tree conflicts.

    Attributes
    ----------
    components: List[:class:`dict`]
        The list of components to be sent to discord. Do not modify this directly.
    children: List[Union[:class:`Button`, :class:`Select`]]
        The list of children to be sent to discord. Do not modify this directly.
    """

    def __init__(self):
        self.components: List[Dict[str, Any]] = []
        self.children: List[Union[Button, Select]] = []

    def add_buttons(self, *buttons: Union[Button, Any]):
        """
        Adds a row of buttons to the view.
        Each row can only contain up to 5 buttons.
        Action rows having buttons can not have select menus.

        Parameters
        ----------
        *buttons: :class:`Button`
            The buttons to be added to the view.
        """
        self.components.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [btn.to_dict() for btn in buttons[:5]],
            }
        )
        # TODO: Add support auto parse more than 5 buttons and add them to the next row.
        self.children.extend(buttons[:5])

    # noinspection PyShadowingNames
    def add_select(self, select: Union[Select, Any]):
        """
        Adds a row of select to the view.
        Each row can only contain up to 1 select menu.
        Action rows having select menu can not have buttons.

        Parameters
        ----------
        select: :class:`Select`
            The select menu to be added to the view.
        """
        self.components.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [select.to_dict()],
            }
        )
        self.children.append(select)


def button(
    label: Optional[str] = None,
    *,
    url: Optional[str] = None,
    style: ButtonStyle = ButtonStyle.blurple,
    disabled: Optional[bool] = False,
    emoji: Optional[Union[str, PartialEmoji]] = None,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a button and registers a callback to be called when the button is clicked.

    Parameters
    ----------
    label: Optional[:class:`str`]
        The label of the button.
    url: Optional[:class:`str`]
        The url of the button. This is only used if the style is set to :attr:`ButtonStyle.link`.
    style: :class:`ButtonStyle`
        The style of the button.
    disabled: Optional[:class:`bool`]
        Whether the button is disabled or not.
    emoji: Optional[Union[:class:`str`, :class:`PartialEmoji`]]
        The emoji of the button.
    custom_id: Optional[:class:`str`]
        The custom id of the button.

    Returns
    -------
    :class:`Button`

    Raises
    ------
    TypeError
        If the callback is not a coroutine.
    """

    def decorator(coro: Callable):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        btn = Button(label=label, style=style, url=url, disabled=disabled, emoji=emoji, custom_id=custom_id)
        btn.callback = coro
        return btn

    return decorator


def select(
    options: Optional[List[SelectOption]] = None,
    *,
    placeholder: Optional[str] = None,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    channel_types: Optional[List[ChannelType]] = None,
    type: Union[MessageComponentType, SelectType] = MessageComponentType.text_select,
    disabled: Optional[bool] = False,
    custom_id: Optional[str] = None,
):
    """
    A decorator that creates a select menu and registers a callback.

    Parameters
    ----------
    options: Optional[List[:class:`SelectOption`]]
        The options to be displayed on the select menu.
    placeholder: Optional[:class:`str`]
        The placeholder to be displayed on the select menu.
    min_values: Optional[:class:`int`]
        The minimum number of options that can be selected.
    max_values: Optional[:class:`int`]
        The maximum number of options that can be selected.
    channel_types: Optional[List[:class:`ChannelType`]]
        The channel types to be displayed on the select menu. Used only for channel select menus.
    disabled: Optional[:class:`bool`]
        Whether the select menu is disabled or not.
    type: :class:`SelectType`
        The type of the select menu.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.

    Returns
    -------
    :class:`Select`

    Raises
    ------
    TypeError
        If the callback is not a coroutine.
    """

    def decorator(coro: Callable):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Callback must be a coroutine.")
        menu = Select(
            options=options,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            channel_types=channel_types,
            type=type,
            disabled=disabled,
            custom_id=custom_id,
        )
        menu.callback = coro
        return menu

    return decorator


def component_checker(*checks: Callable):
    """
    Decorator for adding a checks to a component.

    Parameters
    ----------
    *checks: Callable
        The checks to be added to the component.

    Returns
    -------
    Component
        The component with the checks added to it.

    Raises
    ------
    TypeError
        If any of the checks is not a coroutine.
    """

    def decorator(comp: Component):
        for check in checks:
            if not asyncio.iscoroutinefunction(check):
                raise TypeError(f"check `{check.__name__}` must be a coroutine.")
        comp.checks.extend(checks)
        return comp

    return decorator

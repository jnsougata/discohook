import asyncio
import secrets
from typing import Any, Dict, List, Optional, Union, Callable, TYPE_CHECKING

from .abc import Interactable
from .emoji import PartialEmoji
from .enums import ButtonStyle, ChannelType, ComponentType, SelectType

if TYPE_CHECKING:
    from .interaction import Interaction


class Component(Interactable):
    """
    Represents a discord component.

    Parameters
    ----------
    kind: :class:`ComponentType`
        The type of the component.
    """

    def __init__(self, kind: Optional[ComponentType] = None, custom_id: Optional[str] = None):
        super().__init__()
        self.kind = kind
        self.callback: Optional[Callable[["Interaction", Any], Any]] = None
        self.custom_id = custom_id or secrets.token_urlsafe(8)

    def on_interaction(self):
        """
        Decorator that registers a callback to be called when the component is interacted with.

        Raises
        ------
        TypeError
            If the callback is not a coroutine.
        """

        def decorator(coro: Callable[["Interaction", ...], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Callback must be a coroutine.")
            self.callback = coro

        return decorator

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
        super().__init__(ComponentType.button, custom_id)
        self.url = url
        self.label = label
        self.style = style
        self.disabled = disabled
        self.emoji = PartialEmoji(name=emoji) if isinstance(emoji, str) else emoji

    @classmethod
    def link(cls, label: str, url: str):
        """
        A decorator that creates a link button.

        Parameters
        ----------
        label: str
            The text to be displayed on the button.
        url: str
            The url to be opened when the button is clicked.
        """
        return cls(label=label, url=url, style=ButtonStyle.link)

    @classmethod
    def new(
        cls,
        label: str,
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
        label: str
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
            self = cls(
                label=label,
                style=style,
                disabled=disabled,
                emoji=emoji,
                custom_id=custom_id,
            )
            self.callback = coro
            return self

        return decorator

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
            "style": self.style,
            "disabled": self.disabled,
        }
        if self.label:
            payload["label"] = self.label
        if self.emoji:
            payload["emoji"] = self.emoji
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
            payload["emoji"] = self.emoji
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

    @classmethod
    def text(
        cls,
        *options: SelectOption,
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
        def decorator(coro: Callable[["Interaction", List[Any]], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Callback must be a coroutine.")
            self = cls(
                kind=SelectType.channel,
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

    @classmethod
    def channel(
        cls,
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
        def decorator(coro: Callable[["Interaction", List[Any]], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Callback must be a coroutine.")
            self = cls(
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

    @classmethod
    def new(
        cls,
        placeholder: Optional[str] = None,
        *,
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        disabled: Optional[bool] = False,
        custom_id: Optional[str] = None,
        kind: SelectType,
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
        kind: :class:`SelectType`
            The type of the select menu.
        custom_id: Optional[:class:`str`]
            The custom id of the select menu.

        Raises
        ------
        TypeError
            If the callback is not a coroutine.
        """

        def decorator(coro: Callable[["Interaction", List[Any]], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Callback must be a coroutine.")
            self = cls(
                kind=kind,
                placeholder=placeholder,
                min_values=min_values,
                max_values=max_values,
                disabled=disabled,
                custom_id=custom_id,
            )
            self.callback = coro
            return self

        return decorator

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
        batches = [buttons[i: i + 5] for i in range(0, len(buttons), 5)]
        for batch in batches:
            self.components.append(
                {
                    "type": ComponentType.action_row.value,
                    "components": [btn.to_dict() for btn in batch],
                }
            )
            self.children.extend(batch)

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
                "type": ComponentType.action_row.value,
                "components": [select.to_dict()],
            }
        )
        self.children.append(select)

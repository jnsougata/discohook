import secrets
from .emoji import PartialEmoji
from typing import Optional, List, Dict, Any, Callable, Union
from .enums import ButtonStyle, MessageComponentType, ChannelType, SelectMenuType


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

    def on_interaction(self, coro: Callable):
        """
        Decorator that registers a callback to be called when the component is interacted with.

        Parameters
        ----------
        coro

        Returns
        -------
        None
        """
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
    label: :class:`str`
        The text to be displayed on the button.
    url: Optional[:class:`str`]
        The url to be opened when the button is clicked if the style is set to :attr:`ButtonStyle.link`.
    style: :class:`ButtonStyle`
        The style of the button.
    disabled: Optional[:class:`bool`]
        Whether the button is disabled or not.
    emoji: Optional[:class:`PartialEmoji`]
        The emoji to be displayed on the button.
    """
    def __init__(
        self,
        label: str,
        *,
        url: Optional[str] = None,
        style: ButtonStyle = ButtonStyle.blurple,
        disabled: Optional[bool] = False,
        emoji: Optional[Union[str, PartialEmoji]] = None,
        custom_id: Optional[str] = None,
    ):
        super().__init__(MessageComponentType.button, custom_id)
        self.url = url  # type: ignore
        self.label = label
        self.style = style
        self.disabled = disabled  # type: ignore
        self.emoji = emoji if isinstance(emoji, PartialEmoji) else PartialEmoji(name=emoji)  # type: ignore

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
    """
    Represents a discord select menu option object.

    Parameters
    ----------
    label: :class:`str`
        The text to be displayed on the option.
    value: :class:`str`
        The value to be sent to the bot when the option is selected.
    description: Optional[:class:`str`]
        The description to be displayed on the option.
    emoji: Optional[:class:`PartialEmoji`]
        The emoji to be displayed on the option.
    default: Optional[:class:`bool`]
        Whether the option is selected by default or not.
    """
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
        self.description = description  # type: ignore
        self.emoji = emoji  # type: ignore
        self.default = default  # type: ignore

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
    type: :class:`SelectMenuType`
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
        type: Union[MessageComponentType, SelectMenuType] = MessageComponentType.text_select_menu,
        disabled: Optional[bool] = False,
        custom_id: Optional[str] = None,
    ):
        super().__init__(type, custom_id)
        self.data = {"type": type.value, "custom_id": self.custom_id}
        if (type.value == MessageComponentType.text_select_menu.value) and (options is not None):
            self.data["options"] = [option.to_dict() for option in options]
        if (type == MessageComponentType.channel_select_menu) and (channel_types is not None):
            self.data["channel_types"] = [channel_type.value for channel_type in channel_types]
        if placeholder:
            self.data["placeholder"] = placeholder
        if min_values:
            self.data["min_values"] = min_values
        if max_values:
            self.data["max_values"] = max_values
        if disabled:
            self.data["disabled"] = disabled

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the button.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the button.
        """
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

    def add_button_row(self, *buttons: Union[Button, Any]):
        """
        Adds a row of buttons to the view.

        Each actions rows can only contain up to 5 buttons. Action rows having buttons can not have select menus.

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
        self.children.extend(buttons[:5])

    def add_select_menu(self, menu: Union[Select, Any]):
        """
        Adds a select menu to the view.

        Each actions rows can only contain up to 1 select menu. Action rows having select menu can not have buttons.
        """
        self.components.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [menu.to_dict()],
            }
        )
        self.children.append(menu)


def button(
    label: str,
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
    label: :class:`str`
        The label of the button.
    url: Optional[:class:`str`]
        The url of the button. This is only used if the style is set to :attr:`ButtonStyle.link`.
    style: :class:`ButtonStyle`
        The style of the button.
    disabled: Optional[:class:`bool`]
        Whether the button is disabled or not.
    emoji: Optional[:class:`PartialEmoji`]
        The emoji of the button.
    custom_id: Optional[:class:`str`]
        The custom id of the button.

    Returns
    -------
    :class:`Button`
    """

    def decorator(coro: Callable):
        btn = Button(label=label, style=style, url=url, disabled=disabled, emoji=emoji, custom_id=custom_id)
        btn.on_interaction(coro)
        return btn
    return decorator


def select(
    options: Optional[List[SelectOption]] = None,
    *,
    placeholder: Optional[str] = None,
    min_values: Optional[int] = None,
    max_values: Optional[int] = None,
    channel_types: Optional[List[ChannelType]] = None,
    type: Union[MessageComponentType, SelectMenuType] = MessageComponentType.text_select_menu,
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
    type: :class:`SelectMenuType`
        The type of the select menu.
    custom_id: Optional[:class:`str`]
        The custom id of the select menu.

    Returns
    -------
    :class:`Select`
    """
    def decorator(coro: Callable):
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
        menu.on_interaction(coro)
        return menu
    return decorator

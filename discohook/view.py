import secrets
from .emoji import PartialEmoji
from typing import Optional, List, Dict, Any, Callable, Union
from .enums import ButtonStyle, MessageComponentType, SelectMenuType, ChannelType


class Button:
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
        """
        Registers a callback to be called when the button is clicked.

        Parameters
        ----------
        coro: :class:`Callable`
            The callback to be called when the button is clicked.
        """
        self._callback = coro

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
    """
    Represents a disocrd select menu option object.

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


class SelectMenu:
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
        type: SelectMenuType = SelectMenuType.text,  # noqa
        disabled: Optional[bool] = False,
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
        """
        Registers a callback to be called when the select menu is selected.

        Parameters
        ----------
        coro: :class:`Callable`
            The callback to be called when the select menu is selected.
        """
        self._callback = coro

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
    children: List[Union[:class:`Button`, :class:`SelectMenu`]]
        The list of children to be sent to discord. Do not modify this directly.
    """
    def __init__(self):
        self.components: List[Dict[str, Any]] = []
        self.children: List[Union[Button, SelectMenu]] = []

    def add_button_row(self, *buttons: Button):
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
                "components": [button.to_dict() for button in buttons[:5]],
            }
        )
        self.children.extend(buttons[:5])

    def add_select_menu(self, select_menu: SelectMenu):
        """
        Adds a select menu to the view.

        Each actions rows can only contain up to 1 select menu. Action rows having select menu can not have buttons.
        """
        self.components.append(
            {
                "type": MessageComponentType.action_row.value,
                "components": [select_menu.to_dict()],
            }
        )
        self.children.append(select_menu)

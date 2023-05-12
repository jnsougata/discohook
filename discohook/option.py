from typing import Any, Dict, List, Optional, Union

from .enums import ApplicationCommandOptionType, ChannelType


class Choice:
    """
    Represents a choice for a string, integer, or number option.

    Parameters
    ----------
    name: str
        The name of the choice.
    value: Union[str, int, float]
        The value of the choice.

    Notes
    -----
    The value of the choice must be of the same type as the option.
    """

    def __init__(self, name: str, value: Union[str, int, float]):
        self.name = name
        self.value = value  # type: ignore

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "value": self.value}


class Option:
    """
    Represents a base option for an application command.

    Parameters
    ----------
    name: str
        The name of the option. Must be a valid python identifier.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    type: AppCmdOptionType
        The type of the option.
    """

    def __init__(
        self,
        name: str,
        description: str,
        required: bool = False,
        *,
        type: ApplicationCommandOptionType,
    ):
        self.name = name
        self.description = description
        self.required = required
        self.type = type.value
        self.data: Dict[str, Any] = {
            "name": self.name,
            "description": self.description,
            "required": self.required,
            "type": self.type,
        }

    def to_dict(self) -> Dict[str, Any]:
        ...


class StringOption(Option):
    """
    Represents a string type option for an application command, subclassed from `Option`

    Parameters
    ----------
    name: str
        The name of the option.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    max_length: int
        The maximum length of the string.
    min_length: int
        The minimum length of the string.
    choices: List[Choice]
        The choices for the string.
    autocomplete: bool
        Whether the string should be auto completed or not.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        max_length: Optional[int] = 100,
        min_length: Optional[int] = 1,
        choices: Optional[List[Choice]] = None,
        autocomplete: Optional[bool] = False,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.string)
        self.choices = choices
        self.max_length = max_length
        self.min_length = min_length
        self.autocomplete = autocomplete

    def to_dict(self) -> Dict[str, Any]:
        if self.choices:
            self.data["choices"] = [choice.to_dict() for choice in self.choices]
        if self.autocomplete:
            self.data["autocomplete"] = self.autocomplete
        if self.max_length:
            self.data["max_length"] = self.max_length
        if self.min_length:
            self.data["min_length"] = self.min_length
        return self.data


class IntegerOption(Option):
    """
    Represents an integer type option for an application command, subclassed from `Option`

    Parameters
    ----------
    name: str
        The name of the option.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    max_value: int
        The maximum value of the integer.
    min_value: int
        The minimum value of the integer.
    choices: List[Choice]
        The choices for the integer.
    autocomplete: bool
        Whether the integer should be auto completed or not.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        max_value: Optional[int] = None,
        min_value: Optional[int] = None,
        choices: Optional[List[Choice]] = None,
        autocomplete: Optional[bool] = False,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.integer)
        self.choices = choices
        self.autocomplete = autocomplete
        self.max_value = max_value
        self.min_value = min_value

    def to_dict(self) -> Dict[str, Any]:
        if self.choices:
            self.data["choices"] = [choice.to_dict() for choice in self.choices]
        if self.autocomplete:
            self.data["autocomplete"] = self.autocomplete
        if self.max_value is not None:
            self.data["max_value"] = self.max_value
        if self.min_value is not None:
            self.data["min_value"] = self.min_value
        return self.data


class NumberOption(Option):
    """
    Represents a number type option for an application command, subclassed from `Option`

    Parameters
    ----------
    name: str
        The name of the option.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    max_value: float
        The maximum value of the number.
    min_value: float
        The minimum value of the number.
    choices: List[Choice]
        The choices for the number.
    autocomplete: bool
        Whether the number should be auto completed or not.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        max_value: Optional[float] = None,
        min_value: Optional[float] = None,
        choices: Optional[List[Choice]] = None,
        autocomplete: Optional[bool] = False,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.number)
        self.choices = choices
        self.max_value = max_value
        self.min_value = min_value
        self.autocomplete = autocomplete

    def to_dict(self) -> Dict[str, Any]:
        if self.choices:
            self.data["choices"] = [choice.to_dict() for choice in self.choices]
        if self.autocomplete:
            self.data["autocomplete"] = self.autocomplete
        if self.max_value is not None:
            self.data["max_value"] = self.max_value
        if self.min_value is not None:
            self.data["min_value"] = self.min_value
        return self.data


class BooleanOption(Option):
    """
    Represents a boolean type option for an application command, subclassed from `Option`
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        """
        Parameters
        ----------
        name: str
            The name of the option.
        description: str
            The description of the option.
        required: bool
            Whether the option is required or not.
        """
        super().__init__(name, description, required, type=ApplicationCommandOptionType.boolean)

    def to_dict(self) -> Dict[str, Any]:
        return self.data


class UserOption(Option):
    """
    Represents a user type option for an application command, subclassed from `Option`
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        """
        Parameters
        ----------
        name: str
            The name of the option.
        description: str
            The description of the option.
        required: bool
            Whether the option is required or not.
        """
        super().__init__(name, description, required, type=ApplicationCommandOptionType.user)

    def to_dict(self) -> Dict[str, Any]:
        return self.data


class ChannelOption(Option):
    """
    Represents a channel type option for an application command, subclassed from `Option`

    Parameters
    ----------
    name: str
        The name of the option.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    channel_types: List[ChannelType]
        The channel types that are allowed for this option.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        channel_types: Optional[List[ChannelType]] = None,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.channel)
        self.channel_types = channel_types

    def to_dict(self) -> Dict[str, Any]:
        if self.channel_types:
            self.data["channel_types"] = [ct.value for ct in self.channel_types]
        return self.data


class RoleOption(Option):
    """
    Represents a role type option for an application command, subclassed from `Option`
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.role)

    def to_dict(self) -> Dict[str, Any]:
        return self.data


class MentionableOption(Option):
    """
    Represents a mentionable type option for an application command, subclassed from `Option`

    Parameters
    ----------
    name: str
        The name of the option.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.mentionable)

    def to_dict(self) -> Dict[str, Any]:
        return self.data


class AttachmentOption(Option):
    """
    Represents an attachment type option for an application command, subclassed from `Option`

    Parameters
    ----------
    name: str
        The name of the option.
    description: str
        The description of the option.
    required: bool
        Whether the option is required or not.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        super().__init__(name, description, required, type=ApplicationCommandOptionType.attachment)

    def to_dict(self) -> Dict[str, Any]:
        return self.data

from typing import Any, Dict, List, Optional, Union
from .enums import ApplicationCommandOptionType, ChannelType


class Choice:
    def __init__(self, name: str, value: Union[str, int, float]):
        self.name = name
        self.value = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value
        }


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
    kind: AppCmdOptionType
        The type of the option.
    """

    def __init__(
        self,
        name: str,
        description: str,
        *,
        required: bool = False,
        kind: ApplicationCommandOptionType,
    ):
        self.name = name
        assert self.name.isidentifier(), "name must be a valid python identifier"
        self.description = description
        self.required = required
        self.kind = kind
        self.data: Dict[str, Any] = {
            "name": self.name,
            "description": self.description,
            "required": self.required,
            "type": self.kind,
        }
        self.max_length: Optional[int] = None
        self.min_length: Optional[int] = None
        self.max_value: Optional[Union[int, float]] = None
        self.min_value: Optional[Union[int, float]] = None
        self.choices: Optional[List[Choice]] = None
        self.autocomplete: Optional[bool] = None
        self.channel_types: Optional[List[ChannelType]] = None

    @classmethod
    def string(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        max_length: Optional[int] = None,
        min_length: Optional[int] = None,
        choices: Optional[List[Choice]] = None,
        autocomplete: Optional[bool] = False,
    ):
        self = cls(name, description, required=required, kind=ApplicationCommandOptionType.string)
        self.max_length = max_length
        self.min_length = min_length
        self.choices = choices
        self.autocomplete = autocomplete
        return self

    @classmethod
    def integer(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        max_value: Optional[int] = None,
        min_value: Optional[int] = None,
        choices: Optional[List[Choice]] = None,
        autocomplete: Optional[bool] = False,
    ):
        self = cls(name, description, required=required, kind=ApplicationCommandOptionType.integer)
        self.max_value = max_value
        self.min_value = min_value
        self.choices = choices
        self.autocomplete = autocomplete
        return self

    @classmethod
    def number(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        max_value: Optional[float] = None,
        min_value: Optional[float] = None,
        choices: Optional[List[Choice]] = None,
        autocomplete: Optional[bool] = False,
    ):
        self = cls(name, description, required=required, kind=ApplicationCommandOptionType.number)
        self.max_value = max_value
        self.min_value = min_value
        self.choices = choices
        self.autocomplete = autocomplete
        return self

    @classmethod
    def boolean(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        return cls(name, description, required=required, kind=ApplicationCommandOptionType.boolean)

    @classmethod
    def user(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        return cls(name, description, required=required, kind=ApplicationCommandOptionType.user)

    @classmethod
    def channel(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
        types: Optional[List[ChannelType]] = None,
    ):
        self = cls(name, description, required=required, kind=ApplicationCommandOptionType.channel)
        self.channel_types = types
        return self

    @classmethod
    def role(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        return cls(name, description, required=required, kind=ApplicationCommandOptionType.role)

    @classmethod
    def mentionable(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        return cls(name, description, required=required, kind=ApplicationCommandOptionType.mentionable)

    @classmethod
    def attachment(
        cls,
        name: str,
        description: str,
        *,
        required: Optional[bool] = False,
    ):
        return cls(name, description, required=required, kind=ApplicationCommandOptionType.attachment)

    def to_dict(self) -> Dict[str, Any]:
        if self.choices:
            self.data["choices"] = [choice.to_dict() for choice in self.choices]
        if (
                self.kind in
                (
                    ApplicationCommandOptionType.integer,
                    ApplicationCommandOptionType.number,
                    ApplicationCommandOptionType.string
                )
        ):
            if self.autocomplete is not None:
                self.data["autocomplete"] = self.autocomplete
            if self.max_value is not None:
                self.data["max_value"] = self.max_value
            if self.min_value is not None:
                self.data["min_value"] = self.min_value
        if self.kind == ApplicationCommandOptionType.string:
            if self.max_length:
                self.data["max_length"] = self.max_length
            if self.min_length:
                self.data["min_length"] = self.min_length
        if self.channel_types and self.kind == ApplicationCommandOptionType.channel:
            self.data["channel_types"] = self.channel_types
        return self.data

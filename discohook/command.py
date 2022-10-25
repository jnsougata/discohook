from typing import Callable, Dict, List, Optional, Union, Any
from .option import Option
from .enums import command_types, option_types
from functools import wraps
import asyncio


class SubCommand:
    def __init__(
            self,
            name: str,
            description: str,
            options: List[Option] = None,
            *,
            callback: Callable = None
    ):
        self.name = name
        self.options = options
        self.callback = callback
        self.description = description
        self._component_callback: Optional[Callable] = None

    def to_json(self) -> Dict[str, Any]:
        payload = {
            "type": option_types.subcommand.value,
            "name": self.name,
            "description": self.description,
        }
        if self.options:
            payload["options"] = [option.to_json() for option in self.options]
        return payload


class SubCommandGroup:
    pass


class ApplicationCommand:

    def __init__(
            self,
            name: str,
            description: str = None,
            options: List[Option] = None,
            dm_access: bool = True,
            permissions: str = None,
            category: command_types = command_types.slash,
            *,
            guild_id: int = None,
            callback: Callable = None,
            **kwargs
    ):
        self.id = None
        self.name = name
        self.description = description
        self.options: List[Option] = options
        self.dm_access = dm_access
        self.guild_id = guild_id
        self.application_id = None
        self.category = category
        self.permissions = permissions
        self._callback = callback
        self.__payload: Dict[str, Any] = {}
        self._subcommand_callbacks: Dict[str, Callable] = {}

    def callback(self, coro: Callable):
        self._callback = coro

    def subcommand(
            self,
            name: str,
            description: str,
            *,
            options: List[Option] = None,
    ) -> None:
        subcommand = SubCommand(name, description, options)
        if self.options:
            self.options.append(subcommand)
        else:
            self.options = [subcommand]

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*args, **kwargs):
                if asyncio.iscoroutinefunction(coro):
                    self._subcommand_callbacks[name] = coro
                    return coro
            return wrapper()
        return decorator  # type: ignore

    def to_json(self) -> Dict[str, Any]:
        if self.category is command_types.slash:
            self.__payload["type"] = self.category.value
            if self.description:
                self.__payload["description"] = self.description
            if self.options:
                self.__payload["options"] = [option.to_json() for option in self.options]
        self.__payload["name"] = self.name
        if not self.dm_access:
            self.__payload["dm_permission"] = self.dm_access
        if self.permissions:
            self.__payload["default_member_permissions"] = self.permissions
        return self.__payload

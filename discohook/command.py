from typing import Callable, Dict, List, Optional, Union, Any
from .option import Option
from .enums import AppCmdType, AppCmdOptionType
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

    def json(self) -> Dict[str, Any]:
        payload = {
            "type": AppCmdOptionType.subcommand.value,
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
            category: AppCmdType = AppCmdType.slash,
            *,
            guild_id: int = None,
    ):
        self.id = None
        self.cog = None
        self.name = name
        self.description = description
        self.options: List[Option] = options
        self.dm_access = dm_access
        self.guild_id = guild_id
        self.application_id = None
        self.category = category
        self.permissions = permissions
        self._callback = None
        self._payload: Dict[str, Any] = {}
        self._subcommand_callbacks: Dict[str, Callable] = {}

    def callback(self, coro: Callable):
        self._callback = coro

    def subcommand(
            self,
            name: str,
            description: str,
            *,
            options: List[Option] = None,
    ):
        subcommand = SubCommand(name, description, options)
        if self.options:
            self.options.append(subcommand)
        else:
            self.options = [subcommand]

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*_, **__):
                if asyncio.iscoroutinefunction(coro):
                    self._subcommand_callbacks[name] = coro
                    return coro
            return wrapper()
        return decorator  # type: ignore

    def json(self) -> Dict[str, Any]:
        self._payload["type"] = self.category.value
        if self.category is AppCmdType.slash:
            if self.description:
                self._payload["description"] = self.description
            if self.options:
                self._payload["options"] = [option.json() for option in self.options]
        self._payload["name"] = self.name
        if not self.dm_access:
            self._payload["dm_permission"] = self.dm_access
        if self.permissions:
            self._payload["default_member_permissions"] = self.permissions
        return self._payload

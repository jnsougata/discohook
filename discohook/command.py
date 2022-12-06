import asyncio
from functools import wraps
from .option import Option
from .permissions import Permissions
from .enums import AppCmdType, AppCmdOptionType
from typing import Callable, Dict, List, Optional, Any


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
            payload["options"] = [option.json() for option in self.options]
        return payload


class SubCommandGroup:
    pass


# noinspection PyShadowingBuiltins
class ApplicationCommand:

    def __init__(
        self,
        name: str,
        id: str = None,
        description: str = None,
        options: List[Option] = None,
        dm_access: bool = True,
        permissions: List[Permissions] = None,
        category: AppCmdType = AppCmdType.slash,
    ):
        self.id = id
        self.cog = None
        self.name = name
        self.description = description
        self.options: List[Option] = options
        self.dm_access = dm_access
        self.application_id = None
        self.category = category
        self.permissions = permissions
        self._callback = None
        self._payload: Dict[str, Any] = {}
        self._autocomplete_callback = None
        self._subcommand_callbacks: Dict[str, Callable] = {}

    def callback(self, coro: Callable):
        self._callback = coro
    
    def autocomplete(self, coro: Callable):
        self._autocomplete_callback = coro

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
            base = 0
            for permission in self.permissions:
                base |= permission.value
            self._payload["default_member_permissions"] = str(base)
        return self._payload

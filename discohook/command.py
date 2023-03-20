import asyncio
from functools import wraps
from .option import Option
from .permissions import Permissions
from .enums import ApplicationCommandType, ApplicationCommandOptionType
from typing import Callable, Dict, List, Optional, Any


class SubCommand:
    """
    A class representing a discord application command subcommand.

    Parameters
    ----------
    name: str
        The name of the subcommand.
    description: str
        The description of the subcommand.
    options: Optional[List[Option]]
        The options of the subcommand.
    callback: Optional[Callable]
        The callback of the subcommand.
    """
    def __init__(
        self,
        name: str,
        description: str,
        options: List[Option] = None,
        *,
        callback: Callable = None,
    ):
        self.name = name
        self.options = options
        self.callback = callback
        self.description = description
        self._component_callback: Optional[Callable] = None

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "type": ApplicationCommandOptionType.subcommand.value,
            "name": self.name,
            "description": self.description,
        }
        if self.options:
            payload["options"] = [option.to_dict() for option in self.options]
        return payload


class SubCommandGroup:
    pass


# noinspection PyShadowingBuiltins
class ApplicationCommand:
    """
    A class representing a discord application command.
        
    Parameters
    ----------
    name: str
        The name of the command.
    id: Optional[str]
        The ID of the command. If not provided, the command will not be synced.
    description: Optional[str]
        The description of the command. Does not apply to user & message commands.
    options: Optional[List[Option]]
        The options of the command. Does not apply to user & message commands.
    dm_access: bool
        Whether the command can be used in DMs. Defaults to True.
    permissions: Optional[List[Permissions]]
        The default permissions of the command.
    category: AppCmdType
        The category of the command. Defaults to slash commands.
    """
    def __init__(
        self,
        name: str,
        id: str = None,
        description: str = None,
        options: List[Option] = None,
        dm_access: bool = True,
        permissions: List[Permissions] = None,
        category: ApplicationCommandType = ApplicationCommandType.slash,
    ):
        self.id = id
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
        """
        A decorator to register a callback for the command.

        Parameters
        ----------
        coro: Callable
            The callback to register.
        """
        self._callback = coro

    def autocomplete(self, coro: Callable):
        """
        A decorator to register a callback for the command's autocomplete.

        Parameters
        ----------
        coro: Callable
            The callback to register.
        """
        self._autocomplete_callback = coro

    def subcommand(
        self,
        name: str,
        description: str,
        *,
        options: List[Option] = None,
    ):
        """
        A decorator to register a subcommand for the command.

        Parameters
        ----------
        name: str
            The name of the subcommand.
        description: str
            The description of the subcommand.
        options: Optional[List[Option]]
            The options of the subcommand.
        """
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

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the command to a dictionary.

        This is used to send the command to the Discord API. Not intended for use by end-users.

        Returns
        -------
        Dict[str, Any]
        """
        self._payload["type"] = self.category.value
        if self.category is ApplicationCommandType.slash:
            if self.description:
                self._payload["description"] = self.description
            if self.options:
                self._payload["options"] = [option.to_dict() for option in self.options]
        self._payload["name"] = self.name
        if not self.dm_access:
            self._payload["dm_permission"] = self.dm_access
        if self.permissions:
            base = 0
            for permission in self.permissions:
                base |= permission.value
            self._payload["default_member_permissions"] = str(base)
        return self._payload

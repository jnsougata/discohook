import asyncio
from functools import wraps
from .option import Option
from .permissions import Permissions
from typing import Callable, Dict, List, Optional, Any
from .enums import ApplicationCommandType, ApplicationCommandOptionType


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
        options: Optional[List[Option]] = None,
        *,
        callback: Optional[Callable] = None,
    ):
        self.name = name
        self.options = options  # type: ignore
        self.callback: Optional[Callable] = callback  # type: ignore
        self.description = description

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning(
                f"subcommand `{self.name}` of command "
                f"`{args[0].data['name']}` (id: {args[0].data['id']}) has no callback")
        return self.callback(*args, **kwargs)

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "type": ApplicationCommandOptionType.subcommand.value,
            "name": self.name,
            "description": self.description,
        }
        if self.options:
            payload["options"] = [option.to_dict() for option in self.options]  # type: ignore
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
        description: Optional[str] = None,
        options: List[Option] = None,
        dm_access: bool = True,
        permissions: Optional[List[Permissions]] = None,
        category: ApplicationCommandType = ApplicationCommandType.slash,
    ):
        self._id = f"{name}:{category.value}"
        self.name = name
        self.description = description  # type: ignore
        self.options: List[Option] = options
        self.dm_access = dm_access
        self.application_id = None
        self.category = category
        self.permissions = permissions  # type: ignore
        self.callback: Optional[Callable] = None
        self.data: Dict[str, Any] = {}
        self.subcommands: Dict[str, SubCommand] = {}
        self.autocomplete_callback: Optional[Callable] = None

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning(f"command `{self._id}` has no callback")
        return self.callback(*args, **kwargs)

    def on_interaction(self, coro: Callable):
        """
        A decorator to register a callback for the command.

        Parameters
        ----------
        coro: Callable
            The callback to register.
        """
        self.callback = coro

    def autocomplete(self, coro: Callable):
        """
        A decorator to register a callback for the command's autocomplete choices.

        Parameters
        ----------
        coro: Callable
            The callback to register.
        """
        self.autocomplete_callback = coro

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
            self.options = [subcommand]  # type: ignore

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*_, **__):
                if asyncio.iscoroutinefunction(coro):
                    self.subcommands[name] = subcommand
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
        self.data["type"] = self.category.value
        if self.category is ApplicationCommandType.slash:
            if self.description:
                self.data["description"] = self.description
            if self.options:
                self.data["options"] = [option.to_dict() for option in self.options]
        self.data["name"] = self.name
        if not self.dm_access:
            self.data["dm_permission"] = self.dm_access
        if self.permissions:
            base = 0
            for permission in self.permissions:
                base |= permission.value
            self.data["default_member_permissions"] = str(base)
        return self.data


def command(
    name: str,
    description: Optional[str] = None,
    *,
    options: Optional[List[Option]] = None,
    permissions: Optional[List[Permissions]] = None,
    dm_access: bool = True,
    category: ApplicationCommandType = ApplicationCommandType.slash,
) -> ApplicationCommand:
    """
    A decorator to register a command.

    Parameters
    ----------
    name: str
        The name of the command.
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
    def decorator(coro: Callable):
        @wraps(coro)
        def wrapper(*_, **__):
            cmd = ApplicationCommand(
                name,
                description,
                options,
                dm_access,
                permissions,
                category,
            )
            cmd.callback = coro
            return cmd
        return wrapper()

    return decorator  # type: ignore

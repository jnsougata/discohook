import asyncio
from typing import Any, Dict, List, Optional, Union

from .enums import ApplicationCommandOptionType, ApplicationCommandType
from .option import Option
from .permissions import Permissions
from .utils import AsyncFunc


class SubCommand:
    """
    A class representing a discord application command subcommand.

    Parameters
    ----------
    name: str
        The name of the subcommand.
    description: str
        The description of the subcommand.
    options: List[Option] | None
        The options of the subcommand.
    callback: `AsyncCallable` | None
        The callback of the subcommand.
    """

    def __init__(
        self,
        name: str,
        description: str,
        options: Optional[List[Option]] = None,
        *,
        callback: Optional[AsyncFunc] = None,
    ):
        self.name = name
        self.options = options
        self.callback = callback
        self.description = description
        self.autocompletes: Dict[str, AsyncFunc] = {}

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning(
                f"subcommand `{self.name}` of command "
                f"`{args[0].data['name']}` (id: {args[0].data['id']}) has no callback"
            )
        return self.callback(*args, **kwargs)

    def autocomplete(self, name: str):
        """
        A decorator to register a callback for the subcommand's autocomplete options.

        Parameters
        ----------
        name: str
            The name of the option to register the autocomplete for.
        """

        def decorator(coro: AsyncFunc):
            self.autocompletes[name] = coro

        return decorator

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
    description: str | None
        The description of the command. Does not apply to user & message commands.
    options: List[Option] | None
        The options of the command. Does not apply to user & message commands.
    dm_access: bool
        Whether the command can be used in DMs. Defaults to True.
    nsfw: bool
        Whether the command is age restricted. Defaults to False.
    permissions: List[Permissions] | None
        The default permissions of the command.
    category: ApplicationCommandType
        The category of the command. Defaults to slash commands.
    """

    def __init__(
        self,
        name: str,
        *,
        description: Optional[str] = None,
        options: Optional[List[Option]] = None,
        dm_access: bool = True,
        nsfw: bool = False,
        permissions: Optional[List[Permissions]] = None,
        category: ApplicationCommandType = ApplicationCommandType.slash,
    ):
        self.key = f"{name}:{category.value}"
        self.name = name
        self.description = description
        self.options: List[Union[Option, SubCommand]] = options
        self.dm_access = dm_access
        self.nsfw = nsfw
        self.application_id = None
        self.category = category
        self.permissions = permissions
        self.callback: Optional[AsyncFunc] = None
        self.data: Dict[str, Any] = {}
        self.subcommands: Dict[str, SubCommand] = {}
        self.autocompletes: Dict[str, AsyncFunc] = {}
        self.checks: List[AsyncFunc] = []

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning(f"command `{self.key}` has no callback")
        return self.callback(*args, **kwargs)

    def on_interaction(self, coro: AsyncFunc):
        """
        A decorator to register a callback for the command.

        Parameters
        ----------
        coro: AsyncCallable
            The callback to register.
        """
        self.callback = coro

    def autocomplete(self, name: str):
        """
        A decorator to register a callback for the command's autocomplete options.

        Parameters
        ----------
        name: str
            The name of the option to register the autocomplete for.
        """

        def decorator(coro: AsyncFunc):
            self.autocompletes[name] = coro

        return decorator

    def subcommand(
        self,
        name: str,
        description: str,
        *,
        options: Optional[List[Option]] = None,
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

        Returns
        -------
        SubCommand
            The subcommand object.

        Raises
        ------
        TypeError
            If the callback is not a coroutine.
        """

        def decorator(coro: AsyncFunc):
            subcommand = SubCommand(name, description, options, callback=coro)
            if self.options:
                self.options.append(subcommand)
            else:
                self.options = [subcommand]
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("subcommand callback must be a coroutine")
            self.subcommands[name] = subcommand
            return subcommand

        return decorator

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
        if self.nsfw:
            self.data["nsfw"] = self.nsfw
        return self.data


def command(
    name: Optional[str] = None,
    description: Optional[str] = None,
    *,
    options: Optional[List[Option]] = None,
    permissions: Optional[List[Permissions]] = None,
    dm_access: bool = True,
    nsfw: bool = False,
    category: ApplicationCommandType = ApplicationCommandType.slash,
):
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
    nsfw: bool
        Whether the command is age-restricted. Defaults to False.
    permissions: Optional[List[Permissions]]
        The default permissions of the command.
    category: AppCmdType
        The category of the command. Defaults to slash commands.
    """

    def decorator(callback: AsyncFunc):
        if not asyncio.iscoroutinefunction(callback):
            raise TypeError("callback must be a coroutine")
        cmd = ApplicationCommand(
            name or callback.__name__,
            description=description or callback.__doc__,
            options=options,
            dm_access=dm_access,
            permissions=permissions,
            category=category,
            nsfw=nsfw
        )
        cmd.callback = callback
        if cmd.category == ApplicationCommandType.slash and not cmd.description:
            raise ValueError(f"command `{cmd.name}` has no description")
        return cmd

    return decorator


def command_checker(*checks: AsyncFunc):
    """
    Decorator for adding a checks to a command.

    Parameters
    ----------
    *checks: AsyncCallable
        The checks to add to the command.

    Returns
    -------
    ApplicationCommand
        The command with the checks added.

    Raises
    ------
    TypeError
        If the any of the checks is not a coroutine.
    """

    def decorator(cmd: ApplicationCommand):
        for check in checks:
            if not asyncio.iscoroutinefunction(check):
                raise TypeError(f"check `{check.__name__}` must be coroutines")
        cmd.checks.extend(checks)
        return cmd

    return decorator

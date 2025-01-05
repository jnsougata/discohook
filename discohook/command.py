import asyncio
from typing import Any, Dict, List, Optional, Union

from .component import Interactable
from .enums import (
    ApplicationCommandOptionType,
    ApplicationCommandType,
    ApplicationIntegrationType,
    InteractionContextType,
)
from .option import Option
from .permission import Permission
from .utils import Handler, find_description


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
        callback: Optional[Handler] = None,
    ):
        self.name = name
        self.options = options
        self.callback = callback
        self.description = description
        self.autocompletion_handler: Optional[Handler] = None

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning(
                f"subcommand `{self.name}` of command "
                f"`{args[0].data['name']}` (id: {args[0].data['id']}) has no callback"
            )
        return self.callback(*args, **kwargs)

    def on_autocomplete(self, coro: Handler):
        """
        A decorator to register a callback for the subcommand's autocomplete options.
        """
        self.autocompletion_handler = coro
        return coro

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "type": ApplicationCommandOptionType.subcommand,
            "name": self.name,
            "description": self.description,
        }
        if self.options:
            payload["options"] = [option.to_dict() for option in self.options]
        return payload


class SubCommandGroup:
    pass


# noinspection PyShadowingBuiltins
class ApplicationCommand(Interactable):
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
    nsfw: bool
        Whether the command is age restricted. Defaults to False.
    permissions: List[Permission] | None
        The default permissions of the command.
    type: ApplicationCommandType
        The category of the command. Defaults to slash commands.
    integration_types: List[ApplicationIntegrationType] | None
         Installation context(s) where the command is available. only for globally-scoped commands.
    contexts: List[InteractionContextType] | None
         Interaction context(s) where the command can be used, only for globally-scoped commands.
    """

    def __init__(
        self,
        name: str,
        *,
        description: Optional[str] = None,
        options: Optional[List[Option]] = None,
        nsfw: bool = False,
        integration_types: Optional[List[ApplicationIntegrationType]] = None,
        contexts: Optional[List[InteractionContextType]] = None,
        permissions: Optional[List[Permission]] = None,
        type: ApplicationCommandType = ApplicationCommandType.slash,
        guild_id: Optional[str] = None,
        callback: Handler,
    ):
        super().__init__()
        self.name = name
        if not guild_id:
            self.key = f"{name}:{type.value}"
        else:
            self.key = f"{name}:{guild_id}:{type.value}"
        self.description = description
        self.options: List[Union[Option, SubCommand]] = options
        self.nsfw = nsfw
        self.application_id = None
        self.type = type
        self.contexts = [InteractionContextType.guild] if contexts is None else contexts
        self.integration_types = (
            [ApplicationIntegrationType.guild]
            if integration_types is None
            else integration_types
        )
        self.permissions = permissions
        self.guild_id = guild_id
        self.callback: Handler = callback
        self.data: Dict[str, Any] = {}
        self.subcommands: Dict[str, SubCommand] = {}
        self.autocompletion_handler: Optional[Handler] = None

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning(f"command `{self.key}` has no callback")
        return self.callback(*args, **kwargs)

    def on_autocomplete(self, coro: Handler):
        """
        A decorator to register a callback for the command's autocomplete options.
        """
        self.autocompletion_handler = coro
        return coro

    def subcommand(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
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

        def decorator(coro: Handler):
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
        self.data["name"] = self.name
        self.data["type"] = self.type
        if self.description:
            self.data["description"] = self.description
        if self.type == ApplicationCommandType.slash:
            if self.options:
                self.data["options"] = [option.to_dict() for option in self.options]
        if self.permissions:
            base = 0
            for permission in self.permissions:
                base |= permission.value
            self.data["default_member_permissions"] = str(base)
        if self.nsfw:
            self.data["nsfw"] = self.nsfw
        self.data["integration_types"] = self.integration_types
        self.data["contexts"] = self.contexts
        return self.data


def slash(
    name: Optional[str] = None,
    *,
    description: Optional[str] = None,
    options: Optional[List[Option]] = None,
    nsfw: bool = False,
    permissions: Optional[List[Permission]] = None,
    guild_id: Optional[str] = None,
    integration_types: Optional[List[ApplicationIntegrationType]] = None,
    contexts: Optional[List[InteractionContextType]] = None,
):
    """
    A decorator to register a slash command with its callback.
    """

    def decorator(coro: Handler):
        return ApplicationCommand(
            name or coro.__name__,
            description=find_description(name, description, coro),
            options=options,
            nsfw=nsfw,
            permissions=permissions,
            guild_id=guild_id,
            integration_types=integration_types,
            contexts=contexts,
            callback=coro,
        )

    return decorator


def user(
    name: Optional[str] = None,
    *,
    nsfw: bool = False,
    permissions: Optional[List[Permission]] = None,
    guild_id: Optional[str] = None,
    integration_types: Optional[List[ApplicationIntegrationType]] = None,
    contexts: Optional[List[InteractionContextType]] = None,
):
    """
    A decorator to register a user command with its callback.
    """

    def decorator(coro: Handler):
        return ApplicationCommand(
            name or coro.__name__,
            nsfw=nsfw,
            permissions=permissions,
            guild_id=guild_id,
            type=ApplicationCommandType.user,
            integration_types=integration_types,
            contexts=contexts,
            callback=coro,
        )

    return decorator


def message(
    name: Optional[str] = None,
    *,
    nsfw: bool = False,
    permissions: Optional[List[Permission]] = None,
    guild_id: Optional[str] = None,
    integration_types: Optional[List[ApplicationIntegrationType]] = None,
    contexts: Optional[List[InteractionContextType]] = None,
):
    """
    A decorator to register a message command with its callback.
    """

    def decorator(coro: Handler):
        return ApplicationCommand(
            name or coro.__name__,
            nsfw=nsfw,
            permissions=permissions,
            guild_id=guild_id,
            type=ApplicationCommandType.message,
            integration_types=integration_types,
            contexts=contexts,
            callback=coro,
        )

    return decorator

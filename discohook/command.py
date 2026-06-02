import inspect
from typing import (TYPE_CHECKING, Any, Callable, Coroutine, Dict, List,
                    Optional, Union)

from .enums import (ApplicationCommandOptionType, ApplicationCommandType,
                    ApplicationIntegrationType, InteractionContextType)
from .handler import Handler
from .option import Option
from .permission import Permission
from .utils import resolve_description

if TYPE_CHECKING:
    from .interaction import Interaction


class SubCommand:
    """
    Discord application command subcommand class.

    Args:
        name (str): Name of the subcommand.
        description (str): Description of the subcommand.
        options (List[Option] | None): Options of the subcommand.
        handler (Handler): Handler for the subcommand.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str,
        options: Optional[List[Option]] = None,
        handler: Handler,
    ):
        self.name = name
        self.options = options
        self.handler = handler
        self.description = description
        self.autocompletion_handler: Optional[Handler] = None

    def __call__(self, *args, **kwargs):
        if not self.handler:
            raise RuntimeWarning(
                f"subcommand `{self.name}` of command "
                f"`{args[0].data['name']}` (id: {args[0].data['id']}) has no callback"
            )
        return self.handler(*args, **kwargs)

    def on_error(self):
        """
        Decorator that adds an error handler to a specific command or component.
        """

        def decorator(coro: Callable[["Interaction"], None]):
            if not inspect.iscoroutinefunction(coro):
                raise TypeError("error handler must be a coroutine")
            self.handler._error_handler = coro

        return decorator

    def check(self):
        """
        Decorator that adds a check to the command.
        """

        def decorator(coro: Callable[["Interaction"], bool]):
            if not inspect.iscoroutinefunction(coro):
                raise TypeError("check must be a coroutine")
            self.handler.checks.append(coro)  # noqa
            return self

        return decorator

    def on_autocomplete(
        self, coro: Callable[["Interaction", Any], Coroutine[Any, Any, Any]]
    ):
        """
        Decorator to register a callback for a subcommand's autocomplete options.
        """
        self.autocompletion_handler = Handler(self.name, coro)
        return coro

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "type": ApplicationCommandOptionType.subcommand,
            "name": self.name,
            "description": self.description,
        }
        if self.options:
            payload["options"] = [option.to_dict() for option in self.options]  # type: ignore
        return payload


class SubCommandGroup:
    """
    Barely need it.
    """
    pass


# noinspection PyShadowingBuiltins
class ApplicationCommand:
    """
    Discord application command class.

    Args:
        name (str): Name of the command.
        description (str | None): Description of the command. Does not apply to user and message commands.
        options (List[Option] | None): Options of the command. Does not apply to user & message commands.
        nsfw (bool): Whether the command is nsfw. Defaults to False.
        permissions (List[Permission] | None): Permissions of the command. Defaults to None.
        type (ApplicationCommandType): Type of the command. Defaults to slash commands.
        integration_types (List[ApplicationIntegrationType] | None): Integrations of the command. Defaults to None.
        contexts (List[InteractionContextType] | None): Contexts of the command. Defaults to None.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        *,
        description: Optional[str] = None,
        options: Optional[List[Union[Option, SubCommand]]] = None,
        nsfw: bool = False,
        integration_types: Optional[List[ApplicationIntegrationType]] = None,
        contexts: Optional[List[InteractionContextType]] = None,
        permissions: Optional[List[Permission]] = None,
        type: ApplicationCommandType = ApplicationCommandType.slash,
        guild_id: Optional[str] = None,
        handler_func: Callable[["Interaction", Any], Any],
    ):
        self.name = name if name else handler_func.__name__
        handler_id = f"{self.name}:{type.value}"
        if guild_id:
            handler_id += f":{guild_id}"
        self.handler = Handler(handler_id, handler_func)
        if type == ApplicationCommandType.slash:
            self.description = resolve_description(self.name, description, handler_func)
        else:
            self.description = None
        self.options: List[Union[Option, SubCommand]] = options if options else []
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
        self.data: Dict[str, Any] = {}
        self.subcommands: Dict[str, SubCommand] = {}
        self.autocompletion_handler: Optional[Handler] = None

    def check(self):
        """
        Decorator that adds a check to the command.
        """

        def decorator(coro: Callable[["Interaction"], bool]):
            if not inspect.iscoroutinefunction(coro):
                raise TypeError("check must be a coroutine")
            self.handler.checks.append(coro)  # noqa
            return self

        return decorator

    def on_error(self):
        """
        Decorator that adds an error handler to a specific command or component.
        """

        def decorator(coro: Callable[["Interaction"], None]):
            if not inspect.iscoroutinefunction(coro):
                raise TypeError("error handler must be a coroutine")
            self.handler._error_handler = coro

        return decorator

    def on_autocomplete(
        self, coro: Callable[["Interaction", Any], Coroutine[Any, Any, Any]]
    ):
        """
        Decorator to register a callback for the command's autocomplete options.
        """
        self.autocompletion_handler = Handler(self.name, coro)
        return coro

    def subcommand(
        self,
        name: Optional[str] = None,
        *,
        description: Optional[str] = None,
        options: Optional[List[Option]] = None,
    ):
        """
        Decorator to register a subcommand for the command.

        Args:
            name (str): Name of the subcommand.
            description (str): Description of the subcommand.
                If not provided, it will be resolved from the callback's name.
            options (List[Option] | None): Options of the subcommand.

        Raises:
            TypeError: If the callback is not a coroutine.
        """

        def decorator(coro: Callable[["Interaction", Any], Coroutine[Any, Any, Any]]):
            resolved_name = name if name else coro.__name__
            resolved_description = resolve_description(resolved_name, description, coro)
            subcommand = SubCommand(
                name=resolved_name,
                description=resolved_description,
                options=options,
                handler=Handler(self.name, coro),
            )
            self.options.append(subcommand)
            if not inspect.iscoroutinefunction(coro):
                raise TypeError("subcommand callback must be a coroutine")
            self.subcommands[resolved_name] = subcommand
            return subcommand

        return decorator

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the command to a dictionary. Not intended for use by end-users.

        Returns:
            Dictionary of the command object.
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
    Decorator to create a slash command with its callback.
    """

    def decorator(coro: Callable[["Interaction", Any], Coroutine[Any, Any, Any]]):
        return ApplicationCommand(
            name=name,
            description=description,
            options=options,
            nsfw=nsfw,
            permissions=permissions,
            guild_id=guild_id,
            integration_types=integration_types,
            contexts=contexts,
            handler_func=coro,
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
    Decorator to create a user command with its callback.
    """

    def decorator(coro: Callable[["Interaction", Any], Coroutine[Any, Any, Any]]):
        return ApplicationCommand(
            name=name,
            nsfw=nsfw,
            permissions=permissions,
            guild_id=guild_id,
            type=ApplicationCommandType.user,
            integration_types=integration_types,
            contexts=contexts,
            handler_func=coro,
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
    Decorator to create a message command with its callback.
    """

    def decorator(coro: Callable[["Interaction", Any], Coroutine[Any, Any, Any]]):
        return ApplicationCommand(
            name=name,
            nsfw=nsfw,
            permissions=permissions,
            guild_id=guild_id,
            type=ApplicationCommandType.message,
            integration_types=integration_types,
            contexts=contexts,
            handler_func=coro,
        )

    return decorator

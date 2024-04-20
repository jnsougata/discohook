from .command import ApplicationCommand, Option, find_description
from .base import Component
from .enums import ApplicationCommandType, InteractionContextType, ApplicationIntegrationType
from .permission import Permission
from .utils import Handler

from typing import List, Optional


class CommandTree:

    def __init__(self):
        self.commands = []
        self.components = []
        self.active_components = {}

    def preload(self, custom_id: str):
        def decorator(component: Component):
            if not custom_id or not isinstance(custom_id, str):
                raise ValueError("Invalid custom id provided.")
            component.custom_id = custom_id
            self.active_components[custom_id] = component
            return component

        return decorator

    def slash(
        self,
        name: Optional[str] = None,
        *,
        description: Optional[str] = None,
        options: Optional[List[Option]] = None,
        nsfw: bool = False,
        permissions: Optional[List[Permission]] = None,
        guild_id: Optional[str] = None,
        integration_types: Optional[List[ApplicationIntegrationType]] = None,
        contexts: Optional[List[InteractionContextType]] = None
    ):
        """
        A decorator to register a slash command with its callback.
        """

        def decorator(coro: Handler):
            cmd = ApplicationCommand(
                name or coro.__name__,
                description=find_description(name, description, coro),
                options=options,
                nsfw=nsfw,
                permissions=permissions,
                guild_id=guild_id,
                integration_types=integration_types,
                contexts=contexts,
                callback=coro
            )
            self.commands.append(cmd)
            return cmd

        return decorator

    def user(
        self,
        name: Optional[str] = None,
        *,
        nsfw: bool = False,
        permissions: Optional[List[Permission]] = None,
        guild_id: Optional[str] = None,
        integration_types: Optional[List[ApplicationIntegrationType]] = None,
        contexts: Optional[List[InteractionContextType]] = None
    ):
        """
        A decorator to register a user command with its callback.
        """

        def decorator(coro: Handler):
            cmd = ApplicationCommand(
                name or coro.__name__,
                nsfw=nsfw,
                permissions=permissions,
                guild_id=guild_id,
                integration_types=integration_types,
                contexts=contexts,
                type=ApplicationCommandType.user,
                callback=coro
            )
            self.commands.append(cmd)
            return cmd

        return decorator

    def message(
        self,
        name: Optional[str] = None,
        *,
        nsfw: bool = False,
        permissions: Optional[List[Permission]] = None,
        guild_id: Optional[str] = None,
        integration_types: Optional[List[ApplicationIntegrationType]] = None,
        contexts: Optional[List[InteractionContextType]] = None
    ):
        """
        A decorator to register a message command with its callback.
        """

        def decorator(coro: Handler):
            cmd = ApplicationCommand(
                name or coro.__name__,
                nsfw=nsfw,
                permissions=permissions,
                guild_id=guild_id,
                integration_types=integration_types,
                contexts=contexts,
                type=ApplicationCommandType.message,
                callback=coro
            )
            self.commands.append(cmd)
            return cmd

        return decorator

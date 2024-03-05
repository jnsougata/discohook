from .command import ApplicationCommand, Option, try_description
from .base import Component
from .enums import ApplicationCommandType
from .permission import Permission
from .utils import Handler

from typing import List, Optional


class CommandTree:

    def __init__(self):
        self.commands = []
        self.components = []
        self.active_components = {}

    def preload_component(self, custom_id: Optional[str]):
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
        dm_access: bool = True,
        nsfw: bool = False,
        permissions: Optional[List[Permission]] = None,
        guild_id: Optional[str] = None,
    ):
        """
        A decorator to register a slash command with its callback.
        """

        def decorator(coro: Handler):
            cmd = ApplicationCommand(
                name or coro.__name__,
                description=try_description(name, description, coro),
                options=options,
                dm_access=dm_access,
                nsfw=nsfw,
                permissions=permissions,
                guild_id=guild_id,
                callback=coro
            )
            self.commands.append(cmd)
            return cmd

        return decorator

    def user(
        self,
        name: Optional[str] = None,
        *,
        dm_access: bool = True,
        nsfw: bool = False,
        permissions: Optional[List[Permission]] = None,
        guild_id: Optional[str] = None
    ):
        """
        A decorator to register a user command with its callback.
        """

        def decorator(coro: Handler):
            cmd = ApplicationCommand(
                name or coro.__name__,
                dm_access=dm_access,
                nsfw=nsfw,
                permissions=permissions,
                guild_id=guild_id,
                kind=ApplicationCommandType.user,
                callback=coro
            )
            self.commands.append(cmd)
            return cmd

        return decorator

    def message(
        self,
        name: Optional[str] = None,
        *,
        dm_access: bool = True,
        nsfw: bool = False,
        permissions: Optional[List[Permission]] = None,
        guild_id: Optional[str] = None
    ):
        """
        A decorator to register a message command with its callback.
        """

        def decorator(coro: Handler):
            cmd = ApplicationCommand(
                name or coro.__name__,
                dm_access=dm_access,
                nsfw=nsfw,
                permissions=permissions,
                guild_id=guild_id,
                kind=ApplicationCommandType.message,
                callback=coro
            )
            self.commands.append(cmd)
            return cmd

        return decorator

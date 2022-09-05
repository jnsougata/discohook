from __future__ import annotations
import asyncio
import secrets
import requests
from .command import *
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import command_types
from .command import ApplicationCommand
from typing import Optional, List, Dict, Any, Union, Callable
from .errors import catch_exceptions_middleware


class Client(FastAPI):
    root_url = "https://discord.com/api/v10"

    def __init__(
            self,
            application_id: int,
            *,
            token: str,
            public_key: str,
            route: str = '/interactions',
            **kwargs
    ):
        super().__init__(**kwargs)
        self.application_id = application_id
        self.public_key = public_key
        self.token = token
        self._sync_able_commands: List[ApplicationCommand] = []
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self.add_route(route, handler, methods=['POST'], include_in_schema=False)
        self.middleware('http')(catch_exceptions_middleware)

    def command(
            self,
            name: str,
            description: str = None,
            *,
            options: List[Option] = None,
            permissions: str = None,
            dm_access: bool = True,
            guild_id: int = None,
            category: command_types = command_types.slash
    ):
        apc = ApplicationCommand(
            name=name,
            description=description,
            options=options,
            permissions=permissions,
            dm_access=dm_access,
            guild_id=guild_id,
            category=category
        )

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*args, **kwargs):
                if asyncio.iscoroutinefunction(coro):
                    apc.callback = coro
                    self._sync_able_commands.append(apc)
                    return apc
            return wrapper()
        return decorator

    def sync(self):
        headers = {"Authorization": f"Bot {self.token}"}
        for command in self._sync_able_commands:
            if command.guild_id:
                url = f"{self.root_url}/applications/{self.application_id}/guilds/{command.guild_id}/commands"
            else:
                url = f"{self.root_url}/applications/{self.application_id}/commands"
            payload = command.to_json()
            resp = requests.post(url, headers=headers, json=payload).json()
            command.id = resp['id']
            self.application_commands[resp['id']] = command
        self._sync_able_commands.clear()

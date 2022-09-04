from __future__ import annotations
import asyncio
import secrets
import requests
from .command import *
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import CommandType
from .command import ApplicationCommand
from typing import Optional, List, Dict, Any, Union, Callable


class Bot(FastAPI):
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
        self._sync_able_commands: Dict[str, ApplicationCommand] = {}
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self.add_route(route, handler, methods=['POST'], include_in_schema=False)

    def command(
            self,
            name: str,
            description: str = None,
            *,
            options: List[Option] = None,
            permissions: str = None,
            dm_access: bool = True,
            guild_id: int = None,
            category: CommandType = CommandType.SLASH
    ):
        unique_id = secrets.token_urlsafe(16)
        apc = ApplicationCommand(
            name=name,
            description=description,
            options=options,
            permissions=permissions,
            dm_access=dm_access,
            guild_id=guild_id,
            category=category
        )
        apc.id = unique_id

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*args, **kwargs):
                if asyncio.iscoroutinefunction(coro):
                    apc.callback = coro
                    self._sync_able_commands[unique_id] = apc
                    return apc
            return wrapper()
        return decorator

    def sync(self):
        headers = {"Authorization": f"Bot {self.token}"}
        for command in self._sync_able_commands.values():
            if command.guild_id:
                url = f"{self.root_url}/applications/{self.application_id}/guilds/{command.guild_id}/commands"
            else:
                url = f"{self.root_url}/applications/{self.application_id}/commands"
            payload = command.to_json()
            resp = requests.post(url, headers=headers, json=payload).json()
            command.id = resp['id']
            self.application_commands[resp['id']] = command
        self._sync_able_commands.clear()

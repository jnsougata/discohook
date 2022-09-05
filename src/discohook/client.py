from __future__ import annotations
import aiohttp
import asyncio
import secrets
from .command import *
from fastapi import FastAPI
from functools import wraps
from .listener import listener
from .enums import command_types
from .command import ApplicationCommand
from typing import Optional, List, Dict, Any, Union, Callable
from .errors import catch_exceptions_middleware


class Client(FastAPI):
    root_url = "https://discord.com/api/v10"

    def __init__(
            self,
            application_id: int,
            public_key: str,
            *,
            token: str = None,
            route: str = '/interactions',
            **kwargs
    ):
        super().__init__(**kwargs)
        self.application_id = application_id
        self.public_key = public_key
        self.token = token
        self._sync_able_commands: List[ApplicationCommand] = []
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self.add_route(route, listener, methods=['POST'], include_in_schema=False)
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

    def sync(self) -> None:
        async def sync_():
            headers = {"Authorization": f"Bot {self.token}"}
            async with aiohttp.ClientSession() as session:
                for command in self._sync_able_commands:
                    if command.guild_id:
                        url = f"{self.root_url}/applications/{self.application_id}/guilds/{command.guild_id}/commands"
                    else:
                        url = f"{self.root_url}/applications/{self.application_id}/commands"
                    payload = command.to_json()
                    resp = await (await session.post(url, headers=headers, json=payload)).json()
                    command.id = resp['id']
                    self.application_commands[resp['id']] = command
            self._sync_able_commands.clear()
        if self.token:
            asyncio.get_event_loop().run_until_complete(sync_())

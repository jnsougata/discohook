from __future__ import annotations
import aiohttp
import asyncio
import secrets
from .command import *
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import AppCmdType
from .modal import Modal
from .component import Button
from .command import ApplicationCommand
from typing import Optional, List, Dict, Any, Union, Callable


class Client(FastAPI):
    root_url = "https://discord.com/api/v10"

    def __init__(
            self,
            application_id: int,
            public_key: str,
            token: str,
            *,
            commands: List[ApplicationCommand] = None,
            route: str = '/interactions',
            express_debug: bool = False,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.token = token
        self.public_key = public_key
        self.application_id = application_id
        self.express_debug = express_debug
        self.ui_factory: Optional[Dict[str, Union[Button, Modal]]] = {}
        self._sync_able_commands: List[ApplicationCommand] = commands or []
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self._component_interaction_original_authors: Dict[str, str] = {}
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
            category: AppCmdType = AppCmdType.slash,
    ):
        command = ApplicationCommand(
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
            def wrapper(*_, **__):
                if asyncio.iscoroutinefunction(coro):
                    command._callback = coro
                    self._sync_able_commands.append(command)
                    return command
            return wrapper()
        return decorator

    def load_commands(self, *commands: ApplicationCommand):
        self._sync_able_commands.extend(commands)

    async def __call__(self, scope, receive, send):
        if self.root_path:
            scope["root_path"] = self.root_path
        if not self.token:
            raise ValueError("Token is not provided")
        headers = {"Authorization": f"Bot {self.token}"}
        async with aiohttp.ClientSession() as session:
            for command in self._sync_able_commands:
                if command.guild_id:
                    url = f"{self.root_url}/applications/{self.application_id}/guilds/{command.guild_id}/commands"
                else:
                    url = f"{self.root_url}/applications/{self.application_id}/commands"
                resp = await (await session.post(url, headers=headers, json=command.json())).json()
                command.id = resp['id']
                self.application_commands[resp['id']] = command
        self._sync_able_commands.clear()
        await super().__call__(scope, receive, send)

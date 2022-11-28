import aiohttp
import asyncio
from .cog import Cog
from .command import *
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import AppCmdType
from .modal import Modal
from .command import ApplicationCommand
from .component import Button, SelectMenu
from typing import Optional, List, Dict, Union, Callable


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

        self.ui_factory: Optional[Dict[str, Union[Button, Modal, SelectMenu]]] = {}

        self._qualified_commands: List[ApplicationCommand] = commands or []
        self.application_commands: Dict[str, ApplicationCommand] = {}

        self.add_route(route, handler, methods=['POST'], include_in_schema=False)
        self.cached_inter_tokens: Dict[str, str] = {}

    def _load_component(self, component: Union[Button, Modal, SelectMenu]):
        self.ui_factory[component.custom_id] = component

    def _load_inter_token(self, interaction_id: str, token: str):
        self.cached_inter_tokens[interaction_id] = token

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
                    self._qualified_commands.append(command)
                    return command
            return wrapper()
        return decorator

    def load_commands(self, *commands: ApplicationCommand):
        self._qualified_commands.extend(commands)
    
    async def delete_command(self, command_id: str, guild_id: int = None):
        if not guild_id:
            url = f"{self.root_url}/applications/{self.application_id}/commands/{command_id}"
        else:
            url = f"{self.root_url}/applications/{self.application_id}/guilds/{guild_id}/commands/{command_id}"
        headers = {"Authorization": f"Bot {self.token}"}
        async with aiohttp.ClientSession() as session:
            await session.delete(url, headers=headers)
            
    async def __call__(self, scope, receive, send):
        if self.root_path:
            scope["root_path"] = self.root_path
        if not self.token:
            raise ValueError("Token is not provided")
        headers = {"Authorization": f"Bot {self.token}"}
        async with aiohttp.ClientSession() as session:
            for command in self._qualified_commands:
                if command.guild_id:
                    url = f"{self.root_url}/applications/{self.application_id}/guilds/{command.guild_id}/commands"
                else:
                    url = f"{self.root_url}/applications/{self.application_id}/commands"
                resp = await (await session.post(url, headers=headers, json=command.json())).json()
                try:
                    command.id = resp['id']
                except KeyError:
                    raise ValueError(str(resp))
                self.application_commands[resp['id']] = command
        self._qualified_commands.clear()
        await super().__call__(scope, receive, send)

    def add_cog(self, cog: Cog):
        if isinstance(cog, Cog):
            self.load_commands(*cog.private_commands)

    def load_cog(self, path: str):
        import importlib
        importlib.import_module(path).setup(self)

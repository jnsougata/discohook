import aiohttp
import asyncio
from .cog import Cog
from .command import *
from .modal import Modal
from fastapi import FastAPI
from functools import wraps
from .handler import handler
from .enums import AppCmdType
from .user import ClientUser
from .permissions import Permissions
from .command import ApplicationCommand
from .component import Button, SelectMenu
from fastapi.requests import Request
from .dash import dashboard
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional, List, Dict, Union, Callable

async def del_cmd(request: Request, command_id: str):
    resp = await request.app.delete_command(command_id)
    if resp.status == 204:
        return JSONResponse({'success': True}, status_code=resp.status)
    return JSONResponse({'error': 'Failed to delete command'}, status_code=resp.status)

async def sync(request: Request, secret: str = None):
    if secret == request.app.token:
        return JSONResponse(await request.app.sync())
    return JSONResponse({'error': 'Unauthorized'}, status_code=401)


class Client(FastAPI):

    def __init__(
        self,
        application_id: Union[int, str],
        public_key: str,
        token: str,
        *,
        static: bool = False,
        route: str = '/interactions',
        log_channel_id: int = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.redoc_url = None
        self.docs_url = None
        self.token = token
        self.static = static
        self.public_key = public_key
        self.application_id = application_id
        self.log_channel_id: Optional[int] = log_channel_id
        self._session: Optional[aiohttp.ClientSession] = aiohttp.ClientSession(
            base_url="https://discord.com", 
            headers={"Authorization": f"Bot {self.token}"}
        )
        self.ui_factory: Optional[Dict[str, Union[Button, Modal, SelectMenu]]] = {}
        self._sync_queue: List[ApplicationCommand] = []
        self.application_commands: Dict[str, ApplicationCommand] = {}
        self.cached_inter_tokens: Dict[str, str] = {}
        self._populated_return: Optional[JSONResponse] = None
        self.add_route(route, handler, methods=['POST'], include_in_schema=False)
        self.add_api_route('/dh/sync/{secret}', sync, methods=['GET'], include_in_schema=False)
        self.add_api_route('/dh/dash/{secret}', dashboard, methods=['GET'], include_in_schema=False)
        self.add_api_route('/dh/delete/{command_id}', del_cmd, methods=['GET'], include_in_schema=False)
        self._global_error_handler: Optional[Callable] = None

    def _load_component(self, component: Union[Button, Modal, SelectMenu]):
        self.ui_factory[component.custom_id] = component

    def _load_inter_token(self, interaction_id: str, token: str):
        self.cached_inter_tokens[interaction_id] = token

    def command(
            self,
            name: str,
            description: str = None,
            *,
            id: str = None,
            options: List[Option] = None,
            permissions: List[Permissions] = None,
            dm_access: bool = True,
            category: AppCmdType = AppCmdType.slash,
    ):
        command = ApplicationCommand(
            name=name,
            description=description,
            options=options,
            permissions=permissions,
            dm_access=dm_access,
            category=category,
            id=id
        )

        def decorator(coro: Callable):
            @wraps(coro)
            def wrapper(*_, **__):
                if asyncio.iscoroutinefunction(coro):
                    command._callback = coro
                    if command.id:
                        self.application_commands[command.id] = command
                    self._sync_queue.append(command)
                    return command
            return wrapper()
        return decorator
    
    def load_commands(self, *commands: ApplicationCommand):
        static_commands = {command.id: command for command in commands if command.id}
        self.application_commands.update(static_commands)
        self._sync_queue.extend(commands)
            
    async def delete_command(self, command_id: str):
        return await self._session.delete(f"/api/v10/applications/{self.application_id}/commands/{command_id}")
             
    def add_cog(self, cog: Cog):
        if isinstance(cog, Cog):
            self.load_commands(*cog.private_commands)

    def load_cogs(self, *paths: str):
        import importlib
        for path in paths:
            importlib.import_module(path).setup(self)

    def on_error(self, coro: Callable):
        self._global_error_handler = coro

    async def send_message(self, channel_id: int, payload: Dict[str, Any]):
        url = f"/api/v10/channels/{channel_id}/messages"
        await self._session.post(url, json=payload)

    async def as_user(self) -> ClientUser:
        data = await (await self._session.get(f"/api/v10/oauth2/applications/@me")).json()
        return ClientUser(data)

    async def sync(self):
        url = f"/api/v10/applications/{self.application_id}/commands"
        payload  = [command.json() for command in self._sync_queue]
        resp = await self._session.put(url, json=payload)
        return await resp.json()
    
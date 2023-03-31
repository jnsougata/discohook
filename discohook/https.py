import aiohttp
from .message import Message
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client


async def request(
    method: str = "GET", *, path: str, session: aiohttp.ClientSession, **kwargs
):
    r = await session.request(method, f"/api/v10/{path}", **kwargs)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}


async def multipart_request(
    method: str = "POST", 
    *, 
    path: str, 
    session: aiohttp.ClientSession, 
    form: aiohttp.MultipartWriter, 
):
    r = await session.request(method, f"/api/v10/{path}", data=form, headers=form.headers)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}


class HTTPClient:

    def __init__(self, token: str, client: "Client"):
        self.token = token
        self.client = client
        self.session = aiohttp.ClientSession("https://discord.com")
    
    async def request(
            self, 
            method: str,
            path: str, 
            *, 
            use_auth: bool = False, 
            **kwargs
    ):
        headers = kwargs.pop("headers", {})
        if use_auth:
            headers["Authorization"] = f"Bot {self.token}"
        headers["Content-Type"] = "application/json"
        kwargs["headers"] = headers
        return await self.session.request(method, f"/api/v10{path}", **kwargs)

    async def multipart(
        self, method: str, 
        path: str, 
        *, 
        form: aiohttp.MultipartWriter, 
        use_auth: bool = False
    ):
        if use_auth:
            form.headers.add("Authorization", f"Bot {self.token}")
        return await self.session.request(method, f"/api/v10{path}", data=form, headers=form.headers)

    async def send_message(self, channel_id: str, form: aiohttp.MultipartWriter):
        r = await self.multipart("POST", f"/channels/{channel_id}/messages", form=form, use_auth=True)
        data = await r.json()
        return Message(data, self.client)
    
    async def delete_message(self, channel_id: str, message_id: str):
        await self.request("DELETE", f"/channels/{channel_id}/messages/{message_id}", use_auth=True)
    
    async def edit_channel_message(self, channel_id: str, message_id: str, form: aiohttp.MultipartWriter):
        r = await self.multipart("PATCH", f"/channels/{channel_id}/messages/{message_id}", form=form, use_auth=True)
        data = await r.json()
        return Message(data, self.client)

    async def send_webhook_message(self, webhook_id: str, webhook_token: str, form: aiohttp.MultipartWriter):
        r = await self.multipart("POST", f"/webhooks/{webhook_id}/{webhook_token}", form=form)
        data = await r.json()
        return Message(data, self.client)
    
    async def delete_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str):
        await self.request("DELETE", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
    
    async def edit_webhook_message(
        self,
        webhook_id: str,
        webhook_token: str,
        message_id: str,
        form: aiohttp.MultipartWriter
    ):
        r = await self.multipart("PATCH", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}", form=form)
        data = await r.json()
        return Message(data, self.client)

    async def fetch_original_webhook_message(self, webhook_id: str, webhook_token: str):
        return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}/messages/@original")

    async def add_role(self, guild_id: str, user_id: str, role_id: str):
        return await self.request("PUT", f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", use_auth=True)

    async def remove_role(self, guild_id: str, user_id: str, role_id: str):
        return await self.request("DELETE", f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", use_auth=True)

    async def kick_user(self, guild_id: str, user_id: str):
        return await self.request("DELETE", f"/guilds/{guild_id}/members/{user_id}", use_auth=True)

    async def ban_user(self, guild_id: str, user_id: str, delete_message_seconds: int = 0):
        return await self.request(
            "PUT", f"/guilds/{guild_id}/bans/{user_id}", use_auth=True,
            json={"delete_message_seconds": delete_message_seconds}
        )

    async def fetch_guild(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}?with_counts=true", use_auth=True)

    async def send_interaction_callback(self, interaction_id: str, interaction_token: str, data: dict):
        return await self.request("POST", f"/interactions/{interaction_id}/{interaction_token}/callback", json=data)

    async def send_interaction_mp_callback(
            self,
            interaction_id: str,
            interaction_token: str,
            form: aiohttp.MultipartWriter
    ):
        return await self.multipart("POST", f"/interactions/{interaction_id}/{interaction_token}/callback", form=form)

    async def edit_interaction_mp_callback(
            self,
            interaction_id: str,
            interaction_token: str,
            form: aiohttp.MultipartWriter
    ):
        return await self.multipart("PATCH", f"/interactions/{interaction_id}/{interaction_token}/callback", form=form)

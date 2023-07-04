from typing import TYPE_CHECKING, Any, Dict, List, Optional

import aiohttp

if TYPE_CHECKING:
    from .client import Client


class HTTPClient:
    def __init__(self, client: "Client", token: str, session: aiohttp.ClientSession):
        self.token = token
        self.client = client
        self.session = session

    async def request(self, method: str, path: str, *, use_auth: bool = False, **kwargs):
        headers = kwargs.pop("headers", {})
        if use_auth:
            headers["Authorization"] = f"Bot {self.token}"
        headers["Content-Type"] = "application/json"
        kwargs["headers"] = headers
        return await self.session.request(method, f"/api/v10{path}", **kwargs)

    async def multipart(self, method: str, path: str, *, form: aiohttp.MultipartWriter, use_auth: bool = False):
        if use_auth:
            form.headers.add("Authorization", f"Bot {self.token}")
        return await self.session.request(method, f"/api/v10{path}", data=form, headers=form.headers)

    async def sync_commands(self, application_id: str, commands: List[Dict[str, Any]]):
        return await self.request("PUT", f"/applications/{application_id}/commands", json=commands, use_auth=True)

    async def fetch_client_info(self):
        return await self.request("GET", "/oauth2/applications/@me", use_auth=True)

    async def delete_command(self, application_id: str, command_id: str):
        return await self.request("DELETE", f"/applications/{application_id}/commands/{command_id}", use_auth=True)

    async def send_message(self, channel_id: str, form: aiohttp.MultipartWriter):
        return await self.multipart("POST", f"/channels/{channel_id}/messages", form=form, use_auth=True)

    async def create_dm_channel(self, payload: Dict[str, Any]):
        return await self.request("POST", "/users/@me/channels", json=payload, use_auth=True)

    async def delete_channel(self, channel_id: str):
        return await self.request("DELETE", f"/channels/{channel_id}", use_auth=True)

    async def delete_message(self, channel_id: str, message_id: str):
        await self.request("DELETE", f"/channels/{channel_id}/messages/{message_id}", use_auth=True)

    async def edit_channel_message(self, channel_id: str, message_id: str, form: aiohttp.MultipartWriter):
        return await self.multipart("PATCH", f"/channels/{channel_id}/messages/{message_id}", form=form, use_auth=True)

    async def send_webhook_message(self, webhook_id: str, webhook_token: str, form: aiohttp.MultipartWriter):
        return await self.multipart("POST", f"/webhooks/{webhook_id}/{webhook_token}", form=form)

    async def delete_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str):
        await self.request("DELETE", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")

    async def edit_webhook_message(
        self, webhook_id: str, webhook_token: str, message_id: str, form: aiohttp.MultipartWriter
    ):
        return await self.multipart(
            "PATCH", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}", form=form
        )

    async def fetch_original_webhook_message(self, webhook_id: str, webhook_token: str):
        return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}/messages/@original")

    async def add_role(self, guild_id: str, user_id: str, role_id: str):
        return await self.request("PUT", f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", use_auth=True)

    async def remove_role(self, guild_id: str, user_id: str, role_id: str):
        return await self.request("DELETE", f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", use_auth=True)

    async def fetch_user(self, user_id: str):
        return await self.request("GET", f"/users/{user_id}", use_auth=True)
    
    async def kick_user(self, guild_id: str, user_id: str):
        return await self.request("DELETE", f"/guilds/{guild_id}/members/{user_id}", use_auth=True)

    async def ban_user(self, guild_id: str, user_id: str, delete_message_seconds: int = 0):
        return await self.request(
            "PUT",
            f"/guilds/{guild_id}/bans/{user_id}",
            use_auth=True,
            json={"delete_message_seconds": delete_message_seconds},
        )

    async def send_interaction_callback(self, interaction_id: str, interaction_token: str, data: dict):
        return await self.request("POST", f"/interactions/{interaction_id}/{interaction_token}/callback", json=data)

    async def send_interaction_mp_callback(
        self, interaction_id: str, interaction_token: str, form: aiohttp.MultipartWriter
    ):
        return await self.multipart("POST", f"/interactions/{interaction_id}/{interaction_token}/callback", form=form)

    async def edit_interaction_mp_callback(
        self, interaction_id: str, interaction_token: str, form: aiohttp.MultipartWriter
    ):
        return await self.multipart("PATCH", f"/interactions/{interaction_id}/{interaction_token}/callback", form=form)

    async def fetch_guild(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}?with_counts=true", use_auth=True)

    async def fetch_guild_channels(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/channels", use_auth=True)

    async def fetch_guild_roles(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/roles", use_auth=True)

    async def create_guild_channel(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request("POST", f"/guilds/{guild_id}/channels", json=payload, use_auth=True)

    async def edit_channel(self, channel_id: str, payload: Dict[str, Any]):
        return await self.request("PATCH", f"/channels/{channel_id}", json=payload, use_auth=True)

    async def edit_guild_channel_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request("PATCH", f"/guilds/{guild_id}/channels", json=payload, use_auth=True)

    async def create_guild_role(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request("POST", f"/guilds/{guild_id}/roles", json=payload, use_auth=True)

    async def edit_guild_role_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request("PATCH", f"/guilds/{guild_id}/roles", json=payload, use_auth=True)

    async def edit_guild_role(self, guild_id: str, role_id: str, payload: Dict[str, Any]):
        return await self.request("PATCH", f"/guilds/{guild_id}/roles/{role_id}", json=payload, use_auth=True)

    async def create_webhook(self, channel_id: str, payload: Dict[str, Any]):
        return await self.request("POST", f"/channels/{channel_id}/webhooks", json=payload, use_auth=True)

    async def edit_webhook(self, webhook_id: str, payload: Dict[str, Any]):
        return await self.request("PATCH", f"/webhooks/{webhook_id}", json=payload, use_auth=True)

    async def fetch_webhook(self, webhook_id: str, webhook_token: Optional[str] = None):
        if webhook_token:
            return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}")
        return await self.request("GET", f"/webhooks/{webhook_id}", use_auth=True)

    async def delete_webhook(self, webhook_id: str):
        return await self.request("DELETE", f"/webhooks/{webhook_id}", use_auth=True)

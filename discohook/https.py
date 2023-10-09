from typing import TYPE_CHECKING, Any, Dict, List, Optional

import aiohttp

if TYPE_CHECKING:
    from .client import Client


class HTTPClient:
    """Represents an HTTP client for Discord's API."""

    DISCORD_API_VERSION: int = 10

    def __init__(self, client: "Client", token: str, session: aiohttp.ClientSession):
        self.token = token
        self.client = client
        self.session = session

    async def request(self, method: str, path: str, *, use_auth: bool = False, **kwargs):
        headers = kwargs.pop("headers", {})
        reason = kwargs.pop("reason", None)
        if use_auth:
            headers["Authorization"] = f"Bot {self.token}"
        if reason:
            headers["X-Audit-Log-Reason"] = reason
        headers["Content-Type"] = "application/json"
        kwargs["headers"] = headers
        return await self.session.request(method, f"/api/v{self.DISCORD_API_VERSION}{path}", **kwargs)

    async def multipart(
            self, method: str,
            path: str,
            *,
            form: aiohttp.MultipartWriter,
            use_auth: bool = False,
            **kwargs
    ):
        for key, value in kwargs.pop("headers", {}).items():
            form.headers.add(key, value)
        reason = kwargs.pop("reason", None)
        if reason:
            form.headers.add("X-Audit-Log-Reason", reason)
        if use_auth:
            form.headers.add("Authorization", f"Bot {self.token}")
        return await self.session.request(method, f"/api/v10{path}", data=form, headers=form.headers)

    async def fetch_application(self):
        return await self.request("GET", "/applications/@me", use_auth=True)

    async def sync_global_commands(self, application_id: str, commands: List[Dict[str, Any]]):
        return await self.request("PUT", f"/applications/{application_id}/commands", json=commands, use_auth=True)

    async def sync_guild_commands(self, application_id: str, guild_id: str, commands: List[Dict[str, Any]]):
        return await self.request(
            "PUT", f"/applications/{application_id}/guilds/{guild_id}/commands", json=commands, use_auth=True)

    async def fetch_global_application_commands(self, application_id: str):
        return await self.request("GET", f"/applications/{application_id}/commands", use_auth=True)

    async def edit_client(self, payload: Dict[str, Any]):
        return await self.request("PATCH", "/users/@me", json=payload, use_auth=True)

    async def delete_command(self, application_id: str, command_id: str, guild_id: Optional[str] = None):
        if guild_id:
            return await self.request(
                "DELETE", f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}", use_auth=True)
        return await self.request("DELETE", f"/applications/{application_id}/commands/{command_id}", use_auth=True)

    async def send_message(self, channel_id: str, form: aiohttp.MultipartWriter):
        return await self.multipart("POST", f"/channels/{channel_id}/messages", form=form, use_auth=True)

    async def create_dm_channel(self, payload: Dict[str, Any]):
        return await self.request("POST", "/users/@me/channels", json=payload, use_auth=True)

    async def fetch_channel(self, channel_id: str):
        return await self.request("GET", f"/channels/{channel_id}", use_auth=True)

    async def delete_channel(self, channel_id: str, *, reason: Optional[str] = None):
        return await self.request("DELETE", f"/channels/{channel_id}", reason=reason, use_auth=True)

    async def fetch_channel_message(self, channel_id: str, message_id: str):
        return await self.request("GET", f"/channels/{channel_id}/messages/{message_id}", use_auth=True)

    async def fetch_channel_messages(self, channel_id: str, params: Dict[str, Any]):
        return await self.request("GET", f"/channels/{channel_id}/messages", params=params, use_auth=True)

    async def delete_channel_message(self, channel_id: str, message_id: str, *, reason: Optional[str] = None):
        await self.request("DELETE", f"/channels/{channel_id}/messages/{message_id}", reason=reason, use_auth=True)

    async def delete_channel_messages(self, channel_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        await self.request("POST", f"/channels/{channel_id}/messages/bulk-delete", json=payload, reason=reason, use_auth=True)

    async def pin_channel_message(self, channel_id: str, message_id: str, *, reason: Optional[str] = None):
        await self.request("PUT", f"/channels/{channel_id}/messages/{message_id}/pin", reason=reason, use_auth=True)

    async def unpin_channel_message(self, channel_id: str, message_id: str, *, reason: Optional[str] = None):
        await self.request("DELETE", f"/channels/{channel_id}/messages/{message_id}/pin", reason=reason, use_auth=True)

    async def edit_channel_message(self, channel_id: str, message_id: str, form: aiohttp.MultipartWriter):
        return await self.multipart("PATCH", f"/channels/{channel_id}/messages/{message_id}", form=form, use_auth=True)

    async def send_webhook_message(self, webhook_id: str, webhook_token: str, form: aiohttp.MultipartWriter):
        return await self.multipart("POST", f"/webhooks/{webhook_id}/{webhook_token}", form=form)

    async def delete_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str):
        await self.request("DELETE", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")

    async def edit_webhook_message(
        self, webhook_id: str, webhook_token: str, message_id: str, form: aiohttp.MultipartWriter
    ):
        return await self.multipart("PATCH", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}", form=form)

    async def fetch_original_webhook_message(self, webhook_id: str, webhook_token: str):
        return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}/messages/@original")

    async def add_role(self, guild_id: str, user_id: str, role_id: str, *, reason: Optional[str] = None):
        return await self.request(
            "PUT", f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", reason=reason, use_auth=True)

    async def remove_role(self, guild_id: str, user_id: str, role_id: str, *, reason: Optional[str] = None):
        return await self.request("DELETE", f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", reason=reason, use_auth=True)

    async def fetch_user(self, user_id: str):
        return await self.request("GET", f"/users/{user_id}", use_auth=True)
    
    async def kick_user(self, guild_id: str, user_id: str, *, reason: Optional[str] = None):
        return await self.request("DELETE", f"/guilds/{guild_id}/members/{user_id}", reason=reason, use_auth=True)

    async def ban_user(self, guild_id: str, user_id: str, delete_message_seconds: int = 0, *, reason: Optional[str] = None):
        return await self.request(
            "PUT",
            f"/guilds/{guild_id}/bans/{user_id}",
            reason=reason,
            use_auth=True,
            json={"delete_message_seconds": delete_message_seconds},
        )

    async def send_interaction_callback(self, interaction_id: str, interaction_token: str, data: dict):
        return await self.request("POST", f"/interactions/{interaction_id}/{interaction_token}/callback", json=data)

    async def send_interaction_mp_callback(
        self, interaction_id: str, interaction_token: str, form: aiohttp.MultipartWriter
    ):
        return await self.multipart("POST", f"/interactions/{interaction_id}/{interaction_token}/callback", form=form)

    async def fetch_guild(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}?with_counts=true", use_auth=True)

    async def fetch_guild_member(self, guild_id: str, user_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/members/{user_id}", use_auth=True)

    async def fetch_guild_channels(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/channels", use_auth=True)

    async def fetch_guild_roles(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/roles", use_auth=True)

    async def create_guild_channel(self, guild_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("POST", f"/guilds/{guild_id}/channels", json=payload, reason=reason, use_auth=True)

    async def crosspost_channel_message(self, channel_id: str, message_id: str):
        return await self.request("POST", f"/channels/{channel_id}/messages/{message_id}/crosspost", use_auth=True)

    async def edit_channel(self, channel_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("PATCH", f"/channels/{channel_id}", json=payload, reason=reason, use_auth=True)

    async def edit_guild_channel_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request("PATCH", f"/guilds/{guild_id}/channels", json=payload, use_auth=True)

    async def create_guild_role(self, guild_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("POST", f"/guilds/{guild_id}/roles", json=payload, reason=reason, use_auth=True)

    async def edit_guild_role_position(self, guild_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("PATCH", f"/guilds/{guild_id}/roles", json=payload, use_auth=True)

    async def edit_guild_role(self, guild_id: str, role_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("PATCH", f"/guilds/{guild_id}/roles/{role_id}", json=payload, reason=reason, use_auth=True)

    async def create_guild_emoji(self, guild_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("POST", f"/guilds/{guild_id}/emojis", json=payload, reason=reason, use_auth=True)

    async def create_webhook(self, channel_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("POST", f"/channels/{channel_id}/webhooks", json=payload, reason=reason, use_auth=True)

    async def execute_webhook(self, webhook_id: str, webhook_token: str, form: aiohttp.MultipartWriter):
        return await self.multipart("POST", f"/webhooks/{webhook_id}/{webhook_token}", form=form)

    async def edit_webhook(self, webhook_id: str, payload: Dict[str, Any], *, reason: Optional[str] = None):
        return await self.request("PATCH", f"/webhooks/{webhook_id}", json=payload, reason=reason, use_auth=True)

    async def fetch_webhook(self, webhook_id: str, webhook_token: Optional[str] = None):
        if webhook_token:
            return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}")
        return await self.request("GET", f"/webhooks/{webhook_id}", use_auth=True)

    async def delete_webhook(self, webhook_id: str, *, reason: Optional[str] = None):
        return await self.request("DELETE", f"/webhooks/{webhook_id}", reason=reason, use_auth=True)

    async def create_message_reaction(self, channel_id: str, message_id: str, emoji: str):
        return await self.request(
            "PUT", f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", use_auth=True)

    async def delete_message_reaction(self, message_id: str, emoji: str, user_id: str):
        return await self.request(
            "DELETE", f"/channels/{message_id}/messages/{message_id}/reactions/{emoji}/{user_id}", use_auth=True)

    async def delete_all_message_reactions(self, message_id: str, emoji: Optional[str] = None):
        path = f"/channels/{message_id}/messages/{message_id}/reactions"
        if emoji:
            path += f"/{emoji}"
        return await self.request("DELETE", path, use_auth=True)

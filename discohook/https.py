from typing import TYPE_CHECKING, Any, Dict, List, Optional

import aiohttp

from .errors import HTTPException

if TYPE_CHECKING:
    from .client import Client


class HTTPClient:
    """Represents an HTTP client for Discord's API."""

    DISCORD_API_VERSION: int = 10

    def __init__(self, client: "Client", token: str):
        self.token = token
        self.client = client
        self.session: Optional[aiohttp.ClientSession] = None

    async def request(
        self,
        method: str,
        path: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        reason: Optional[str] = None,
        json: Any = None,
        form: aiohttp.MultipartWriter = None,
        params: Optional[Dict[str, Any]] = None,
        authorize: bool = False,
    ):
        headers = headers or {}
        if authorize:
            headers["Authorization"] = f"Bot {self.token}"
        if reason:
            headers["X-Audit-Log-Reason"] = reason
        if not form:
            headers["Content-Type"] = "application/json"
        if form:
            for key, value in headers.items():
                form.headers.add(key, value)
        if not self.session:
            self.session = aiohttp.ClientSession("https://discord.com")
        resp = await self.session.request(
            method,
            f"/api/v{self.DISCORD_API_VERSION}{path}",
            params=params,
            headers=form.headers if form else headers,
            data=form,
            json=json,
        )
        if resp.status >= 400:
            raise HTTPException(resp, await resp.json())
        return resp

    async def fetch_application(self):
        return await self.request("GET", "/applications/@me", authorize=True)

    async def sync_global_commands(
        self, application_id: str, commands: List[Dict[str, Any]]
    ):
        return await self.request(
            "PUT",
            f"/applications/{application_id}/commands",
            json=commands,
            authorize=True,
        )

    async def sync_guild_commands(
        self, application_id: str, guild_id: str, commands: List[Dict[str, Any]]
    ):
        return await self.request(
            "PUT",
            f"/applications/{application_id}/guilds/{guild_id}/commands",
            json=commands,
            authorize=True,
        )

    async def fetch_global_application_commands(self, application_id: str):
        return await self.request(
            "GET", f"/applications/{application_id}/commands", authorize=True
        )

    async def edit_client(self, payload: Dict[str, Any]):
        return await self.request("PATCH", "/users/@me", json=payload, authorize=True)

    async def delete_command(
        self, application_id: str, command_id: str, guild_id: Optional[str] = None
    ):
        if guild_id:
            return await self.request(
                "DELETE",
                f"/applications/{application_id}/guilds/{guild_id}/commands/{command_id}",
                authorize=True,
            )
        return await self.request(
            "DELETE",
            f"/applications/{application_id}/commands/{command_id}",
            authorize=True,
        )

    async def send_message(self, channel_id: str, form: aiohttp.MultipartWriter):
        return await self.request(
            "POST", f"/channels/{channel_id}/messages", form=form, authorize=True
        )

    async def create_dm_channel(self, payload: Dict[str, Any]):
        return await self.request(
            "POST", "/users/@me/channels", json=payload, authorize=True
        )

    async def fetch_channel(self, channel_id: str):
        return await self.request("GET", f"/channels/{channel_id}", authorize=True)

    async def delete_channel(self, channel_id: str):
        return await self.request("DELETE", f"/channels/{channel_id}", authorize=True)

    async def fetch_channel_message(self, channel_id: str, message_id: str):
        return await self.request(
            "GET", f"/channels/{channel_id}/messages/{message_id}", authorize=True
        )

    async def fetch_channel_messages(self, channel_id: str, params: Dict[str, Any]):
        return await self.request(
            "GET", f"/channels/{channel_id}/messages", params=params, authorize=True
        )

    async def delete_channel_message(self, channel_id: str, message_id: str):
        await self.request(
            "DELETE", f"/channels/{channel_id}/messages/{message_id}", authorize=True
        )

    async def delete_channel_messages(self, channel_id: str, payload: Dict[str, Any]):
        await self.request(
            "POST",
            f"/channels/{channel_id}/messages/bulk-delete",
            json=payload,
            authorize=True,
        )

    async def pin_channel_message(self, channel_id: str, message_id: str):
        await self.request(
            "PUT", f"/channels/{channel_id}/messages/{message_id}/pin", authorize=True
        )

    async def unpin_channel_message(self, channel_id: str, message_id: str):
        await self.request(
            "DELETE",
            f"/channels/{channel_id}/messages/{message_id}/pin",
            authorize=True,
        )

    async def edit_channel_message(
        self, channel_id: str, message_id: str, form: aiohttp.MultipartWriter
    ):
        return await self.request(
            "PATCH",
            f"/channels/{channel_id}/messages/{message_id}",
            form=form,
            authorize=True,
        )

    async def send_webhook_message(
        self, webhook_id: str, webhook_token: str, form: aiohttp.MultipartWriter
    ):
        return await self.request(
            "POST", f"/webhooks/{webhook_id}/{webhook_token}", form=form
        )

    async def delete_webhook_message(
        self, webhook_id: str, webhook_token: str, message_id: str
    ):
        await self.request(
            "DELETE", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}"
        )

    async def edit_webhook_message(
        self,
        webhook_id: str,
        webhook_token: str,
        message_id: str,
        form: aiohttp.MultipartWriter,
    ):
        return await self.request(
            "PATCH",
            f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}",
            form=form,
        )

    async def fetch_original_webhook_message(self, webhook_id: str, webhook_token: str):
        return await self.request(
            "GET", f"/webhooks/{webhook_id}/{webhook_token}/messages/@original"
        )

    async def add_role(
        self, guild_id: str, user_id: str, role_id: str, *, reason: Optional[str] = None
    ):
        return await self.request(
            "PUT",
            f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}",
            reason=reason,
            authorize=True,
        )

    async def remove_role(self, guild_id: str, user_id: str, role_id: str):
        return await self.request(
            "DELETE",
            f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}",
            authorize=True,
        )

    async def fetch_user(self, user_id: str):
        return await self.request("GET", f"/users/{user_id}", authorize=True)

    async def kick_user(self, guild_id: str, user_id: str):
        return await self.request(
            "DELETE", f"/guilds/{guild_id}/members/{user_id}", authorize=True
        )

    async def ban_user(
        self, guild_id: str, user_id: str, delete_message_seconds: int = 0
    ):
        return await self.request(
            "PUT",
            f"/guilds/{guild_id}/bans/{user_id}",
            authorize=True,
            json={"delete_message_seconds": delete_message_seconds},
        )

    async def send_interaction_callback(
        self, interaction_id: str, interaction_token: str, data: dict
    ):
        return await self.request(
            "POST",
            f"/interactions/{interaction_id}/{interaction_token}/callback",
            json=data,
        )

    async def send_interaction_mp_callback(
        self, interaction_id: str, interaction_token: str, form: aiohttp.MultipartWriter
    ):
        return await self.request(
            "POST",
            f"/interactions/{interaction_id}/{interaction_token}/callback",
            form=form,
        )

    async def fetch_guild(self, guild_id: str):
        return await self.request(
            "GET", f"/guilds/{guild_id}?with_counts=true", authorize=True
        )

    async def fetch_guild_member(self, guild_id: str, user_id: str):
        return await self.request(
            "GET", f"/guilds/{guild_id}/members/{user_id}", authorize=True
        )

    async def fetch_guild_channels(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/channels", authorize=True)

    async def fetch_guild_roles(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/roles", authorize=True)

    async def create_guild_channel(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/guilds/{guild_id}/channels", json=payload, authorize=True
        )

    async def crosspost_channel_message(self, channel_id: str, message_id: str):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages/{message_id}/crosspost",
            authorize=True,
        )

    async def edit_channel(self, channel_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/channels/{channel_id}", json=payload, authorize=True
        )

    async def edit_guild_channel_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/guilds/{guild_id}/channels", json=payload, authorize=True
        )

    async def create_guild_role(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/guilds/{guild_id}/roles", json=payload, authorize=True
        )

    async def edit_guild_role_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/guilds/{guild_id}/roles", json=payload, authorize=True
        )

    async def edit_guild_role(
        self, guild_id: str, role_id: str, payload: Dict[str, Any]
    ):
        return await self.request(
            "PATCH", f"/guilds/{guild_id}/roles/{role_id}", json=payload, authorize=True
        )

    async def create_guild_emoji(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/guilds/{guild_id}/emojis", json=payload, authorize=True
        )

    async def create_webhook(self, channel_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/channels/{channel_id}/webhooks", json=payload, authorize=True
        )

    async def execute_webhook(
        self,
        webhook_id: str,
        webhook_token: str,
        form: aiohttp.MultipartWriter,
        params: Dict[str, Any],
    ):
        return await self.request(
            "POST", f"/webhooks/{webhook_id}/{webhook_token}", form=form, params=params
        )

    async def edit_webhook(self, webhook_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/webhooks/{webhook_id}", json=payload, authorize=True
        )

    async def fetch_webhook(self, webhook_id: str, webhook_token: Optional[str] = None):
        if webhook_token:
            return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}")
        return await self.request("GET", f"/webhooks/{webhook_id}", authorize=True)

    async def delete_webhook(self, webhook_id: str):
        return await self.request("DELETE", f"/webhooks/{webhook_id}", authorize=True)

    async def create_message_reaction(
        self, channel_id: str, message_id: str, emoji: str
    ):
        return await self.request(
            "PUT",
            f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
            authorize=True,
        )

    async def delete_message_reaction(self, message_id: str, emoji: str, user_id: str):
        return await self.request(
            "DELETE",
            f"/channels/{message_id}/messages/{message_id}/reactions/{emoji}/{user_id}",
            authorize=True,
        )

    async def delete_all_message_reactions(
        self, message_id: str, emoji: Optional[str] = None
    ):
        path = f"/channels/{message_id}/messages/{message_id}/reactions"
        if emoji:
            path += f"/{emoji}"
        return await self.request("DELETE", path, authorize=True)

    async def create_test_entitlement(
        self, application_id: str, payload: Dict[str, Any]
    ):
        return await self.request(
            "POST",
            f"/applications/{application_id}/entitlements",
            json=payload,
            authorize=True,
        )

    async def delete_test_entitlement(self, application_id: str, entitlement_id: str):
        return await self.request(
            "DELETE",
            f"/applications/{application_id}/entitlements/{entitlement_id}",
            authorize=True,
        )

    async def fetch_entitlement(self, application_id: str, entitlement_id: str):
        return await self.request(
            "GET",
            f"/applications/{application_id}/entitlements/{entitlement_id}",
            authorize=True,
        )

    async def fetch_entitlements(self, application_id: str, params: Dict[str, Any]):
        return await self.request(
            "GET",
            f"/applications/{application_id}/entitlements",
            params=params,
            authorize=True,
        )

    async def fetch_skus(self, application_id: str):
        return await self.request(
            "GET", f"/applications/{application_id}/skus", authorize=True
        )

    async def start_thread_without_message(
        self, channel_id: str, payload: Dict[str, Any], reason: Optional[str] = None
    ):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/threads",
            json=payload,
            authorize=True,
            reason=reason,
        )

    async def start_thread_with_message(
        self,
        channel_id: str,
        message_id: str,
        payload: Dict[str, Any],
        reason: Optional[str] = None,
    ):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages/{message_id}/threads",
            json=payload,
            authorize=True,
            reason=reason,
        )

    async def fetch_answer_voters(
        self,
        channel_id: str,
        message_id: str,
        answer_id: int,
        *,
        params: Dict[str, Any] = None,
    ):
        return await self.request(
            "GET",
            f"/channels/{channel_id}/polls/{message_id}/answers/{answer_id}",
            params=params,
            authorize=True,
        )

    async def end_poll(self, channel_id: str, message_id: str):
        return await self.request(
            "POST", f"/channels/{channel_id}/polls/{message_id}/expire", authorize=True
        )

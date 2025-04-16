import json
from typing import Any, Dict, List, Optional, Union

import aiohttp

from . import __url__, __version__
from .errors import HTTPException


class HTTPClient:
    """Represents an HTTP client for Discord's API."""

    DISCORD_API_VERSION: int = 10
    USER_AGENT: str = f"discohook ({__url__}, {__version__})"

    def __init__(
        self,
        *,
        token: Optional[str] = None,
        application_id: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ):
        self.token = token
        self.application_id = application_id
        self.session: Optional[aiohttp.ClientSession] = session

    async def request(
        self,
        method: str,
        path: str,
        *,
        body: Union[aiohttp.MultipartWriter, Any] = None,
        params: Optional[Dict[str, Any]] = None,
        authorize: bool = False,
        reason: Optional[str] = None,
    ):
        headers = {"User-Agent": self.USER_AGENT}
        if authorize:
            headers["Authorization"] = f"Bot {self.token}"
        if reason:
            headers["X-Audit-Log-Reason"] = reason
        if body:
            if isinstance(body, aiohttp.MultipartWriter):
                for key, value in headers.items():
                    body.headers.add(key, value)
                headers = body.headers
            else:
                headers["Content-Type"] = "application/json"
                body = json.dumps(body)
        if not self.session:
            self.session = aiohttp.ClientSession("https://discord.com")
        resp = await self.session.request(
            method,
            f"/api/v{self.DISCORD_API_VERSION}{path}",
            params=params,
            headers=headers,
            data=body,
        )
        if resp.status >= 400:
            raise HTTPException(resp, await resp.read())
        return resp

    # Interactions
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interactions

    async def create_interaction_response(): pass
    async def get_original_interaction_response(): pass # get_webhook_message(), message_id as @original
    async def edit_original_interaction_response(): pass # edit_webhook_message(), message_id as @original
    async def delete_original_interaction_response(): pass # delete_webhook_message(), message_id as @original + no thread_id param
    async def create_followup_message(): pass # execute_webhook()
    async def get_followup_message(): pass # get_webhook_message()
    async def edit_followup_message(): pass # edit_webhook_message()
    async def delete_followup_message(): pass # delete_webhook_message()

    # Application Role Connection Metadata
    # https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata

    async def get_application_role_connection_metadata_records(): pass
    async def update_application_role_connection_metadata_records(): pass

    # Application Resource
    # https://discord.com/developers/docs/resources/application#application-resource

    async def get_current_application(self):
        return await self.request("GET", "/applications/@me", authorize=True)

    async def edit_current_application(): pass
    async def get_application_activity_instance(): pass

    # Audit Logs Resource
    # https://discord.com/developers/docs/resources/audit-log#audit-logs-resource

    async def get_audit_log(): pass

    # Auto Moderation
    # https://discord.com/developers/docs/resources/auto-moderation#auto-moderation

    async def list_auto_moderation_rules_for_guild(): pass
    async def get_auto_moderation_rule(): pass
    async def create_auto_moderation_rule(): pass
    async def modify_auto_moderation_rule(): pass
    async def delete_auto_moderation_rule(): pass

    # Channels Resource
    # https://discord.com/developers/docs/resources/channel#channels-resource

    async def get_channel(): pass
    async def modify_channel(): pass
    async def delete_or_close_channel(): pass # "closes" a dm channel
    async def edit_channel_permissions(): pass
    async def get_channel_invites(): pass
    async def create_channel_invite(): pass
    async def delete_channel_permission(): pass
    async def follow_announcement_channel(): pass
    async def trigger_typing_indicator(): pass
    async def get_pinned_messages(): pass
    async def pin_message(): pass
    async def unpin_message(): pass
    async def group_dm_add_recipient(): pass
    async def group_dm_remove_recipient(): pass
    async def start_thread_from_message(): pass
    async def start_thread_without_message(): pass
    async def start_thread_in_forum_or_media_channel(): pass
    async def join_thread(): pass
    async def add_thread_member(): pass
    async def leave_thread(): pass
    async def remove_thread_member(): pass
    async def get_thread_member(): pass
    async def list_thread_member(): pass
    async def list_public_archived_threads(): pass
    async def list_private_archived_threads(): pass
    async def list_joined_private_threads(): pass
    
    # Emoji Resource
    # https://discord.com/developers/docs/resources/emoji#emoji-resource

    async def list_guild_emojis(): pass
    async def get_guild_emoji(): pass
    async def create_guild_emoji(): pass
    async def modify_guild_emoji(): pass
    async def delete_guild_emoji(): pass
    async def list_application_emojis(): pass
    async def get_application_emoji(): pass
    async def create_application_emoji(): pass
    async def modify_application_emoji(): pass
    
    # Entitlements Resource
    # https://discord.com/developers/docs/resources/entitlement#entitlements-resource

    async def list_entitlements(): pass
    async def get_entitlement(): pass
    async def consume_entitlement(): pass
    async def create_test_entitlement(): pass
    async def delete_test_entitlement(): pass

    # Guild Scheduled Event
    # https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event

    async def list_scheduled_events_for_guild(): pass
    async def create_guild_scheduled_event(): pass
    async def get_guild_scheduled_event(): pass
    async def modify_guild_scheduled_event(): pass
    async def delete_guild_scheduled_event(): pass
    async def get_guild_scheduled_event_users(): pass

    # Guild Template Resource
    # https://discord.com/developers/docs/resources/guild-template#guild-template-resource

    async def get_guild_template(): pass
    async def create_guild_from_guild_template(): pass
    async def get_guild_templates(): pass
    async def create_guild_template(): pass
    async def sync_guild_template(): pass
    async def modify_guild_template(): pass
    async def delete_guild_template(): pass

    # Guild Resource
    # https://discord.com/developers/docs/resources/guild#guild-resource

    async def create_guild(): pass
    async def get_guild(): pass
    async def get_guild_preview(): pass
    async def modify_guild(): pass
    async def delete_guild(): pass
    async def get_guild_channels(): pass
    async def create_guild_channel(): pass
    async def modify_guild_channel_positions(): pass
    async def list_active_guild_threads(): pass
    async def get_guild_member(): pass
    async def list_guild_members(): pass
    async def search_guild_members(): pass
    async def add_guild_member(): pass
    async def modify_guild_member(): pass
    async def modify_current_member(): pass
    async def modify_current_user_nick(): pass
    async def add_guild_member_role(): pass
    async def remove_guild_member_role(): pass
    async def remove_guild_member(): pass
    async def get_guild_bans(): pass
    async def get_guild_ban(): pass
    async def create_guild_ban(): pass
    async def remove_guild_ban(): pass
    async def bulk_guild_ban(): pass
    async def get_guild_roles(): pass
    async def get_guild_role(): pass
    async def create_guild_role(): pass
    async def modify_guild_role_positions(): pass
    async def modify_guild_role(): pass
    async def modify_guild_mfa_level(): pass
    async def delete_guild_role(): pass
    async def get_guild_prune_count(): pass
    async def begin_guild_prune(): pass
    async def get_guild_voice_regions(): pass
    async def get_guild_invites(): pass
    async def get_guild_integrations(): pass
    async def delete_guild_integration(): pass
    async def get_guild_widget_settings(): pass
    async def modify_guild_widget(): pass
    async def get_guild_widget(): pass
    async def get_guild_vanity_url(): pass
    async def get_guild_widget_image(): pass
    async def get_guild_welcome_screen(): pass
    async def modify_guild_welcome_screen(): pass
    async def get_guild_onboarding(): pass
    async def modify_guild_onboarding(): pass
    async def modify_guild_incident_actions(): pass

    # Invite Resource
    # https://discord.com/developers/docs/resources/invite#invite-resource

    async def get_invite(): pass
    async def delete_invite(): pass

    # Lobby Resource
    # https://discord.com/developers/docs/resources/lobby#lobby-resource

    async def create_lobby(): pass
    async def get_lobby(): pass
    async def modify_lobby(): pass
    async def delete_lobby(): pass
    async def add_a_member_to_a_lobby(): pass
    async def remove_a_member_from_a_lobby(): pass
    async def leave_lobby(): pass
    async def link_channel_to_lobby(): pass
    async def unlink_channel_from_lobby(): pass

    # Messages Resource
    # https://discord.com/developers/docs/resources/channel#message-resource

    async def get_channel_messages(): pass
    async def get_channel_message(): pass
    async def create_message(): pass
    async def crosspost_message(): pass
    async def create_reaction(): pass
    async def delete_own_reaction(): pass
    async def delete_user_reaction(): pass
    async def get_reactions(): pass
    async def delete_all_reactions(): pass
    async def delete_all_reactions_for_emoji(): pass
    async def edit_message(): pass
    async def delete_message(): pass
    async def bulk_delete_messages(): pass

    # Poll Resource
    # https://discord.com/developers/docs/resources/poll#poll-resource

    async def get_answer_voters(): pass
    async def end_poll(): pass

    # SKU Resource
    # https://discord.com/developers/docs/resources/sku#sku-resource

    async def list_skus(): pass

    # Soundboard Resource
    # https://discord.com/developers/docs/resources/soundboard#soundboard-resource

    async def send_soundboard_sound(): pass
    async def list_default_soundboard_sounds(): pass
    async def list_guild_soundboard_sounds(): pass
    async def get_guild_soundboard_sound(): pass
    async def create_guild_soundboard_sound(): pass
    async def modify_guild_soundboard_sound(): pass
    async def delete_guild_soundboard_sound(): pass

    # Stage Instance Resource
    # https://discord.com/developers/docs/resources/stage-instance#stage-instance-resource

    async def create_stage_instance(): pass
    async def get_stage_instance(): pass
    async def modify_stage_instance(): pass
    async def delete_stage_instance(): pass

    # Sticker Resource
    # https://discord.com/developers/docs/resources/sticker#sticker-resource

    async def get_sticker(): pass
    async def list_sticker_packs(): pass
    async def get_sticker_pack(): pass
    async def list_guild_stickers(): pass
    async def get_guild_sticker(): pass
    async def create_guild_sticker(): pass
    async def modify_guild_sticker(): pass
    async def delete_guild_sticker(): pass

    # Subscription Resource
    # https://discord.com/developers/docs/resources/subscription#subscription-resource

    async def list_sku_subscriptions(): pass
    async def get_sku_subscription(): pass

    # Users Resource
    # https://discord.com/developers/docs/resources/user#user-resource

    async def get_current_user(): pass
    async def get_user(): pass
    async def modify_current_user(): pass
    async def get_current_user_guilds(): pass
    async def get_current_user_guild_member(): pass
    async def leave_guild(): pass
    async def create_dm(): pass
    async def create_group_dm(): pass
    async def get_current_user_connections(): pass
    async def get_current_user_application_role_connection(): pass
    async def update_current_user_application_role_connection(): pass

    # Voice Resource
    # https://discord.com/developers/docs/resources/voice#voice-resource

    async def list_voice_regions(): pass
    async def get_current_user_voice_state(): pass
    async def get_user_voice_state(): pass
    async def modify_current_user_voice_state(): pass
    async def modify_user_voice_state(): pass

    # Webhook Resource
    # https://discord.com/developers/docs/resources/webhook#webhook-resource

    async def create_webhook(): pass
    async def get_channel_webhooks(): pass
    async def get_guild_webhooks(): pass
    async def get_webhook(): pass
    async def get_webhook_with_token(): pass
    async def modify_webhook(): pass
    async def modify_webhook_with_token(): pass
    async def delete_webhook(): pass
    async def delete_webhook_with_token(): pass
    async def execute_webhook(): pass
    async def execute_slack_compatible_webhook(): pass
    async def execute_github_compatible_webhook(): pass
    async def get_webhook_message(): pass
    async def edit_webhook_message(): pass
    async def delete_webhook_message(): pass

    # todo

    async def sync_global_commands(
        self, application_id: str, commands: List[Dict[str, Any]]
    ):
        return await self.request(
            "PUT",
            f"/applications/{application_id}/commands",
            body=commands,
            authorize=True,
        )

    async def sync_guild_commands(
        self, application_id: str, guild_id: str, commands: List[Dict[str, Any]]
    ):
        return await self.request(
            "PUT",
            f"/applications/{application_id}/guilds/{guild_id}/commands",
            body=commands,
            authorize=True,
        )

    async def fetch_global_application_commands(self, application_id: str):
        return await self.request(
            "GET", f"/applications/{application_id}/commands", authorize=True
        )

    async def edit_client(self, payload: Dict[str, Any]):
        return await self.request("PATCH", "/users/@me", body=payload, authorize=True)

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

    async def send_message(self, channel_id: str, data: Any):
        return await self.request(
            "POST", f"/channels/{channel_id}/messages", body=data, authorize=True
        )

    async def create_dm_channel(self, payload: Dict[str, Any]):
        return await self.request(
            "POST", "/users/@me/channels", body=payload, authorize=True
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
            body=payload,
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

    async def edit_channel_message(self, channel_id: str, message_id: str, data: Any):
        return await self.request(
            "PATCH",
            f"/channels/{channel_id}/messages/{message_id}",
            body=data,
            authorize=True,
        )

    async def send_webhook_message(
        self, webhook_id: str, webhook_token: str, form: aiohttp.MultipartWriter
    ):
        return await self.request(
            "POST", f"/webhooks/{webhook_id}/{webhook_token}", body=form
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
        data: Any,
    ):
        return await self.request(
            "PATCH",
            f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}",
            body=data,
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
            body={"delete_message_seconds": delete_message_seconds},
        )

    async def send_interaction_callback(
        self, interaction_id: str, interaction_token: str, data: Any
    ):
        return await self.request(
            "POST",
            f"/interactions/{interaction_id}/{interaction_token}/callback",
            body=data,
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
            "POST", f"/guilds/{guild_id}/channels", body=payload, authorize=True
        )

    async def crosspost_channel_message(self, channel_id: str, message_id: str):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages/{message_id}/crosspost",
            authorize=True,
        )

    async def edit_channel(self, channel_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/channels/{channel_id}", body=payload, authorize=True
        )

    async def edit_guild_channel_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/guilds/{guild_id}/channels", body=payload, authorize=True
        )

    async def create_guild_role(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/guilds/{guild_id}/roles", body=payload, authorize=True
        )

    async def edit_guild_role_position(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/guilds/{guild_id}/roles", body=payload, authorize=True
        )

    async def edit_guild_role(
        self, guild_id: str, role_id: str, payload: Dict[str, Any]
    ):
        return await self.request(
            "PATCH", f"/guilds/{guild_id}/roles/{role_id}", body=payload, authorize=True
        )

    async def create_guild_emoji(self, guild_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/guilds/{guild_id}/emojis", body=payload, authorize=True
        )

    async def create_webhook(self, channel_id: str, payload: Dict[str, Any]):
        return await self.request(
            "POST", f"/channels/{channel_id}/webhooks", body=payload, authorize=True
        )

    async def execute_webhook(
        self,
        webhook_id: str,
        webhook_token: str,
        data: Any,
        params: Dict[str, Any],
    ):
        return await self.request(
            "POST", f"/webhooks/{webhook_id}/{webhook_token}", body=data, params=params
        )

    async def edit_webhook(self, webhook_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH", f"/webhooks/{webhook_id}", body=payload, authorize=True
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
            body=payload,
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
            body=payload,
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
            body=payload,
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

    async def fetch_application_emojis(self):
        return await self.request(
            "GET",
            f"/applications/{self.application_id}/emojis",
            authorize=True,
        )

    async def fetch_application_emoji(self, emoji_id: str):
        return await self.request(
            "GET",
            f"/applications/{self.application_id}/emojis/{emoji_id}",
            authorize=True,
        )

    async def create_application_emoji(self, payload: Dict[str, Any]):
        return await self.request(
            "POST",
            f"/applications/{self.application_id}/emojis",
            body=payload,
            authorize=True,
        )

    async def edit_application_emoji(self, emoji_id: str, payload: Dict[str, Any]):
        return await self.request(
            "PATCH",
            f"/applications/{self.application_id}/emojis/{emoji_id}",
            body=payload,
            authorize=True,
        )

    async def delete_application_emoji(self, emoji_id: str):
        return await self.request(
            "DELETE",
            f"/applications/{self.application_id}/emojis/{emoji_id}",
            authorize=True,
        )

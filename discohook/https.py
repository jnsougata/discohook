import json
from typing import Any, Dict, List, Optional, Union

import aiohttp

from . import __url__, __version__
from .errors import HTTPException


class HTTPClient:
    """Represents an HTTP client for Discord's API."""

    DISCORD_API_VERSION: int = 10
    USER_AGENT: str = f"DiscordBot ({__url__}, {__version__})"

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
        authorize: bool = False,
        reason: Optional[str] = None,
        **params: Any
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

    async def create_interaction_response(
        self,
        interaction_id: str,
        interaction_token: str,
        data: Any,
        with_response: bool = False,
    ):
        return await self.request(
            "POST",
            f"/interactions/{interaction_id}/{interaction_token}/callback",
            body=data,
            with_response=str(with_response),
        )

    async def get_original_interaction_response(self, webhook_id: str, webhook_token: str):
        return await self.get_webhook_message(webhook_id, webhook_token, "@original")

    async def edit_original_interaction_response(self): pass # edit_webhook_message(self), message_id as @original
    async def delete_original_interaction_response(self): pass # delete_webhook_message(self), message_id as @original + no thread_id param
    async def create_followup_message(self): pass # execute_webhook(self)
    async def get_followup_message(self): pass # get_webhook_message(self)
    async def edit_followup_message(self): pass # edit_webhook_message(self)
    async def delete_followup_message(self): pass # delete_webhook_message(self)

    # Application Commands
    # https://discord.com/developers/docs/interactions/application-commands#application-commands

    async def get_global_application_commands(
            self,
            application_id: str,
            *,
            with_localizations: bool = False
    ):
        return await self.request(
            "GET",
            f"/applications/{application_id}/commands",
            authorize=True,
            with_localizations=with_localizations
        )

    async def create_global_application_command(self): pass
    async def get_global_application_command(self): pass
    async def edit_global_application_command(self): pass
    async def delete_global_application_command(self): pass

    async def delete_application_command(
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

    async def bulk_overwrite_global_application_commands(
        self,
        application_id: str,
        commands: List[Dict[str, Any]]
    ):
        return await self.request(
            "PUT",
            f"/applications/{application_id}/commands",
            body=commands,
            authorize=True,
        )

    async def get_guild_application_commands(self): pass
    async def create_guild_application_command(self): pass
    async def get_guild_application_command(self): pass
    async def edit_guild_application_command(self): pass
    async def delete_guild_application_command(self): pass

    async def bulk_overwrite_guild_application_commands(
        self,
        application_id: str,
        guild_id: str,
        commands: List[Dict[str, Any]]
    ):
        return await self.request(
            "PUT",
            f"/applications/{application_id}/guilds/{guild_id}/commands",
            body=commands,
            authorize=True,
        )

    async def get_guild_application_command_permissions(self): pass
    async def get_application_command_permissions(self): pass
    async def edit_application_command_permissions(self): pass

    # Application Role Connection Metadata
    # https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata

    async def get_application_role_connection_metadata_records(self): pass
    async def update_application_role_connection_metadata_records(self): pass

    # Application Resource
    # https://discord.com/developers/docs/resources/application#application-resource

    async def get_current_application(self):
        return await self.request("GET", "/applications/@me", authorize=True)

    async def edit_current_application(self): pass
    async def get_application_activity_instance(self): pass

    # Audit Logs Resource
    # https://discord.com/developers/docs/resources/audit-log#audit-logs-resource

    async def get_audit_log(self): pass

    # Auto Moderation
    # https://discord.com/developers/docs/resources/auto-moderation#auto-moderation

    async def list_auto_moderation_rules_for_guild(self): pass
    async def get_auto_moderation_rule(self): pass
    async def create_auto_moderation_rule(self): pass
    async def modify_auto_moderation_rule(self): pass
    async def delete_auto_moderation_rule(self): pass

    # Channels Resource
    # https://discord.com/developers/docs/resources/channel#channels-resource

    async def get_channel(self, channel_id: str):
        return await self.request("GET", f"/channels/{channel_id}", authorize=True)

    async def modify_channel(
        self,
        channel_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "PATCH",
            f"/channels/{channel_id}",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def delete_or_close_channel(
        self,
        channel_id: str,
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "DELETE",
            f"/channels/{channel_id}",
            authorize=True,
            reason=reason
        )

    async def edit_channel_permissions(self): pass
    async def get_channel_invites(self): pass
    async def create_channel_invite(self): pass
    async def delete_channel_permission(self): pass
    async def follow_announcement_channel(self): pass
    async def trigger_typing_indicator(self): pass
    async def get_pinned_messages(self): pass

    async def pin_message(
        self,
        channel_id: str,
        message_id: str,
        *,
        reason: Optional[str] = None
    ):
        await self.request(
            "PUT",
            f"/channels/{channel_id}/messages/{message_id}/pin",
            authorize=True,
            reason=reason
        )

    async def unpin_message(
        self,
        channel_id: str,
        message_id: str,
        *,
        reason: Optional[str] = None
    ):
        await self.request(
            "DELETE",
            f"/channels/{channel_id}/messages/{message_id}/pin",
            authorize=True,
            reason=reason
        )

    async def group_dm_add_recipient(self): pass
    async def group_dm_remove_recipient(self): pass

    async def start_thread_from_message(
        self,
        channel_id: str,
        message_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None,
    ):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages/{message_id}/threads",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def start_thread_without_message(
        self, 
        channel_id: str, 
        payload: Dict[str, Any], 
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/threads",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def start_thread_in_forum_or_media_channel(self): pass
    async def join_thread(self): pass
    async def add_thread_member(self): pass
    async def leave_thread(self): pass
    async def remove_thread_member(self): pass
    async def get_thread_member(self): pass
    async def list_thread_member(self): pass
    async def list_public_archived_threads(self): pass
    async def list_private_archived_threads(self): pass
    async def list_joined_private_threads(self): pass
    
    # Emoji Resource
    # https://discord.com/developers/docs/resources/emoji#emoji-resource

    async def list_guild_emojis(self): pass
    async def get_guild_emoji(self): pass

    async def create_guild_emoji(
        self, 
        guild_id: str, 
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "POST", 
            f"/guilds/{guild_id}/emojis", 
            body=payload, 
            authorize=True,
            reason=reason
        )

    async def modify_guild_emoji(self): pass
    async def delete_guild_emoji(self): pass

    async def list_application_emojis(self):
        return await self.request(
            "GET",
            f"/applications/{self.application_id}/emojis",
            authorize=True,
        )

    async def get_application_emoji(self, emoji_id: str):
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

    async def modify_application_emoji(self, emoji_id: str, name: str):
        return await self.request(
            "PATCH",
            f"/applications/{self.application_id}/emojis/{emoji_id}",
            body={"name": name},
            authorize=True,
        )
    
    async def delete_application_emoji(self, emoji_id: str):
        return await self.request(
            "DELETE",
            f"/applications/{self.application_id}/emojis/{emoji_id}",
            authorize=True,
        )
    
    # Entitlements Resource
    # https://discord.com/developers/docs/resources/entitlement#entitlements-resource

    async def list_entitlements(self, application_id: str, **params):
        return await self.request(
            "GET",
            f"/applications/{application_id}/entitlements",
            authorize=True,
            **params
        )

    async def get_entitlement(self, application_id: str, entitlement_id: str):
        return await self.request(
            "GET",
            f"/applications/{application_id}/entitlements/{entitlement_id}",
            authorize=True,
        )

    async def consume_entitlement(self): pass    
    
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

    # Guild Scheduled Event
    # https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event

    async def list_scheduled_events_for_guild(self): pass
    async def create_guild_scheduled_event(self): pass
    async def get_guild_scheduled_event(self): pass
    async def modify_guild_scheduled_event(self): pass
    async def delete_guild_scheduled_event(self): pass
    async def get_guild_scheduled_event_users(self): pass

    # Guild Template Resource
    # https://discord.com/developers/docs/resources/guild-template#guild-template-resource

    async def get_guild_template(self): pass
    async def create_guild_from_guild_template(self): pass
    async def get_guild_templates(self): pass
    async def create_guild_template(self): pass
    async def sync_guild_template(self): pass
    async def modify_guild_template(self): pass
    async def delete_guild_template(self): pass

    # Guild Resource
    # https://discord.com/developers/docs/resources/guild#guild-resource

    async def create_guild(self): pass

    async def get_guild(self, guild_id: str, with_counts: Optional[str] = False):
        return await self.request(
            "GET", f"/guilds/{guild_id}", authorize=True, with_counts=with_counts
        )
    
    async def get_guild_preview(self): pass
    async def modify_guild(self): pass
    async def delete_guild(self): pass

    async def get_guild_channels(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/channels", authorize=True)

    async def create_guild_channel(
        self,
        guild_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "POST",
            f"/guilds/{guild_id}/channels",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def modify_guild_channel_positions(
        self,
        guild_id: str,
        payload: Dict[str, Any]
    ):
        return await self.request(
            "PATCH",
            f"/guilds/{guild_id}/channels",
            body=payload,
            authorize=True
        )

    async def list_active_guild_threads(self): pass

    async def get_guild_member(self, guild_id: str, user_id: str):
        return await self.request(
            "GET",
            f"/guilds/{guild_id}/members/{user_id}",
            authorize=True
        )

    async def list_guild_members(self): pass
    async def search_guild_members(self): pass
    async def add_guild_member(self): pass
    async def modify_guild_member(self): pass
    async def modify_current_member(self): pass
    async def modify_current_user_nick(self): pass

    async def add_guild_member_role(
        self,
        guild_id: str,
        user_id: str,
        role_id: str,
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "PUT",
            f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}",
            authorize=True,
            reason=reason
        )

    async def remove_guild_member_role(
        self,
        guild_id: str,
        user_id: str,
        role_id: str,
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "DELETE",
            f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}",
            authorize=True,
            reason=reason
        )

    async def remove_guild_member(
        self,
        guild_id: str,
        user_id: str,
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "DELETE",
            f"/guilds/{guild_id}/members/{user_id}",
            authorize=True,
            reason=reason
        )

    async def get_guild_bans(self): pass
    async def get_guild_ban(self): pass

    async def create_guild_ban(
        self,
        guild_id: str,
        user_id: str,
        delete_message_seconds: int = 0,
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "PUT",
            f"/guilds/{guild_id}/bans/{user_id}",
            authorize=True,
            body={"delete_message_seconds": delete_message_seconds},
            reason=reason
        )

    async def remove_guild_ban(self): pass
    async def bulk_guild_ban(self): pass

    async def get_guild_roles(self, guild_id: str):
        return await self.request("GET", f"/guilds/{guild_id}/roles", authorize=True)

    async def get_guild_role(self): pass

    async def create_guild_role(
        self,
        guild_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "POST",
            f"/guilds/{guild_id}/roles",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def modify_guild_role_positions(
        self,
        guild_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "PATCH",
            f"/guilds/{guild_id}/roles",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def modify_guild_role(
        self,
        guild_id: str,
        role_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "PATCH",
            f"/guilds/{guild_id}/roles/{role_id}",
            body=payload,
            authorize=True,
            reason=reason
        )

    async def modify_guild_mfa_level(self): pass
    async def delete_guild_role(self): pass
    async def get_guild_prune_count(self): pass
    async def begin_guild_prune(self): pass
    async def get_guild_voice_regions(self): pass
    async def get_guild_invites(self): pass
    async def get_guild_integrations(self): pass
    async def delete_guild_integration(self): pass
    async def get_guild_widget_settings(self): pass
    async def modify_guild_widget(self): pass
    async def get_guild_widget(self): pass
    async def get_guild_vanity_url(self): pass
    async def get_guild_widget_image(self): pass
    async def get_guild_welcome_screen(self): pass
    async def modify_guild_welcome_screen(self): pass
    async def get_guild_onboarding(self): pass
    async def modify_guild_onboarding(self): pass
    async def modify_guild_incident_actions(self): pass

    # Invite Resource
    # https://discord.com/developers/docs/resources/invite#invite-resource

    async def get_invite(self): pass
    async def delete_invite(self): pass

    # Lobby Resource
    # https://discord.com/developers/docs/resources/lobby#lobby-resource

    async def create_lobby(self): pass
    async def get_lobby(self): pass
    async def modify_lobby(self): pass
    async def delete_lobby(self): pass
    async def add_a_member_to_a_lobby(self): pass
    async def remove_a_member_from_a_lobby(self): pass
    async def leave_lobby(self): pass
    async def link_channel_to_lobby(self): pass
    async def unlink_channel_from_lobby(self): pass

    # Messages Resource
    # https://discord.com/developers/docs/resources/channel#message-resource

    async def get_channel_messages(self, channel_id: str, **params):
        return await self.request(
            "GET", 
            f"/channels/{channel_id}/messages", 
            authorize=True,
            **params
        )

    async def get_channel_message(self, channel_id: str, message_id: str):
        return await self.request(
            "GET",
            f"/channels/{channel_id}/messages/{message_id}",
            authorize=True
        )

    async def create_message(self, channel_id: str, data: Any):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages",
            body=data,
            authorize=True
        )

    async def crosspost_message(self, channel_id: str, message_id: str):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages/{message_id}/crosspost",
            authorize=True,
        )

    async def create_reaction(
        self, channel_id: str, message_id: str, emoji: str
    ):
        return await self.request(
            "PUT",
            f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
            authorize=True,
        )

    async def delete_own_reaction(self, message_id: str, emoji: str):
        return await self.delete_user_reaction(message_id, emoji, '@me')

    async def delete_user_reaction(self, message_id: str, emoji: str, user_id: str):
        return await self.request(
            "DELETE",
            f"/channels/{message_id}/messages/{message_id}/reactions/{emoji}/{user_id}",
            authorize=True
        )

    async def get_reactions(self): pass
    async def delete_all_reactions(self): pass
    async def delete_all_reactions_for_emoji(self): pass

    async def edit_message(self, channel_id: str, message_id: str, data: Any):
        return await self.request(
            "PATCH",
            f"/channels/{channel_id}/messages/{message_id}",
            body=data,
            authorize=True,
        )

    async def delete_message(
        self,
        channel_id: str,
        message_id: str,
        *,
        reason: Optional[str] = None
    ):
        await self.request(
            "DELETE",
            f"/channels/{channel_id}/messages/{message_id}",
            authorize=True,
            reason=reason
        )

    async def bulk_delete_messages(
        self,
        channel_id: str,
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        await self.request(
            "POST",
            f"/channels/{channel_id}/messages/bulk-delete",
            body=payload,
            authorize=True,
            reason=reason
        )

    # Poll Resource
    # https://discord.com/developers/docs/resources/poll#poll-resource

    async def get_answer_voters(self): pass

    async def end_poll(self, channel_id: str, message_id: str):
        return await self.request(
            "POST", f"/channels/{channel_id}/polls/{message_id}/expire", authorize=True
        )

    # SKU Resource
    # https://discord.com/developers/docs/resources/sku#sku-resource

    async def list_skus(self, application_id: str):
        return await self.request(
            "GET", f"/applications/{application_id}/skus", authorize=True
        )

    # Soundboard Resource
    # https://discord.com/developers/docs/resources/soundboard#soundboard-resource

    async def send_soundboard_sound(self): pass
    async def list_default_soundboard_sounds(self): pass
    async def list_guild_soundboard_sounds(self): pass
    async def get_guild_soundboard_sound(self): pass
    async def create_guild_soundboard_sound(self): pass
    async def modify_guild_soundboard_sound(self): pass
    async def delete_guild_soundboard_sound(self): pass

    # Stage Instance Resource
    # https://discord.com/developers/docs/resources/stage-instance#stage-instance-resource

    async def create_stage_instance(self): pass
    async def get_stage_instance(self): pass
    async def modify_stage_instance(self): pass
    async def delete_stage_instance(self): pass

    # Sticker Resource
    # https://discord.com/developers/docs/resources/sticker#sticker-resource

    async def get_sticker(self): pass
    async def list_sticker_packs(self): pass
    async def get_sticker_pack(self): pass
    async def list_guild_stickers(self): pass
    async def get_guild_sticker(self): pass
    async def create_guild_sticker(self): pass
    async def modify_guild_sticker(self): pass
    async def delete_guild_sticker(self): pass

    # Subscription Resource
    # https://discord.com/developers/docs/resources/subscription#subscription-resource

    async def list_sku_subscriptions(self): pass
    async def get_sku_subscription(self): pass

    # Users Resource
    # https://discord.com/developers/docs/resources/user#user-resource

    async def get_current_user(self): pass

    async def get_user(self, user_id: str):
        return await self.request("GET", f"/users/{user_id}", authorize=True)
    
    async def modify_current_user(self, payload: Dict[str, Any]):
        return await self.request("PATCH", "/users/@me", body=payload, authorize=True)

    async def get_current_user_guilds(self): pass
    async def get_current_user_guild_member(self): pass
    async def leave_guild(self): pass

    async def create_dm(self, payload: Dict[str, Any]):
        return await self.request(
            "POST",
            "/users/@me/channels",
            body=payload,
            authorize=True
        )

    async def create_group_dm(self): pass
    async def get_current_user_connections(self): pass
    async def get_current_user_application_role_connection(self): pass
    async def update_current_user_application_role_connection(self): pass

    # Voice Resource
    # https://discord.com/developers/docs/resources/voice#voice-resource

    async def list_voice_regions(self): pass
    async def get_current_user_voice_state(self): pass
    async def get_user_voice_state(self): pass
    async def modify_current_user_voice_state(self): pass
    async def modify_user_voice_state(self): pass

    # Webhook Resource
    # https://discord.com/developers/docs/resources/webhook#webhook-resource

    async def create_webhook(
        self, 
        channel_id: str, 
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "POST", 
            f"/channels/{channel_id}/webhooks", 
            body=payload, 
            authorize=True,
            reason=reason
        )

    async def get_channel_webhooks(self): pass
    async def get_guild_webhooks(self): pass

    async def get_webhook(self, webhook_id: str):
        return await self.request("GET", f"/webhooks/{webhook_id}", authorize=True)

    async def get_webhook_with_token(webhook_id: str, webhook_token: str):
        return await self.request("GET", f"/webhooks/{webhook_id}/{webhook_token}")

    async def modify_webhook(
        self, 
        webhook_id: str, 
        payload: Dict[str, Any],
        *,
        reason: Optional[str] = None
    ):
        return await self.request(
            "PATCH", 
            f"/webhooks/{webhook_id}", 
            body=payload, 
            authorize=True,
            reason=reason
        )

    async def modify_webhook_with_token(self): pass

    async def delete_webhook(self, webhook_id: str, *, reason: Optional[str] = None):
        return await self.request(
            "DELETE", 
            f"/webhooks/{webhook_id}", 
            authorize=True,
            reason=reason
        )

    async def delete_webhook_with_token(self): pass

    async def execute_webhook(
            self,
            webhook_id: str,
            webhook_token: str,
            data: Any,
            **params: Any,
    ):
        return await self.request(
            "POST", f"/webhooks/{webhook_id}/{webhook_token}", body=data, **params
        )

    async def execute_slack_compatible_webhook(self): pass
    async def execute_github_compatible_webhook(self): pass

    async def get_webhook_message(
        self,
        webhook_id: str,
        webhook_token: str,
        message_id: str,
        **params
    ):
        return await self.request(
            "GET", 
            f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}", 
            **params
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

    async def delete_webhook_message(
            self, webhook_id: str, webhook_token: str, message_id: str
    ):
        await self.request(
            "DELETE", f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}"
        )

    # TODO

    async def delete_all_message_reactions(
        self, message_id: str, emoji: Optional[str] = None
    ):
        path = f"/channels/{message_id}/messages/{message_id}/reactions"
        if emoji:
            path += f"/{emoji}"
        return await self.request("DELETE", path, authorize=True)

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
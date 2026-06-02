---
title: discohook.https
---

# `discohook.https`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/https.py`

## Classes

- [HTTPClient](#class-httpclient)

## Class `HTTPClient`

Represents an HTTP client for Discord's API.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/https.py`
- Line: `11`

### Methods

#### `add_a_member_to_a_lobby`

```python
add_a_member_to_a_lobby(self)
```

#### `add_guild_member`

```python
add_guild_member(self)
```

#### `add_guild_member_role`

```python
add_guild_member_role(self, guild_id: str, user_id: str, role_id: str, *, reason: str | None = None)
```

#### `add_thread_member`

```python
add_thread_member(self)
```

#### `begin_guild_prune`

```python
begin_guild_prune(self)
```

#### `bulk_delete_messages`

```python
bulk_delete_messages(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `bulk_guild_ban`

```python
bulk_guild_ban(self)
```

#### `bulk_overwrite_global_application_commands`

```python
bulk_overwrite_global_application_commands(self, application_id: str, commands: List[Dict[str, Any]])
```

#### `bulk_overwrite_guild_application_commands`

```python
bulk_overwrite_guild_application_commands(self, application_id: str, guild_id: str, commands: List[Dict[str, Any]])
```

#### `consume_entitlement`

```python
consume_entitlement(self)
```

#### `create_application_emoji`

```python
create_application_emoji(self, payload: Dict[str, Any])
```

#### `create_auto_moderation_rule`

```python
create_auto_moderation_rule(self)
```

#### `create_channel_invite`

```python
create_channel_invite(self)
```

#### `create_dm`

```python
create_dm(self, payload: Dict[str, Any])
```

#### `create_followup_message`

```python
create_followup_message(self)
```

#### `create_global_application_command`

```python
create_global_application_command(self)
```

#### `create_group_dm`

```python
create_group_dm(self)
```

#### `create_guild`

```python
create_guild(self)
```

#### `create_guild_application_command`

```python
create_guild_application_command(self)
```

#### `create_guild_ban`

```python
create_guild_ban(self, guild_id: str, user_id: str, delete_message_seconds: int = 0, *, reason: str | None = None)
```

#### `create_guild_channel`

```python
create_guild_channel(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `create_guild_emoji`

```python
create_guild_emoji(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `create_guild_from_guild_template`

```python
create_guild_from_guild_template(self)
```

#### `create_guild_role`

```python
create_guild_role(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `create_guild_scheduled_event`

```python
create_guild_scheduled_event(self)
```

#### `create_guild_soundboard_sound`

```python
create_guild_soundboard_sound(self)
```

#### `create_guild_sticker`

```python
create_guild_sticker(self)
```

#### `create_guild_template`

```python
create_guild_template(self)
```

#### `create_interaction_response`

```python
create_interaction_response(self, interaction_id: str, interaction_token: str, data: Any, with_response: bool = False)
```

#### `create_lobby`

```python
create_lobby(self)
```

#### `create_message`

```python
create_message(self, channel_id: str, data: Any)
```

#### `create_reaction`

```python
create_reaction(self, channel_id: str, message_id: str, emoji: str)
```

#### `create_stage_instance`

```python
create_stage_instance(self)
```

#### `create_test_entitlement`

```python
create_test_entitlement(self, application_id: str, payload: Dict[str, Any])
```

#### `create_webhook`

```python
create_webhook(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `crosspost_message`

```python
crosspost_message(self, channel_id: str, message_id: str)
```

#### `delete_all_message_reactions`

```python
delete_all_message_reactions(self, message_id: str, emoji: str | None = None)
```

#### `delete_all_reactions`

```python
delete_all_reactions(self)
```

#### `delete_all_reactions_for_emoji`

```python
delete_all_reactions_for_emoji(self)
```

#### `delete_application_command`

```python
delete_application_command(self, application_id: str, command_id: str, guild_id: str | None = None)
```

#### `delete_application_emoji`

```python
delete_application_emoji(self, emoji_id: str)
```

#### `delete_auto_moderation_rule`

```python
delete_auto_moderation_rule(self)
```

#### `delete_channel_permission`

```python
delete_channel_permission(self)
```

#### `delete_followup_message`

```python
delete_followup_message(self)
```

#### `delete_global_application_command`

```python
delete_global_application_command(self)
```

#### `delete_guild`

```python
delete_guild(self)
```

#### `delete_guild_application_command`

```python
delete_guild_application_command(self)
```

#### `delete_guild_emoji`

```python
delete_guild_emoji(self)
```

#### `delete_guild_integration`

```python
delete_guild_integration(self)
```

#### `delete_guild_role`

```python
delete_guild_role(self)
```

#### `delete_guild_scheduled_event`

```python
delete_guild_scheduled_event(self)
```

#### `delete_guild_soundboard_sound`

```python
delete_guild_soundboard_sound(self)
```

#### `delete_guild_sticker`

```python
delete_guild_sticker(self)
```

#### `delete_guild_template`

```python
delete_guild_template(self)
```

#### `delete_invite`

```python
delete_invite(self)
```

#### `delete_lobby`

```python
delete_lobby(self)
```

#### `delete_message`

```python
delete_message(self, channel_id: str, message_id: str, *, reason: str | None = None)
```

#### `delete_message_reaction`

```python
delete_message_reaction(self, message_id: str, emoji: str, user_id: str)
```

#### `delete_or_close_channel`

```python
delete_or_close_channel(self, channel_id: str, *, reason: str | None = None)
```

#### `delete_original_interaction_response`

```python
delete_original_interaction_response(self)
```

#### `delete_own_reaction`

```python
delete_own_reaction(self)
```

#### `delete_stage_instance`

```python
delete_stage_instance(self)
```

#### `delete_test_entitlement`

```python
delete_test_entitlement(self, application_id: str, entitlement_id: str)
```

#### `delete_user_reaction`

```python
delete_user_reaction(self)
```

#### `delete_webhook`

```python
delete_webhook(self, webhook_id: str, *, reason: str | None = None)
```

#### `delete_webhook_message`

```python
delete_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str)
```

#### `delete_webhook_with_token`

```python
delete_webhook_with_token(self)
```

#### `edit_application_command_permissions`

```python
edit_application_command_permissions(self)
```

#### `edit_channel_permissions`

```python
edit_channel_permissions(self)
```

#### `edit_current_application`

```python
edit_current_application(self)
```

#### `edit_followup_message`

```python
edit_followup_message(self)
```

#### `edit_global_application_command`

```python
edit_global_application_command(self)
```

#### `edit_guild_application_command`

```python
edit_guild_application_command(self)
```

#### `edit_message`

```python
edit_message(self, channel_id: str, message_id: str, data: Any)
```

#### `edit_original_interaction_response`

```python
edit_original_interaction_response(self)
```

#### `edit_webhook_message`

```python
edit_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str, data: Any, **params: Any)
```

#### `end_poll`

```python
end_poll(self, channel_id: str, message_id: str)
```

#### `execute_github_compatible_webhook`

```python
execute_github_compatible_webhook(self)
```

#### `execute_slack_compatible_webhook`

```python
execute_slack_compatible_webhook(self)
```

#### `execute_webhook`

```python
execute_webhook(self, webhook_id: str, webhook_token: str, data: Any, **params: Any)
```

#### `fetch_answer_voters`

```python
fetch_answer_voters(self, *, channel_id: str, message_id: str, answer_id: int, params: Dict[str, Any] = None)
```

#### `fetch_channel_messages`

```python
fetch_channel_messages(self, channel_id: str, params: Dict[str, Any])
```

#### `fetch_entitlements`

```python
fetch_entitlements(self, application_id: str, params: Dict[str, Any])
```

#### `fetch_guild`

```python
fetch_guild(self, guild_id: str)
```

#### `fetch_original_webhook_message`

```python
fetch_original_webhook_message(self, webhook_id: str, webhook_token: str)
```

#### `fetch_webhook`

```python
fetch_webhook(self, webhook_id: str, webhook_token: str | None = None)
```

#### `follow_announcement_channel`

```python
follow_announcement_channel(self)
```

#### `get_answer_voters`

```python
get_answer_voters(self)
```

#### `get_application_activity_instance`

```python
get_application_activity_instance(self)
```

#### `get_application_command_permissions`

```python
get_application_command_permissions(self)
```

#### `get_application_emoji`

```python
get_application_emoji(self, emoji_id: str)
```

#### `get_application_role_connection_metadata_records`

```python
get_application_role_connection_metadata_records(self)
```

#### `get_audit_log`

```python
get_audit_log(self)
```

#### `get_auto_moderation_rule`

```python
get_auto_moderation_rule(self)
```

#### `get_channel`

```python
get_channel(self, channel_id: str)
```

#### `get_channel_invites`

```python
get_channel_invites(self)
```

#### `get_channel_message`

```python
get_channel_message(self, channel_id: str, message_id: str)
```

#### `get_channel_messages`

```python
get_channel_messages(self)
```

#### `get_channel_webhooks`

```python
get_channel_webhooks(self)
```

#### `get_current_application`

```python
get_current_application(self)
```

#### `get_current_user`

```python
get_current_user(self)
```

#### `get_current_user_application_role_connection`

```python
get_current_user_application_role_connection(self)
```

#### `get_current_user_connections`

```python
get_current_user_connections(self)
```

#### `get_current_user_guild_member`

```python
get_current_user_guild_member(self)
```

#### `get_current_user_guilds`

```python
get_current_user_guilds(self)
```

#### `get_current_user_voice_state`

```python
get_current_user_voice_state(self)
```

#### `get_entitlement`

```python
get_entitlement(self, application_id: str, entitlement_id: str)
```

#### `get_followup_message`

```python
get_followup_message(self)
```

#### `get_global_application_command`

```python
get_global_application_command(self)
```

#### `get_global_application_commands`

```python
get_global_application_commands(self, application_id: str, *, with_localizations: bool = False)
```

#### `get_guild`

```python
get_guild(self, guild_id: str, **params: str)
```

#### `get_guild_application_command`

```python
get_guild_application_command(self)
```

#### `get_guild_application_command_permissions`

```python
get_guild_application_command_permissions(self)
```

#### `get_guild_application_commands`

```python
get_guild_application_commands(self)
```

#### `get_guild_ban`

```python
get_guild_ban(self)
```

#### `get_guild_bans`

```python
get_guild_bans(self)
```

#### `get_guild_channels`

```python
get_guild_channels(self, guild_id: str)
```

#### `get_guild_emoji`

```python
get_guild_emoji(self)
```

#### `get_guild_integrations`

```python
get_guild_integrations(self)
```

#### `get_guild_invites`

```python
get_guild_invites(self)
```

#### `get_guild_member`

```python
get_guild_member(self, guild_id: str, user_id: str)
```

#### `get_guild_onboarding`

```python
get_guild_onboarding(self)
```

#### `get_guild_preview`

```python
get_guild_preview(self)
```

#### `get_guild_prune_count`

```python
get_guild_prune_count(self)
```

#### `get_guild_role`

```python
get_guild_role(self)
```

#### `get_guild_roles`

```python
get_guild_roles(self, guild_id: str)
```

#### `get_guild_scheduled_event`

```python
get_guild_scheduled_event(self)
```

#### `get_guild_scheduled_event_users`

```python
get_guild_scheduled_event_users(self)
```

#### `get_guild_soundboard_sound`

```python
get_guild_soundboard_sound(self)
```

#### `get_guild_sticker`

```python
get_guild_sticker(self)
```

#### `get_guild_template`

```python
get_guild_template(self)
```

#### `get_guild_templates`

```python
get_guild_templates(self)
```

#### `get_guild_vanity_url`

```python
get_guild_vanity_url(self)
```

#### `get_guild_voice_regions`

```python
get_guild_voice_regions(self)
```

#### `get_guild_webhooks`

```python
get_guild_webhooks(self)
```

#### `get_guild_welcome_screen`

```python
get_guild_welcome_screen(self)
```

#### `get_guild_widget`

```python
get_guild_widget(self)
```

#### `get_guild_widget_image`

```python
get_guild_widget_image(self)
```

#### `get_guild_widget_settings`

```python
get_guild_widget_settings(self)
```

#### `get_invite`

```python
get_invite(self)
```

#### `get_lobby`

```python
get_lobby(self)
```

#### `get_original_interaction_response`

```python
get_original_interaction_response(self)
```

#### `get_pinned_messages`

```python
get_pinned_messages(self)
```

#### `get_reactions`

```python
get_reactions(self)
```

#### `get_sku_subscription`

```python
get_sku_subscription(self)
```

#### `get_stage_instance`

```python
get_stage_instance(self)
```

#### `get_sticker`

```python
get_sticker(self)
```

#### `get_sticker_pack`

```python
get_sticker_pack(self)
```

#### `get_thread_member`

```python
get_thread_member(self)
```

#### `get_user`

```python
get_user(self, user_id: str)
```

#### `get_user_voice_state`

```python
get_user_voice_state(self)
```

#### `get_webhook`

```python
get_webhook(self, webhook_id: str, webhook_token: str | None = None)
```

#### `get_webhook_message`

```python
get_webhook_message(self)
```

#### `group_dm_add_recipient`

```python
group_dm_add_recipient(self)
```

#### `group_dm_remove_recipient`

```python
group_dm_remove_recipient(self)
```

#### `join_thread`

```python
join_thread(self)
```

#### `leave_guild`

```python
leave_guild(self)
```

#### `leave_lobby`

```python
leave_lobby(self)
```

#### `leave_thread`

```python
leave_thread(self)
```

#### `link_channel_to_lobby`

```python
link_channel_to_lobby(self)
```

#### `list_active_guild_threads`

```python
list_active_guild_threads(self)
```

#### `list_application_emojis`

```python
list_application_emojis(self)
```

#### `list_auto_moderation_rules_for_guild`

```python
list_auto_moderation_rules_for_guild(self)
```

#### `list_default_soundboard_sounds`

```python
list_default_soundboard_sounds(self)
```

#### `list_entitlements`

```python
list_entitlements(self)
```

#### `list_guild_emojis`

```python
list_guild_emojis(self)
```

#### `list_guild_members`

```python
list_guild_members(self)
```

#### `list_guild_soundboard_sounds`

```python
list_guild_soundboard_sounds(self)
```

#### `list_guild_stickers`

```python
list_guild_stickers(self)
```

#### `list_joined_private_threads`

```python
list_joined_private_threads(self)
```

#### `list_private_archived_threads`

```python
list_private_archived_threads(self)
```

#### `list_public_archived_threads`

```python
list_public_archived_threads(self)
```

#### `list_scheduled_events_for_guild`

```python
list_scheduled_events_for_guild(self)
```

#### `list_sku_subscriptions`

```python
list_sku_subscriptions(self)
```

#### `list_skus`

```python
list_skus(self, application_id: str)
```

#### `list_sticker_packs`

```python
list_sticker_packs(self)
```

#### `list_thread_member`

```python
list_thread_member(self)
```

#### `list_voice_regions`

```python
list_voice_regions(self)
```

#### `modify_application_emoji`

```python
modify_application_emoji(self, emoji_id: str, name: str)
```

#### `modify_auto_moderation_rule`

```python
modify_auto_moderation_rule(self)
```

#### `modify_channel`

```python
modify_channel(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `modify_current_member`

```python
modify_current_member(self)
```

#### `modify_current_user`

```python
modify_current_user(self, payload: Dict[str, Any])
```

#### `modify_current_user_nick`

```python
modify_current_user_nick(self)
```

#### `modify_current_user_voice_state`

```python
modify_current_user_voice_state(self)
```

#### `modify_guild`

```python
modify_guild(self)
```

#### `modify_guild_channel_positions`

```python
modify_guild_channel_positions(self, guild_id: str, payload: Dict[str, Any])
```

#### `modify_guild_emoji`

```python
modify_guild_emoji(self)
```

#### `modify_guild_incident_actions`

```python
modify_guild_incident_actions(self)
```

#### `modify_guild_member`

```python
modify_guild_member(self)
```

#### `modify_guild_mfa_level`

```python
modify_guild_mfa_level(self)
```

#### `modify_guild_onboarding`

```python
modify_guild_onboarding(self)
```

#### `modify_guild_role`

```python
modify_guild_role(self, guild_id: str, role_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `modify_guild_role_positions`

```python
modify_guild_role_positions(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `modify_guild_scheduled_event`

```python
modify_guild_scheduled_event(self)
```

#### `modify_guild_soundboard_sound`

```python
modify_guild_soundboard_sound(self)
```

#### `modify_guild_sticker`

```python
modify_guild_sticker(self)
```

#### `modify_guild_template`

```python
modify_guild_template(self)
```

#### `modify_guild_welcome_screen`

```python
modify_guild_welcome_screen(self)
```

#### `modify_guild_widget`

```python
modify_guild_widget(self)
```

#### `modify_lobby`

```python
modify_lobby(self)
```

#### `modify_stage_instance`

```python
modify_stage_instance(self)
```

#### `modify_user_voice_state`

```python
modify_user_voice_state(self)
```

#### `modify_webhook`

```python
modify_webhook(self, webhook_id: str, payload: Dict[str, Any], *, token: str = '', reason: str | None = None)
```

#### `modify_webhook_with_token`

```python
modify_webhook_with_token(self)
```

#### `pin_message`

```python
pin_message(self, channel_id: str, message_id: str, *, reason: str | None = None)
```

#### `remove_a_member_from_a_lobby`

```python
remove_a_member_from_a_lobby(self)
```

#### `remove_guild_ban`

```python
remove_guild_ban(self)
```

#### `remove_guild_member`

```python
remove_guild_member(self, guild_id: str, user_id: str, *, reason: str | None = None)
```

#### `remove_guild_member_role`

```python
remove_guild_member_role(self, guild_id: str, user_id: str, role_id: str, *, reason: str | None = None)
```

#### `remove_thread_member`

```python
remove_thread_member(self)
```

#### `request`

```python
request(self, method: str, path: str, *, body: aiohttp.multipart.MultipartWriter | Any = None, authorize: bool = False, reason: str | None = None, **params: Any)
```

#### `request_exp`

```python
request_exp(self, method: str, template: str, *minor: str, body: aiohttp.multipart.MultipartWriter | Any = None, authorize: bool = False, reason: str | None = None, params: Dict[str, Any] | None = None, **major: str)
```

#### `search_guild_members`

```python
search_guild_members(self)
```

#### `send_soundboard_sound`

```python
send_soundboard_sound(self)
```

#### `start_thread_from_message`

```python
start_thread_from_message(self, channel_id: str, message_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `start_thread_in_forum_or_media_channel`

```python
start_thread_in_forum_or_media_channel(self)
```

#### `start_thread_without_message`

```python
start_thread_without_message(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

#### `sync_guild_template`

```python
sync_guild_template(self)
```

#### `trigger_typing_indicator`

```python
trigger_typing_indicator(self)
```

#### `unlink_channel_from_lobby`

```python
unlink_channel_from_lobby(self)
```

#### `unpin_message`

```python
unpin_message(self, channel_id: str, message_id: str, *, reason: str | None = None)
```

#### `update_application_role_connection_metadata_records`

```python
update_application_role_connection_metadata_records(self)
```

#### `update_current_user_application_role_connection`

```python
update_current_user_application_role_connection(self)
```


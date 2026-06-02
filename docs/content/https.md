---
title: discohook.https
---

# `discohook.https`

## Classes

- [HTTPClient](#class-httpclient)

<a id="class-httpclient"></a>
## Class `HTTPClient`

**Qualified Name:** `discohook.https.HTTPClient`

Represents an HTTP client for Discord's API.

### Method Index

- [add_a_member_to_a_lobby](#httpclient-add-a-member-to-a-lobby)
- [add_guild_member](#httpclient-add-guild-member)
- [add_guild_member_role](#httpclient-add-guild-member-role)
- [add_thread_member](#httpclient-add-thread-member)
- [begin_guild_prune](#httpclient-begin-guild-prune)
- [bulk_delete_messages](#httpclient-bulk-delete-messages)
- [bulk_guild_ban](#httpclient-bulk-guild-ban)
- [bulk_overwrite_global_application_commands](#httpclient-bulk-overwrite-global-application-commands)
- [bulk_overwrite_guild_application_commands](#httpclient-bulk-overwrite-guild-application-commands)
- [consume_entitlement](#httpclient-consume-entitlement)
- [create_application_emoji](#httpclient-create-application-emoji)
- [create_auto_moderation_rule](#httpclient-create-auto-moderation-rule)
- [create_channel_invite](#httpclient-create-channel-invite)
- [create_dm](#httpclient-create-dm)
- [create_followup_message](#httpclient-create-followup-message)
- [create_global_application_command](#httpclient-create-global-application-command)
- [create_group_dm](#httpclient-create-group-dm)
- [create_guild](#httpclient-create-guild)
- [create_guild_application_command](#httpclient-create-guild-application-command)
- [create_guild_ban](#httpclient-create-guild-ban)
- [create_guild_channel](#httpclient-create-guild-channel)
- [create_guild_emoji](#httpclient-create-guild-emoji)
- [create_guild_from_guild_template](#httpclient-create-guild-from-guild-template)
- [create_guild_role](#httpclient-create-guild-role)
- [create_guild_scheduled_event](#httpclient-create-guild-scheduled-event)
- [create_guild_soundboard_sound](#httpclient-create-guild-soundboard-sound)
- [create_guild_sticker](#httpclient-create-guild-sticker)
- [create_guild_template](#httpclient-create-guild-template)
- [create_interaction_response](#httpclient-create-interaction-response)
- [create_lobby](#httpclient-create-lobby)
- [create_message](#httpclient-create-message)
- [create_reaction](#httpclient-create-reaction)
- [create_stage_instance](#httpclient-create-stage-instance)
- [create_test_entitlement](#httpclient-create-test-entitlement)
- [create_webhook](#httpclient-create-webhook)
- [crosspost_message](#httpclient-crosspost-message)
- [delete_all_message_reactions](#httpclient-delete-all-message-reactions)
- [delete_all_reactions](#httpclient-delete-all-reactions)
- [delete_all_reactions_for_emoji](#httpclient-delete-all-reactions-for-emoji)
- [delete_application_command](#httpclient-delete-application-command)
- [delete_application_emoji](#httpclient-delete-application-emoji)
- [delete_auto_moderation_rule](#httpclient-delete-auto-moderation-rule)
- [delete_channel_permission](#httpclient-delete-channel-permission)
- [delete_followup_message](#httpclient-delete-followup-message)
- [delete_global_application_command](#httpclient-delete-global-application-command)
- [delete_guild](#httpclient-delete-guild)
- [delete_guild_application_command](#httpclient-delete-guild-application-command)
- [delete_guild_emoji](#httpclient-delete-guild-emoji)
- [delete_guild_integration](#httpclient-delete-guild-integration)
- [delete_guild_role](#httpclient-delete-guild-role)
- [delete_guild_scheduled_event](#httpclient-delete-guild-scheduled-event)
- [delete_guild_soundboard_sound](#httpclient-delete-guild-soundboard-sound)
- [delete_guild_sticker](#httpclient-delete-guild-sticker)
- [delete_guild_template](#httpclient-delete-guild-template)
- [delete_invite](#httpclient-delete-invite)
- [delete_lobby](#httpclient-delete-lobby)
- [delete_message](#httpclient-delete-message)
- [delete_message_reaction](#httpclient-delete-message-reaction)
- [delete_or_close_channel](#httpclient-delete-or-close-channel)
- [delete_original_interaction_response](#httpclient-delete-original-interaction-response)
- [delete_own_reaction](#httpclient-delete-own-reaction)
- [delete_stage_instance](#httpclient-delete-stage-instance)
- [delete_test_entitlement](#httpclient-delete-test-entitlement)
- [delete_user_reaction](#httpclient-delete-user-reaction)
- [delete_webhook](#httpclient-delete-webhook)
- [delete_webhook_message](#httpclient-delete-webhook-message)
- [delete_webhook_with_token](#httpclient-delete-webhook-with-token)
- [edit_application_command_permissions](#httpclient-edit-application-command-permissions)
- [edit_channel_permissions](#httpclient-edit-channel-permissions)
- [edit_current_application](#httpclient-edit-current-application)
- [edit_followup_message](#httpclient-edit-followup-message)
- [edit_global_application_command](#httpclient-edit-global-application-command)
- [edit_guild_application_command](#httpclient-edit-guild-application-command)
- [edit_message](#httpclient-edit-message)
- [edit_original_interaction_response](#httpclient-edit-original-interaction-response)
- [edit_webhook_message](#httpclient-edit-webhook-message)
- [end_poll](#httpclient-end-poll)
- [execute_github_compatible_webhook](#httpclient-execute-github-compatible-webhook)
- [execute_slack_compatible_webhook](#httpclient-execute-slack-compatible-webhook)
- [execute_webhook](#httpclient-execute-webhook)
- [fetch_answer_voters](#httpclient-fetch-answer-voters)
- [fetch_channel_messages](#httpclient-fetch-channel-messages)
- [fetch_entitlements](#httpclient-fetch-entitlements)
- [fetch_guild](#httpclient-fetch-guild)
- [fetch_original_webhook_message](#httpclient-fetch-original-webhook-message)
- [fetch_webhook](#httpclient-fetch-webhook)
- [follow_announcement_channel](#httpclient-follow-announcement-channel)
- [get_answer_voters](#httpclient-get-answer-voters)
- [get_application_activity_instance](#httpclient-get-application-activity-instance)
- [get_application_command_permissions](#httpclient-get-application-command-permissions)
- [get_application_emoji](#httpclient-get-application-emoji)
- [get_application_role_connection_metadata_records](#httpclient-get-application-role-connection-metadata-records)
- [get_audit_log](#httpclient-get-audit-log)
- [get_auto_moderation_rule](#httpclient-get-auto-moderation-rule)
- [get_channel](#httpclient-get-channel)
- [get_channel_invites](#httpclient-get-channel-invites)
- [get_channel_message](#httpclient-get-channel-message)
- [get_channel_messages](#httpclient-get-channel-messages)
- [get_channel_webhooks](#httpclient-get-channel-webhooks)
- [get_current_application](#httpclient-get-current-application)
- [get_current_user](#httpclient-get-current-user)
- [get_current_user_application_role_connection](#httpclient-get-current-user-application-role-connection)
- [get_current_user_connections](#httpclient-get-current-user-connections)
- [get_current_user_guild_member](#httpclient-get-current-user-guild-member)
- [get_current_user_guilds](#httpclient-get-current-user-guilds)
- [get_current_user_voice_state](#httpclient-get-current-user-voice-state)
- [get_entitlement](#httpclient-get-entitlement)
- [get_followup_message](#httpclient-get-followup-message)
- [get_global_application_command](#httpclient-get-global-application-command)
- [get_global_application_commands](#httpclient-get-global-application-commands)
- [get_guild](#httpclient-get-guild)
- [get_guild_application_command](#httpclient-get-guild-application-command)
- [get_guild_application_command_permissions](#httpclient-get-guild-application-command-permissions)
- [get_guild_application_commands](#httpclient-get-guild-application-commands)
- [get_guild_ban](#httpclient-get-guild-ban)
- [get_guild_bans](#httpclient-get-guild-bans)
- [get_guild_channels](#httpclient-get-guild-channels)
- [get_guild_emoji](#httpclient-get-guild-emoji)
- [get_guild_integrations](#httpclient-get-guild-integrations)
- [get_guild_invites](#httpclient-get-guild-invites)
- [get_guild_member](#httpclient-get-guild-member)
- [get_guild_onboarding](#httpclient-get-guild-onboarding)
- [get_guild_preview](#httpclient-get-guild-preview)
- [get_guild_prune_count](#httpclient-get-guild-prune-count)
- [get_guild_role](#httpclient-get-guild-role)
- [get_guild_roles](#httpclient-get-guild-roles)
- [get_guild_scheduled_event](#httpclient-get-guild-scheduled-event)
- [get_guild_scheduled_event_users](#httpclient-get-guild-scheduled-event-users)
- [get_guild_soundboard_sound](#httpclient-get-guild-soundboard-sound)
- [get_guild_sticker](#httpclient-get-guild-sticker)
- [get_guild_template](#httpclient-get-guild-template)
- [get_guild_templates](#httpclient-get-guild-templates)
- [get_guild_vanity_url](#httpclient-get-guild-vanity-url)
- [get_guild_voice_regions](#httpclient-get-guild-voice-regions)
- [get_guild_webhooks](#httpclient-get-guild-webhooks)
- [get_guild_welcome_screen](#httpclient-get-guild-welcome-screen)
- [get_guild_widget](#httpclient-get-guild-widget)
- [get_guild_widget_image](#httpclient-get-guild-widget-image)
- [get_guild_widget_settings](#httpclient-get-guild-widget-settings)
- [get_invite](#httpclient-get-invite)
- [get_lobby](#httpclient-get-lobby)
- [get_original_interaction_response](#httpclient-get-original-interaction-response)
- [get_pinned_messages](#httpclient-get-pinned-messages)
- [get_reactions](#httpclient-get-reactions)
- [get_sku_subscription](#httpclient-get-sku-subscription)
- [get_stage_instance](#httpclient-get-stage-instance)
- [get_sticker](#httpclient-get-sticker)
- [get_sticker_pack](#httpclient-get-sticker-pack)
- [get_thread_member](#httpclient-get-thread-member)
- [get_user](#httpclient-get-user)
- [get_user_voice_state](#httpclient-get-user-voice-state)
- [get_webhook](#httpclient-get-webhook)
- [get_webhook_message](#httpclient-get-webhook-message)
- [group_dm_add_recipient](#httpclient-group-dm-add-recipient)
- [group_dm_remove_recipient](#httpclient-group-dm-remove-recipient)
- [join_thread](#httpclient-join-thread)
- [leave_guild](#httpclient-leave-guild)
- [leave_lobby](#httpclient-leave-lobby)
- [leave_thread](#httpclient-leave-thread)
- [link_channel_to_lobby](#httpclient-link-channel-to-lobby)
- [list_active_guild_threads](#httpclient-list-active-guild-threads)
- [list_application_emojis](#httpclient-list-application-emojis)
- [list_auto_moderation_rules_for_guild](#httpclient-list-auto-moderation-rules-for-guild)
- [list_default_soundboard_sounds](#httpclient-list-default-soundboard-sounds)
- [list_entitlements](#httpclient-list-entitlements)
- [list_guild_emojis](#httpclient-list-guild-emojis)
- [list_guild_members](#httpclient-list-guild-members)
- [list_guild_soundboard_sounds](#httpclient-list-guild-soundboard-sounds)
- [list_guild_stickers](#httpclient-list-guild-stickers)
- [list_joined_private_threads](#httpclient-list-joined-private-threads)
- [list_private_archived_threads](#httpclient-list-private-archived-threads)
- [list_public_archived_threads](#httpclient-list-public-archived-threads)
- [list_scheduled_events_for_guild](#httpclient-list-scheduled-events-for-guild)
- [list_sku_subscriptions](#httpclient-list-sku-subscriptions)
- [list_skus](#httpclient-list-skus)
- [list_sticker_packs](#httpclient-list-sticker-packs)
- [list_thread_member](#httpclient-list-thread-member)
- [list_voice_regions](#httpclient-list-voice-regions)
- [modify_application_emoji](#httpclient-modify-application-emoji)
- [modify_auto_moderation_rule](#httpclient-modify-auto-moderation-rule)
- [modify_channel](#httpclient-modify-channel)
- [modify_current_member](#httpclient-modify-current-member)
- [modify_current_user](#httpclient-modify-current-user)
- [modify_current_user_nick](#httpclient-modify-current-user-nick)
- [modify_current_user_voice_state](#httpclient-modify-current-user-voice-state)
- [modify_guild](#httpclient-modify-guild)
- [modify_guild_channel_positions](#httpclient-modify-guild-channel-positions)
- [modify_guild_emoji](#httpclient-modify-guild-emoji)
- [modify_guild_incident_actions](#httpclient-modify-guild-incident-actions)
- [modify_guild_member](#httpclient-modify-guild-member)
- [modify_guild_mfa_level](#httpclient-modify-guild-mfa-level)
- [modify_guild_onboarding](#httpclient-modify-guild-onboarding)
- [modify_guild_role](#httpclient-modify-guild-role)
- [modify_guild_role_positions](#httpclient-modify-guild-role-positions)
- [modify_guild_scheduled_event](#httpclient-modify-guild-scheduled-event)
- [modify_guild_soundboard_sound](#httpclient-modify-guild-soundboard-sound)
- [modify_guild_sticker](#httpclient-modify-guild-sticker)
- [modify_guild_template](#httpclient-modify-guild-template)
- [modify_guild_welcome_screen](#httpclient-modify-guild-welcome-screen)
- [modify_guild_widget](#httpclient-modify-guild-widget)
- [modify_lobby](#httpclient-modify-lobby)
- [modify_stage_instance](#httpclient-modify-stage-instance)
- [modify_user_voice_state](#httpclient-modify-user-voice-state)
- [modify_webhook](#httpclient-modify-webhook)
- [modify_webhook_with_token](#httpclient-modify-webhook-with-token)
- [pin_message](#httpclient-pin-message)
- [remove_a_member_from_a_lobby](#httpclient-remove-a-member-from-a-lobby)
- [remove_guild_ban](#httpclient-remove-guild-ban)
- [remove_guild_member](#httpclient-remove-guild-member)
- [remove_guild_member_role](#httpclient-remove-guild-member-role)
- [remove_thread_member](#httpclient-remove-thread-member)
- [request](#httpclient-request)
- [request_exp](#httpclient-request-exp)
- [search_guild_members](#httpclient-search-guild-members)
- [send_soundboard_sound](#httpclient-send-soundboard-sound)
- [start_thread_from_message](#httpclient-start-thread-from-message)
- [start_thread_in_forum_or_media_channel](#httpclient-start-thread-in-forum-or-media-channel)
- [start_thread_without_message](#httpclient-start-thread-without-message)
- [sync_guild_template](#httpclient-sync-guild-template)
- [trigger_typing_indicator](#httpclient-trigger-typing-indicator)
- [unlink_channel_from_lobby](#httpclient-unlink-channel-from-lobby)
- [unpin_message](#httpclient-unpin-message)
- [update_application_role_connection_metadata_records](#httpclient-update-application-role-connection-metadata-records)
- [update_current_user_application_role_connection](#httpclient-update-current-user-application-role-connection)

### Methods

<a id="httpclient-add-a-member-to-a-lobby"></a>
#### `add_a_member_to_a_lobby`

```python
async add_a_member_to_a_lobby(self)
```

<a id="httpclient-add-guild-member"></a>
#### `add_guild_member`

```python
async add_guild_member(self)
```

<a id="httpclient-add-guild-member-role"></a>
#### `add_guild_member_role`

```python
async add_guild_member_role(self, guild_id: str, user_id: str, role_id: str, *, reason: str | None = None)
```

<a id="httpclient-add-thread-member"></a>
#### `add_thread_member`

```python
async add_thread_member(self)
```

<a id="httpclient-begin-guild-prune"></a>
#### `begin_guild_prune`

```python
async begin_guild_prune(self)
```

<a id="httpclient-bulk-delete-messages"></a>
#### `bulk_delete_messages`

```python
async bulk_delete_messages(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-bulk-guild-ban"></a>
#### `bulk_guild_ban`

```python
async bulk_guild_ban(self)
```

<a id="httpclient-bulk-overwrite-global-application-commands"></a>
#### `bulk_overwrite_global_application_commands`

```python
async bulk_overwrite_global_application_commands(self, application_id: str, commands: List[Dict[str, Any]])
```

<a id="httpclient-bulk-overwrite-guild-application-commands"></a>
#### `bulk_overwrite_guild_application_commands`

```python
async bulk_overwrite_guild_application_commands(self, application_id: str, guild_id: str, commands: List[Dict[str, Any]])
```

<a id="httpclient-consume-entitlement"></a>
#### `consume_entitlement`

```python
async consume_entitlement(self)
```

<a id="httpclient-create-application-emoji"></a>
#### `create_application_emoji`

```python
async create_application_emoji(self, payload: Dict[str, Any])
```

<a id="httpclient-create-auto-moderation-rule"></a>
#### `create_auto_moderation_rule`

```python
async create_auto_moderation_rule(self)
```

<a id="httpclient-create-channel-invite"></a>
#### `create_channel_invite`

```python
async create_channel_invite(self)
```

<a id="httpclient-create-dm"></a>
#### `create_dm`

```python
async create_dm(self, payload: Dict[str, Any])
```

<a id="httpclient-create-followup-message"></a>
#### `create_followup_message`

```python
async create_followup_message(self)
```

<a id="httpclient-create-global-application-command"></a>
#### `create_global_application_command`

```python
async create_global_application_command(self)
```

<a id="httpclient-create-group-dm"></a>
#### `create_group_dm`

```python
async create_group_dm(self)
```

<a id="httpclient-create-guild"></a>
#### `create_guild`

```python
async create_guild(self)
```

<a id="httpclient-create-guild-application-command"></a>
#### `create_guild_application_command`

```python
async create_guild_application_command(self)
```

<a id="httpclient-create-guild-ban"></a>
#### `create_guild_ban`

```python
async create_guild_ban(self, guild_id: str, user_id: str, delete_message_seconds: int = 0, *, reason: str | None = None)
```

<a id="httpclient-create-guild-channel"></a>
#### `create_guild_channel`

```python
async create_guild_channel(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-create-guild-emoji"></a>
#### `create_guild_emoji`

```python
async create_guild_emoji(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-create-guild-from-guild-template"></a>
#### `create_guild_from_guild_template`

```python
async create_guild_from_guild_template(self)
```

<a id="httpclient-create-guild-role"></a>
#### `create_guild_role`

```python
async create_guild_role(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-create-guild-scheduled-event"></a>
#### `create_guild_scheduled_event`

```python
async create_guild_scheduled_event(self)
```

<a id="httpclient-create-guild-soundboard-sound"></a>
#### `create_guild_soundboard_sound`

```python
async create_guild_soundboard_sound(self)
```

<a id="httpclient-create-guild-sticker"></a>
#### `create_guild_sticker`

```python
async create_guild_sticker(self)
```

<a id="httpclient-create-guild-template"></a>
#### `create_guild_template`

```python
async create_guild_template(self)
```

<a id="httpclient-create-interaction-response"></a>
#### `create_interaction_response`

```python
async create_interaction_response(self, interaction_id: str, interaction_token: str, data: Any, with_response: bool = False)
```

<a id="httpclient-create-lobby"></a>
#### `create_lobby`

```python
async create_lobby(self)
```

<a id="httpclient-create-message"></a>
#### `create_message`

```python
async create_message(self, channel_id: str, data: Any)
```

<a id="httpclient-create-reaction"></a>
#### `create_reaction`

```python
async create_reaction(self, channel_id: str, message_id: str, emoji: str)
```

<a id="httpclient-create-stage-instance"></a>
#### `create_stage_instance`

```python
async create_stage_instance(self)
```

<a id="httpclient-create-test-entitlement"></a>
#### `create_test_entitlement`

```python
async create_test_entitlement(self, application_id: str, payload: Dict[str, Any])
```

<a id="httpclient-create-webhook"></a>
#### `create_webhook`

```python
async create_webhook(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-crosspost-message"></a>
#### `crosspost_message`

```python
async crosspost_message(self, channel_id: str, message_id: str)
```

<a id="httpclient-delete-all-message-reactions"></a>
#### `delete_all_message_reactions`

```python
async delete_all_message_reactions(self, message_id: str, emoji: str | None = None)
```

<a id="httpclient-delete-all-reactions"></a>
#### `delete_all_reactions`

```python
async delete_all_reactions(self)
```

<a id="httpclient-delete-all-reactions-for-emoji"></a>
#### `delete_all_reactions_for_emoji`

```python
async delete_all_reactions_for_emoji(self)
```

<a id="httpclient-delete-application-command"></a>
#### `delete_application_command`

```python
async delete_application_command(self, application_id: str, command_id: str, guild_id: str | None = None)
```

<a id="httpclient-delete-application-emoji"></a>
#### `delete_application_emoji`

```python
async delete_application_emoji(self, emoji_id: str)
```

<a id="httpclient-delete-auto-moderation-rule"></a>
#### `delete_auto_moderation_rule`

```python
async delete_auto_moderation_rule(self)
```

<a id="httpclient-delete-channel-permission"></a>
#### `delete_channel_permission`

```python
async delete_channel_permission(self)
```

<a id="httpclient-delete-followup-message"></a>
#### `delete_followup_message`

```python
async delete_followup_message(self)
```

<a id="httpclient-delete-global-application-command"></a>
#### `delete_global_application_command`

```python
async delete_global_application_command(self)
```

<a id="httpclient-delete-guild"></a>
#### `delete_guild`

```python
async delete_guild(self)
```

<a id="httpclient-delete-guild-application-command"></a>
#### `delete_guild_application_command`

```python
async delete_guild_application_command(self)
```

<a id="httpclient-delete-guild-emoji"></a>
#### `delete_guild_emoji`

```python
async delete_guild_emoji(self)
```

<a id="httpclient-delete-guild-integration"></a>
#### `delete_guild_integration`

```python
async delete_guild_integration(self)
```

<a id="httpclient-delete-guild-role"></a>
#### `delete_guild_role`

```python
async delete_guild_role(self)
```

<a id="httpclient-delete-guild-scheduled-event"></a>
#### `delete_guild_scheduled_event`

```python
async delete_guild_scheduled_event(self)
```

<a id="httpclient-delete-guild-soundboard-sound"></a>
#### `delete_guild_soundboard_sound`

```python
async delete_guild_soundboard_sound(self)
```

<a id="httpclient-delete-guild-sticker"></a>
#### `delete_guild_sticker`

```python
async delete_guild_sticker(self)
```

<a id="httpclient-delete-guild-template"></a>
#### `delete_guild_template`

```python
async delete_guild_template(self)
```

<a id="httpclient-delete-invite"></a>
#### `delete_invite`

```python
async delete_invite(self)
```

<a id="httpclient-delete-lobby"></a>
#### `delete_lobby`

```python
async delete_lobby(self)
```

<a id="httpclient-delete-message"></a>
#### `delete_message`

```python
async delete_message(self, channel_id: str, message_id: str, *, reason: str | None = None)
```

<a id="httpclient-delete-message-reaction"></a>
#### `delete_message_reaction`

```python
async delete_message_reaction(self, message_id: str, emoji: str, user_id: str)
```

<a id="httpclient-delete-or-close-channel"></a>
#### `delete_or_close_channel`

```python
async delete_or_close_channel(self, channel_id: str, *, reason: str | None = None)
```

<a id="httpclient-delete-original-interaction-response"></a>
#### `delete_original_interaction_response`

```python
async delete_original_interaction_response(self)
```

<a id="httpclient-delete-own-reaction"></a>
#### `delete_own_reaction`

```python
async delete_own_reaction(self)
```

<a id="httpclient-delete-stage-instance"></a>
#### `delete_stage_instance`

```python
async delete_stage_instance(self)
```

<a id="httpclient-delete-test-entitlement"></a>
#### `delete_test_entitlement`

```python
async delete_test_entitlement(self, application_id: str, entitlement_id: str)
```

<a id="httpclient-delete-user-reaction"></a>
#### `delete_user_reaction`

```python
async delete_user_reaction(self)
```

<a id="httpclient-delete-webhook"></a>
#### `delete_webhook`

```python
async delete_webhook(self, webhook_id: str, *, reason: str | None = None)
```

<a id="httpclient-delete-webhook-message"></a>
#### `delete_webhook_message`

```python
async delete_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str)
```

<a id="httpclient-delete-webhook-with-token"></a>
#### `delete_webhook_with_token`

```python
async delete_webhook_with_token(self)
```

<a id="httpclient-edit-application-command-permissions"></a>
#### `edit_application_command_permissions`

```python
async edit_application_command_permissions(self)
```

<a id="httpclient-edit-channel-permissions"></a>
#### `edit_channel_permissions`

```python
async edit_channel_permissions(self)
```

<a id="httpclient-edit-current-application"></a>
#### `edit_current_application`

```python
async edit_current_application(self)
```

<a id="httpclient-edit-followup-message"></a>
#### `edit_followup_message`

```python
async edit_followup_message(self)
```

<a id="httpclient-edit-global-application-command"></a>
#### `edit_global_application_command`

```python
async edit_global_application_command(self)
```

<a id="httpclient-edit-guild-application-command"></a>
#### `edit_guild_application_command`

```python
async edit_guild_application_command(self)
```

<a id="httpclient-edit-message"></a>
#### `edit_message`

```python
async edit_message(self, channel_id: str, message_id: str, data: Any)
```

<a id="httpclient-edit-original-interaction-response"></a>
#### `edit_original_interaction_response`

```python
async edit_original_interaction_response(self)
```

<a id="httpclient-edit-webhook-message"></a>
#### `edit_webhook_message`

```python
async edit_webhook_message(self, webhook_id: str, webhook_token: str, message_id: str, data: Any, **params: Any)
```

<a id="httpclient-end-poll"></a>
#### `end_poll`

```python
async end_poll(self, channel_id: str, message_id: str)
```

<a id="httpclient-execute-github-compatible-webhook"></a>
#### `execute_github_compatible_webhook`

```python
async execute_github_compatible_webhook(self)
```

<a id="httpclient-execute-slack-compatible-webhook"></a>
#### `execute_slack_compatible_webhook`

```python
async execute_slack_compatible_webhook(self)
```

<a id="httpclient-execute-webhook"></a>
#### `execute_webhook`

```python
async execute_webhook(self, webhook_id: str, webhook_token: str, data: Any, **params: Any)
```

<a id="httpclient-fetch-answer-voters"></a>
#### `fetch_answer_voters`

```python
async fetch_answer_voters(self, *, channel_id: str, message_id: str, answer_id: int, params: Dict[str, Any] = None)
```

<a id="httpclient-fetch-channel-messages"></a>
#### `fetch_channel_messages`

```python
async fetch_channel_messages(self, channel_id: str, params: Dict[str, Any])
```

<a id="httpclient-fetch-entitlements"></a>
#### `fetch_entitlements`

```python
async fetch_entitlements(self, application_id: str, params: Dict[str, Any])
```

<a id="httpclient-fetch-guild"></a>
#### `fetch_guild`

```python
async fetch_guild(self, guild_id: str)
```

<a id="httpclient-fetch-original-webhook-message"></a>
#### `fetch_original_webhook_message`

```python
async fetch_original_webhook_message(self, webhook_id: str, webhook_token: str)
```

<a id="httpclient-fetch-webhook"></a>
#### `fetch_webhook`

```python
async fetch_webhook(self, webhook_id: str, webhook_token: str | None = None)
```

<a id="httpclient-follow-announcement-channel"></a>
#### `follow_announcement_channel`

```python
async follow_announcement_channel(self)
```

<a id="httpclient-get-answer-voters"></a>
#### `get_answer_voters`

```python
async get_answer_voters(self)
```

<a id="httpclient-get-application-activity-instance"></a>
#### `get_application_activity_instance`

```python
async get_application_activity_instance(self)
```

<a id="httpclient-get-application-command-permissions"></a>
#### `get_application_command_permissions`

```python
async get_application_command_permissions(self)
```

<a id="httpclient-get-application-emoji"></a>
#### `get_application_emoji`

```python
async get_application_emoji(self, emoji_id: str)
```

<a id="httpclient-get-application-role-connection-metadata-records"></a>
#### `get_application_role_connection_metadata_records`

```python
async get_application_role_connection_metadata_records(self)
```

<a id="httpclient-get-audit-log"></a>
#### `get_audit_log`

```python
async get_audit_log(self)
```

<a id="httpclient-get-auto-moderation-rule"></a>
#### `get_auto_moderation_rule`

```python
async get_auto_moderation_rule(self)
```

<a id="httpclient-get-channel"></a>
#### `get_channel`

```python
async get_channel(self, channel_id: str)
```

<a id="httpclient-get-channel-invites"></a>
#### `get_channel_invites`

```python
async get_channel_invites(self)
```

<a id="httpclient-get-channel-message"></a>
#### `get_channel_message`

```python
async get_channel_message(self, channel_id: str, message_id: str)
```

<a id="httpclient-get-channel-messages"></a>
#### `get_channel_messages`

```python
async get_channel_messages(self)
```

<a id="httpclient-get-channel-webhooks"></a>
#### `get_channel_webhooks`

```python
async get_channel_webhooks(self)
```

<a id="httpclient-get-current-application"></a>
#### `get_current_application`

```python
async get_current_application(self)
```

<a id="httpclient-get-current-user"></a>
#### `get_current_user`

```python
async get_current_user(self)
```

<a id="httpclient-get-current-user-application-role-connection"></a>
#### `get_current_user_application_role_connection`

```python
async get_current_user_application_role_connection(self)
```

<a id="httpclient-get-current-user-connections"></a>
#### `get_current_user_connections`

```python
async get_current_user_connections(self)
```

<a id="httpclient-get-current-user-guild-member"></a>
#### `get_current_user_guild_member`

```python
async get_current_user_guild_member(self)
```

<a id="httpclient-get-current-user-guilds"></a>
#### `get_current_user_guilds`

```python
async get_current_user_guilds(self)
```

<a id="httpclient-get-current-user-voice-state"></a>
#### `get_current_user_voice_state`

```python
async get_current_user_voice_state(self)
```

<a id="httpclient-get-entitlement"></a>
#### `get_entitlement`

```python
async get_entitlement(self, application_id: str, entitlement_id: str)
```

<a id="httpclient-get-followup-message"></a>
#### `get_followup_message`

```python
async get_followup_message(self)
```

<a id="httpclient-get-global-application-command"></a>
#### `get_global_application_command`

```python
async get_global_application_command(self)
```

<a id="httpclient-get-global-application-commands"></a>
#### `get_global_application_commands`

```python
async get_global_application_commands(self, application_id: str, *, with_localizations: bool = False)
```

<a id="httpclient-get-guild"></a>
#### `get_guild`

```python
async get_guild(self, guild_id: str, **params: str)
```

<a id="httpclient-get-guild-application-command"></a>
#### `get_guild_application_command`

```python
async get_guild_application_command(self)
```

<a id="httpclient-get-guild-application-command-permissions"></a>
#### `get_guild_application_command_permissions`

```python
async get_guild_application_command_permissions(self)
```

<a id="httpclient-get-guild-application-commands"></a>
#### `get_guild_application_commands`

```python
async get_guild_application_commands(self)
```

<a id="httpclient-get-guild-ban"></a>
#### `get_guild_ban`

```python
async get_guild_ban(self)
```

<a id="httpclient-get-guild-bans"></a>
#### `get_guild_bans`

```python
async get_guild_bans(self)
```

<a id="httpclient-get-guild-channels"></a>
#### `get_guild_channels`

```python
async get_guild_channels(self, guild_id: str)
```

<a id="httpclient-get-guild-emoji"></a>
#### `get_guild_emoji`

```python
async get_guild_emoji(self)
```

<a id="httpclient-get-guild-integrations"></a>
#### `get_guild_integrations`

```python
async get_guild_integrations(self)
```

<a id="httpclient-get-guild-invites"></a>
#### `get_guild_invites`

```python
async get_guild_invites(self)
```

<a id="httpclient-get-guild-member"></a>
#### `get_guild_member`

```python
async get_guild_member(self, guild_id: str, user_id: str)
```

<a id="httpclient-get-guild-onboarding"></a>
#### `get_guild_onboarding`

```python
async get_guild_onboarding(self)
```

<a id="httpclient-get-guild-preview"></a>
#### `get_guild_preview`

```python
async get_guild_preview(self)
```

<a id="httpclient-get-guild-prune-count"></a>
#### `get_guild_prune_count`

```python
async get_guild_prune_count(self)
```

<a id="httpclient-get-guild-role"></a>
#### `get_guild_role`

```python
async get_guild_role(self)
```

<a id="httpclient-get-guild-roles"></a>
#### `get_guild_roles`

```python
async get_guild_roles(self, guild_id: str)
```

<a id="httpclient-get-guild-scheduled-event"></a>
#### `get_guild_scheduled_event`

```python
async get_guild_scheduled_event(self)
```

<a id="httpclient-get-guild-scheduled-event-users"></a>
#### `get_guild_scheduled_event_users`

```python
async get_guild_scheduled_event_users(self)
```

<a id="httpclient-get-guild-soundboard-sound"></a>
#### `get_guild_soundboard_sound`

```python
async get_guild_soundboard_sound(self)
```

<a id="httpclient-get-guild-sticker"></a>
#### `get_guild_sticker`

```python
async get_guild_sticker(self)
```

<a id="httpclient-get-guild-template"></a>
#### `get_guild_template`

```python
async get_guild_template(self)
```

<a id="httpclient-get-guild-templates"></a>
#### `get_guild_templates`

```python
async get_guild_templates(self)
```

<a id="httpclient-get-guild-vanity-url"></a>
#### `get_guild_vanity_url`

```python
async get_guild_vanity_url(self)
```

<a id="httpclient-get-guild-voice-regions"></a>
#### `get_guild_voice_regions`

```python
async get_guild_voice_regions(self)
```

<a id="httpclient-get-guild-webhooks"></a>
#### `get_guild_webhooks`

```python
async get_guild_webhooks(self)
```

<a id="httpclient-get-guild-welcome-screen"></a>
#### `get_guild_welcome_screen`

```python
async get_guild_welcome_screen(self)
```

<a id="httpclient-get-guild-widget"></a>
#### `get_guild_widget`

```python
async get_guild_widget(self)
```

<a id="httpclient-get-guild-widget-image"></a>
#### `get_guild_widget_image`

```python
async get_guild_widget_image(self)
```

<a id="httpclient-get-guild-widget-settings"></a>
#### `get_guild_widget_settings`

```python
async get_guild_widget_settings(self)
```

<a id="httpclient-get-invite"></a>
#### `get_invite`

```python
async get_invite(self)
```

<a id="httpclient-get-lobby"></a>
#### `get_lobby`

```python
async get_lobby(self)
```

<a id="httpclient-get-original-interaction-response"></a>
#### `get_original_interaction_response`

```python
async get_original_interaction_response(self)
```

<a id="httpclient-get-pinned-messages"></a>
#### `get_pinned_messages`

```python
async get_pinned_messages(self)
```

<a id="httpclient-get-reactions"></a>
#### `get_reactions`

```python
async get_reactions(self)
```

<a id="httpclient-get-sku-subscription"></a>
#### `get_sku_subscription`

```python
async get_sku_subscription(self)
```

<a id="httpclient-get-stage-instance"></a>
#### `get_stage_instance`

```python
async get_stage_instance(self)
```

<a id="httpclient-get-sticker"></a>
#### `get_sticker`

```python
async get_sticker(self)
```

<a id="httpclient-get-sticker-pack"></a>
#### `get_sticker_pack`

```python
async get_sticker_pack(self)
```

<a id="httpclient-get-thread-member"></a>
#### `get_thread_member`

```python
async get_thread_member(self)
```

<a id="httpclient-get-user"></a>
#### `get_user`

```python
async get_user(self, user_id: str)
```

<a id="httpclient-get-user-voice-state"></a>
#### `get_user_voice_state`

```python
async get_user_voice_state(self)
```

<a id="httpclient-get-webhook"></a>
#### `get_webhook`

```python
async get_webhook(self, webhook_id: str, webhook_token: str | None = None)
```

<a id="httpclient-get-webhook-message"></a>
#### `get_webhook_message`

```python
async get_webhook_message(self)
```

<a id="httpclient-group-dm-add-recipient"></a>
#### `group_dm_add_recipient`

```python
async group_dm_add_recipient(self)
```

<a id="httpclient-group-dm-remove-recipient"></a>
#### `group_dm_remove_recipient`

```python
async group_dm_remove_recipient(self)
```

<a id="httpclient-join-thread"></a>
#### `join_thread`

```python
async join_thread(self)
```

<a id="httpclient-leave-guild"></a>
#### `leave_guild`

```python
async leave_guild(self)
```

<a id="httpclient-leave-lobby"></a>
#### `leave_lobby`

```python
async leave_lobby(self)
```

<a id="httpclient-leave-thread"></a>
#### `leave_thread`

```python
async leave_thread(self)
```

<a id="httpclient-link-channel-to-lobby"></a>
#### `link_channel_to_lobby`

```python
async link_channel_to_lobby(self)
```

<a id="httpclient-list-active-guild-threads"></a>
#### `list_active_guild_threads`

```python
async list_active_guild_threads(self)
```

<a id="httpclient-list-application-emojis"></a>
#### `list_application_emojis`

```python
async list_application_emojis(self)
```

<a id="httpclient-list-auto-moderation-rules-for-guild"></a>
#### `list_auto_moderation_rules_for_guild`

```python
async list_auto_moderation_rules_for_guild(self)
```

<a id="httpclient-list-default-soundboard-sounds"></a>
#### `list_default_soundboard_sounds`

```python
async list_default_soundboard_sounds(self)
```

<a id="httpclient-list-entitlements"></a>
#### `list_entitlements`

```python
async list_entitlements(self)
```

<a id="httpclient-list-guild-emojis"></a>
#### `list_guild_emojis`

```python
async list_guild_emojis(self)
```

<a id="httpclient-list-guild-members"></a>
#### `list_guild_members`

```python
async list_guild_members(self)
```

<a id="httpclient-list-guild-soundboard-sounds"></a>
#### `list_guild_soundboard_sounds`

```python
async list_guild_soundboard_sounds(self)
```

<a id="httpclient-list-guild-stickers"></a>
#### `list_guild_stickers`

```python
async list_guild_stickers(self)
```

<a id="httpclient-list-joined-private-threads"></a>
#### `list_joined_private_threads`

```python
async list_joined_private_threads(self)
```

<a id="httpclient-list-private-archived-threads"></a>
#### `list_private_archived_threads`

```python
async list_private_archived_threads(self)
```

<a id="httpclient-list-public-archived-threads"></a>
#### `list_public_archived_threads`

```python
async list_public_archived_threads(self)
```

<a id="httpclient-list-scheduled-events-for-guild"></a>
#### `list_scheduled_events_for_guild`

```python
async list_scheduled_events_for_guild(self)
```

<a id="httpclient-list-sku-subscriptions"></a>
#### `list_sku_subscriptions`

```python
async list_sku_subscriptions(self)
```

<a id="httpclient-list-skus"></a>
#### `list_skus`

```python
async list_skus(self, application_id: str)
```

<a id="httpclient-list-sticker-packs"></a>
#### `list_sticker_packs`

```python
async list_sticker_packs(self)
```

<a id="httpclient-list-thread-member"></a>
#### `list_thread_member`

```python
async list_thread_member(self)
```

<a id="httpclient-list-voice-regions"></a>
#### `list_voice_regions`

```python
async list_voice_regions(self)
```

<a id="httpclient-modify-application-emoji"></a>
#### `modify_application_emoji`

```python
async modify_application_emoji(self, emoji_id: str, name: str)
```

<a id="httpclient-modify-auto-moderation-rule"></a>
#### `modify_auto_moderation_rule`

```python
async modify_auto_moderation_rule(self)
```

<a id="httpclient-modify-channel"></a>
#### `modify_channel`

```python
async modify_channel(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-modify-current-member"></a>
#### `modify_current_member`

```python
async modify_current_member(self)
```

<a id="httpclient-modify-current-user"></a>
#### `modify_current_user`

```python
async modify_current_user(self, payload: Dict[str, Any])
```

<a id="httpclient-modify-current-user-nick"></a>
#### `modify_current_user_nick`

```python
async modify_current_user_nick(self)
```

<a id="httpclient-modify-current-user-voice-state"></a>
#### `modify_current_user_voice_state`

```python
async modify_current_user_voice_state(self)
```

<a id="httpclient-modify-guild"></a>
#### `modify_guild`

```python
async modify_guild(self)
```

<a id="httpclient-modify-guild-channel-positions"></a>
#### `modify_guild_channel_positions`

```python
async modify_guild_channel_positions(self, guild_id: str, payload: Dict[str, Any])
```

<a id="httpclient-modify-guild-emoji"></a>
#### `modify_guild_emoji`

```python
async modify_guild_emoji(self)
```

<a id="httpclient-modify-guild-incident-actions"></a>
#### `modify_guild_incident_actions`

```python
async modify_guild_incident_actions(self)
```

<a id="httpclient-modify-guild-member"></a>
#### `modify_guild_member`

```python
async modify_guild_member(self)
```

<a id="httpclient-modify-guild-mfa-level"></a>
#### `modify_guild_mfa_level`

```python
async modify_guild_mfa_level(self)
```

<a id="httpclient-modify-guild-onboarding"></a>
#### `modify_guild_onboarding`

```python
async modify_guild_onboarding(self)
```

<a id="httpclient-modify-guild-role"></a>
#### `modify_guild_role`

```python
async modify_guild_role(self, guild_id: str, role_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-modify-guild-role-positions"></a>
#### `modify_guild_role_positions`

```python
async modify_guild_role_positions(self, guild_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-modify-guild-scheduled-event"></a>
#### `modify_guild_scheduled_event`

```python
async modify_guild_scheduled_event(self)
```

<a id="httpclient-modify-guild-soundboard-sound"></a>
#### `modify_guild_soundboard_sound`

```python
async modify_guild_soundboard_sound(self)
```

<a id="httpclient-modify-guild-sticker"></a>
#### `modify_guild_sticker`

```python
async modify_guild_sticker(self)
```

<a id="httpclient-modify-guild-template"></a>
#### `modify_guild_template`

```python
async modify_guild_template(self)
```

<a id="httpclient-modify-guild-welcome-screen"></a>
#### `modify_guild_welcome_screen`

```python
async modify_guild_welcome_screen(self)
```

<a id="httpclient-modify-guild-widget"></a>
#### `modify_guild_widget`

```python
async modify_guild_widget(self)
```

<a id="httpclient-modify-lobby"></a>
#### `modify_lobby`

```python
async modify_lobby(self)
```

<a id="httpclient-modify-stage-instance"></a>
#### `modify_stage_instance`

```python
async modify_stage_instance(self)
```

<a id="httpclient-modify-user-voice-state"></a>
#### `modify_user_voice_state`

```python
async modify_user_voice_state(self)
```

<a id="httpclient-modify-webhook"></a>
#### `modify_webhook`

```python
async modify_webhook(self, webhook_id: str, payload: Dict[str, Any], *, token: str = '', reason: str | None = None)
```

<a id="httpclient-modify-webhook-with-token"></a>
#### `modify_webhook_with_token`

```python
async modify_webhook_with_token(self)
```

<a id="httpclient-pin-message"></a>
#### `pin_message`

```python
async pin_message(self, channel_id: str, message_id: str, *, reason: str | None = None)
```

<a id="httpclient-remove-a-member-from-a-lobby"></a>
#### `remove_a_member_from_a_lobby`

```python
async remove_a_member_from_a_lobby(self)
```

<a id="httpclient-remove-guild-ban"></a>
#### `remove_guild_ban`

```python
async remove_guild_ban(self)
```

<a id="httpclient-remove-guild-member"></a>
#### `remove_guild_member`

```python
async remove_guild_member(self, guild_id: str, user_id: str, *, reason: str | None = None)
```

<a id="httpclient-remove-guild-member-role"></a>
#### `remove_guild_member_role`

```python
async remove_guild_member_role(self, guild_id: str, user_id: str, role_id: str, *, reason: str | None = None)
```

<a id="httpclient-remove-thread-member"></a>
#### `remove_thread_member`

```python
async remove_thread_member(self)
```

<a id="httpclient-request"></a>
#### `request`

```python
async request(self, method: str, path: str, *, body: aiohttp.multipart.MultipartWriter | Any = None, authorize: bool = False, reason: str | None = None, **params: Any)
```

<a id="httpclient-request-exp"></a>
#### `request_exp`

```python
async request_exp(self, method: str, template: str, *minor: str, body: aiohttp.multipart.MultipartWriter | Any = None, authorize: bool = False, reason: str | None = None, params: Dict[str, Any] | None = None, **major: str)
```

<a id="httpclient-search-guild-members"></a>
#### `search_guild_members`

```python
async search_guild_members(self)
```

<a id="httpclient-send-soundboard-sound"></a>
#### `send_soundboard_sound`

```python
async send_soundboard_sound(self)
```

<a id="httpclient-start-thread-from-message"></a>
#### `start_thread_from_message`

```python
async start_thread_from_message(self, channel_id: str, message_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-start-thread-in-forum-or-media-channel"></a>
#### `start_thread_in_forum_or_media_channel`

```python
async start_thread_in_forum_or_media_channel(self)
```

<a id="httpclient-start-thread-without-message"></a>
#### `start_thread_without_message`

```python
async start_thread_without_message(self, channel_id: str, payload: Dict[str, Any], *, reason: str | None = None)
```

<a id="httpclient-sync-guild-template"></a>
#### `sync_guild_template`

```python
async sync_guild_template(self)
```

<a id="httpclient-trigger-typing-indicator"></a>
#### `trigger_typing_indicator`

```python
async trigger_typing_indicator(self)
```

<a id="httpclient-unlink-channel-from-lobby"></a>
#### `unlink_channel_from_lobby`

```python
async unlink_channel_from_lobby(self)
```

<a id="httpclient-unpin-message"></a>
#### `unpin_message`

```python
async unpin_message(self, channel_id: str, message_id: str, *, reason: str | None = None)
```

<a id="httpclient-update-application-role-connection-metadata-records"></a>
#### `update_application_role_connection_metadata_records`

```python
async update_application_role_connection_metadata_records(self)
```

<a id="httpclient-update-current-user-application-role-connection"></a>
#### `update_current_user_application_role_connection`

```python
async update_current_user_application_role_connection(self)
```


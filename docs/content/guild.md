---
title: discohook.guild
---

# `discohook.guild`

## Classes

- [Guild](#class-guild)
- [PartialGuild](#class-partialguild)

<a id="class-guild"></a>
## Class `Guild`

**Qualified Name:** `discohook.guild.Guild`

Represents a Discord guild.

### Attributes

- **id** (`str`): The id of the guild.
- **name** (`str`): The name of the guild.
- **icon** (`str | None`): The icon hash of the guild.
- **icon_hash** (`str | None`): The icon hash of the guild.
- **splash** (`str | None`): The splash hash of the guild.
- **discovery_splash** (`str | None`): The discovery splash hash of the guild.
- **owner** (`bool | None`): Whether the user is the owner of the guild.
- **owner_id** (`str`): The id of the owner of the guild.
- **permissions** (`int | None`): The total permissions of the user in the guild (does not include channel overrides).
- **afk_channel_id** (`str | None`): The id of the afk channel.
- **afk_timeout** (`int`): The afk timeout in seconds.
- **widget_enabled** (`bool | None`): Whether the widget is enabled.
- **widget_channel_id** (`str | None`): The id of the channel for the widget.
- **verification_level** (`int`): The verification level required for the guild.
- **default_message_notifications** (`int`): The default message notifications level.
- **explicit_content_filter** (`int`): The explicit content filter level.
- **roles** (`list[Role]`): The roles in the guild.
- **emojis** (`list[Emoji]`): The emojis in the guild.
- **features** (`list[str]`): The features of the guild.
- **mfa_level** (`int`): The MFA level required for the guild.
- **application_id** (`str | None`): The application id of the guild creator if it is bot-created.
- **system_channel_id** (`str | None`): The id of the system channel.
- **system_channel_flags** (`int`): The system channel flags.
- **rules_channel_id** (`str | None`): The id of the rules channel.
- **max_presences** (`int | None`): The maximum number of presences for the guild.
- **max_members** (`int`): The maximum number of members for the guild.
- **vanity_url_code** (`str | None`): The vanity URL code of the guild.
- **description** (`str | None`): The description of the guild.
- **banner** (`str | None`): The banner hash of the guild.
- **premium_tier** (`int`): The premium tier of the guild.
- **premium_subscription_count** (`int`): The number of boosts of the guild.
- **preferred_locale** (`str`): The preferred locale of the guild.
- **public_updates_channel_id** (`str | None`): The id of the public updates channel.
- **max_video_channel_users** (`int | None`): The maximum number of users in a video channel.
- **approximate_member_count** (`int | None`): The approximate number of members in the guild.
- **approximate_presence_count** (`int | None`): The approximate number of presences in the guild.
- **welcome_screen** (`dict | None`): The welcome screen object of the guild.
- **nsfw_level** (`int`): The NSFW level of the guild.
- **stickers** (`list[Sticker]`): The stickers in the guild.
- **premium_progress_bar_enabled** (`bool | None`): Whether the premium progress bar is enabled.

### Inheritance

- `discohook.guild.PartialGuild`


<a id="class-partialguild"></a>
## Class `PartialGuild`

**Qualified Name:** `discohook.guild.PartialGuild`

Represents a partial guild.

### Method Index

- [create_channel](#partialguild-create-channel)
- [create_emoji](#partialguild-create-emoji)
- [create_role](#partialguild-create-role)
- [edit_channel_position](#partialguild-edit-channel-position)
- [fetch_channels](#partialguild-fetch-channels)
- [fetch_member](#partialguild-fetch-member)
- [fetch_roles](#partialguild-fetch-roles)

### Methods

<a id="partialguild-create-channel"></a>
#### `create_channel`

```python
async create_channel(self, name: str, *, type: discohook.enums.ChannelType = <ChannelType.guild_text: 0>, topic: str | None = None, bitrate: int | None = None, user_limit: int | None = None, rate_limit_per_user: int | None = None, position: int | None = None, permission_overwrites: List[Dict[str, Any]] | None = None, parent_id: str | None = None, nsfw: bool | None = None, rtc_region: str | None = None, video_quality_mode: int | None = None, default_auto_archive_duration: int | None = None, default_reaction_emoji: discohook.emoji.PartialEmoji | None = None, available_tags: List[Dict[str, Any]] | None = None, default_sort_order: int | None = None, reason: str | None = None) -> discohook.channel.Channel
```

Creates a channel in the guild. Requires the MANAGE_CHANNELS permission.

### Arguments

- **name** (`str`): Name of the channel (2-100 characters).
- **type** (`ChannelType`): Channel type.
- **topic** (`str | None`): Channel topic (0-1024 characters).
- **bitrate** (`int | None`): Channel bitrate (in bits) of the voice channel.
- **user_limit** (`int | None`): User limit of the voice channel.
- **rate_limit_per_user** (`int | None`): Amount of seconds a user has to wait before sending another message (0-21600). Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
- **position** (`int | None`): Sorting position of the channel.
- **permission_overwrites** (`List[Dict[str, Any]] | None`): Channel's permission overwrites.
- **parent_id** (`str | None`): ID of the parent category for a channel.
- **nsfw** (`bool | None`): Whether the channel is nsfw.
- **rtc_region** (`str | None`): ID of the voice region.
- **video_quality_mode** (`int | None`): Video quality mode of the voice channel, 1 when not present.
- **default_auto_archive_duration** (`int | None`): Default duration for newly created threads, in minutes, to automatically archive the thread.
- **default_reaction_emoji** (`PartialEmoji | None`): Default auto-emoji for newly created threads, custom guild emojis must be enabled.
- **available_tags** (`List[Dict[str, Any]] | None`): Channel tags used for public guilds.
- **default_sort_order** (`int | None`): Default sorting order for posts in a forum channel.
- **reason** (`str | None`): Reason for the creating the channel. Shows up on the audit log.

### Returns

- **Type:** `Channel`
  - Channel object.

<a id="partialguild-create-emoji"></a>
#### `create_emoji`

```python
async create_emoji(self, name: str, image: str, *, roles: List[str] | None = None, reason: str | None = None)
```

Creates a new emoji in the guild.

### Arguments

- **name** (`str`): Name of the new emoji.
- **image** (`str`): Image data of the emoji in base64 data uri format.
- **roles** (`List[str] | None`): List of role ids to limit the emoji to.
- **reason** (`str | None`): Reason for the new emoji creation. Shows up on the audit log.

### Returns

- **Type:** `Emoji`
  - Emoji object.

<a id="partialguild-create-role"></a>
#### `create_role`

```python
async create_role(self, name: str, *, permissions: List[discohook.permission.Permission] | None = None, color: int = 0, hoist: bool = False, mentionable: bool = True, icon_data_uri: str | None = None, unicode_emoji: str | None = None, reason: str | None = None)
```

Creates a new role in the guild.

### Arguments

- **name** (`str`): Name of the new role.
- **permissions** (`List[Permission] | None`): Permissions associated with the new role.
- **color** (`int`): Color for the new role. Defaults to 0.
- **hoist** (`bool`): If the new role should be hoisted. Defaults to False.
- **mentionable** (`bool`): If the new role should be mentionable. Defaults to True.
- **icon_data_uri** (`str | None`): Icon data URI for the new role.
- **unicode_emoji** (`str | None`): Emoji data for the new role.
- **reason** (`str | None`): Reason for the new role creation. Shows up on the audit log.

### Returns

- **Type:** `Role`
  - Role object.

<a id="partialguild-edit-channel-position"></a>
#### `edit_channel_position`

```python
async edit_channel_position(self, channel_id: str, *, position: int, lock_permissions: bool = False, parent_id: str | None = None)
```

Changes the position of the channel. Only available for guild channels.

### Arguments

- **channel_id** (`str`): ID of the channel to edit.
- **position** (`int`): New position of the channel.
- **lock_permissions** (`bool`): Whether to sync the permissions of the channel with the parent category.
- **parent_id** (`str | None`): ID of the parent category to move the channel to. If not provided, the channel will be moved to the root.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Response object.

<a id="partialguild-fetch-channels"></a>
#### `fetch_channels`

```python
async fetch_channels(self) -> List[discohook.channel.Channel]
```

Fetches all channels in the guild.

### Returns

- **Type:** `List[Channel]`
  - Channels in the guild.

<a id="partialguild-fetch-member"></a>
#### `fetch_member`

```python
async fetch_member(self, user_id: str) -> discohook.member.Member | None
```

Fetches a member from the guild.

### Arguments

- **user_id** (`str`): The id of the user to fetch.

### Returns

- **Type:** `Member | None`
  - Member object or None.

<a id="partialguild-fetch-roles"></a>
#### `fetch_roles`

```python
async fetch_roles(self) -> List[discohook.role.Role]
```

Fetches all roles in the guild.

### Returns

- **Type:** `List[Role]`
  - Roles in the guild.


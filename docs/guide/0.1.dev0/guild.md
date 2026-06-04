---
title: discohook.guild
---

# `discohook.guild`

## Classes

- [Guild](#class-guild)
- [PartialGuild](#class-partialguild)

<a id="class-guild"></a>
## Guild

`discohook.guild.Guild`

Represents a Discord guild.
#### _Attributes_

- _**id** (`str`): The id of the guild._
- _**name** (`str`): The name of the guild._
- _**icon** (`str | None`): The icon hash of the guild._
- _**icon_hash** (`str | None`): The icon hash of the guild._
- _**splash** (`str | None`): The splash hash of the guild._
- _**discovery_splash** (`str | None`): The discovery splash hash of the guild._
- _**owner** (`bool | None`): Whether the user is the owner of the guild._
- _**owner_id** (`str`): The id of the owner of the guild._
- _**permissions** (`int | None`): The total permissions of the user in the guild_ (does not include channel overrides).
- _**afk_channel_id** (`str | None`): The id of the afk channel._
- _**afk_timeout** (`int`): The afk timeout in seconds._
- _**widget_enabled** (`bool | None`): Whether the widget is enabled._
- _**widget_channel_id** (`str | None`): The id of the channel for the widget._
- _**verification_level** (`int`): The verification level required for the guild._
- _**default_message_notifications** (`int`): The default message notifications level._
- _**explicit_content_filter** (`int`): The explicit content filter level._
- _**roles** (`list[Role]`): The roles in the guild._
- _**emojis** (`list[Emoji]`): The emojis in the guild._
- _**features** (`list[str]`): The features of the guild._
- _**mfa_level** (`int`): The MFA level required for the guild._
- _**application_id** (`str | None`): The application id of the guild creator if it is_ bot-created.
- _**system_channel_id** (`str | None`): The id of the system channel._
- _**system_channel_flags** (`int`): The system channel flags._
- _**rules_channel_id** (`str | None`): The id of the rules channel._
- _**max_presences** (`int | None`): The maximum number of presences for the guild._
- _**max_members** (`int`): The maximum number of members for the guild._
- _**vanity_url_code** (`str | None`): The vanity URL code of the guild._
- _**description** (`str | None`): The description of the guild._
- _**banner** (`str | None`): The banner hash of the guild._
- _**premium_tier** (`int`): The premium tier of the guild._
- _**premium_subscription_count** (`int`): The number of boosts of the guild._
- _**preferred_locale** (`str`): The preferred locale of the guild._
- _**public_updates_channel_id** (`str | None`): The id of the public updates channel._
- _**max_video_channel_users** (`int | None`): The maximum number of users in a video_ channel.
- _**approximate_member_count** (`int | None`): The approximate number of members in the_ guild.
- _**approximate_presence_count** (`int | None`): The approximate number of presences in_ the guild.
- _**welcome_screen** (`dict | None`): The welcome screen object of the guild._
- _**nsfw_level** (`int`): The NSFW level of the guild._
- _**stickers** (`list[Sticker]`): The stickers in the guild._
- _**premium_progress_bar_enabled** (`bool | None`): Whether the premium progress bar is_ enabled.

### Inheritance

- `discohook.guild.PartialGuild`


<a id="class-partialguild"></a>
## PartialGuild

`discohook.guild.PartialGuild`

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
#### _Arguments_

- _**name** (`str`): Name of the channel (2-100 characters)._
- _**type** (`ChannelType`): Channel type._
- _**topic** (`str | None`): Channel topic (0-1024 characters)._
- _**bitrate** (`int | None`): Channel bitrate (in bits) of the voice channel._
- _**user_limit** (`int | None`): User limit of the voice channel._
- _**rate_limit_per_user** (`int | None`): Amount of seconds a user has to wait before sending another message (0-21600)._ Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
- _**position** (`int | None`): Sorting position of the channel._
- _**permission_overwrites** (`List[Dict[str, Any]] | None`): Channel's permission overwrites._
- _**parent_id** (`str | None`): ID of the parent category for a channel._
- _**nsfw** (`bool | None`): Whether the channel is nsfw._
- _**rtc_region** (`str | None`): ID of the voice region._
- _**video_quality_mode** (`int | None`): Video quality mode of the voice channel, 1 when not present._
- _**default_auto_archive_duration** (`int | None`): Default duration for newly created threads,_ in minutes, to automatically archive the thread.
- _**default_reaction_emoji** (`PartialEmoji | None`): Default auto-emoji for newly created threads,_ custom guild emojis must be enabled.
- _**available_tags** (`List[Dict[str, Any]] | None`): Channel tags used for public guilds._
- _**default_sort_order** (`int | None`): Default sorting order for posts in a forum channel._
- _**reason** (`str | None`): Reason for the creating the channel. Shows up on the audit log._
#### _Returns_

- **Type:** `Channel`
  - Channel object.

<a id="partialguild-create-emoji"></a>
#### `create_emoji`

```python
async create_emoji(self, name: str, image: str, *, roles: List[str] | None = None, reason: str | None = None)
```

Creates a new emoji in the guild.
#### _Arguments_

- _**name** (`str`): Name of the new emoji._
- _**image** (`str`): Image data of the emoji in base64 data uri format._
- _**roles** (`List[str] | None`): List of role ids to limit the emoji to._
- _**reason** (`str | None`): Reason for the new emoji creation. Shows up on the audit log._
#### _Returns_

- **Type:** `Emoji`
  - Emoji object.

<a id="partialguild-create-role"></a>
#### `create_role`

```python
async create_role(self, name: str, *, permissions: List[discohook.permission.Permission] | None = None, color: int = 0, hoist: bool = False, mentionable: bool = True, icon_data_uri: str | None = None, unicode_emoji: str | None = None, reason: str | None = None)
```

Creates a new role in the guild.
#### _Arguments_

- _**name** (`str`): Name of the new role._
- _**permissions** (`List[Permission] | None`): Permissions associated with the new role._
- _**color** (`int`): Color for the new role. Defaults to 0._
- _**hoist** (`bool`): If the new role should be hoisted. Defaults to False._
- _**mentionable** (`bool`): If the new role should be mentionable. Defaults to True._
- _**icon_data_uri** (`str | None`): Icon data URI for the new role._
- _**unicode_emoji** (`str | None`): Emoji data for the new role._
- _**reason** (`str | None`): Reason for the new role creation. Shows up on the audit log._
#### _Returns_

- **Type:** `Role`
  - Role object.

<a id="partialguild-edit-channel-position"></a>
#### `edit_channel_position`

```python
async edit_channel_position(self, channel_id: str, *, position: int, lock_permissions: bool = False, parent_id: str | None = None)
```

Changes the position of the channel. Only available for guild channels.
#### _Arguments_

- _**channel_id** (`str`): ID of the channel to edit._
- _**position** (`int`): New position of the channel._
- _**lock_permissions** (`bool`): Whether to sync the permissions of the channel with the parent category._
- _**parent_id** (`str | None`): ID of the parent category to move the channel to._ If not provided, the channel will be moved to the root.
#### _Returns_

- **Type:** `aiohttp.ClientResponse`
  - Response object.

<a id="partialguild-fetch-channels"></a>
#### `fetch_channels`

```python
async fetch_channels(self) -> List[discohook.channel.Channel]
```

Fetches all channels in the guild.
#### _Returns_

- **Type:** `List[Channel]`
  - Channels in the guild.

<a id="partialguild-fetch-member"></a>
#### `fetch_member`

```python
async fetch_member(self, user_id: str) -> discohook.member.Member | None
```

Fetches a member from the guild.
#### _Arguments_

- _**user_id** (`str`): The id of the user to fetch._
#### _Returns_

- **Type:** `Member | None`
  - Member object or None.

<a id="partialguild-fetch-roles"></a>
#### `fetch_roles`

```python
async fetch_roles(self) -> List[discohook.role.Role]
```

Fetches all roles in the guild.
#### _Returns_

- **Type:** `List[Role]`
  - Roles in the guild.


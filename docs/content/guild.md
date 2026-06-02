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

Represents a Discord guild. Subclass of :class:`PartialGuild`.

Attributes
----------
id: :class:`str`
The id of the guild.
name: :class:`str`
The name of the guild.
icon: Optional[:class:`str`]
The icon hash of the guild.
icon_hash: Optional[:class:`str`]
The icon hash of the guild.
splash: Optional[:class:`str`]
The splash hash of the guild.
discovery_splash: Optional[:class:`str`]
The discovery splash hash of the guild.
owner: Optional[:class:`bool`]
Whether the user is the owner of the guild.
owner_id: :class:`str`
The id of the owner of the guild.
permissions: Optional[:class:`int`]
The total permissions of the user in the guild (does not include channel overrides).
afk_channel_id: Optional[:class:`str`]
The id of the afk channel.
afk_timeout: :class:`int`
The afk timeout in seconds.
widget_enabled: Optional[:class:`bool`]
Whether the widget is enabled.
widget_channel_id: Optional[:class:`str`]
The id of the channel for the widget.
verification_level: :class:`int`
The verification level required for the guild.
default_message_notifications: :class:`int`
The default message notifications level.
explicit_content_filter: :class:`int`
The explicit content filter level.
roles: List[:class:`Role`]
The roles in the guild.
emojis: List[:class:`Emoji`]
The emojis in the guild.
features: List[:class:`str`]
The features of the guild.
mfa_level: :class:`int`
The mfa level required for the guild.
application_id: Optional[:class:`str`]
The application id of the guild creator if it is bot-created.
system_channel_id: Optional[:class:`str`]
The id of the system channel.
system_channel_flags: :class:`int`
The system channel flags.
rules_channel_id: Optional[:class:`str`]
The id of the rules channel.
max_presences: Optional[:class:`int`]
The maximum number of presences for the guild.
max_members: :class:`int`
The maximum number of members for the guild.
vanity_url_code: Optional[:class:`str`]
The vanity url code of the guild.
description: Optional[:class:`str`]
The description of the guild.
banner: Optional[:class:`str`]
The banner hash of the guild.
premium_tier: :class:`int`
The premium tier of the guild.
premium_subscription_count: :class:`int`
The number of boosts of the guild.
preferred_locale: :class:`str`
The preferred locale of the guild.
public_updates_channel_id: Optional[:class:`str`]
The id of the public updates channel.
max_video_channel_users: Optional[:class:`int`]
The maximum number of users in a video channel.
approximate_member_count: Optional[:class:`int`]
The approximate number of members in the guild.
approximate_presence_count: Optional[:class:`int`]
The approximate number of presences in the guild.
welcome_screen: Optional[:class:`dict`]
The welcome screen object of the guild.
nsfw_level: :class:`int`
The nsfw level of the guild.
stickers: List[:class:`Sticker`]
The stickers in the guild.
premium_progress_bar_enabled: Optional[:class:`bool`]
Whether the premium progress bar is enabled.

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

Parameters
----------
name: str
Name of the channel (2-100 characters)
type: ChannelType
The type of channel
topic: str
Channel topic (0-1024 characters)
bitrate: int
The bitrate (in bits) of the voice channel (voice only)
user_limit: int
The user limit of the voice channel (voice only)
rate_limit_per_user: int
Amount of seconds a user has to wait before sending another message (0-21600)
bots, as well as users with the permission manage_messages or manage_channel, are unaffected
position: int
Sorting position of the channel
permission_overwrites: List[Dict[str, Any]]
The channel's permission overwrites
parent_id: str
The id of the parent category for a channel (each parent category can contain up to 50 channels)
nsfw: bool
Whether the channel is nsfw
rtc_region: str
The id of the voice region
video_quality_mode: int
The camera video quality mode of the voice channel, 1 when not present
default_auto_archive_duration: int
The default duration for newly created threads, in minutes, to automatically archive the thread
after recent activity, can be set to: 60, 1440, 4320, 10080
default_reaction_emoji: PartialEmoji
The default auto-emoji for newly created threads, custom guild emojis must be enabled
available_tags: List[Dict[str, Any]]
The channel tags used for public guilds
default_sort_order: int
The default sorting order for posts in a forum channel

Returns
-------
:class:`Channel`

<a id="partialguild-create-emoji"></a>
#### `create_emoji`

```python
async create_emoji(self, name: str, image: str, *, roles: List[str] | None = None, reason: str | None = None)
```

Creates a new emoji for the guild.

Parameters
----------
name: :class:`str`
The name of the emoji.
image: :class:`str`
The image data of the emoji in base64 data uri format.
roles: Optional[List[:class:`str`]]
A list of role ids to limit the emoji to.

Returns
-------
:class:`Emoji`

<a id="partialguild-create-role"></a>
#### `create_role`

```python
async create_role(self, name: str, *, permissions: List[discohook.permission.Permission] | None = None, color: int = 0, hoist: bool = False, mentionable: bool | None = False, icon_data_uri: str | None = None, unicode_emoji: str | None = None, reason: str | None = None)
```

<a id="partialguild-edit-channel-position"></a>
#### `edit_channel_position`

```python
async edit_channel_position(self, channel_id: str, *, position: int, lock_permissions: bool = False, parent_id: str | None = None)
```

Changes the position of the channel. Only available for guild channels.

Parameters
----------
channel_id: :class:`str`
The id of the channel to move.
position: :class:`int`
The new position of the channel.
lock_permissions:
Whether to sync the permissions of the channel with the parent category.
parent_id: Optional[:class:`str`]
The id of the parent category to move the channel to.
If not provided, the channel will be moved to the root.

<a id="partialguild-fetch-channels"></a>
#### `fetch_channels`

```python
async fetch_channels(self) -> List[discohook.channel.Channel]
```

Fetches all channels in the guild.

Returns
-------
List[Channel]

<a id="partialguild-fetch-member"></a>
#### `fetch_member`

```python
async fetch_member(self, user_id: str) -> discohook.member.Member | None
```

Fetches a member from the guild.

Parameters
----------
user_id: :class:`str`
The id of the user to fetch.

Returns
-------
Optional[:class:`Member`]

<a id="partialguild-fetch-roles"></a>
#### `fetch_roles`

```python
async fetch_roles(self) -> List[discohook.role.Role]
```

Fetches all roles in the guild.

Returns
-------
List[Role]


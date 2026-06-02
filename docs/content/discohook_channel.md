---
title: discohook.channel
---

# `discohook.channel`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/channel.py`

## Classes

- [Channel](#class-channel)
- [PartialChannel](#class-partialchannel)

## Class `Channel`

Represents a discord channel object.

Attributes:
    id (str): ID of the channel.
    type (int): Type of the channel.
    guild_id (str): ID of the guild the channel belongs to.
    position (int): Position of the channel in the guild.
    permission_overwrites (List[dict]): A list of permission overwrites for the channel.
    name (str): Name of the channel.
    topic (str): Topic of the channel.
    nsfw (bool): Whether the channel is NSFW.
    last_message_id (str): ID of the last message sent in the channel.
    bitrate (int): Bitrate of the channel if it is a voice channel.
    user_limit (int): User limit of the channel if it is a voice channel.
    rate_limit_per_user (int): Rate limit per user of the channel if it is a text channel.
    recipients (List[dict]): A list of recipients of the channel if it is a DM channel.
    icon (str): Icon of the channel if it is a DM channel.
    owner_id (str): ID of the owner of the channel if it is a DM channel.
    application_id (str): ID of the application of the channel if it is a group DM channel.
    parent_id (str): ID of the parent category of the channel.
    last_pin_timestamp (str): Timestamp of the last pinned message in the channel.
    rtc_region (str): RTC region of the channel.
    video_quality_mode (int): Video quality mode of the channel.
    message_count (int): Message count of the channel.
    member_count (int): Member count of the channel.
    thread_metadata (dict): Thread metadata of the channel.
    member (dict): Member of the channel. Appears in thread channels.
    default_auto_archive_duration (int): Default auto archive duration of the channel. Appears in thread channels.
    permissions (str): Permissions of the channel.
    flags (int): Flags of the channel.
    total_message_sent (int): Total message sent of the channel.
    available_tags (List[str]): A list of available tags of the channel. Appears in thread channels.
    default_reaction_emoji (dict): Default reaction emoji of the channel. Appers in thread channels.
    default_thread_rate_limit_per_user (int): Default rate limit per user of the channel. Appears in thread channels.
    default_sort_order (int): Default sort order of the channel. Appears in forum channels.
    default_forum_layout (int): Default channel layout of the channel. Appears in forum channels.

### Inheritance

- `discohook.channel.PartialChannel`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/channel.py`
- Line: `317`

### Methods

#### `crosspost`

```python
crosspost(self, message_id: str)
```

Crosspost a message in the channel.

Args:
    message_id (str): The id of the message to crosspost.

Returns:
    Message: Message crossposted from the channel.

#### `delete`

```python
delete(self, *, reason: str | None = None)
```

Deletes the channel.

Args:
    reason (str): The reason for the purge. This will be shown in the audit log.

#### `edit`

```python
edit(self, *, name: str | None = None, type: discohook.enums.ChannelType | None = None, position: int | None = None, topic: str | None = None, nsfw: bool | None = None, rate_limit_per_user: int | None = None, bitrate: int | None = None, user_limit: int | None = None, permission_overwrites: List[Dict[str, Any]] | None = None, parent_id: str | None = None, rtc_region: str | None = None, video_quality_mode: int | None = None, default_auto_archive_duration: int | None = None, flags: int | None = None, available_tags: List[Dict[str, Any]] | None = None, icon: str | None = None, default_reaction_emoji: discohook.emoji.PartialEmoji | None = None, default_thread_rate_limit_per_user: int | None = None, default_sort_order: int | None = None, default_forum_layout: int | None = None, reason: str | None = None) -> 'Channel'
```

Edits all kinds of channels.

Args:
    name (str | None): Updated name of the channel.
    type (ChannelType): Updated type of the channel.
    position (int | None): Updated position of the channel.
    topic (str | None): Updated topic of the channel.
    nsfw (bool | None): Whether the channel should be marked as NSFW.
    rate_limit_per_user (int | None): Updated rate limit per user.
        Must be between 0 and 21600. Applies to text and forum channels.
    bitrate (int | None): Updated bitrate of the channel.
        Must be between 8000 and 96000. Applies to voice channels.
    user_limit (int | None): Updated user limit of the channel.
        Must be between 0 and 99. Applies to voice channels.
    permission_overwrites (List[dict] | None): Updated list permission overwrites to apply.
    parent_id (str | None): ID of the parent category to move the channel to.
    rtc_region (str | None): Updated region of the channel. Applies to voice channels.
    video_quality_mode (int | None): New video quality mode of the channel. Applies to voice channels.
    default_auto_archive_duration (int | None): Updated default auto archive duration of the channel.
        Applies to text and forum channels.
    flags (int | None): Updated flags of the channel. Applies to all channel types.
    available_tags (List[dict] | None): Updated available tags of the channel.
        Applies to text and forum channels.
    icon (str | None): Updated icon of the channel. Applies to Group DMs. Must be a base64 encoded string.
    default_reaction_emoji (PartialEmoji | None): Updated default reaction emoji of the channel.
        Applies to text and forum channels.
    default_thread_rate_limit_per_user (int | None): Updated default thread rate limit per user of the channel.
        Applies to text and forum channels.
    default_sort_order (int | None): Updated default sort order of the channel.
        Applies to text and forum channels.
    default_forum_layout (int | None): Updated default forum layout of the channel.
        Applies to text and forum channels.
    reason (str | None): The reason for the edit. This will be shown in the audit log.

Returns:
    Channel: Updated channel.

#### `fetch_message`

```python
fetch_message(self, message_id: str) -> discohook.message.Message | None
```

Fetches a message by its id from the channel.

Args:
    message_id (str): The id of the message to fetch.

Returns:
    Message: Message fetched from the channel.

#### `fetch_messages`

```python
fetch_messages(self, limit: int = 50, *, around: str | None = None, before: str | None = None, after: str | None = None) -> List[discohook.message.Message]
```

Fetch multiple messages from the channel.

Args:
    limit (int): Maximum number of messages to fetch.
    around (str): ID of the message to fetch around.
    before (str): ID of the message to fetch before.
    after (str): ID of the message to fetch after.

Returns:
    List[Message]: Messages fetched from the channel.

#### `fetch_webhooks`

```python
fetch_webhooks(self)
```

#### `from_dict`

```python
from_dict(client: 'Client', data: dict)
```

Create a channel object from a dictionary.

Args:
    client (Client): Client object.
    data (dict): Dictionary to create the channel from.

Returns:
    Channel: Channel object.

#### `from_response`

```python
from_response(client: 'Client', response: aiohttp.client_reqrep.ClientResponse)
```

Create a channel object from an aiohttp response.

Args:
    client (Client): Client object.
    response (aiohttp.ClientResponse): Response to create the channel from.

Returns:
    Channel: Channel object.

#### `purge`

```python
purge(self, limit: int = 50, *, before: str | None = None, after: str | None = None, around: str | None = None, reason: str | None = None) -> List[discohook.message.Message]
```

Delete messages from the channel in bulk.

Args:
    limit (int): Maximum number of messages to purge.
    around (str): ID of the message to purge around.
    before (str): ID of the message to purge before.
    after (str): ID of the message to purge after.
    reason (str): The reason for the purge. This will be shown in the audit log.

Returns:
    List[Message]: Messages purged from the channel.

#### `send`

```python
send(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Sends a message to the channel.

Args:
    components (Tuple(TopLevelComponent)): The components to send in the message.

Returns:
    Message: Message object returned by the API.

#### `start_thread`

```python
start_thread(self, name: str, *, auto_archive_duration: int = 60, invitable: bool = True, rate_limit_per_user: int = 0, reason: str | None = None) -> 'Channel'
```

Creates a thread from the channel.

Args:
    name (str): Name of the thread.
    auto_archive_duration (int): The duration in minutes to automatically archive the thread.
        Defaults to 60.
    invitable (bool): Whether non-moderators can add other non-moderators to the thread.
        Defaults to True.
    rate_limit_per_user (int): Amount of seconds a user has to wait before
        sending another message (0-21600). Defaults to 0.
    reason (str | None): The reason for the action. This will be shown in the audit log.

Returns:
    Channel: Thread channel.


## Class `PartialChannel`

Represents a partial discord channel object.

Args:
    channel_id (str): ID of the channel.
    guild_id (str | None): Guild id of the channel.
    client (Client): Client that the channel belongs to.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/channel.py`
- Line: `16`

### Methods

#### `crosspost`

```python
crosspost(self, message_id: str)
```

Crosspost a message in the channel.

Args:
    message_id (str): The id of the message to crosspost.

Returns:
    Message: Message crossposted from the channel.

#### `delete`

```python
delete(self, *, reason: str | None = None)
```

Deletes the channel.

Args:
    reason (str): The reason for the purge. This will be shown in the audit log.

#### `edit`

```python
edit(self, *, name: str | None = None, type: discohook.enums.ChannelType | None = None, position: int | None = None, topic: str | None = None, nsfw: bool | None = None, rate_limit_per_user: int | None = None, bitrate: int | None = None, user_limit: int | None = None, permission_overwrites: List[Dict[str, Any]] | None = None, parent_id: str | None = None, rtc_region: str | None = None, video_quality_mode: int | None = None, default_auto_archive_duration: int | None = None, flags: int | None = None, available_tags: List[Dict[str, Any]] | None = None, icon: str | None = None, default_reaction_emoji: discohook.emoji.PartialEmoji | None = None, default_thread_rate_limit_per_user: int | None = None, default_sort_order: int | None = None, default_forum_layout: int | None = None, reason: str | None = None) -> 'Channel'
```

Edits all kinds of channels.

Args:
    name (str | None): Updated name of the channel.
    type (ChannelType): Updated type of the channel.
    position (int | None): Updated position of the channel.
    topic (str | None): Updated topic of the channel.
    nsfw (bool | None): Whether the channel should be marked as NSFW.
    rate_limit_per_user (int | None): Updated rate limit per user.
        Must be between 0 and 21600. Applies to text and forum channels.
    bitrate (int | None): Updated bitrate of the channel.
        Must be between 8000 and 96000. Applies to voice channels.
    user_limit (int | None): Updated user limit of the channel.
        Must be between 0 and 99. Applies to voice channels.
    permission_overwrites (List[dict] | None): Updated list permission overwrites to apply.
    parent_id (str | None): ID of the parent category to move the channel to.
    rtc_region (str | None): Updated region of the channel. Applies to voice channels.
    video_quality_mode (int | None): New video quality mode of the channel. Applies to voice channels.
    default_auto_archive_duration (int | None): Updated default auto archive duration of the channel.
        Applies to text and forum channels.
    flags (int | None): Updated flags of the channel. Applies to all channel types.
    available_tags (List[dict] | None): Updated available tags of the channel.
        Applies to text and forum channels.
    icon (str | None): Updated icon of the channel. Applies to Group DMs. Must be a base64 encoded string.
    default_reaction_emoji (PartialEmoji | None): Updated default reaction emoji of the channel.
        Applies to text and forum channels.
    default_thread_rate_limit_per_user (int | None): Updated default thread rate limit per user of the channel.
        Applies to text and forum channels.
    default_sort_order (int | None): Updated default sort order of the channel.
        Applies to text and forum channels.
    default_forum_layout (int | None): Updated default forum layout of the channel.
        Applies to text and forum channels.
    reason (str | None): The reason for the edit. This will be shown in the audit log.

Returns:
    Channel: Updated channel.

#### `fetch_message`

```python
fetch_message(self, message_id: str) -> discohook.message.Message | None
```

Fetches a message by its id from the channel.

Args:
    message_id (str): The id of the message to fetch.

Returns:
    Message: Message fetched from the channel.

#### `fetch_messages`

```python
fetch_messages(self, limit: int = 50, *, around: str | None = None, before: str | None = None, after: str | None = None) -> List[discohook.message.Message]
```

Fetch multiple messages from the channel.

Args:
    limit (int): Maximum number of messages to fetch.
    around (str): ID of the message to fetch around.
    before (str): ID of the message to fetch before.
    after (str): ID of the message to fetch after.

Returns:
    List[Message]: Messages fetched from the channel.

#### `fetch_webhooks`

```python
fetch_webhooks(self)
```

#### `purge`

```python
purge(self, limit: int = 50, *, before: str | None = None, after: str | None = None, around: str | None = None, reason: str | None = None) -> List[discohook.message.Message]
```

Delete messages from the channel in bulk.

Args:
    limit (int): Maximum number of messages to purge.
    around (str): ID of the message to purge around.
    before (str): ID of the message to purge before.
    after (str): ID of the message to purge after.
    reason (str): The reason for the purge. This will be shown in the audit log.

Returns:
    List[Message]: Messages purged from the channel.

#### `send`

```python
send(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Sends a message to the channel.

Args:
    components (Tuple(TopLevelComponent)): The components to send in the message.

Returns:
    Message: Message object returned by the API.

#### `start_thread`

```python
start_thread(self, name: str, *, auto_archive_duration: int = 60, invitable: bool = True, rate_limit_per_user: int = 0, reason: str | None = None) -> 'Channel'
```

Creates a thread from the channel.

Args:
    name (str): Name of the thread.
    auto_archive_duration (int): The duration in minutes to automatically archive the thread.
        Defaults to 60.
    invitable (bool): Whether non-moderators can add other non-moderators to the thread.
        Defaults to True.
    rate_limit_per_user (int): Amount of seconds a user has to wait before
        sending another message (0-21600). Defaults to 0.
    reason (str | None): The reason for the action. This will be shown in the audit log.

Returns:
    Channel: Thread channel.


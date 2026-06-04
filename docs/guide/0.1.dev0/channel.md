---
title: discohook.channel
---

# `discohook.channel`

## Classes

- [Channel](#class-channel)
- [PartialChannel](#class-partialchannel)

<a id="class-channel"></a>
## Channel

`discohook.channel.Channel`

Represents a discord channel object.
#### _Attributes_

- _**id** (`str`): ID of the channel._
- _**type** (`int`): Type of the channel._
- _**guild_id** (`str`): ID of the guild the channel belongs to._
- _**position** (`int`): Position of the channel in the guild._
- _**permission_overwrites** (`List[dict]`): A list of permission overwrites for the channel._
- _**name** (`str`): Name of the channel._
- _**topic** (`str`): Topic of the channel._
- _**nsfw** (`bool`): Whether the channel is NSFW._
- _**last_message_id** (`str`): ID of the last message sent in the channel._
- _**bitrate** (`int`): Bitrate of the channel if it is a voice channel._
- _**user_limit** (`int`): User limit of the channel if it is a voice channel._
- _**rate_limit_per_user** (`int`): Rate limit per user of the channel if it is a text channel._
- _**recipients** (`List[dict]`): A list of recipients of the channel if it is a DM channel._
- _**icon** (`str`): Icon of the channel if it is a DM channel._
- _**owner_id** (`str`): ID of the owner of the channel if it is a DM channel._
- _**application_id** (`str`): ID of the application of the channel if it is a group DM channel._
- _**parent_id** (`str`): ID of the parent category of the channel._
- _**last_pin_timestamp** (`str`): Timestamp of the last pinned message in the channel._
- _**rtc_region** (`str`): RTC region of the channel._
- _**video_quality_mode** (`int`): Video quality mode of the channel._
- _**message_count** (`int`): Message count of the channel._
- _**member_count** (`int`): Member count of the channel._
- _**thread_metadata** (`dict`): Thread metadata of the channel._
- _**member** (`dict`): Member of the channel. Appears in thread channels._
- _**default_auto_archive_duration** (`int`): Default auto archive duration of the channel. Appears in thread channels._
- _**permissions** (`str`): Permissions of the channel._
- _**flags** (`int`): Flags of the channel._
- _**total_message_sent** (`int`): Total message sent of the channel._
- _**available_tags** (`List[str]`): A list of available tags of the channel. Appears in thread channels._
- _**default_reaction_emoji** (`dict`): Default reaction emoji of the channel. Appers in thread channels._
- _**default_thread_rate_limit_per_user** (`int`): Default rate limit per user of the channel. Appears in thread channels._
- _**default_sort_order** (`int`): Default sort order of the channel. Appears in forum channels._
- _**default_forum_layout** (`int`): Default channel layout of the channel. Appears in forum channels._

### Inheritance

- `discohook.channel.PartialChannel`

### Method Index

- [from_dict](#channel-from-dict)
- [from_response](#channel-from-response)

### Methods

<a id="channel-from-dict"></a>
#### `from_dict`

Create a channel object from a dictionary.
#### _Arguments_

- _**client** (`Client`): Client object._
- _**data** (`dict`): Dictionary to create the channel from._
#### _Returns_

- **Type:** `Channel`
  - Channel object.

<a id="channel-from-response"></a>
#### `from_response`

Create a channel object from an aiohttp response.
#### _Arguments_

- _**client** (`Client`): Client object._
- _**response** (`aiohttp.ClientResponse`): Response to create the channel from._
#### _Returns_

- **Type:** `Channel`
  - Channel object.


<a id="class-partialchannel"></a>
## PartialChannel

`discohook.channel.PartialChannel`

Represents a partial discord channel object.
#### _Arguments_

- _**channel_id** (`str`): ID of the channel._
- _**guild_id** (`str | None`): Guild id of the channel._
- _**client** (`Client`): Client that the channel belongs to._

### Property Index

- [mention](#partialchannel-mention)

### Method Index

- [crosspost](#partialchannel-crosspost)
- [delete](#partialchannel-delete)
- [edit](#partialchannel-edit)
- [fetch_message](#partialchannel-fetch-message)
- [fetch_messages](#partialchannel-fetch-messages)
- [purge](#partialchannel-purge)
- [send](#partialchannel-send)
- [start_thread](#partialchannel-start-thread)

### Properties

<a id="partialchannel-mention"></a>
#### `mention`

Builds channel mention formatting.
#### _Returns_

- **Type:** `str`
  - String representation of the channel mention.

### Methods

<a id="partialchannel-crosspost"></a>
#### `crosspost`

```python
async crosspost(self, message_id: str)
```

Crosspost a message in the channel.
#### _Arguments_

- _**message_id** (`str`): The id of the message to crosspost._
#### _Returns_

- **Type:** `Message`
  - Message crossposted from the channel.

<a id="partialchannel-delete"></a>
#### `delete`

```python
async delete(self, *, reason: str | None = None)
```

Deletes the channel.
#### _Arguments_

- _**reason** (`str`): The reason for the purge. This will be shown in the audit log._

<a id="partialchannel-edit"></a>
#### `edit`

```python
async edit(self, *, name: str | None = None, type: discohook.enums.ChannelType | None = None, position: int | None = None, topic: str | None = None, nsfw: bool | None = None, rate_limit_per_user: int | None = None, bitrate: int | None = None, user_limit: int | None = None, permission_overwrites: List[Dict[str, Any]] | None = None, parent_id: str | None = None, rtc_region: str | None = None, video_quality_mode: int | None = None, default_auto_archive_duration: int | None = None, flags: int | None = None, available_tags: List[Dict[str, Any]] | None = None, icon: str | None = None, default_reaction_emoji: discohook.emoji.PartialEmoji | None = None, default_thread_rate_limit_per_user: int | None = None, default_sort_order: int | None = None, default_forum_layout: int | None = None, reason: str | None = None) -> 'Channel'
```

Edits all kinds of channels.
#### _Arguments_

- _**name** (`str | None`): Updated name of the channel._
- _**type** (`ChannelType`): Updated type of the channel._
- _**position** (`int | None`): Updated position of the channel._
- _**topic** (`str | None`): Updated topic of the channel._
- _**nsfw** (`bool | None`): Whether the channel should be marked as NSFW._
- _**rate_limit_per_user** (`int | None`): Updated rate limit per user._ Must be between 0 and 21600. Applies to text and forum channels.
- _**bitrate** (`int | None`): Updated bitrate of the channel._ Must be between 8000 and 96000. Applies to voice channels.
- _**user_limit** (`int | None`): Updated user limit of the channel._ Must be between 0 and 99. Applies to voice channels.
- _**permission_overwrites** (`List[dict] | None`): Updated list permission overwrites to apply._
- _**parent_id** (`str | None`): ID of the parent category to move the channel to._
- _**rtc_region** (`str | None`): Updated region of the channel. Applies to voice channels._
- _**video_quality_mode** (`int | None`): New video quality mode of the channel. Applies to voice channels._
- _**default_auto_archive_duration** (`int | None`): Updated default auto archive duration of the channel._ Applies to text and forum channels.
- _**flags** (`int | None`): Updated flags of the channel. Applies to all channel types._
- _**available_tags** (`List[dict] | None`): Updated available tags of the channel._ Applies to text and forum channels.
- _**icon** (`str | None`): Updated icon of the channel. Applies to Group DMs. Must be a base64 encoded string._
- _**default_reaction_emoji** (`PartialEmoji | None`): Updated default reaction emoji of the channel._ Applies to text and forum channels.
- _**default_thread_rate_limit_per_user** (`int | None`): Updated default thread rate limit per user of the channel._ Applies to text and forum channels.
- _**default_sort_order** (`int | None`): Updated default sort order of the channel._ Applies to text and forum channels.
- _**default_forum_layout** (`int | None`): Updated default forum layout of the channel._ Applies to text and forum channels.
- _**reason** (`str | None`): The reason for the edit. This will be shown in the audit log._
#### _Returns_

- **Type:** `Channel`
  - Updated channel.

<a id="partialchannel-fetch-message"></a>
#### `fetch_message`

```python
async fetch_message(self, message_id: str) -> discohook.message.Message | None
```

Fetches a message by its id from the channel.
#### _Arguments_

- _**message_id** (`str`): The id of the message to fetch._
#### _Returns_

- **Type:** `Message`
  - Message fetched from the channel.

<a id="partialchannel-fetch-messages"></a>
#### `fetch_messages`

```python
async fetch_messages(self, limit: int = 50, *, around: str | None = None, before: str | None = None, after: str | None = None) -> List[discohook.message.Message]
```

Fetch multiple messages from the channel.
#### _Arguments_

- _**limit** (`int`): Maximum number of messages to fetch._
- _**around** (`str`): ID of the message to fetch around._
- _**before** (`str`): ID of the message to fetch before._
- _**after** (`str`): ID of the message to fetch after._
#### _Returns_

- **Type:** `List[Message]`
  - Messages fetched from the channel.

<a id="partialchannel-purge"></a>
#### `purge`

```python
async purge(self, limit: int = 50, *, before: str | None = None, after: str | None = None, around: str | None = None, reason: str | None = None) -> List[discohook.message.Message]
```

Delete messages from the channel in bulk.
#### _Arguments_

- _**limit** (`int`): Maximum number of messages to purge._
- _**around** (`str`): ID of the message to purge around._
- _**before** (`str`): ID of the message to purge before._
- _**after** (`str`): ID of the message to purge after._
- _**reason** (`str`): The reason for the purge. This will be shown in the audit log._
#### _Returns_

- **Type:** `List[Message]`
  - Messages purged from the channel.

<a id="partialchannel-send"></a>
#### `send`

```python
async send(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Sends a message to the channel.
#### _Arguments_

components (Tuple(TopLevelComponent)): The components to send in the message.
#### _Returns_

- **Type:** `Message`
  - Message object returned by the API.

<a id="partialchannel-start-thread"></a>
#### `start_thread`

```python
async start_thread(self, name: str, *, auto_archive_duration: int = 60, invitable: bool = True, rate_limit_per_user: int = 0, reason: str | None = None) -> 'Channel'
```

Creates a thread from the channel.
#### _Arguments_

- _**name** (`str`): Name of the thread._
- _**auto_archive_duration** (`int`): The duration in minutes to automatically archive the thread._ Defaults to 60.
- _**invitable** (`bool`): Whether non-moderators can add other non-moderators to the thread._ Defaults to True.
- _**rate_limit_per_user** (`int`): Amount of seconds a user has to wait before_ sending another message (0-21600). Defaults to 0.
- _**reason** (`str | None`): The reason for the action. This will be shown in the audit log._
#### _Returns_

- **Type:** `Channel`
  - Thread channel.


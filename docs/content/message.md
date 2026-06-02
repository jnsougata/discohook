---
title: discohook.message
---

# `discohook.message`

## Classes

- [Message](#class-message)
- [MessageInteraction](#class-messageinteraction)

<a id="class-message"></a>
## Class `Message`

**Qualified Name:** `discohook.message.Message`

Represents a Discord message.

Properties
----------
id: :class:`str`
The id of the message.
channel_id: :class:`str`
The id of the channel the message was sent in.
author: :class:`User`
The author of the message.
content: :class:`str`
The content of the message.
timestamp: :class:`str`
The timestamp of the message.
edited_timestamp: Optional[:class:`str`]
The timestamp of when the message was last edited.
tts: :class:`bool`
Whether the message was sent using text-to-speech.
mention_everyone: :class:`bool`
Whether the message mentions everyone.
mentions: List[:class:`User`]
The users mentioned in the message.
mention_roles: List[:class:`Role`]
The roles mentioned in the message.
mention_channels: Optional[:class:`dict`]
The channels mentioned in the message.
attachments: :class:`dict`
The attachments in the message.
embeds: :class:`list`
The embeds in the message.
reactions: Optional[:class:`list`]
The reactions in the message.
...

### Property Index

- [activity](#message-activity)
- [application](#message-application)
- [application_id](#message-application-id)
- [attachments](#message-attachments)
- [author](#message-author)
- [channel_id](#message-channel-id)
- [components](#message-components)
- [content](#message-content)
- [edited_timestamp](#message-edited-timestamp)
- [embeds](#message-embeds)
- [flags](#message-flags)
- [id](#message-id)
- [interaction](#message-interaction)
- [mention_channels](#message-mention-channels)
- [mention_everyone](#message-mention-everyone)
- [mention_roles](#message-mention-roles)
- [mentions](#message-mentions)
- [message_reference](#message-message-reference)
- [nonce](#message-nonce)
- [pinned](#message-pinned)
- [poll](#message-poll)
- [position](#message-position)
- [reactions](#message-reactions)
- [referenced_message](#message-referenced-message)
- [sticker_items](#message-sticker-items)
- [stickers](#message-stickers)
- [thread](#message-thread)
- [timestamp](#message-timestamp)
- [tts](#message-tts)
- [type](#message-type)
- [webhook_id](#message-webhook-id)

### Method Index

- [add_reaction](#message-add-reaction)
- [crosspost](#message-crosspost)
- [delete](#message-delete)
- [edit](#message-edit)
- [pin](#message-pin)
- [remove_reaction](#message-remove-reaction)
- [remove_reactions](#message-remove-reactions)
- [reply](#message-reply)
- [start_thread](#message-start-thread)
- [unpin](#message-unpin)

### Properties

<a id="message-activity"></a>
#### `activity`

<a id="message-application"></a>
#### `application`

<a id="message-application-id"></a>
#### `application_id`

<a id="message-attachments"></a>
#### `attachments`

<a id="message-author"></a>
#### `author`

<a id="message-channel-id"></a>
#### `channel_id`

<a id="message-components"></a>
#### `components`

<a id="message-content"></a>
#### `content`

<a id="message-edited-timestamp"></a>
#### `edited_timestamp`

<a id="message-embeds"></a>
#### `embeds`

<a id="message-flags"></a>
#### `flags`

<a id="message-id"></a>
#### `id`

<a id="message-interaction"></a>
#### `interaction`

<a id="message-mention-channels"></a>
#### `mention_channels`

<a id="message-mention-everyone"></a>
#### `mention_everyone`

<a id="message-mention-roles"></a>
#### `mention_roles`

<a id="message-mentions"></a>
#### `mentions`

<a id="message-message-reference"></a>
#### `message_reference`

<a id="message-nonce"></a>
#### `nonce`

<a id="message-pinned"></a>
#### `pinned`

<a id="message-poll"></a>
#### `poll`

<a id="message-position"></a>
#### `position`

<a id="message-reactions"></a>
#### `reactions`

<a id="message-referenced-message"></a>
#### `referenced_message`

<a id="message-sticker-items"></a>
#### `sticker_items`

<a id="message-stickers"></a>
#### `stickers`

<a id="message-thread"></a>
#### `thread`

<a id="message-timestamp"></a>
#### `timestamp`

<a id="message-tts"></a>
#### `tts`

<a id="message-type"></a>
#### `type`

<a id="message-webhook-id"></a>
#### `webhook_id`

### Methods

<a id="message-add-reaction"></a>
#### `add_reaction`

```python
async add_reaction(self, emoji: discohook.emoji.PartialEmoji | str)
```

Creates a reaction on the message.

Parameters
----------
emoji: Union[Emoji, str]
The emoji to react with.

<a id="message-crosspost"></a>
#### `crosspost`

```python
async crosspost(self)
```

Crossposts the message.

<a id="message-delete"></a>
#### `delete`

```python
async delete(self, *, reason: str | None = None)
```

Deletes the message.

<a id="message-edit"></a>
#### `edit`

```python
async edit(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Edits the message.

Parameters
----------
components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]
The components to edit the message with. This can be a mix of different component types.

<a id="message-pin"></a>
#### `pin`

```python
async pin(self, *, reason: str | None = None)
```

Pins the message to the channel.

<a id="message-remove-reaction"></a>
#### `remove_reaction`

```python
async remove_reaction(self, emoji: discohook.emoji.PartialEmoji | str, user_id: str | None = None)
```

Removes a reaction on the message.

Parameters
----------
emoji: Union[Emoji, str]
The emoji to delete.
user_id: Optional[str]
The user to delete the reaction of.

<a id="message-remove-reactions"></a>
#### `remove_reactions`

```python
async remove_reactions(self, emoji: discohook.emoji.PartialEmoji | str | None = None)
```

Removes all reactions on the message.

Parameters
----------
emoji: Union[Emoji, str, None]
The emoji to remove reactions of.

<a id="message-reply"></a>
#### `reply`

```python
async reply(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, allowed_mentions: discohook.models.AllowedMentions | None = None, mention_author: bool | None = None)
```

Replies to the message.

Parameters
----------
components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]
The components to include in the reply. This can be a mix of different component types.
allowed_mentions: Optional[AllowedMentions]
The allowed mentions for the message.
mention_author: Optional[bool]
Whether the author should be mentioned.

Returns
-------
Message

<a id="message-start-thread"></a>
#### `start_thread`

```python
async start_thread(self, name: str, *, auto_archive_duration: int = 60, rate_limit_per_user: int = 0, reason: str | None = None) -> aiohttp.client_reqrep.ClientResponse
```

Starts a thread from the message.

Parameters
----------
name: str
The name of the thread.
auto_archive_duration: int
The duration of the thread in minutes.
rate_limit_per_user: int
The rate limit per user in seconds.
reason: Optional[str]
The reason for starting the thread.

Returns
-------
aiohttp.ClientResponse

<a id="message-unpin"></a>
#### `unpin`

```python
async unpin(self, *, reason: str | None = None)
```

Unpins the message from the channel.


<a id="class-messageinteraction"></a>
## Class `MessageInteraction`

**Qualified Name:** `discohook.message.MessageInteraction`

Represents a partial interaction received with message.

### Property Index

- [id](#messageinteraction-id)
- [token](#messageinteraction-token)
- [type](#messageinteraction-type)
- [user](#messageinteraction-user)

### Properties

<a id="messageinteraction-id"></a>
#### `id`

The id of the interaction.

<a id="messageinteraction-token"></a>
#### `token`

The token of the interaction.

<a id="messageinteraction-type"></a>
#### `type`

The type of interaction.

<a id="messageinteraction-user"></a>
#### `user`

The user who invoked the interaction.


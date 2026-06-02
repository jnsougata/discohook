---
title: discohook.message
---

# `discohook.message`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/message.py`

## Classes

- [Message](#class-message)
- [MessageInteraction](#class-messageinteraction)

## Class `Message`

Represents a Discord message.

### Properties

- **id** (`:class:`str``)
    The id of the message.
- **channel_id** (`:class:`str``)
    The id of the channel the message was sent in.
- **author** (`:class:`User``)
    The author of the message.
- **content** (`:class:`str``)
    The content of the message.
- **timestamp** (`:class:`str``)
    The timestamp of the message.
- **edited_timestamp** (`Optional[:class:`str`]`)
    The timestamp of when the message was last edited.
- **tts** (`:class:`bool``)
    Whether the message was sent using text-to-speech.
- **mention_everyone** (`:class:`bool``)
    Whether the message mentions everyone.
- **mentions** (`List[:class:`User`]`)
    The users mentioned in the message.
- **mention_roles** (`List[:class:`Role`]`)
    The roles mentioned in the message.
- **mention_channels** (`Optional[:class:`dict`]`)
    The channels mentioned in the message.
- **attachments** (`:class:`dict``)
    The attachments in the message.
- **embeds** (`:class:`list``)
    The embeds in the message.
- **reactions** (`Optional[:class:`list`]`)
    The reactions in the message.
    ...

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/message.py`
- Line: `58`

### Methods

#### `add_reaction`

```python
add_reaction(self, emoji: discohook.emoji.PartialEmoji | str)
```

Creates a reaction on the message.

### Parameters

- **emoji** (`Union[Emoji, str]`)
    The emoji to react with.

#### `crosspost`

```python
crosspost(self)
```

Crossposts the message.

#### `delete`

```python
delete(self, *, reason: str | None = None)
```

Deletes the message.

#### `edit`

```python
edit(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Edits the message.

### Parameters

- **components** (`Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]`)
    The components to edit the message with. This can be a mix of different component types.

#### `pin`

```python
pin(self, *, reason: str | None = None)
```

Pins the message to the channel.

#### `remove_reaction`

```python
remove_reaction(self, emoji: discohook.emoji.PartialEmoji | str, user_id: str | None = None)
```

Removes a reaction on the message.

### Parameters

- **emoji** (`Union[Emoji, str]`)
    The emoji to delete.
- **user_id** (`Optional[str]`)
    The user to delete the reaction of.

#### `remove_reactions`

```python
remove_reactions(self, emoji: discohook.emoji.PartialEmoji | str | None = None)
```

Removes all reactions on the message.

### Parameters

- **emoji** (`Union[Emoji, str, None]`)
    The emoji to remove reactions of.

#### `reply`

```python
reply(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, allowed_mentions: discohook.models.AllowedMentions | None = None, mention_author: bool | None = None)
```

Replies to the message.

### Parameters

- **components** (`Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]`)
    The components to include in the reply. This can be a mix of different component types.
- **allowed_mentions** (`Optional[AllowedMentions]`)
    The allowed mentions for the message.
- **mention_author** (`Optional[bool]`)
    Whether the author should be mentioned.

### Returns

Message

#### `start_thread`

```python
start_thread(self, name: str, *, auto_archive_duration: int = 60, rate_limit_per_user: int = 0, reason: str | None = None) -> aiohttp.client_reqrep.ClientResponse
```

Starts a thread from the message.

### Parameters

- **name** (`str`)
    The name of the thread.
- **auto_archive_duration** (`int`)
    The duration of the thread in minutes.
- **rate_limit_per_user** (`int`)
    The rate limit per user in seconds.
- **reason** (`Optional[str]`)
    The reason for starting the thread.

### Returns

aiohttp.ClientResponse

#### `unpin`

```python
unpin(self, *, reason: str | None = None)
```

Unpins the message from the channel.


## Class `MessageInteraction`

Represents a partial interaction received with message.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/message.py`
- Line: `20`


---
title: discohook.webhook
---

# `discohook.webhook`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/webhook.py`

## Classes

- [Webhook](#class-webhook)

## Class `Webhook`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/webhook.py`
- Line: `21`

### Methods

#### `delete`

```python
delete(self, *, reason: str | None = None)
```

Deletes the webhook.
### Returns

None

#### `delete_message`

```python
delete_message(self, message_id: str) -> aiohttp.client_reqrep.ClientResponse
```

Deletes a message from the webhook.

### Parameters

- **message_id** (`:class:`str``)
    The id of the message to delete.

### Returns

aiohttp.ClientResponse

#### `edit_message`

```python
edit_message(self, message_id: str, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container, thread_id: str | None = None) -> discohook.message.Message
```

Edits a message from the webhook.

### Parameters

- **message_id** (`:class:`str``)
    The id of the message to edit.
*components:
    Components to be sent with the message.
- **thread_id** (`Optional[:class:`str`]`)
    The thread id the message is in.

### Returns

:class:`Message`

#### `fetch`

```python
fetch(id: str, *, token: str | None = None, client: ForwardRef('Client') | None = None)
```

Fetches the webhook from Discord.

### Returns

:class:`Webhook`
    The fetched webhook.

#### `fetch_message`

```python
fetch_message(self, message_id: str, *, thread_id: str | None = None)
```

Fetches a message sent by the webhook.

### Parameters

- **message_id** (`:class:`str``)
    The id of the message to edit.
- **thread_id** (`Optional[:class:`str`]`)
    The thread id the message is in.

### Returns

:class:`Message`

#### `from_url`

```python
from_url(url: str, *, client: ForwardRef('Client') | None = None) -> 'Webhook'
```

#### `modify`

```python
modify(self, name: str | None = None, image_base64: str | None = None, channel_id: str | None = None, reason: str | None = None)
```

Edits the webhook.

### Parameters

- **name** (`Optional[:class:`str`]`)
    The new name of the webhook.
- **image_base64** (`Optional[:class:`str`]`)
    The new avatar of the webhook.
- **channel_id** (`Optional[:class:`str`]`)
    The new channel id of the webhook.
- **reason** (`Optional[:class:`str`]`)
    The reason for editing the webhook to be logged.

### Returns

:class:`Webhook`

### Notes

The image must be a base64 encoded string.
All parameters are optional.

#### `send`

```python
send(self, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container, username: str | None = None, avatar_url: str | None = None, thread_name: str | None = None, wait: bool = False, thread_id: str | None = None) -> aiohttp.client_reqrep.ClientResponse
```

Sends a message to the webhook.

### Parameters

*components:
    Components to be sent with the message.
username:
    The username of the webhook.
avatar_url:
    The avatar url of the webhook. (Overrides the webhook's avatar)
- **thread_name** (`Optional[:class:`str`]`)
    The name of the thread to create.
- **wait** (`:class:`bool``)
    Waits for server confirmation of the message.
- **thread_id** (`Optional[:class:`str`]`)
    Whether to send to a specified thread within the webhook's channel.

### Returns

aiohttp.ClientResponse


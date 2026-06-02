---
title: discohook.webhook
---

# `discohook.webhook`

## Classes

- [Webhook](#class-webhook)

<a id="class-webhook"></a>
## Class `Webhook`

**Qualified Name:** `discohook.webhook.Webhook`

### Property Index

- [application_id](#webhook-application-id)
- [avatar](#webhook-avatar)
- [channel_id](#webhook-channel-id)
- [guild_id](#webhook-guild-id)
- [id](#webhook-id)
- [name](#webhook-name)
- [source_channel](#webhook-source-channel)
- [source_guild](#webhook-source-guild)
- [token](#webhook-token)
- [type](#webhook-type)
- [url](#webhook-url)
- [user](#webhook-user)

### Method Index

- [delete](#webhook-delete)
- [delete_message](#webhook-delete-message)
- [edit_message](#webhook-edit-message)
- [fetch](#webhook-fetch)
- [fetch_message](#webhook-fetch-message)
- [from_url](#webhook-from-url)
- [modify](#webhook-modify)
- [send](#webhook-send)

### Properties

<a id="webhook-application-id"></a>
#### `application_id`

<a id="webhook-avatar"></a>
#### `avatar`

<a id="webhook-channel-id"></a>
#### `channel_id`

<a id="webhook-guild-id"></a>
#### `guild_id`

<a id="webhook-id"></a>
#### `id`

<a id="webhook-name"></a>
#### `name`

<a id="webhook-source-channel"></a>
#### `source_channel`

<a id="webhook-source-guild"></a>
#### `source_guild`

<a id="webhook-token"></a>
#### `token`

<a id="webhook-type"></a>
#### `type`

<a id="webhook-url"></a>
#### `url`

<a id="webhook-user"></a>
#### `user`

### Methods

<a id="webhook-delete"></a>
#### `delete`

```python
async delete(self, *, reason: str | None = None)
```

Deletes the webhook.
Returns
-------
None

<a id="webhook-delete-message"></a>
#### `delete_message`

```python
async delete_message(self, message_id: str) -> aiohttp.client_reqrep.ClientResponse
```

Deletes a message from the webhook.

Parameters
----------
message_id: :class:`str`
The id of the message to delete.

Returns
-------
aiohttp.ClientResponse

<a id="webhook-edit-message"></a>
#### `edit_message`

```python
async edit_message(self, message_id: str, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container, thread_id: str | None = None) -> discohook.message.Message
```

Edits a message from the webhook.

Parameters
----------
message_id: :class:`str`
The id of the message to edit.
*components:
Components to be sent with the message.
thread_id: Optional[:class:`str`]
The thread id the message is in.

Returns
-------
:class:`Message`

<a id="webhook-fetch"></a>
#### `fetch`

Fetches the webhook from Discord.

Returns
-------
:class:`Webhook`
The fetched webhook.

<a id="webhook-fetch-message"></a>
#### `fetch_message`

```python
async fetch_message(self, message_id: str, *, thread_id: str | None = None)
```

Fetches a message sent by the webhook.

Parameters
----------
message_id: :class:`str`
The id of the message to edit.
thread_id: Optional[:class:`str`]
The thread id the message is in.

Returns
-------
:class:`Message`

<a id="webhook-from-url"></a>
#### `from_url`

<a id="webhook-modify"></a>
#### `modify`

```python
async modify(self, name: str | None = None, image_base64: str | None = None, channel_id: str | None = None, reason: str | None = None)
```

Edits the webhook.

Parameters
----------
name: Optional[:class:`str`]
The new name of the webhook.
image_base64: Optional[:class:`str`]
The new avatar of the webhook.
channel_id: Optional[:class:`str`]
The new channel id of the webhook.
reason: Optional[:class:`str`]
The reason for editing the webhook to be logged.

Returns
-------
:class:`Webhook`

Notes
-----
The image must be a base64 encoded string.
All parameters are optional.

<a id="webhook-send"></a>
#### `send`

```python
async send(self, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container, username: str | None = None, avatar_url: str | None = None, thread_name: str | None = None, wait: bool = False, thread_id: str | None = None) -> aiohttp.client_reqrep.ClientResponse
```

Sends a message to the webhook.

Parameters
----------
*components:
Components to be sent with the message.
username:
The username of the webhook.
avatar_url:
The avatar url of the webhook. (Overrides the webhook's avatar)
thread_name: Optional[:class:`str`]
The name of the thread to create.
wait: :class:`bool`
Waits for server confirmation of the message.
thread_id: Optional[:class:`str`]
Whether to send to a specified thread within the webhook's channel.

Returns
-------
aiohttp.ClientResponse


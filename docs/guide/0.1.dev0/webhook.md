---
title: discohook.webhook
---

# `discohook.webhook`

## Classes

- [PartialWebhook](#class-partialwebhook)
- [Webhook](#class-webhook)

<a id="class-partialwebhook"></a>
## PartialWebhook

`discohook.webhook.PartialWebhook`

Represents a Discord webhook with no authentication.
#### _Attributes_

- _**id** (`str`): Discord webhook id._
- _**token** (`str`): Discord webhook token._
- _**type** (`int`): Discord webhook type._
- _**guild_id** (`str`): Discord webhook guild id._
- _**channel_id** (`str`): Discord webhook channel id._
- _**name** (`str`): Discord webhook name._
- _**avatar** (`str`): Discord webhook avatar hash._
- _**application_id** (`str`): ID of the application that created it._
- _**source_guild** (`str`): Guild of the channel that this webhook is following_ (returned for Channel Follower Webhooks).
- _**source_channel** (`str`): Channel that this webhook is following_ (returned for Channel Follower Webhooks).

### Method Index

- [delete](#partialwebhook-delete)
- [delete_message](#partialwebhook-delete-message)
- [edit_message](#partialwebhook-edit-message)
- [execute](#partialwebhook-execute)
- [fetch_message](#partialwebhook-fetch-message)
- [from_data](#partialwebhook-from-data)
- [from_url](#partialwebhook-from-url)
- [modify](#partialwebhook-modify)
- [resolve](#partialwebhook-resolve)

### Methods

<a id="partialwebhook-delete"></a>
#### `delete`

```python
async delete(self)
```

Deletes the webhook.

<a id="partialwebhook-delete-message"></a>
#### `delete_message`

```python
async delete_message(self, message_id: str) -> aiohttp.client_reqrep.ClientResponse
```

Deletes a message from the webhook.
#### _Arguments_

- _**message_id** (`str`): Message id to delete._
#### _Returns_

- **Type:** `aiohttp.ClientResponse`
  - Response from the webhook.

<a id="partialwebhook-edit-message"></a>
#### `edit_message`

```python
async edit_message(self, message_id: str, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, thread_id: str | None = None) -> discohook.message.Message
```

Edits a message from the webhook.
#### _Arguments_

- _**message_id** (`str`): Message id to edit._
- _**components** (`Tuple[TopLevelComponent]`): Components to be sent with the message._
- _**thread_id** (`str | None`): ID of the thread the message is in._
#### _Returns_

- **Type:** `aiohttp.ClientResponse`
  - Response from the webhook.

<a id="partialwebhook-execute"></a>
#### `execute`

```python
async execute(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, poll: discohook.poll.Poll | None = None, username: str | None = None, avatar_url: str | None = None, thread_name: str | None = None, wait: bool = False, thread_id: str | None = None) -> aiohttp.client_reqrep.ClientResponse
```

Executes the webhook.
#### _Arguments_

- _**components** (`Tuple[TopLevelComponent]`): Components to be sent with the message._
- _**poll** (`Poll | None`): Poll to be sent with the message._
- _**username** (`str | None`): Name of the webhook. (Overrides the default username)_
- _**avatar_url** (`str | None`): Avatar of the webhook. (Overrides the default avatar)_
- _**thread_name** (`str | None`): Name of the thread to create._ (Requires the webhook channel to be a forum or media channel)
- _**wait** (`bool`): Whether to wait for server confirmation of the message before responding._
- _**thread_id** (`str`): Whether to send to a specified thread within the webhook's channel._
#### _Returns_

- **Type:** `aiohttp.ClientResponse`
  - Response from the webhook.
#### _Raises_

- **ValueError**: If the webhook token is not set or resolved.

<a id="partialwebhook-fetch-message"></a>
#### `fetch_message`

```python
async fetch_message(self, message_id: str, *, thread_id: str | None = None)
```

Fetches a message sent by the webhook.
#### _Arguments_

- _**message_id** (`str`): Message id to fetch._
- _**thread_id** (`str | None`): ID of the thread the message is in._
#### _Returns_

- **Type:** `aiohttp.ClientResponse`
  - Response from the webhook.
#### _Raises_

- **ValueError**: If the webhook token is not set or resolved.

<a id="partialwebhook-from-data"></a>
#### `from_data`

Creates a webhook from a Discord webhook data.
#### _Arguments_

- _**data** (`dict`): Discord webhook data._
#### _Returns_

- **Type:** `PartialWebhook`
  - Webhook object.

<a id="partialwebhook-from-url"></a>
#### `from_url`

Creates a webhook from a Discord webhook URL.
#### _Arguments_

- _**url** (`str`): Discord webhook URL._
#### _Returns_

- **Type:** `PartialWebhook`
  - Webhook object.

<a id="partialwebhook-modify"></a>
#### `modify`

```python
async modify(self, *, name: str | None = None, image_base64: str | None = None, channel_id: str | None = None)
```

Edits the webhook.
#### _Arguments_

- _**name** (`str | None`): Name of the webhook._
- _**image_base64** (`str | None`): Avatar of the webhook as a base64 encoded string._
- _**channel_id** (`str | None`): Channel id of the webhook._

<a id="partialwebhook-resolve"></a>
#### `resolve`

```python
async resolve(self)
```

Populates the webhook attributes.


<a id="class-webhook"></a>
## Webhook

`discohook.webhook.Webhook`

Represents a Discord webhook.

### Inheritance

- `discohook.webhook.PartialWebhook`

### Method Index

- [delete](#webhook-delete)
- [modify](#webhook-modify)
- [resolve](#webhook-resolve)

### Methods

<a id="webhook-delete"></a>
#### `delete`

```python
async delete(self, *, reason: str | None = None)
```

Deletes the webhook.
#### _Arguments_

- _**reason** (`str | None`): Reason to delete the webhook. Shows up in audit log._

<a id="webhook-modify"></a>
#### `modify`

```python
async modify(self, name: str | None = None, image_base64: str | None = None, channel_id: str | None = None, reason: str | None = None)
```

Edits the webhook.
#### _Arguments_

- _**name** (`str | None`): Name of the webhook._
- _**image_base64** (`str | None`): Avatar of the webhook as a base64 encoded string._
- _**channel_id** (`str | None`): Channel id of the webhook._
- _**reason** (`str | None`): Reason to edit the webhook. Shows up in audit log._
#### _Returns_

- **Type:** `Webhook`
  - Modified webhook object.

<a id="webhook-resolve"></a>
#### `resolve`

```python
async resolve(self)
```

Populates the webhook attributes.


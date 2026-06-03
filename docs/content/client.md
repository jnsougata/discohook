---
title: discohook.client
---

# `discohook.client`

## Classes

- [Client](#class-client)

<a id="class-client"></a>
## Class `Client`

**Qualified Name:** `discohook.client.Client`

Base client class.

### Arguments

- **application_id** (`int | str`): Application ID of the bot.
- **public_key** (`str`): Public key of the bot.
- **token** (`str`): Token of the bot.
- **route** (`str`): Route to listen for interactions on. Defaults to `/interactions`.
- **password** (`str | None`): Password to use for the dashboard.
- **default_help_command** (`bool`): Whether to use the default help command or not. Defaults to False.
- **ratelimit_mux** (`RatelimitMux | None`): Whether to use a custom ratelimit mux or not. Defaults to None.
- **kwargs**: Keyword arguments to pass to the Starlette instance.

### Inheritance

- `starlette.applications.Starlette`

### Method Index

- [commands](#client-commands)
- [create_application_emoji](#client-create-application-emoji)
- [create_webhook](#client-create-webhook)
- [custom_id_parser](#client-custom-id-parser)
- [delete_application_emoji](#client-delete-application-emoji)
- [delete_command](#client-delete-command)
- [edit](#client-edit)
- [edit_application_emoji](#client-edit-application-emoji)
- [fetch_application_emoji](#client-fetch-application-emoji)
- [fetch_application_emojis](#client-fetch-application-emojis)
- [fetch_channel](#client-fetch-channel)
- [fetch_commands](#client-fetch-commands)
- [fetch_guild](#client-fetch-guild)
- [fetch_info](#client-fetch-info)
- [fetch_user](#client-fetch-user)
- [fetch_webhook](#client-fetch-webhook)
- [from_env](#client-from-env)
- [me](#client-me)
- [on_error](#client-on-error)
- [on_interaction_error](#client-on-interaction-error)
- [register](#client-register)
- [send](#client-send)

### Methods

<a id="client-commands"></a>
#### `commands`

```python
commands(self, *commands: discohook.command.ApplicationCommand | Any)
```

Adds commands to the client.

### Arguments

- **commands**: Commands to add to the client.

<a id="client-create-application-emoji"></a>
#### `create_application_emoji`

```python
async create_application_emoji(self, *, name: str, image: bytes, image_type: Literal['png', 'jpeg', 'gif']) -> discohook.emoji.PartialEmoji
```

Create a new application emoji.

### Arguments

- **name** (`str`): Name of the emoji.
- **image** (`bytes`): Image of the emoji in bytes.
- **image_type** (`str`): Image type of the emoji. (e.g. "png", "jpeg", "gif")

### Returns

- **Type:** `PartialEmoji`
  - PartialEmoji object.

<a id="client-create-webhook"></a>
#### `create_webhook`

```python
async create_webhook(self, channel_id: str, *, name: str, image_base64: str | None = None, reason: str | None = None)
```

Creates a webhook in a channel.

### Arguments

- **channel_id** (`str`): ID of the channel to create the webhook in.
- **name** (`str`): Name of the webhook.
- **image_base64** (`str | None`): Base64 encoded image of the webhook.
- **reason** (`str | None`): Reason for creating the webhook. This will be shown in the audit log.

### Returns

- **Type:** `Webhook`
  - Webhook object.

<a id="client-custom-id-parser"></a>
#### `custom_id_parser`

```python
custom_id_parser(self, coro: Callable[[discohook.interaction.Interaction, str], str])
```

Decorator to register a developer defined custom_id parser.

<a id="client-delete-application-emoji"></a>
#### `delete_application_emoji`

```python
async delete_application_emoji(self, emoji_id: str)
```

Delete an existing emoji in a guild.

### Arguments

- **emoji_id** (`str`): ID of the emoji.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Aiohttp response object.

<a id="client-delete-command"></a>
#### `delete_command`

```python
async delete_command(self, command_id: str, *, guild_id: str | None = None)
```

Delete a command from the client.

### Arguments

- **command_id** (`str`): ID of the command to delete.
- **guild_id** (`str | None`): ID of the guild to delete the command from. Defaults to None.

<a id="client-edit"></a>
#### `edit`

```python
async edit(self, username: str, *, avatar: str | None = None)
```

Edits the client user.

### Arguments

- **username** (`str`): Updated username.
- **avatar** (`str | None`): Updated avatar of the client user in base64 data URI scheme. Defaults to None.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Updated client user.

<a id="client-edit-application-emoji"></a>
#### `edit_application_emoji`

```python
async edit_application_emoji(self, emoji_id: str, name: str)
```

Edits an existing emoji in a guild.

### Arguments

- **emoji_id** (`str`): ID of the emoji.
- **name** (`str`): Name of the emoji.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Aiohttp response object.

<a id="client-fetch-application-emoji"></a>
#### `fetch_application_emoji`

```python
async fetch_application_emoji(self, emoji_id: str)
```

Fetches an emoji from the client.

### Arguments

- **emoji_id** (`str`): ID of the emoji.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Aiohttp response object.

<a id="client-fetch-application-emojis"></a>
#### `fetch_application_emojis`

```python
async fetch_application_emojis(self)
```

Fetch all emojis from the client.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Aiohttp response object.

<a id="client-fetch-channel"></a>
#### `fetch_channel`

```python
async fetch_channel(self, channel_id: str) -> discohook.channel.Channel | None
```

Fetches the channel from given ID.

### Arguments

- **channel_id** (`str`): ID of the channel to fetch.

### Returns

- **Type:** `Channel`
  - Channel object or None.

<a id="client-fetch-commands"></a>
#### `fetch_commands`

```python
async fetch_commands(self)
```

Fetches the commands of the client.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Aiohttp response object.

<a id="client-fetch-guild"></a>
#### `fetch_guild`

```python
async fetch_guild(self, guild_id: str, *, with_counts: bool | None = False) -> discohook.guild.Guild | None
```

Fetches the guild of given id.

### Arguments

- **guild_id** (`str`): ID of the guild to fetch.
- **with_counts** (`bool`): Whether the guild count is returned or not.

### Returns

- **Type:** `Guild | None`
  - Guild object or None.

<a id="client-fetch-info"></a>
#### `fetch_info`

```python
async fetch_info(self) -> Dict[str, Any]
```

Fetches the application object associated with the requesting client user.

### Returns

- **Type:** `aiohttp.ClientResponse`
  - Aiohttp response object.

<a id="client-fetch-user"></a>
#### `fetch_user`

```python
async fetch_user(self, user_id: str) -> discohook.user.User | None
```

Fetches the user from given ID.

### Arguments

- **user_id** (`str`): ID of the user to fetch.

### Returns

- **Type:** `User | None`
  - User object or None.

<a id="client-fetch-webhook"></a>
#### `fetch_webhook`

```python
async fetch_webhook(self, webhook_id: str, *, webhook_token: str | None = None)
```

Fetch a webhook from the client.

### Arguments

- **webhook_id** (`str`): ID of the webhook to fetch.
- **webhook_token** (`str | None`): Token of the webhook to fetch.

### Returns

- **Type:** `Webhook`
  - Webhook object.

<a id="client-from-env"></a>
#### `from_env`

Creates a client using environment variables.
The environment variables are APPLICATION_ID, PUBLIC_KEY, BOT_TOKEN, and optionally APPLICATION_PASSWORD.

### Arguments

- **path** (`str`): Path to the .env file. Defaults to ".env".
- **default_help_command** (`bool`): Whether to use the default help command or not. Defaults to False.
- **ratelimit_mux** (`RatelimitMux | None`): Whether to use a custom ratelimit mux or not. Defaults to None.
- **kwargs**: Keyword arguments to pass to the Starlette instance.

### Returns

- **Type:** `Client`
  - The client instance.

<a id="client-me"></a>
#### `me`

```python
async me(self) -> discohook.user.User
```

Fetch the client as a discord user.

### Returns

- **Type:** `User`
  - Client as a discord user.

<a id="client-on-error"></a>
#### `on_error`

```python
on_error(self)
```

Decorator to add an error handler for any server side error.

<a id="client-on-interaction-error"></a>
#### `on_interaction_error`

```python
on_interaction_error(self)
```

Decorator to register a global interaction error handler.

<a id="client-register"></a>
#### `register`

```python
register(self, item: discohook.handler.Handler | discohook.command.ApplicationCommand) -> discohook.handler.Handler | discohook.command.ApplicationCommand
```

Registers a handler or command to the client.

### Arguments

- **item** (`Handler | ApplicationCommand`): The handler or command to register.

<a id="client-send"></a>
#### `send`

```python
async send(self, channel_id: str, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery) -> discohook.message.Message
```

Send a message to a channel.

### Arguments

- **channel_id** (`str`): ID of the channel to send the message to.
- **components** (`Tuple[TopLevelComponent]`): Components to send in the message.

### Returns

- **Type:** `Message`
  - Message object.


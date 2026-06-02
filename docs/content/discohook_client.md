---
title: discohook.client
---

# `discohook.client`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/client.py`

## Classes

- [Client](#class-client)

## Class `Client`

Base client class.

Args:
    application_id (int | str): Application ID of the bot.
    public_key (str): Public key of the bot.
    token (str): Token of the bot.
    route (str): Route to listen for interactions on. Defaults to `/interactions`.
    password (str | None): Password to use for the dashboard.
    default_help_command (bool): Whether to use the default help command or not. Defaults to False.
    ratelimit_mux (RatelimitMux | None): Whether to use a custom ratelimit mux or not. Defaults to None.
    kwargs: Keyword arguments to pass to the Starlette instance.

### Inheritance

- `starlette.applications.Starlette`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/client.py`
- Line: `28`

### Methods

#### `add_exception_handler`

```python
add_exception_handler(self, exc_class_or_status_code: 'int | type[Exception]', handler: 'ExceptionHandler') -> 'None'
```

#### `add_middleware`

```python
add_middleware(self, middleware_class: '_MiddlewareFactory[P]', *args: 'P.args', **kwargs: 'P.kwargs') -> 'None'
```

#### `add_route`

```python
add_route(self, path: 'str', route: 'Callable[[Request], Awaitable[Response] | Response]', methods: 'list[str] | None' = None, name: 'str | None' = None, include_in_schema: 'bool' = True) -> 'None'
```

#### `build_middleware_stack`

```python
build_middleware_stack(self) -> 'ASGIApp'
```

#### `commands`

```python
commands(self, *commands: discohook.command.ApplicationCommand | Any)
```

Adds commands to the client.

Args:
    commands: Commands to add to the client.

#### `create_application_emoji`

```python
create_application_emoji(self, *, name: str, image: bytes, image_type: Literal['png', 'jpeg', 'gif']) -> discohook.emoji.PartialEmoji
```

Create a new application emoji.

Args:
    name (str): Name of the emoji.
    image (bytes): Image of the emoji in bytes.
    image_type (str): Image type of the emoji. (e.g. "png", "jpeg", "gif")

Returns:
    PartialEmoji object.

#### `create_webhook`

```python
create_webhook(self, channel_id: str, *, name: str, image_base64: str | None = None, reason: str | None = None)
```

Creates a webhook in a channel.

Args:
    channel_id (str): ID of the channel to create the webhook in.
    name (str): Name of the webhook.
    image_base64 (str | None): Base64 encoded image of the webhook.
    reason (str | None): Reason for creating the webhook. This will be shown in the audit log.

Returns:
    Webhook object.

#### `custom_id_parser`

```python
custom_id_parser(self, coro: Callable[[discohook.interaction.Interaction, str], str])
```

Decorator to register a developer defined custom_id parser.

#### `delete_application_emoji`

```python
delete_application_emoji(self, emoji_id: str)
```

Delete an existing emoji in a guild.

Args:
    emoji_id (str): ID of the emoji.

Returns:
    Aiohttp response object.

#### `delete_command`

```python
delete_command(self, command_id: str, *, guild_id: str | None = None)
```

Delete a command from the client.

Args:
    command_id (str): ID of the command to delete.
    guild_id (str | None): ID of the guild to delete the command from. Defaults to None.

#### `edit`

```python
edit(self, username: str, *, avatar: str | None = None)
```

Edits the client user.

Args:
    username (str): Updated username.
    avatar (str | None): Updated avatar of the client user in base64 data URI scheme. Defaults to None.

#### `edit_application_emoji`

```python
edit_application_emoji(self, emoji_id: str, name: str)
```

Edits an existing emoji in a guild.

Args:
    emoji_id (str): ID of the emoji.
    name (str): Name of the emoji.

Returns:
    Aiohttp response object.

#### `fetch_application_emoji`

```python
fetch_application_emoji(self, emoji_id: str)
```

Fetches an emoji from the client.

Args:
    emoji_id (str): ID of the emoji.

Returns:
    Aiohttp response object.

#### `fetch_application_emojis`

```python
fetch_application_emojis(self)
```

Fetch all emojis from the client.

#### `fetch_channel`

```python
fetch_channel(self, channel_id: str) -> discohook.channel.Channel | None
```

Fetches the channel from given ID.

Args:
    channel_id (str): ID of the channel to fetch.

Returns:
    Channel object or None.

#### `fetch_commands`

```python
fetch_commands(self)
```

Fetches the commands of the client.

Returns:
    Aiohttp response object.

#### `fetch_guild`

```python
fetch_guild(self, guild_id: str, *, with_counts: bool | None = False) -> discohook.guild.Guild | None
```

Fetches the guild of given id.

Args:
    guild_id (str): ID of the guild to fetch.
    with_counts (bool): Whether the guild count is returned or not.

Returns:
    Guild object or None.

#### `fetch_info`

```python
fetch_info(self) -> Dict[str, Any]
```

Fetches the application object associated with the requesting client user.

Returns:
    Aiohttp response object.

#### `fetch_user`

```python
fetch_user(self, user_id: str) -> discohook.user.User | None
```

Fetches the user from given ID.

Args:
    user_id (str): ID of the user to fetch.

Returns:
    User object or None.

#### `fetch_webhook`

```python
fetch_webhook(self, webhook_id: str, *, webhook_token: str | None = None)
```

Fetch a webhook from the client.

Args:
    webhook_id (str): ID of the webhook to fetch.
    webhook_token (str | None): Token of the webhook to fetch.

Returns:
    Webhook object.

#### `from_env`

```python
from_env(path: str = '.env', *, default_help_command: bool = False, ratelimit_mux: discohook.ratelimit.RatelimitMux | None = None, **kwargs) -> 'Client'
```

Creates a client using environment variables.
The environment variables are APPLICATION_ID, PUBLIC_KEY, BOT_TOKEN, and optionally APPLICATION_PASSWORD.

Args:
    path (str): Path to the .env file. Defaults to ".env".
    default_help_command (bool): Whether to use the default help command or not. Defaults to False.
    ratelimit_mux (RatelimitMux | None): Whether to use a custom ratelimit mux or not. Defaults to None.
    kwargs: Keyword arguments to pass to the Starlette instance.

Returns:
    Client: The client instance.

#### `host`

```python
host(self, host: 'str', app: 'ASGIApp', name: 'str | None' = None) -> 'None'
```

#### `me`

```python
me(self) -> discohook.user.User
```

Fetch the client as a discord user.

Returns:
      Client as a discord user.

#### `mount`

```python
mount(self, path: 'str', app: 'ASGIApp', name: 'str | None' = None) -> 'None'
```

#### `on_error`

```python
on_error(self)
```

Decorator to add an error handler for any server side error.

#### `on_interaction_error`

```python
on_interaction_error(self)
```

Decorator to register a global interaction error handler.

#### `register`

```python
register(self, item: discohook.handler.Handler | discohook.command.ApplicationCommand) -> discohook.handler.Handler | discohook.command.ApplicationCommand
```

Registers a handler or command to the client.

Args:
    item (Handler | ApplicationCommand): The handler or command to register.

#### `send`

```python
send(self, channel_id: str, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery) -> discohook.message.Message
```

Send a message to a channel.

Args:
    channel_id (str): ID of the channel to send the message to.
    components (Tuple[TopLevelComponent]): Components to send in the message.

Returns:
    Message object.

#### `url_path_for`

```python
url_path_for(self, name: 'str', /, **path_params: 'Any') -> 'URLPath'
```


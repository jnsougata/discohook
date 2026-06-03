---
title: discohook.interaction
---

# `discohook.interaction`

## Classes

- [Interaction](#class-interaction)

<a id="class-interaction"></a>
## Class `Interaction`

**Qualified Name:** `discohook.interaction.Interaction`

Represents a discord interaction.

### Property Index

- [app_permissions](#interaction-app-permissions)
- [application_id](#interaction-application-id)
- [author](#interaction-author)
- [channel](#interaction-channel)
- [channel_id](#interaction-channel-id)
- [context](#interaction-context)
- [created_at](#interaction-created-at)
- [data](#interaction-data)
- [error](#interaction-error)
- [from_originator](#interaction-from-originator)
- [guild](#interaction-guild)
- [guild_id](#interaction-guild-id)
- [guild_locale](#interaction-guild-locale)
- [id](#interaction-id)
- [locale](#interaction-locale)
- [message](#interaction-message)
- [parsed_command_options](#interaction-parsed-command-options)
- [responded](#interaction-responded)
- [response](#interaction-response)
- [token](#interaction-token)
- [traceback](#interaction-traceback)
- [type](#interaction-type)
- [version](#interaction-version)

### Method Index

- [original_response](#interaction-original-response)

### Properties

<a id="interaction-app-permissions"></a>
#### `app_permissions`

The permissions of the application

Returns
-------
Optional[int]

<a id="interaction-application-id"></a>
#### `application_id`

The id of the application that the interaction was triggered for

Returns
-------
str

<a id="interaction-author"></a>
#### `author`

The author of the interaction
If the interaction was triggered in a guild, this will return a member object else it will return user object.

Returns
-------
Union[User, Member]

<a id="interaction-channel"></a>
#### `channel`

The channel where the interaction was triggered

Returns
-------
PartialChannel

<a id="interaction-channel-id"></a>
#### `channel_id`

The channel id of the interaction

Returns
-------
Optional[str]

<a id="interaction-context"></a>
#### `context`

Context where the interaction was triggered from.

Returns
-------
InteractionContextType | None

<a id="interaction-created-at"></a>
#### `created_at`

The timestamp when the interaction was created

Returns
-------
float

<a id="interaction-data"></a>
#### `data`

Command data payload (if the interaction is a command).

### Returns

- **Type:** `Dict[str, Any]`
  - Command data payload.

<a id="interaction-error"></a>
#### `error`

Error that occurred during the interaction

### Returns

- **Type:** `Exception | None`
  - Exception object.

<a id="interaction-from-originator"></a>
#### `from_originator`

Whether the interaction was triggered by the same user who triggered the message

Returns
-------
bool

<a id="interaction-guild"></a>
#### `guild`

<a id="interaction-guild-id"></a>
#### `guild_id`

The guild id of the interaction

Returns
-------
Optional[str]

<a id="interaction-guild-locale"></a>
#### `guild_locale`

The guild locale of the interaction

Returns
-------
Optional[str]

<a id="interaction-id"></a>
#### `id`

Unique id of the interaction

### Returns

- **Type:** `str`
  - Interaction id.

<a id="interaction-locale"></a>
#### `locale`

The locale of the interaction

Returns
-------
Optional[str]

<a id="interaction-message"></a>
#### `message`

The message from which the component interaction was triggered

Returns
-------
Message

<a id="interaction-parsed-command-options"></a>
#### `parsed_command_options`

Resolved command options payload (if the interaction is a command).

<a id="interaction-responded"></a>
#### `responded`

Whether the interaction has been responded to.

### Returns

- **Type:** `bool`
  - Whether the interaction has been responded to.

<a id="interaction-response"></a>
#### `response`

The response adapter for the interaction

Returns
-------
ResponseAdapter

<a id="interaction-token"></a>
#### `token`

The token of the interaction

Returns
-------
str

<a id="interaction-traceback"></a>
#### `traceback`

Traceback of the error that occurred during the interaction

### Returns

- **Type:** `str | None`
  - Traceback string.

<a id="interaction-type"></a>
#### `type`

The type of the interaction

Returns
-------
Optional[InteractionType]

<a id="interaction-version"></a>
#### `version`

The version of the interaction

Returns
-------
int

### Methods

<a id="interaction-original-response"></a>
#### `original_response`

```python
async original_response(self) -> discohook.message.Message | None
```

Gets the original response message of the interaction if the interaction has been responded to.

Returns
-------
InteractionResponse
The original response message


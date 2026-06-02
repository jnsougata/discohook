---
title: discohook.interaction
---

# `discohook.interaction`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/interaction.py`

## Classes

- [Interaction](#class-interaction)

## Class `Interaction`

Base interaction class for all interactions

### Properties

- **id** (`str`)
    The unique id of the interaction
- **type** (`int`)
    The type of the interaction
- **token** (`str`)
    The token of the interaction
- **version** (`int`)
    The version of the interaction
- **application_id** (`str`)
    The id of the application that the interaction was triggered for
- **data** (`Optional[Dict[str, Any]]`)
    The command data payload (if the interaction is a command)
- **guild_id** (`Optional[str]`)
    The guild id of the interaction
- **channel_id** (`Optional[str]`)
    The channel id of the interaction
- **app_permissions** (`Optional[int]`)
    The permissions of the application
- **locale** (`Optional[str]`)
    The locale of the interaction
- **guild_locale** (`Optional[str]`)
    The guild locale of the interaction
- **created_at** (`int`)
    The timestamp when the interaction was created

### Parameters

- **data** (`Dict[str, Any]`)
    The interaction data payload
- **client** (`Client`)
    The stateful client

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/interaction.py`
- Line: `17`

### Methods

#### `original_response`

```python
original_response(self) -> discohook.message.Message | None
```

Gets the original response message of the interaction if the interaction has been responded to.

### Returns

InteractionResponse
    The original response message


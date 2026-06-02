---
title: discohook.models
---

# `discohook.models`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/models.py`

## Classes

- [AllowedMentions](#class-allowedmentions)
- [MessageReference](#class-messagereference)
- [PermissionOverwrite](#class-permissionoverwrite)

## Class `AllowedMentions`

Represents a discord allowed mentions object.

### Parameters

- **parse** (`List[AllowedMentionsType] | None`)
    The types of mentions to parse from the message content.
- **roles** (`List[str] | None`)
    The roles to mention.
- **users** (`List[str] | None`)
    The users to mention.
- **replied_user** (`bool | None`)
    Whether to mention the user the message is replying to.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/models.py`
- Line: `6`

### Methods

#### `to_dict`

```python
to_dict(self) -> dict
```

Returns a dictionary representation of the allowed mentions object.

This is used internally by the library. You should not need to use this method.

### Returns

:class:`dict`
    The dictionary representation of the allowed mentions object.


## Class `MessageReference`

Represents a discord message reference object.

### Parameters

- **message_id** (`str | None`)
    The id of the message.
- **channel_id** (`str | None`)
    The id of the channel where the message was sent.
- **guild_id** (`str | None`)
    The id of the guild where the message was sent.
- **fail_if_not_exists** (`bool | None`)
    Whether to throw an error if the message does not exist.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/models.py`
- Line: `57`

### Methods

#### `to_dict`

```python
to_dict(self) -> dict
```

Returns a dictionary representation of the message reference object.

This is used internally by the library. You should not need to use this method.

### Returns

:class:`dict`
    The dictionary representation of the message reference object.


## Class `PermissionOverwrite`

Represents a permission overwrite object.

### Parameters

- **id** (`str`)
    The id of the role or user.
- **type** (`str`)
    The type of the overwrite.
- **allow** (`int`)
    The permissions allowed by the overwrite.
- **deny** (`int`)
    The permissions denied by the overwrite.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/models.py`
- Line: `110`

### Methods

#### `to_dict`

```python
to_dict(self) -> dict
```

Returns a dictionary representation of the permission overwrite object.

This is used internally by the library. You should not need to use this method.

### Returns

:class:`dict`
    The dictionary representation of the permission overwrite object.


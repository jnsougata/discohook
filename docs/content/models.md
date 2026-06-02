---
title: discohook.models
---

# `discohook.models`

## Classes

- [AllowedMentions](#class-allowedmentions)
- [MessageReference](#class-messagereference)
- [PermissionOverwrite](#class-permissionoverwrite)

<a id="class-allowedmentions"></a>
## Class `AllowedMentions`

**Qualified Name:** `discohook.models.AllowedMentions`

Represents a discord allowed mentions object.

Parameters
----------
parse: List[AllowedMentionsType] | None
The types of mentions to parse from the message content.
roles: List[str] | None
The roles to mention.
users: List[str] | None
The users to mention.
replied_user: bool | None
Whether to mention the user the message is replying to.

### Method Index

- [to_dict](#allowedmentions-to-dict)

### Methods

<a id="allowedmentions-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> dict
```

Returns a dictionary representation of the allowed mentions object.

This is used internally by the library. You should not need to use this method.

Returns
-------
:class:`dict`
The dictionary representation of the allowed mentions object.


<a id="class-messagereference"></a>
## Class `MessageReference`

**Qualified Name:** `discohook.models.MessageReference`

Represents a discord message reference object.

Parameters
----------
message_id: str | None
The id of the message.
channel_id: str | None
The id of the channel where the message was sent.
guild_id: str | None
The id of the guild where the message was sent.
fail_if_not_exists: bool | None
Whether to throw an error if the message does not exist.

### Method Index

- [to_dict](#messagereference-to-dict)

### Methods

<a id="messagereference-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> dict
```

Returns a dictionary representation of the message reference object.

This is used internally by the library. You should not need to use this method.

Returns
-------
:class:`dict`
The dictionary representation of the message reference object.


<a id="class-permissionoverwrite"></a>
## Class `PermissionOverwrite`

**Qualified Name:** `discohook.models.PermissionOverwrite`

Represents a permission overwrite object.

Parameters
----------
id: str
The id of the role or user.
type: str
The type of the overwrite.
allow: int
The permissions allowed by the overwrite.
deny: int
The permissions denied by the overwrite.

### Method Index

- [to_dict](#permissionoverwrite-to-dict)

### Methods

<a id="permissionoverwrite-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> dict
```

Returns a dictionary representation of the permission overwrite object.

This is used internally by the library. You should not need to use this method.

Returns
-------
:class:`dict`
The dictionary representation of the permission overwrite object.


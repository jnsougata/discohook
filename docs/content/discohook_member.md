---
title: discohook.member
---

# `discohook.member`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/member.py`

## Classes

- [Member](#class-member)

## Class `Member`

Represents a member of a guild, subclassed from :class:`User`.

### Inheritance

- `discohook.user.User`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/member.py`
- Line: `12`

### Methods

#### `add_role`

```python
add_role(self, role_id: str, *, reason: str | None = None)
```

Add a role to the member.

### Parameters

- **role_id** (`str`)
    The ID of the role.
- **reason** (`Optional[str]`)
    The reason for adding the role to be logged.

#### `ban`

```python
ban(self, *, delete_message_seconds: int = 0, reason: str | None = None)
```

Ban the member.

### Parameters

- **delete_message_seconds** (`int`)
    The number of days to delete messages for.
    This must be between 0 and 604800 (7 days).
- **reason** (`Optional[str]`)
    The reason for banning the member to be logged.

#### `has_permission`

```python
has_permission(self, permission: discohook.permission.Permission) -> bool
```

#### `kick`

```python
kick(self, *, reason: str | None = None)
```

Kick the member.

#### `remove_role`

```python
remove_role(self, role_id: str, *, reason: str | None = None)
```

Remove a role from the member.

### Parameters

- **role_id** (`str`)
    The ID of the role.
- **reason** (`Optional[str]`)
    The reason for removing the role to be logged.

#### `send`

```python
send(self, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container) -> aiohttp.client_reqrep.ClientResponse
```

Sends a message to the user.

### Parameters

*components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]
    The components to send in the message.


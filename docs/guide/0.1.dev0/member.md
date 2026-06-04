---
title: discohook.member
---

# `discohook.member`

## Classes

- [Member](#class-member)

<a id="class-member"></a>
## Member

`discohook.member.Member`

Represents a member of a guild, subclassed from :class:`User`.

### Inheritance

- `discohook.user.User`

### Property Index

- [mention](#member-mention)

### Method Index

- [add_role](#member-add-role)
- [ban](#member-ban)
- [kick](#member-kick)
- [remove_role](#member-remove-role)

### Properties

<a id="member-mention"></a>
#### `mention`

Returns a string that allows you to mention the member.

### Methods

<a id="member-add-role"></a>
#### `add_role`

```python
async add_role(self, role_id: str, *, reason: str | None = None)
```

Add a role to the member.
Parameters
----------
role_id : str
The ID of the role.
reason: Optional[str]
The reason for adding the role to be logged.

<a id="member-ban"></a>
#### `ban`

```python
async ban(self, *, delete_message_seconds: int = 0, reason: str | None = None)
```

Ban the member.
Parameters
----------
delete_message_seconds: int
The number of days to delete messages for.
This must be between 0 and 604800 (7 days).
reason: Optional[str]
The reason for banning the member to be logged.

<a id="member-kick"></a>
#### `kick`

```python
async kick(self, *, reason: str | None = None)
```

Kick the member.

<a id="member-remove-role"></a>
#### `remove_role`

```python
async remove_role(self, role_id: str, *, reason: str | None = None)
```

Remove a role from the member.
Parameters
----------
role_id : str
The ID of the role.
reason: Optional[str]
The reason for removing the role to be logged.


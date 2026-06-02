---
title: discohook.role
---

# `discohook.role`

## Classes

- [PartialRole](#class-partialrole)
- [Role](#class-role)

<a id="class-partialrole"></a>
## Class `PartialRole`

**Qualified Name:** `discohook.role.PartialRole`

### Property Index

- [mention](#partialrole-mention)

### Method Index

- [edit](#partialrole-edit)
- [edit_position](#partialrole-edit-position)

### Properties

<a id="partialrole-mention"></a>
#### `mention`

Returns a string that allows you to mention the role.

Returns
-------
:class:`str`

### Methods

<a id="partialrole-edit"></a>
#### `edit`

```python
async edit(self, *, name: str | None = None, permissions: List[discohook.permission.Permission] | None = None, color: int | None = None, hoist: bool | None = None, mentionable: bool | None = None, description: str | None = None, unicode_emoji: str | None = None, icon_data_uri: str | None = None, reason: str | None = None) -> 'Role'
```

Edits the role.

Parameters
----------
name: Optional[:class:`str`]
The name of the role.
permissions: Optional[:class:`Permission`]
The permissions of the role.
color: Optional[:class:`int`]
The color of the role.
hoist: Optional[:class:`bool`]
Whether the role has separability in the member list.
mentionable: Optional[:class:`bool`]
Whether the role is mentionable.
description: Optional[:class:`str`]
The description of the role.
unicode_emoji: Optional[:class:`str`]
The unicode emoji of the role.
icon_data_uri: Optional[:class:`str`]
The icon of the role. Must be a data URI (base64 encoded).

Returns
-------
:class:`Role`

<a id="partialrole-edit-position"></a>
#### `edit_position`

```python
async edit_position(self, role_id: str, *, position: int, reason: str | None = None) -> List[ForwardRef('Role')]
```

Changes the position of the role.
Parameters
----------
role_id: :class:`str`
The id of the role to move.
position: :class:`int`
The new position of the role.
reason: Optional[:class:`str`]
The reason for changing the position to be logged.

Returns
-------
:class:`Role`


<a id="class-role"></a>
## Class `Role`

**Qualified Name:** `discohook.role.Role`

Represents a discord Role.

Attributes
----------
id: :class:`str`
The unique ID of the role.
name: :class:`str`
The name of the role.
color: :class:`int`
The color of the role.
hoist: :class:`bool`
Whether the role has separability in the member list.
position: :class:`int`
The position of the role.
permissions: :class:`str`
The permissions of the role.
managed: :class:`bool`
Whether the role is managed by an integration.
mentionable: :class:`bool`
Whether the role is mentionable.
description: Optional[:class:`str`]
The description of the role.
unicode_emoji: Optional[:class:`str`]
The unicode emoji of the role.
icon: Optional[:class:`str`]
The icon of the role.
flags: :class:`int`
The flags of the role.

### Inheritance

- `discohook.role.PartialRole`

### Method Index

- [has_permission](#role-has-permission)

### Methods

<a id="role-has-permission"></a>
#### `has_permission`

```python
has_permission(self, permission: discohook.permission.Permission) -> bool
```

Checks if the role has the given permissions.

Parameters
----------
permission: :class:`Permission`
The permissions to check.

Returns
-------
:class:`bool`


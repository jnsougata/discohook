---
title: discohook.select
---

# `discohook.select`

## Classes

- [Select](#class-select)
- [SelectDefaultValue](#class-selectdefaultvalue)
- [SelectOption](#class-selectoption)

<a id="class-select"></a>
## Class `Select`

**Qualified Name:** `discohook.select.Select`

Represents a discord select menu component.

Parameters
----------
placeholder: Optional[:class:`str`]
The placeholder to be displayed on the select menu.
min_values: Optional[:class:`int`]
The minimum number of options that can be selected.
max_values: Optional[:class:`int`]
The maximum number of options that can be selected.
disabled: Optional[:class:`bool`]
Whether the select menu is disabled or not.
type: :class:`SelectType`
The type of the select menu.

### Method Index

- [channel](#select-channel)
- [mentionable](#select-mentionable)
- [role](#select-role)
- [string](#select-string)
- [to_dict](#select-to-dict)
- [user](#select-user)

### Methods

<a id="select-channel"></a>
#### `channel`

Creates a channel select menu and registers a callback.

Parameters
----------
types: Optional[List[:class:`ChannelType`]]
The channel types to be displayed on the select menu.
placeholder: Optional[:class:`str`]
The placeholder to be displayed on the select menu.
min_values: Optional[:class:`int`]
The minimum number of options that can be selected.
max_values: Optional[:class:`int`]
The maximum number of options that can be selected.
disabled: Optional[:class:`bool`]
Whether the select menu is disabled or not.
default_values: Optional[List[:class:`SelectDefaultValue`]]
The default values of the select menu.
handler: :class:`Handler`
The handler for the select menu.

<a id="select-mentionable"></a>
#### `mentionable`

Creates a mentionable select menu and registers a callback.

Parameters
----------
placeholder: Optional[:class:`str`]
The placeholder to be displayed on the select menu.
min_values: Optional[:class:`int`]
The minimum number of options that can be selected.
max_values: Optional[:class:`int`]
The maximum number of options that can be selected.
disabled: Optional[:class:`bool`]
Whether the select menu is disabled or not.
default_values: Optional[List[:class:`SelectDefaultValue`]]
The default values of the select menu.
handler: :class:`Handler`
The handler for the select menu.

<a id="select-role"></a>
#### `role`

Creates a role select menu and registers a callback.

Parameters
----------
placeholder: Optional[:class:`str`]
The placeholder to be displayed on the select menu.
min_values: Optional[:class:`int`]
The minimum number of options that can be selected.
max_values: Optional[:class:`int`]
The maximum number of options that can be selected.
disabled: Optional[:class:`bool`]
Whether the select menu is disabled or not.
default_values: Optional[List[:class:`SelectDefaultValue`]]
The default values of the select menu.
handler: :class:`Handler`
The handler for the select menu.

<a id="select-string"></a>
#### `string`

Creates a text select menu and registers a callback.

Parameters
----------
*option: Tuple[:class:`SelectOption`]
The options to be displayed on the select menu.
placeholder: Optional[:class:`str`]
The placeholder to be displayed on the select menu.
min_values: Optional[:class:`int`]
The minimum number of options that can be selected.
max_values: Optional[:class:`int`]
The maximum number of options that can be selected.
disabled: Optional[:class:`bool`]
Whether the select menu is disabled or not.
handler: :class:`Handler`
The handler for the select menu.

<a id="select-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns a dictionary representation of the button.

This is used internally by the library. You should not need to use this method.

Returns
-------
:class:`dict`
The dictionary representation of the button.

<a id="select-user"></a>
#### `user`

Creates a user select menu and registers a callback.

Parameters
----------
placeholder: Optional[:class:`str`]
The placeholder to be displayed on the select menu.
min_values: Optional[:class:`int`]
The minimum number of options that can be selected.
max_values: Optional[:class:`int`]
The maximum number of options that can be selected.
disabled: Optional[:class:`bool`]
Whether the select menu is disabled or not.
default_values: Optional[List[:class:`SelectDefaultValue`]]
The default values of the select menu.
handler: :class:`Handler`
The handler for the select menu.


<a id="class-selectdefaultvalue"></a>
## Class `SelectDefaultValue`

**Qualified Name:** `discohook.select.SelectDefaultValue`

Represents a discord select menu default option object.
Only applicable for non string select menus.

Parameters
----------
id: :class:`str`
The id of the user, role or channel.
type: :class:`SelectDefaultValueType`
The type of the default value.

### Method Index

- [to_dict](#selectdefaultvalue-to-dict)

### Methods

<a id="selectdefaultvalue-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns a dictionary representation of the button.

This is used internally by the library. You should not need to use this method.

Returns
-------
:class:`dict`
The dictionary representation of the button.


<a id="class-selectoption"></a>
## Class `SelectOption`

**Qualified Name:** `discohook.select.SelectOption`

Represents a discord select menu option object.

Parameters
----------
label: :class:`str`
The text to be displayed on the option.
value: :class:`str`
The value to be sent to the bot when the option is selected.
description: str | None
The description to be displayed on the option.
emoji: :class:`str` | :class:`PartialEmoji` | None
The emoji to be displayed on the option.
default: :class:`bool`
Whether the option is selected by default or not.

### Method Index

- [to_dict](#selectoption-to-dict)

### Methods

<a id="selectoption-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns a dictionary representation of the button.

This is used internally by the library. You should not need to use this method.

Returns
-------
:class:`dict`
The dictionary representation of the button.


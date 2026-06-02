---
title: discohook.select
---

# `discohook.select`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/select.py`

## Classes

- [Select](#class-select)
- [SelectDefaultValue](#class-selectdefaultvalue)
- [SelectOption](#class-selectoption)

## Class `Select`

Represents a discord select menu component.

### Parameters

- **placeholder** (`Optional[:class:`str`]`)
    The placeholder to be displayed on the select menu.
- **min_values** (`Optional[:class:`int`]`)
    The minimum number of options that can be selected.
- **max_values** (`Optional[:class:`int`]`)
    The maximum number of options that can be selected.
- **disabled** (`Optional[:class:`bool`]`)
    Whether the select menu is disabled or not.
- **type** (`:class:`SelectType``)
    The type of the select menu.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/select.py`
- Line: `98`

### Methods

#### `channel`

```python
channel(types: List[discohook.enums.ChannelType] | None = None, *, placeholder: str | None = None, min_values: int | None = None, max_values: int | None = None, disabled: bool | None = False, default_values: List[discohook.select.SelectDefaultValue] | None = None, handler: discohook.handler.Handler)
```

Creates a channel select menu and registers a callback.

### Parameters

- **types** (`Optional[List[:class:`ChannelType`]]`)
    The channel types to be displayed on the select menu.
- **placeholder** (`Optional[:class:`str`]`)
    The placeholder to be displayed on the select menu.
- **min_values** (`Optional[:class:`int`]`)
    The minimum number of options that can be selected.
- **max_values** (`Optional[:class:`int`]`)
    The maximum number of options that can be selected.
- **disabled** (`Optional[:class:`bool`]`)
    Whether the select menu is disabled or not.
- **default_values** (`Optional[List[:class:`SelectDefaultValue`]]`)
    The default values of the select menu.
- **handler** (`:class:`Handler``)
    The handler for the select menu.

#### `mentionable`

```python
mentionable(placeholder: str | None = None, *, min_values: int | None = None, max_values: int | None = None, disabled: bool | None = False, default_values: List[discohook.select.SelectDefaultValue] | None = None, handler: discohook.handler.Handler)
```

Creates a mentionable select menu and registers a callback.

### Parameters

 placeholder: Optional[:class:`str`]
    The placeholder to be displayed on the select menu.
- **min_values** (`Optional[:class:`int`]`)
    The minimum number of options that can be selected.
- **max_values** (`Optional[:class:`int`]`)
    The maximum number of options that can be selected.
- **disabled** (`Optional[:class:`bool`]`)
    Whether the select menu is disabled or not.
- **default_values** (`Optional[List[:class:`SelectDefaultValue`]]`)
    The default values of the select menu.
- **handler** (`:class:`Handler``)
    The handler for the select menu.

#### `role`

```python
role(placeholder: str | None = None, *, min_values: int | None = None, max_values: int | None = None, disabled: bool | None = False, default_values: List[discohook.select.SelectDefaultValue] | None = None, handler: discohook.handler.Handler)
```

Creates a role select menu and registers a callback.

### Parameters

- **placeholder** (`Optional[:class:`str`]`)
    The placeholder to be displayed on the select menu.
- **min_values** (`Optional[:class:`int`]`)
    The minimum number of options that can be selected.
- **max_values** (`Optional[:class:`int`]`)
    The maximum number of options that can be selected.
- **disabled** (`Optional[:class:`bool`]`)
    Whether the select menu is disabled or not.
- **default_values** (`Optional[List[:class:`SelectDefaultValue`]]`)
    The default values of the select menu.
- **handler** (`:class:`Handler``)
    The handler for the select menu.

#### `string`

```python
string(*option: discohook.select.SelectOption, placeholder: str | None = None, min_values: int | None = None, max_values: int | None = None, disabled: bool | None = False, handler: discohook.handler.Handler)
```

Creates a text select menu and registers a callback.

### Parameters

*option: Tuple[:class:`SelectOption`]
    The options to be displayed on the select menu.
- **placeholder** (`Optional[:class:`str`]`)
    The placeholder to be displayed on the select menu.
- **min_values** (`Optional[:class:`int`]`)
    The minimum number of options that can be selected.
- **max_values** (`Optional[:class:`int`]`)
    The maximum number of options that can be selected.
- **disabled** (`Optional[:class:`bool`]`)
    Whether the select menu is disabled or not.
- **handler** (`:class:`Handler``)
    The handler for the select menu.

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns a dictionary representation of the button.

This is used internally by the library. You should not need to use this method.

### Returns

:class:`dict`
    The dictionary representation of the button.

#### `user`

```python
user(placeholder: str | None = None, *, min_values: int | None = None, max_values: int | None = None, disabled: bool | None = False, default_values: List[discohook.select.SelectDefaultValue] | None = None, handler: discohook.handler.Handler)
```

Creates a user select menu and registers a callback.

### Parameters

- **placeholder** (`Optional[:class:`str`]`)
    The placeholder to be displayed on the select menu.
- **min_values** (`Optional[:class:`int`]`)
    The minimum number of options that can be selected.
- **max_values** (`Optional[:class:`int`]`)
    The maximum number of options that can be selected.
- **disabled** (`Optional[:class:`bool`]`)
    Whether the select menu is disabled or not.
- **default_values** (`Optional[List[:class:`SelectDefaultValue`]]`)
    The default values of the select menu.
- **handler** (`:class:`Handler``)
    The handler for the select menu.


## Class `SelectDefaultValue`

Represents a discord select menu default option object.
Only applicable for non string select menus.

### Parameters

- **id** (`:class:`str``)
    The id of the user, role or channel.
- **type** (`:class:`SelectDefaultValueType``)
    The type of the default value.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/select.py`
- Line: `10`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns a dictionary representation of the button.

This is used internally by the library. You should not need to use this method.

### Returns

:class:`dict`
    The dictionary representation of the button.


## Class `SelectOption`

Represents a discord select menu option object.

### Parameters

- **label** (`:class:`str``)
    The text to be displayed on the option.
- **value** (`:class:`str``)
    The value to be sent to the bot when the option is selected.
- **description** (`str | None`)
    The description to be displayed on the option.
- **emoji** (`:class:`str` | :class:`PartialEmoji` | None`)
    The emoji to be displayed on the option.
- **default** (`:class:`bool``)
    Whether the option is selected by default or not.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/select.py`
- Line: `42`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns a dictionary representation of the button.

This is used internally by the library. You should not need to use this method.

### Returns

:class:`dict`
    The dictionary representation of the button.


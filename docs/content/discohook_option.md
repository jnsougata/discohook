---
title: discohook.option
---

# `discohook.option`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/option.py`

## Classes

- [Choice](#class-choice)
- [Option](#class-option)

## Class `Choice`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/option.py`
- Line: `6`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `Option`

Represents a base option for an application command.

### Parameters

- **name** (`str`)
    The name of the option. Must be a valid python identifier.
- **description** (`str`)
    The description of the option.
- **required** (`bool`)
    Whether the option is required or not.
- **kind** (`AppCmdOptionType`)
    The type of the option.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/option.py`
- Line: `15`

### Methods

#### `attachment`

```python
attachment(name: str, description: str, *, required: bool | None = False)
```

#### `boolean`

```python
boolean(name: str, description: str, *, required: bool | None = False)
```

#### `channel`

```python
channel(name: str, description: str, *, required: bool | None = False, types: List[discohook.enums.ChannelType] | None = None)
```

#### `integer`

```python
integer(name: str, description: str, *, required: bool | None = False, max_value: int | None = None, min_value: int | None = None, choices: List[discohook.option.Choice] | None = None, autocomplete: bool | None = False)
```

#### `mentionable`

```python
mentionable(name: str, description: str, *, required: bool | None = False)
```

#### `number`

```python
number(name: str, description: str, *, required: bool | None = False, max_value: float | None = None, min_value: float | None = None, choices: List[discohook.option.Choice] | None = None, autocomplete: bool | None = False)
```

#### `role`

```python
role(name: str, description: str, *, required: bool | None = False)
```

#### `string`

```python
string(name: str, description: str, *, required: bool | None = False, max_length: int | None = None, min_length: int | None = None, choices: List[discohook.option.Choice] | None = None, autocomplete: bool | None = False)
```

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

#### `user`

```python
user(name: str, description: str, *, required: bool | None = False)
```


---
title: discohook.option
---

# `discohook.option`

## Classes

- [Choice](#class-choice)
- [Option](#class-option)

<a id="class-choice"></a>
## Class `Choice`

**Qualified Name:** `discohook.option.Choice`

### Method Index

- [to_dict](#choice-to-dict)

### Methods

<a id="choice-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-option"></a>
## Class `Option`

**Qualified Name:** `discohook.option.Option`

Represents a base option for an application command.

Parameters
----------
name: str
The name of the option. Must be a valid python identifier.
description: str
The description of the option.
required: bool
Whether the option is required or not.
kind: AppCmdOptionType
The type of the option.

### Method Index

- [attachment](#option-attachment)
- [boolean](#option-boolean)
- [channel](#option-channel)
- [integer](#option-integer)
- [mentionable](#option-mentionable)
- [number](#option-number)
- [role](#option-role)
- [string](#option-string)
- [to_dict](#option-to-dict)
- [user](#option-user)

### Methods

<a id="option-attachment"></a>
#### `attachment`

<a id="option-boolean"></a>
#### `boolean`

<a id="option-channel"></a>
#### `channel`

<a id="option-integer"></a>
#### `integer`

<a id="option-mentionable"></a>
#### `mentionable`

<a id="option-number"></a>
#### `number`

<a id="option-role"></a>
#### `role`

<a id="option-string"></a>
#### `string`

<a id="option-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

<a id="option-user"></a>
#### `user`


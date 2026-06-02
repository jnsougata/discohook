---
title: discohook.common
---

# `discohook.common`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/common.py`

## Classes

- [Component](#class-component)
- [Interactable](#class-interactable)

## Class `Component`

Represents a discord component.

### Parameters

- **type** (`:class:`ComponentType``)
    The type of the component.

### Inheritance

- `discohook.common.Interactable`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/common.py`
- Line: `61`

### Methods

#### `check`

```python
check(self)
```

A decorator that adds a check to a specific command or component.

#### `error_handler`

```python
error_handler(self)
```

A decorator that adds an error handler to a specific command or component.

#### `to_dict`

```python
to_dict(self)
```

Convert the component to a dict to be sent to discord. For internal use only.


## Class `Interactable`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/common.py`
- Line: `10`

### Methods

#### `check`

```python
check(self)
```

A decorator that adds a check to a specific command or component.

#### `error_handler`

```python
error_handler(self)
```

A decorator that adds an error handler to a specific command or component.

#### `to_dict`

```python
to_dict(self)
```

Convert the component to a dict to be sent to discord. For internal use only.


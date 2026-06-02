---
title: discohook.handler
---

# `discohook.handler`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/handler.py`

## Classes

- [Handler](#class-handler)

## Class `Handler`

A class to handle interactions from a component or command.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/handler.py`
- Line: `9`

### Methods

#### `check`

```python
check(self)
```

A decorator that adds a check to a specific command or component.

#### `fork`

```python
fork(self, suffix: str, separator: str = '::') -> 'Handler'
```

Forks a generic handler into a new handler with a different ID.

### Parameters

- **suffix** (`str`)
    The suffix to append to the original ID.
- **separator** (`str`)
    The separator to use between the original ID and the suffix. Default is "::".

#### `on_error`

```python
on_error(self)
```

A decorator that adds an error handler to a specific command or component.


## Functions

- [handler](#handler)

## `handler`

### Signature

```python
handler(id: str) -> Callable[[Callable[[ForwardRef('Interaction'), Any], Any]], discohook.handler.Handler]
```

A decorator that creates a handler.

### Parameters

- **id** (`str`)
    The ID of the component or command.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/handler.py`
- Line: `77`


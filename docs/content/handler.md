---
title: discohook.handler
---

# `discohook.handler`

## Classes

- [Handler](#class-handler)

## Functions

- [handler](#handler)

<a id="class-handler"></a>
## Class `Handler`

**Qualified Name:** `discohook.handler.Handler`

A class to handle interactions from a component or command.

### Method Index

- [check](#handler-check)
- [fork](#handler-fork)
- [on_error](#handler-on-error)

### Methods

<a id="handler-check"></a>
#### `check`

```python
check(self)
```

A decorator that adds a check to a specific command or component.

<a id="handler-fork"></a>
#### `fork`

```python
fork(self, suffix: str, separator: str = '::') -> 'Handler'
```

Forks a generic handler into a new handler with a different ID.

Parameters
----------
suffix: str
The suffix to append to the original ID.
separator: str
The separator to use between the original ID and the suffix. Default is "::".

<a id="handler-on-error"></a>
#### `on_error`

```python
on_error(self)
```

A decorator that adds an error handler to a specific command or component.


<a id="handler"></a>
## `handler`

**Qualified Name:** `discohook.handler.handler`

### Signature

```python
handler(id: str) -> Callable[[Callable[[ForwardRef('Interaction'), Any], Any]], discohook.handler.Handler]
```

A decorator that creates a handler.

Parameters
----------
id: str
The ID of the component or command.


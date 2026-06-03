---
title: discohook.common
---

# `discohook.common`

## Classes

- [Component](#class-component)
- [Interactable](#class-interactable)

<a id="class-component"></a>
## Class `Component`

**Qualified Name:** `discohook.common.Component`

Represents a discord component.

### Arguments

- **type** (`ComponentType | None`): Type of the component.
- **custom_id** (`str | None`): Custom ID of the component.

### Inheritance

- `discohook.common.Interactable`


<a id="class-interactable"></a>
## Class `Interactable`

**Qualified Name:** `discohook.common.Interactable`

### Method Index

- [check](#interactable-check)
- [error_handler](#interactable-error-handler)
- [to_dict](#interactable-to-dict)

### Methods

<a id="interactable-check"></a>
#### `check`

```python
check(self)
```

Decorator that adds a check to a specific command or component.

<a id="interactable-error-handler"></a>
#### `error_handler`

```python
error_handler(self)
```

Decorator that adds an error handler to a specific command or component.

<a id="interactable-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```

Convert the component to a dict. For internal use only.


---
title: discohook.button
---

# `discohook.button`

## Classes

- [Button](#class-button)

<a id="class-button"></a>
## Class `Button`

**Qualified Name:** `discohook.button.Button`

Represents a discord button type component.

### Attributes

- **label** (`str`): Label of the button.
- **url** (`str | None`): Url to be opened for `ButtonStyle.link`.
- **style** (`ButtonStyle`): Style of the button.
- **disabled** (`bool`): Whether the button is disabled or not.
- **emoji** (`PartialEmoji`): Emoji object for the button.
- **handler** (`Handler`): Handler for the button.

### Method Index

- [to_dict](#button-to-dict)

### Methods

<a id="button-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Builds a dictionary representation of the button.

This is used internally by the library. It is rarely required for general purpose use cases.

### Returns

- **Type:** `dict`
  - Dictionary representation of the button.


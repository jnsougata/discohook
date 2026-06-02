---
title: discohook.button
---

# `discohook.button`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/button.py`

## Classes

- [Button](#class-button)

## Class `Button`

Represents a discord button type component.

Attributes:
    label (str): Label of the button.
    url (str | None): Url to be opened for `ButtonStyle.link`.
    style (ButtonStyle): Style of the button.
    disabled (bool): Whether the button is disabled or not.
    emoji (PartialEmoji): Emoji object for the button.
    handler (Handler): Handler for the button.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/button.py`
- Line: `8`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Builds a dictionary representation of the button.

This is used internally by the library. It is rarely required for general purpose use cases.

Returns:
    dict: Dictionary representation of the button.


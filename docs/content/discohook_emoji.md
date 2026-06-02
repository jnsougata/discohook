---
title: discohook.emoji
---

# `discohook.emoji`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/emoji.py`

## Classes

- [PartialEmoji](#class-partialemoji)

## Class `PartialEmoji`

Represents a discord PartialEmoji object.

### Parameters

- **name** (`:class:`str``)
    The name of the emoji.
- **id** (`:class:`str``)
    The unique id of the emoji.
- **animated** (`:class:`bool``)
    Whether the emoji is animated.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/emoji.py`
- Line: `5`

### Methods

#### `from_str`

```python
from_str(value: str) -> 'PartialEmoji'
```

Creates a partial emoji from a string formatted emoji.

### Parameters

- **value** (`:class:`str``)
    The string formatted emoji.

#### `to_dict`

```python
to_dict(self) -> dict
```


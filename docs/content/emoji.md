---
title: discohook.emoji
---

# `discohook.emoji`

## Classes

- [PartialEmoji](#class-partialemoji)

<a id="class-partialemoji"></a>
## Class `PartialEmoji`

**Qualified Name:** `discohook.emoji.PartialEmoji`

Represents a discord PartialEmoji object.

### Arguments

- **name** (`str | None`): Name of the emoji.
- **id** (`str | None`): ID of the emoji.
- **animated** (`bool | None`): Whether the emoji is animated.

### Method Index

- [from_str](#partialemoji-from-str)
- [to_dict](#partialemoji-to-dict)

### Methods

<a id="partialemoji-from-str"></a>
#### `from_str`

Creates a partial emoji from a string formatted emoji.

### Arguments

- **value** (`str`): Emoji string.

### Returns

- **Type:** `PartialEmoji`
  - PartialEmoji object.

<a id="partialemoji-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> dict
```


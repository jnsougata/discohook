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

Parameters
----------
name: :class:`str`
The name of the emoji.
id: :class:`str`
The unique id of the emoji.
animated: :class:`bool`
Whether the emoji is animated.

### Method Index

- [from_str](#partialemoji-from-str)
- [to_dict](#partialemoji-to-dict)

### Methods

<a id="partialemoji-from-str"></a>
#### `from_str`

Creates a partial emoji from a string formatted emoji.

Parameters
----------
value: :class:`str`
The string formatted emoji.

<a id="partialemoji-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> dict
```


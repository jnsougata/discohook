---
title: discohook.asset
---

# `discohook.asset`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/asset.py`

## Classes

- [Asset](#class-asset)

## Class `Asset`

Represents a Discord asset.

This is used internally by the library. You should not need to use this.
Args:
    hash (str): The hash of the asset.
    fragment (str): The fragment of the asset.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/asset.py`
- Line: `1`

### Methods

#### `url_as`

```python
url_as(self, *, format: str = 'png', size: int = 1024) -> str
```

Constructs the URL of the asset in the specified size and format.

Args:
    format (str): The format of the asset.
    size (int): The size of the asset.

Returns:
    str: The URL of the asset in the specified size and format.


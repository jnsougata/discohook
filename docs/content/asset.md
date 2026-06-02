---
title: discohook.asset
---

# `discohook.asset`

## Classes

- [Asset](#class-asset)

<a id="class-asset"></a>
## Class `Asset`

**Qualified Name:** `discohook.asset.Asset`

Represents a Discord asset.

This is used internally by the library. You should not need to use this.
### Arguments

- **hash** (`str`): The hash of the asset.
- **fragment** (`str`): The fragment of the asset.

### Property Index

- [default](#asset-default)
- [dynamic](#asset-dynamic)
- [url](#asset-url)

### Method Index

- [url_as](#asset-url-as)

### Properties

<a id="asset-default"></a>
#### `default`

Checks if the asset is a default avatar.

### Returns

- **Type:** `bool`
  - Whether the asset is a default avatar.

<a id="asset-dynamic"></a>
#### `dynamic`

Checks if the asset is animated or not.

### Returns

- **Type:** `bool`
  - Whether the asset is animated.

<a id="asset-url"></a>
#### `url`

Constructs the URL of the asset in its default size with `.webp` format.

### Returns

- **Type:** `str`
  - The URL of the asset in its default size with `.webp` format.

### Methods

<a id="asset-url-as"></a>
#### `url_as`

```python
url_as(self, *, format: str = 'png', size: int = 1024) -> str
```

Constructs the URL of the asset in the specified size and format.

### Arguments

- **format** (`str`): The format of the asset.
- **size** (`int`): The size of the asset.

### Returns

- **Type:** `str`
  - The URL of the asset in the specified size and format.


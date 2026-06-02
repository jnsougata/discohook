---
title: discohook.embed
---

# `discohook.embed`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/embed.py`

## Classes

- [Embed](#class-embed)

## Class `Embed`

Represents a discord Embed object.

### Parameters

- **title** (`str | None`)
    The title of the embed.
- **description** (`str | None`)
    The description of the embed.
- **url** (`str | None`)
    The url of the embed.
- **color** (`int | str | None`)
    The color of the embed in hex or int.
- **timestamp** (`str | None`)
    The timestamp of the embed.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/embed.py`
- Line: `7`

### Methods

#### `add_field`

```python
add_field(self, name: str, value: str, *, inline: bool = False)
```

Adds a field to the embed.

### Parameters

- **name** (`:class:`str``)
    The name of the field.
- **value** (`:class:`str``)
    The value of the field.
- **inline** (`:class:`bool``)
    Whether the field is inline.

#### `from_dict`

```python
from_dict(data: Dict[str, Any]) -> 'Embed'
```

Creates an embed from a dictionary.
This method is handy when you want to create an embed manually.

### Parameters

- **data** (`:class:`dict``)
    The dictionary to create the embed from.

### Returns

:class:`Embed`
    The created embed.

#### `set_author`

```python
set_author(self, *, name: str, url: str | None = None, icon_url: str | None = None)
```

Sets the author of the embed.

### Parameters

- **name** (`:class:`str``)
    The name of the author.
- **url** (`Optional[:class:`str`]`)
    The url of the author.
- **icon_url** (`Optional[:class:`str`]`)
    The icon url of the author.

#### `set_footer`

```python
set_footer(self, text: str, *, icon_url: str | None = None)
```

Sets the footer of the embed.

### Parameters

- **text** (`:class:`str``)
    The text of the footer.
- **icon_url** (`Optional[:class:`str`]`)
    The icon url of the footer.

#### `set_image`

```python
set_image(self, img: str | discohook.file.File)
```

Sets the image of the embed from a file attachment or url.

### Parameters

- **img** (`:class:`str` | :class:`File``)
    The url or file attachment of the image.

#### `set_thumbnail`

```python
set_thumbnail(self, img: str | discohook.file.File)
```

Sets the thumbnail of the embed.

### Parameters

- **img** (`:class:`str` | :class:`File``)
    The url or file attachment of the thumbnail.

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns the embed as a dictionary.

This method is used internally by the library. You will rarely need to use it.

### Returns

:class:`dict`
    The embed as a dictionary.


---
title: discohook.embed
---

# `discohook.embed`

## Classes

- [Embed](#class-embed)

<a id="class-embed"></a>
## Class `Embed`

**Qualified Name:** `discohook.embed.Embed`

Represents a discord Embed object.

Parameters
----------
title: str | None
The title of the embed.
description: str | None
The description of the embed.
url: str | None
The url of the embed.
color: int | str | None
The color of the embed in hex or int.
timestamp: str | None
The timestamp of the embed.

### Property Index

- [attachments](#embed-attachments)

### Method Index

- [add_field](#embed-add-field)
- [from_dict](#embed-from-dict)
- [set_author](#embed-set-author)
- [set_footer](#embed-set-footer)
- [set_image](#embed-set-image)
- [set_thumbnail](#embed-set-thumbnail)
- [to_dict](#embed-to-dict)

### Properties

<a id="embed-attachments"></a>
#### `attachments`

Returns the attachments of the embed.

### Methods

<a id="embed-add-field"></a>
#### `add_field`

```python
add_field(self, name: str, value: str, *, inline: bool = False)
```

Adds a field to the embed.

Parameters
----------
name: :class:`str`
The name of the field.
value: :class:`str`
The value of the field.
inline: :class:`bool`
Whether the field is inline.

<a id="embed-from-dict"></a>
#### `from_dict`

Creates an embed from a dictionary.
This method is handy when you want to create an embed manually.

Parameters
----------
data: :class:`dict`
The dictionary to create the embed from.

Returns
-------
:class:`Embed`
The created embed.

<a id="embed-set-author"></a>
#### `set_author`

```python
set_author(self, *, name: str, url: str | None = None, icon_url: str | None = None)
```

Sets the author of the embed.

Parameters
----------
name: :class:`str`
The name of the author.
url: Optional[:class:`str`]
The url of the author.
icon_url: Optional[:class:`str`]
The icon url of the author.

<a id="embed-set-footer"></a>
#### `set_footer`

```python
set_footer(self, text: str, *, icon_url: str | None = None)
```

Sets the footer of the embed.

Parameters
----------
text: :class:`str`
The text of the footer.
icon_url: Optional[:class:`str`]
The icon url of the footer.

<a id="embed-set-image"></a>
#### `set_image`

```python
set_image(self, img: str | discohook.file.File)
```

Sets the image of the embed from a file attachment or url.

Parameters
----------
img: :class:`str` | :class:`File`
The url or file attachment of the image.

<a id="embed-set-thumbnail"></a>
#### `set_thumbnail`

```python
set_thumbnail(self, img: str | discohook.file.File)
```

Sets the thumbnail of the embed.

Parameters
----------
img: :class:`str` | :class:`File`
The url or file attachment of the thumbnail.

<a id="embed-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Returns the embed as a dictionary.

This method is used internally by the library. You will rarely need to use it.

Returns
-------
:class:`dict`
The embed as a dictionary.


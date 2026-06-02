---
title: discohook.view
---

# `discohook.view`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/view.py`

## Classes

- [View](#class-view)

## Class `View`

Represents a discord message component.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/view.py`
- Line: `13`

### Methods

#### `add_container`

```python
add_container(self, *components: discohook.components.ActionRow | discohook.components.TextDisplay | discohook.components.Section | discohook.components.MediaGallery | discohook.components.Separator | discohook.file.File, accent_color: int | None = None, id: int | None = None)
```

Appends a Container to the view.

### Parameters

- **components** (`Tuple[ActionRow | TextDisplay | Section | MediaGallery | Separator | File]`)
    The components to be added to the container.
- **accent_color** (`Optional[:class:`int`]`)
    The accent color of the container. This is used to identify the container when it is submitted.
- **id** (`str | None`)
    The id of the container. This is used to identify the container when it is submitted.

#### `add_file`

```python
add_file(self, *file: discohook.file.File)
```

Appends a FileAttachment to the view.

### Parameters

*file: :class:`File`
    The file to be attached. This is used to identify the file when it is submitted.

#### `add_gallery`

```python
add_gallery(self, *media: discohook.components.Media, id: int | None = None)
```

Appends a MediaGallery to the view.

### Parameters

- **media** (`:class:`Media``)
    The media to be added to the gallery.
- **id** (`Optional[:class:`int`]`)

#### `add_row`

```python
add_row(self, *components: discohook.button.Button | discohook.select.Select, id: int | None = None)
```

Appends an ActionRow to the view.

### Parameters

- **components** (`:class:`Button` or :class:`Select``)
    The components to be added to the row.
- **id** (`Optional[:class:`str`]`)
    The id of the row. This is used to identify the row when it is submitted.

#### `add_section`

```python
add_section(self, *components: discohook.components.TextDisplay, accessory: discohook.button.Button | discohook.components.Thumbnail, id: int | None = None)
```

Appends a Section to the view.

### Parameters

*components: Tuple[TextDisplay]
    The components to be added to the section.
- **accessory** (`Union[:class:`Button`, :class:`Thumbnail`]`)
    The accessory to be added to the section. This can be a button or a thumbnail.
- **id** (`Optional[:class:`str`]`)
    The id of the section. This is used to identify the section when it is submitted.

#### `add_separator`

```python
add_separator(self, id: int | None = None, spacing: int = 1)
```

Appends a Separator to the view.

#### `from_children`

```python
from_children(*children: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```


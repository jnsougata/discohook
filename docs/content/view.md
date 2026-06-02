---
title: discohook.view
---

# `discohook.view`

## Classes

- [View](#class-view)

<a id="class-view"></a>
## Class `View`

**Qualified Name:** `discohook.view.View`

Represents a discord message component.

### Method Index

- [add_container](#view-add-container)
- [add_file](#view-add-file)
- [add_gallery](#view-add-gallery)
- [add_row](#view-add-row)
- [add_section](#view-add-section)
- [add_separator](#view-add-separator)
- [from_children](#view-from-children)

### Methods

<a id="view-add-container"></a>
#### `add_container`

```python
add_container(self, *components: discohook.components.ActionRow | discohook.components.TextDisplay | discohook.components.Section | discohook.components.MediaGallery | discohook.components.Separator | discohook.file.File, accent_color: int | None = None, id: int | None = None)
```

Appends a Container to the view.

Parameters
----------
components: Tuple[ActionRow | TextDisplay | Section | MediaGallery | Separator | File]
The components to be added to the container.
accent_color: Optional[:class:`int`]
The accent color of the container. This is used to identify the container when it is submitted.
id: str | None
The id of the container. This is used to identify the container when it is submitted.

<a id="view-add-file"></a>
#### `add_file`

```python
add_file(self, *file: discohook.file.File)
```

Appends a FileAttachment to the view.

Parameters
----------
*file: :class:`File`
The file to be attached. This is used to identify the file when it is submitted.

<a id="view-add-gallery"></a>
#### `add_gallery`

```python
add_gallery(self, *media: discohook.components.Media, id: int | None = None)
```

Appends a MediaGallery to the view.

Parameters
----------
media: :class:`Media`
The media to be added to the gallery.
id: Optional[:class:`int`]

<a id="view-add-row"></a>
#### `add_row`

```python
add_row(self, *components: discohook.button.Button | discohook.select.Select, id: int | None = None)
```

Appends an ActionRow to the view.

Parameters
----------
components: :class:`Button` or :class:`Select`
The components to be added to the row.
id: Optional[:class:`str`]
The id of the row. This is used to identify the row when it is submitted.

<a id="view-add-section"></a>
#### `add_section`

```python
add_section(self, *components: discohook.components.TextDisplay, accessory: discohook.button.Button | discohook.components.Thumbnail, id: int | None = None)
```

Appends a Section to the view.

Parameters
----------
*components: Tuple[TextDisplay]
The components to be added to the section.
accessory: Union[:class:`Button`, :class:`Thumbnail`]
The accessory to be added to the section. This can be a button or a thumbnail.
id: Optional[:class:`str`]
The id of the section. This is used to identify the section when it is submitted.

<a id="view-add-separator"></a>
#### `add_separator`

```python
add_separator(self, id: int | None = None, spacing: int = 1)
```

Appends a Separator to the view.

<a id="view-from-children"></a>
#### `from_children`


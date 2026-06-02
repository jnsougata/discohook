---
title: discohook.components
---

# `discohook.components`

## Classes

- [ActionRow](#class-actionrow)
- [Checkbox](#class-checkbox)
- [CheckboxGroup](#class-checkboxgroup)
- [CheckboxGroupOption](#class-checkboxgroupoption)
- [Container](#class-container)
- [FileUpload](#class-fileupload)
- [Label](#class-label)
- [Media](#class-media)
- [MediaGallery](#class-mediagallery)
- [RadioGroup](#class-radiogroup)
- [RadioGroupOption](#class-radiogroupoption)
- [Section](#class-section)
- [Separator](#class-separator)
- [TextDisplay](#class-textdisplay)
- [TextInput](#class-textinput)
- [Thumbnail](#class-thumbnail)

<a id="class-actionrow"></a>
## Class `ActionRow`

**Qualified Name:** `discohook.components.ActionRow`

### Method Index

- [to_dict](#actionrow-to-dict)

### Methods

<a id="actionrow-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-checkbox"></a>
## Class `Checkbox`

**Qualified Name:** `discohook.components.Checkbox`

### Method Index

- [to_dict](#checkbox-to-dict)

### Methods

<a id="checkbox-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-checkboxgroup"></a>
## Class `CheckboxGroup`

**Qualified Name:** `discohook.components.CheckboxGroup`

### Method Index

- [to_dict](#checkboxgroup-to-dict)

### Methods

<a id="checkboxgroup-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-checkboxgroupoption"></a>
## Class `CheckboxGroupOption`

**Qualified Name:** `discohook.components.CheckboxGroupOption`

### Method Index

- [to_dict](#checkboxgroupoption-to-dict)

### Methods

<a id="checkboxgroupoption-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-container"></a>
## Class `Container`

**Qualified Name:** `discohook.components.Container`

### Method Index

- [to_dict](#container-to-dict)

### Methods

<a id="container-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-fileupload"></a>
## Class `FileUpload`

**Qualified Name:** `discohook.components.FileUpload`

Represents a file upload component in a modal.

Parameters
----------
custom_id: :class:`str`
The label of the file upload field.
id: :class:`int`
A unique id of the file upload field. Must be valid python identifier.
min_values: :class:`int`
Minimum number of items that must be uploaded (defaults to 1); min 0, max 10
max_values: :class:`int`
Maximum number of items that can be uploaded (defaults to 1); max 10
required: :class:`bool`
Whether this component is required to be filled (defaults to true).

### Method Index

- [to_dict](#fileupload-to-dict)

### Methods

<a id="fileupload-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-label"></a>
## Class `Label`

**Qualified Name:** `discohook.components.Label`

### Method Index

- [to_dict](#label-to-dict)

### Methods

<a id="label-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-media"></a>
## Class `Media`

**Qualified Name:** `discohook.components.Media`

### Method Index

- [to_dict](#media-to-dict)

### Methods

<a id="media-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-mediagallery"></a>
## Class `MediaGallery`

**Qualified Name:** `discohook.components.MediaGallery`

### Method Index

- [to_dict](#mediagallery-to-dict)

### Methods

<a id="mediagallery-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-radiogroup"></a>
## Class `RadioGroup`

**Qualified Name:** `discohook.components.RadioGroup`

### Method Index

- [to_dict](#radiogroup-to-dict)

### Methods

<a id="radiogroup-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-radiogroupoption"></a>
## Class `RadioGroupOption`

**Qualified Name:** `discohook.components.RadioGroupOption`

### Method Index

- [to_dict](#radiogroupoption-to-dict)

### Methods

<a id="radiogroupoption-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-section"></a>
## Class `Section`

**Qualified Name:** `discohook.components.Section`

### Method Index

- [to_dict](#section-to-dict)

### Methods

<a id="section-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-separator"></a>
## Class `Separator`

**Qualified Name:** `discohook.components.Separator`

### Method Index

- [to_dict](#separator-to-dict)

### Methods

<a id="separator-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-textdisplay"></a>
## Class `TextDisplay`

**Qualified Name:** `discohook.components.TextDisplay`

### Method Index

- [to_dict](#textdisplay-to-dict)

### Methods

<a id="textdisplay-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-textinput"></a>
## Class `TextInput`

**Qualified Name:** `discohook.components.TextInput`

Represents a text input field in a modal.

Parameters
----------
custom_id: :class:`str`
The label of the text input field.
id: :class:`int`
A unique id of the text input field. Must be valid python identifier.
required: :class:`bool`
Whether this component is required to be filled (defaults to true).
placeholder: :class:`str`
Custom placeholder text if the input is empty; max 100 characters.
value: :class:`str`
Pre-filled value for this component; max 4000 characters.
min_length: :class:`int`
The minimum length of the text input field.
max_length: :class:`int`
The maximum length of the text input field.
style: :class:`TextInputFieldLength`
The style of the text input field.

### Method Index

- [to_dict](#textinput-to-dict)

### Methods

<a id="textinput-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```


<a id="class-thumbnail"></a>
## Class `Thumbnail`

**Qualified Name:** `discohook.components.Thumbnail`

### Method Index

- [to_dict](#thumbnail-to-dict)

### Methods

<a id="thumbnail-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


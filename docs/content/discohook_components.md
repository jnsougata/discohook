---
title: discohook.components
---

# `discohook.components`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`

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

## Class `ActionRow`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `31`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `Checkbox`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `337`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `CheckboxGroup`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `381`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `CheckboxGroupOption`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `358`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `Container`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `194`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `FileUpload`

Represents a file upload component in a modal.

### Parameters

- **custom_id** (`:class:`str``)
    The label of the file upload field.
- **id** (`:class:`int``)
    A unique id of the file upload field. Must be valid python identifier.
- **min_values** (`:class:`int``)
    Minimum number of items that must be uploaded (defaults to 1); min 0, max 10
- **max_values** (`:class:`int``)
    Maximum number of items that can be uploaded (defaults to 1); max 10
- **required** (`:class:`bool``)
    Whether this component is required to be filled (defaults to true).

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `291`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `Label`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `461`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `Media`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `53`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `MediaGallery`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `79`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `RadioGroup`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `436`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `RadioGroupOption`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `414`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `Section`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `150`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `Separator`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `177`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `TextDisplay`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `99`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `TextInput`

Represents a text input field in a modal.

### Parameters

- **custom_id** (`:class:`str``)
    The label of the text input field.
- **id** (`:class:`int``)
    A unique id of the text input field. Must be valid python identifier.
- **required** (`:class:`bool``)
    Whether this component is required to be filled (defaults to true).
- **placeholder** (`:class:`str``)
    Custom placeholder text if the input is empty; max 100 characters.
- **value** (`:class:`str``)
    Pre-filled value for this component; max 4000 characters.
- **min_length** (`:class:`int``)
    The minimum length of the text input field.
- **max_length** (`:class:`int``)
    The maximum length of the text input field.
- **style** (`:class:`TextInputFieldLength``)
    The style of the text input field.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `230`

### Methods

#### `to_dict`

```python
to_dict(self)
```


## Class `Thumbnail`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/components.py`
- Line: `114`

### Methods

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


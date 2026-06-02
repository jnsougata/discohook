---
title: discohook.modal
---

# `discohook.modal`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/modal.py`

## Classes

- [Modal](#class-modal)

## Class `Modal`

A modal for discord.

### Parameters

- **title** (`:class:`str``)
    The title of the modal.
- **handler** (`Handler`)
    The handler to control the modal submission.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/modal.py`
- Line: `11`

### Methods

#### `checkbox`

```python
checkbox(self, *, custom_id: str, label: str, id: int | None = None, default: bool = False)
```

Appends a checkbox component to the modal.

#### `checkbox_group`

```python
checkbox_group(self, *, id: int | None = None, custom_id: str, label: str, options: List[discohook.components.CheckboxGroupOption], min_values: int | None = None, max_values: int | None = None, required: bool = True)
```

Appends a checkbox group component to the modal.

#### `display`

```python
display(self, markdown: str, *, id: int | None = None)
```

Appends a text display component to the modal.

### Parameters


#### `file_upload`

```python
file_upload(self, *, label: str, custom_id: str, id: int | None = None, min_values: int = 1, max_values: int = 1, required: bool = True)
```

Appends a file upload component to the modal.

#### `input`

```python
input(self, *, custom_id: str, label: str, description: str | None = None, id: int | None = None, required: bool = True, placeholder: str | None = None, value: str | None = None, min_length: int = 0, max_length: int = 4000, style: discohook.enums.TextInputFieldLength = <TextInputFieldLength.short: 1>)
```

Appends a text input component to the modal.

#### `radio_group`

```python
radio_group(self, *, id: int | None = None, custom_id: str, label: str, options: List[discohook.components.RadioGroupOption], required: bool = True)
```

Appends a radio group component to the modal.

#### `select_menu`

```python
select_menu(self, *, custom_id: str, label: str, type: discohook.enums.SelectType, description: str | None = None, id: int | None = None, placeholder: str | None = None, min_values: int | None = None, max_values: int | None = None, options: List[discohook.select.SelectOption] | None = None, channel_types: List[discohook.enums.ChannelType] | None = None, default_values: List[discohook.select.SelectDefaultValue] | None = None)
```

Appends a select menu component to the modal.

#### `to_dict`

```python
to_dict(self)
```

Convert the modal to a dict to be sent to discord. For internal use only.


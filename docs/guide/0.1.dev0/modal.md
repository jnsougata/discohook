---
title: discohook.modal
---

# `discohook.modal`

## Classes

- [Modal](#class-modal)

<a id="class-modal"></a>
## Modal

`discohook.modal.Modal`

A modal for discord.
Parameters
----------
title: :class:`str`
The title of the modal.
handler: Handler
The handler to control the modal submission.

### Method Index

- [checkbox](#modal-checkbox)
- [checkbox_group](#modal-checkbox-group)
- [display](#modal-display)
- [file_upload](#modal-file-upload)
- [input](#modal-input)
- [radio_group](#modal-radio-group)
- [select_menu](#modal-select-menu)
- [to_dict](#modal-to-dict)

### Methods

<a id="modal-checkbox"></a>
#### `checkbox`

```python
checkbox(self, *, custom_id: str, label: str, id: int | None = None, default: bool = False)
```

Appends a checkbox component to the modal.

<a id="modal-checkbox-group"></a>
#### `checkbox_group`

```python
checkbox_group(self, *, id: int | None = None, custom_id: str, label: str, options: List[discohook.components.CheckboxGroupOption], min_values: int | None = None, max_values: int | None = None, required: bool = True)
```

Appends a checkbox group component to the modal.

<a id="modal-display"></a>
#### `display`

```python
display(self, markdown: str, *, id: int | None = None)
```

Appends a text display component to the modal.
Parameters
----

<a id="modal-file-upload"></a>
#### `file_upload`

```python
file_upload(self, *, label: str, custom_id: str, id: int | None = None, min_values: int = 1, max_values: int = 1, required: bool = True)
```

Appends a file upload component to the modal.

<a id="modal-input"></a>
#### `input`

```python
input(self, *, custom_id: str, label: str, description: str | None = None, id: int | None = None, required: bool = True, placeholder: str | None = None, value: str | None = None, min_length: int = 0, max_length: int = 4000, style: discohook.enums.TextInputFieldLength = <TextInputFieldLength.short: 1>)
```

Appends a text input component to the modal.

<a id="modal-radio-group"></a>
#### `radio_group`

```python
radio_group(self, *, id: int | None = None, custom_id: str, label: str, options: List[discohook.components.RadioGroupOption], required: bool = True)
```

Appends a radio group component to the modal.

<a id="modal-select-menu"></a>
#### `select_menu`

```python
select_menu(self, *, custom_id: str, label: str, type: discohook.enums.SelectType, description: str | None = None, id: int | None = None, placeholder: str | None = None, min_values: int | None = None, max_values: int | None = None, options: List[discohook.select.SelectOption] | None = None, channel_types: List[discohook.enums.ChannelType] | None = None, default_values: List[discohook.select.SelectDefaultValue] | None = None)
```

Appends a select menu component to the modal.

<a id="modal-to-dict"></a>
#### `to_dict`

```python
to_dict(self)
```

Convert the modal to a dict to be sent to discord. For internal use only.


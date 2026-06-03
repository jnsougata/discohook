---
title: discohook.file
---

# `discohook.file`

## Classes

- [File](#class-file)

<a id="class-file"></a>
## Class `File`

**Qualified Name:** `discohook.file.File`

Represents a file to send to Discord.

### Arguments

- **name** (`str | None`): Name of the file.
- **content** (`bytes | None`): Content of the file in bytes.
- **description** (`str | None`): Description of the file.
- **spoiler** (`bool`): Whether the file is a spoiler.
- **id** (`int | None`): ID of the file used to identify the file.

### Method Index

- [from_path](#file-from-path)
- [from_url](#file-from-url)
- [to_dict](#file-to-dict)

### Methods

<a id="file-from-path"></a>
#### `from_path`

Creates a File object from a file path.

### Arguments

- **path** (`str`): Path to the file.
- **spoiler** (`bool`): Whether the file is a spoiler.
- **description** (`str | None`): Description of the file to be sent.
- **id** (`int | None`): ID of the file used to identify the file.

### Returns

- **Type:** `File`
  - File object.

<a id="file-from-url"></a>
#### `from_url`

Creates a File object from a file URL.

### Arguments

- **url** (`str`): URL to the file.
- **description** (`str | None`): Description of the file to be sent.
- **spoiler** (`bool`): Whether the file is a spoiler.
- **id** (`int | None`): ID of the file used to identify the file.

### Returns

- **Type:** `File`
  - File object.

<a id="file-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


---
title: discohook.file
---

# `discohook.file`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/file.py`

## Classes

- [File](#class-file)

## Class `File`

Represents a file to send to Discord.

### Parameters

- **name** (`str`)
    The name of the file.
- **content** (`bytes`)
    The content of the file in bytes.
- **description** (`str | None`)
    The description of the file.
- **spoiler** (`bool`)
    Whether the file is a spoiler.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/file.py`
- Line: `7`

### Methods

#### `from_path`

```python
from_path(path: str, *, spoiler: bool = False, description: str | None = None, id: int | None = None)
```

Creates a File object from a file path.

### Parameters

- **path** (`str`)
    The path to the file.
- **spoiler** (`bool`)
    Whether the file is a spoiler.
- **description** (`str | None`)
    The description of the file to be sent.
- **id** (`int | None`)
    The id of the file. This is used to identify the file when it is submitted.

#### `from_url`

```python
from_url(url: str, *, description: str | None = None, spoiler: bool = False, id: int | None = None)
```

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


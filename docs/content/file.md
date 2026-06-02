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

Parameters
----------
name: str
The name of the file.
content: bytes
The content of the file in bytes.
description: str | None
The description of the file.
spoiler: bool
Whether the file is a spoiler.

### Method Index

- [from_path](#file-from-path)
- [from_url](#file-from-url)
- [to_dict](#file-to-dict)

### Methods

<a id="file-from-path"></a>
#### `from_path`

Creates a File object from a file path.

Parameters
----------
path: str
The path to the file.
spoiler: bool
Whether the file is a spoiler.
description: str | None
The description of the file to be sent.
id: int | None
The id of the file. This is used to identify the file when it is submitted.

<a id="file-from-url"></a>
#### `from_url`

<a id="file-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


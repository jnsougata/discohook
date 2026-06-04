---
title: discohook.file
---

# `discohook.file`

## Classes

- [File](#class-file)

<a id="class-file"></a>
## File

`discohook.file.File`

Represents a file to send to Discord.
#### _Arguments_

- _**name** (`str | None`): Name of the file._
- _**content** (`bytes | None`): Content of the file in bytes._
- _**description** (`str | None`): Description of the file._
- _**spoiler** (`bool`): Whether the file is a spoiler._
- _**id** (`int | None`): ID of the file used to identify the file._

### Method Index

- [from_path](#file-from-path)
- [from_url](#file-from-url)

### Methods

<a id="file-from-path"></a>
#### `from_path`

Creates a File object from a file path.
#### _Arguments_

- _**path** (`str`): Path to the file._
- _**spoiler** (`bool`): Whether the file is a spoiler._
- _**description** (`str | None`): Description of the file to be sent._
- _**id** (`int | None`): ID of the file used to identify the file._
#### _Returns_

- **Type:** `File`
  - File object.

<a id="file-from-url"></a>
#### `from_url`

Creates a File object from a file URL.
#### _Arguments_

- _**url** (`str`): URL to the file._
- _**description** (`str | None`): Description of the file to be sent._
- _**spoiler** (`bool`): Whether the file is a spoiler._
- _**id** (`int | None`): ID of the file used to identify the file._
#### _Returns_

- **Type:** `File`
  - File object.


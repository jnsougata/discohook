---
title: discohook.attachment
---

# `discohook.attachment`

## Classes

- [Attachment](#class-attachment)

<a id="class-attachment"></a>
## Attachment

`discohook.attachment.Attachment`

Represents a discord file attachment.
#### _Attributes_

- _**id** (`str`): ID of attachment._
- _**filename** (`str`): Filename of attachment._
- _**description** (`str`): Description of attachment._
- _**content_type** (`str`): Content type of attachment._
- _**size** (`int`): Size of attachment._
- _**url** (`str`): URL of attachment._
- _**proxy_url** (`str`): Proxy URL of attachment._
- _**height** (`int`): Height of attachment._
- _**width** (`int`): Width of attachment._
- _**ephemeral** (`bool`): Whether attachment is ephemeral._
- _**duration_secs** (`int`): Duration of attachment._
- _**waveform** (`str`): Waveform of attachment._
- _**flags** (`int`): Flags of attachment._
- _**placeholder** (`str`): Placeholder of attachment._
- _**placeholder_version** (`int`): Placeholder version of attachment._

### Method Index

- [iter](#attachment-iter)
- [read](#attachment-read)

### Methods

<a id="attachment-iter"></a>
#### `iter`

```python
async iter(self) -> aiohttp.streams.StreamReader
```

Creates an asynchronous generator.
#### _Returns_

- **Type:** `aiohttp.StreamReader`
  - Asynchronous generator.

<a id="attachment-read"></a>
#### `read`

```python
async read(self) -> bytes
```

Reads content of attachment.
#### _Returns_

- **Type:** `bytes`
  - Content of attachment in bytes.


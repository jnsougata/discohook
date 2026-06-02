---
title: discohook.attachment
---

# `discohook.attachment`

## Classes

- [Attachment](#class-attachment)

<a id="class-attachment"></a>
## Class `Attachment`

**Qualified Name:** `discohook.attachment.Attachment`

Represents a discord file attachment.

### Attributes

- **id** (`str`): ID of attachment.
- **filename** (`str`): Filename of attachment.
- **description** (`str`): Description of attachment.
- **content_type** (`str`): Content type of attachment.
- **size** (`int`): Size of attachment.
- **url** (`str`): URL of attachment.
- **proxy_url** (`str`): Proxy URL of attachment.
- **height** (`int`): Height of attachment.
- **width** (`int`): Width of attachment.
- **ephemeral** (`bool`): Whether attachment is ephemeral.
- **duration_secs** (`int`): Duration of attachment.
- **waveform** (`str`): Waveform of attachment.
- **flags** (`int`): Flags of attachment.
- **placeholder** (`str`): Placeholder of attachment.
- **placeholder_version** (`int`): Placeholder version of attachment.

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

### Returns

- **Type:** `aiohttp.StreamReader`
  - Asynchronous generator.

<a id="attachment-read"></a>
#### `read`

```python
async read(self) -> bytes
```

Reads content of attachment.

### Returns

- **Type:** `bytes`
  - Content of attachment in bytes.


---
title: discohook.attachment
---

# `discohook.attachment`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/attachment.py`

## Classes

- [Attachment](#class-attachment)

## Class `Attachment`

Represents a discord file attachment.

Attributes:
    id (str): ID of attachment.
    filename (str): Filename of attachment.
    description (str): Description of attachment.
    content_type (str): Content type of attachment.
    size (int): Size of attachment.
    url (str): URL of attachment.
    proxy_url (str): Proxy URL of attachment.
    height (int): Height of attachment.
    width (int): Width of attachment.
    ephemeral (bool): Whether attachment is ephemeral.
    duration_secs (int): Duration of attachment.
    waveform (str): Waveform of attachment.
    flags (int): Flags of attachment.
    placeholder (str): Placeholder of attachment.
    placeholder_version (int): Placeholder version of attachment.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/attachment.py`
- Line: `6`

### Methods

#### `iter`

```python
iter(self) -> aiohttp.streams.StreamReader
```

Creates an asynchronous generator.

Returns:
    aiohttp.StreamReader: Asynchronous generator.

#### `read`

```python
read(self) -> bytes
```

Reads content of attachment.

Returns:
    bytes: Content of attachment in bytes.


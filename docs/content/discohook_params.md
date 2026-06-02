---
title: discohook.params
---

# `discohook.params`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/params.py`

## Functions

- [_append_file](#-append-file)
- [_prepare_payload](#-prepare-payload)

## `_append_file`

### Signature

```python
_append_file(form: aiohttp.multipart.MultipartWriter, index: int, file: discohook.file.File) -> None
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/params.py`
- Line: `15`


## `_prepare_payload`

### Signature

```python
_prepare_payload(view: discohook.view.View, *, ephemeral: bool | None = False, allowed_mentions: discohook.models.AllowedMentions | None = None, message_reference: discohook.models.MessageReference | None = None, suppress_embeds: bool | None = False, supress_notifications: bool | None = False, payload_type: discohook.enums.InteractionCallbackType | None = None, **kwargs: Any) -> Dict[str, Any] | aiohttp.multipart.MultipartWriter
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/params.py`
- Line: `26`


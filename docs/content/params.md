---
title: discohook.params
---

# `discohook.params`

## Functions

- [_append_file](#-append-file)
- [_prepare_payload](#-prepare-payload)

<a id="-append-file"></a>
## `_append_file`

**Qualified Name:** `discohook.params._append_file`

### Signature

```python
_append_file(form: aiohttp.multipart.MultipartWriter, index: int, file: discohook.file.File) -> None
```


<a id="-prepare-payload"></a>
## `_prepare_payload`

**Qualified Name:** `discohook.params._prepare_payload`

### Signature

```python
_prepare_payload(view: discohook.view.View, *, ephemeral: bool | None = False, allowed_mentions: discohook.models.AllowedMentions | None = None, message_reference: discohook.models.MessageReference | None = None, suppress_embeds: bool | None = False, supress_notifications: bool | None = False, payload_type: discohook.enums.InteractionCallbackType | None = None, **kwargs: Any) -> Dict[str, Any] | aiohttp.multipart.MultipartWriter
```


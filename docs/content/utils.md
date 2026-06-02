---
title: discohook.utils
---

# `discohook.utils`

## Functions

- [color_parser](#color-parser)
- [compare_password](#compare-password)
- [resolve_description](#resolve-description)
- [snowflake_time](#snowflake-time)
- [unwrap_user](#unwrap-user)

<a id="color-parser"></a>
## `color_parser`

**Qualified Name:** `discohook.utils.color_parser`

### Signature

```python
color_parser(color: int | str) -> int
```


<a id="compare-password"></a>
## `compare_password`

**Qualified Name:** `discohook.utils.compare_password`

### Signature

```python
compare_password(local: str, remote: str) -> bool
```


<a id="resolve-description"></a>
## `resolve_description`

**Qualified Name:** `discohook.utils.resolve_description`

### Signature

```python
resolve_description(name: str, description: Any, callback: Callable[[ForwardRef('Interaction'), Any], Coroutine[Any, Any, Any]]) -> str
```


<a id="snowflake-time"></a>
## `snowflake_time`

**Qualified Name:** `discohook.utils.snowflake_time`

### Signature

```python
snowflake_time(snowflake_id: str) -> float
```


<a id="unwrap-user"></a>
## `unwrap_user`

**Qualified Name:** `discohook.utils.unwrap_user`

### Signature

```python
unwrap_user(data: dict, guild_id: str) -> dict
```


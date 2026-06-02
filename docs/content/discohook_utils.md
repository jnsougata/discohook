---
title: discohook.utils
---

# `discohook.utils`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/utils.py`

## Functions

- [color_parser](#color-parser)
- [compare_password](#compare-password)
- [resolve_description](#resolve-description)
- [snowflake_time](#snowflake-time)
- [unwrap_user](#unwrap-user)

## `color_parser`

### Signature

```python
color_parser(color: int | str) -> int
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/utils.py`
- Line: `14`


## `compare_password`

### Signature

```python
compare_password(local: str, remote: str) -> bool
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/utils.py`
- Line: `10`


## `resolve_description`

### Signature

```python
resolve_description(name: str, description: Any, callback: Callable[[ForwardRef('Interaction'), Any], Coroutine[Any, Any, Any]]) -> str
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/utils.py`
- Line: `29`


## `snowflake_time`

### Signature

```python
snowflake_time(snowflake_id: str) -> float
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/utils.py`
- Line: `24`


## `unwrap_user`

### Signature

```python
unwrap_user(data: dict, guild_id: str) -> dict
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/utils.py`
- Line: `41`


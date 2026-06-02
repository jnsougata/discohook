---
title: discohook.ratelimit
---

# `discohook.ratelimit`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/ratelimit.py`

## Classes

- [Bucket](#class-bucket)
- [RatelimitMux](#class-ratelimitmux)

## Class `Bucket`

A dataclass that represents a rate limit bucket.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/ratelimit.py`
- Line: `5`


## Class `RatelimitMux`

A protocol that defines the methods and properties of a rate limit bucket.

### Inheritance

- `typing.Protocol`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/ratelimit.py`
- Line: `18`

### Methods

#### `get`

```python
get(self, path: str) -> discohook.ratelimit.Bucket | None
```

Get the rate limit bucket for the given path.

#### `insert`

```python
insert(self, path: str, *, limit: int, remaining: int, reset: float, reset_after: float, bucket: str) -> str
```

#### `is_rate_limited`

```python
is_rate_limited(self, path: str) -> bool
```

Check if the rate limit bucket for the given path is rate limited.

#### `reset`

```python
reset(self, path: str) -> None
```

Reset the rate limit bucket for the given path.


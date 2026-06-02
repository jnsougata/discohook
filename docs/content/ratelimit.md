---
title: discohook.ratelimit
---

# `discohook.ratelimit`

## Classes

- [Bucket](#class-bucket)
- [RatelimitMux](#class-ratelimitmux)

<a id="class-bucket"></a>
## Class `Bucket`

**Qualified Name:** `discohook.ratelimit.Bucket`

A dataclass that represents a rate limit bucket.


<a id="class-ratelimitmux"></a>
## Class `RatelimitMux`

**Qualified Name:** `discohook.ratelimit.RatelimitMux`

A protocol that defines the methods and properties of a rate limit bucket.

### Inheritance

- `typing.Protocol`

### Method Index

- [get](#ratelimitmux-get)
- [insert](#ratelimitmux-insert)
- [is_rate_limited](#ratelimitmux-is-rate-limited)
- [reset](#ratelimitmux-reset)

### Methods

<a id="ratelimitmux-get"></a>
#### `get`

```python
async get(self, path: str) -> discohook.ratelimit.Bucket | None
```

Get the rate limit bucket for the given path.

<a id="ratelimitmux-insert"></a>
#### `insert`

```python
async insert(self, path: str, *, limit: int, remaining: int, reset: float, reset_after: float, bucket: str) -> str
```

<a id="ratelimitmux-is-rate-limited"></a>
#### `is_rate_limited`

```python
async is_rate_limited(self, path: str) -> bool
```

Check if the rate limit bucket for the given path is rate limited.

<a id="ratelimitmux-reset"></a>
#### `reset`

```python
async reset(self, path: str) -> None
```

Reset the rate limit bucket for the given path.


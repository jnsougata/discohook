---
title: discohook.ratelimit
---

# `discohook.ratelimit`

## Classes

- [Bucket](#class-bucket)
- [RatelimitMux](#class-ratelimitmux)

<a id="class-bucket"></a>
## Bucket

`discohook.ratelimit.Bucket`

A dataclass that represents a rate limit bucket.


<a id="class-ratelimitmux"></a>
## RatelimitMux

`discohook.ratelimit.RatelimitMux`

A protocol that defines the methods and properties of a rate limit bucket.

### Inheritance

- `typing.Protocol`

### Method Index

- [get](#ratelimitmux-get)
- [is_rate_limited](#ratelimitmux-is-rate-limited)
- [reset](#ratelimitmux-reset)

### Methods

<a id="ratelimitmux-get"></a>
#### `get`

```python
async get(self, path: str) -> discohook.ratelimit.Bucket | None
```

Get the rate limit bucket for the given path.

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


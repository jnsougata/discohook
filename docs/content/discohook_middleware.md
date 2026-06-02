---
title: discohook.middleware
---

# `discohook.middleware`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/middleware.py`

## Classes

- [SingleUseSession](#class-singleusesession)

## Class `SingleUseSession`

This middleware creates a new aiohttp.ClientSession to handle this request.
This is helpful for some serverless providers
that handle each request in a new event loop but keep the same app instance.

### Inheritance

- `starlette.middleware.base.BaseHTTPMiddleware`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/middleware.py`
- Line: `7`

### Methods

#### `dispatch`

```python
dispatch(self, request: starlette.requests.Request, rre: collections.abc.Callable[[starlette.requests.Request], collections.abc.Awaitable[starlette.responses.Response]])
```


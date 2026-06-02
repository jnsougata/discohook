---
title: discohook.middleware
---

# `discohook.middleware`

## Classes

- [SingleUseSession](#class-singleusesession)

<a id="class-singleusesession"></a>
## Class `SingleUseSession`

**Qualified Name:** `discohook.middleware.SingleUseSession`

This middleware creates a new aiohttp.ClientSession to handle this request.
This is helpful for some serverless providers
that handle each request in a new event loop but keep the same app instance.

### Inheritance

- `starlette.middleware.base.BaseHTTPMiddleware`

### Method Index

- [dispatch](#singleusesession-dispatch)

### Methods

<a id="singleusesession-dispatch"></a>
#### `dispatch`

```python
async dispatch(self, request: starlette.requests.Request, rre: collections.abc.Callable[[starlette.requests.Request], collections.abc.Awaitable[starlette.responses.Response]])
```


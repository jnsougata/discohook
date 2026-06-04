---
title: discohook.middleware
---

# `discohook.middleware`

## Classes

- [SingleUseSession](#class-singleusesession)

<a id="class-singleusesession"></a>
## SingleUseSession

`discohook.middleware.SingleUseSession`

This middleware creates a new aiohttp.ClientSession to handle this request.
This is helpful for some serverless providers
that handle each request in a new event loop but keep the same app instance.

### Inheritance

- `starlette.middleware.base.BaseHTTPMiddleware`


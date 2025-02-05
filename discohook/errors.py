from typing import Any

import aiohttp


class InteractionTypeMismatch(Exception):
    """Raised when the interaction type is not the expected type."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class CheckFailure(Exception):
    """Raised when a check fails."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class UnknownInteractionType(Exception):
    """Raised when the interaction type is unknown."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class HTTPException(Exception):
    """Raised when an HTTP request operation fails."""

    def __init__(self, resp: aiohttp.ClientResponse, message: str):
        self.resp = resp
        super().__init__(message)

    @classmethod
    async def create(cls, resp: aiohttp.ClientResponse):
        if resp.headers.get("content-type") == "application/json":
            data = await resp.json()
        else:
            data = await resp.text()
        message = f"[{resp.status} {resp.method}] {resp.url.path}\n{data}"
        return cls(resp, message)

import json

import aiohttp

from .ratelimit import Bucket


class InteractionTypeMismatch(Exception):
    """Raised when the interaction type is not the expected type."""

    def __init__(self, message: str):
        super().__init__(message)


class CheckFailure(Exception):
    """Raised when a check fails."""

    def __init__(self, message: str):
        super().__init__(message)


class UnknownInteractionType(Exception):
    """Raised when the interaction type is unknown."""

    def __init__(self, message: str):
        super().__init__(message)


class HTTPException(Exception):
    """Raised when an HTTP request operation fails."""

    def __init__(self, response: aiohttp.ClientResponse, data: bytes):
        self.response = response
        if response.content_type == "application/json":
            self.data = json.loads(data)
        else:
            self.data = data.decode("utf-8")
        message = (
            f"[{response.method} {response.status}] {response.url.path}\n{self.data}"
        )
        super().__init__(message)


class RateLimitExceeded(Exception):
    """Raised when a rate limit is exceeded."""

    def __init__(self, path: str, bucket: Bucket):
        super().__init__(
            f"Rate limit exceeded for {path}. Retry after {bucket.reset_after} seconds."
        )
        self.bucket = bucket

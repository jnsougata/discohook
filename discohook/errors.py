import json
from typing import TYPE_CHECKING

import aiohttp

from .ratelimit import Bucket

if TYPE_CHECKING:
    from .interaction import Interaction


class InteractionException(Exception):
    """Base exception for Discohook."""

    def __init__(self, message: str, interaction: "Interaction"):
        self.message = message
        self.interaction = interaction
        super().__init__(message)


class InteractionTypeMismatch(InteractionException):
    """Raised when the interaction type is not the expected type."""

    def __init__(self, message: str, interaction: "Interaction"):
        super().__init__(message, interaction)


class CheckFailure(InteractionException):
    """Raised when a check fails."""

    def __init__(self, message: str, interaction: "Interaction"):
        super().__init__(message, interaction)


class UnknownInteractionType(InteractionException):
    """Raised when the interaction type is unknown."""

    def __init__(self, message: str, interaction: "Interaction"):
        super().__init__(message, interaction)


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
        message = (
            f"Rate limit exceeded for {path}. Retry after {bucket.reset_after} seconds."
        )
        super().__init__(message)

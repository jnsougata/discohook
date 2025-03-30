from typing import Any, TYPE_CHECKING

import aiohttp

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

    def __init__(self, resp: aiohttp.ClientResponse, data: Any):
        self.resp = resp
        message = f"[{resp.method}] {resp.url.path} {resp.status} with code({data['code']}): {data['message']}"
        super().__init__(message)

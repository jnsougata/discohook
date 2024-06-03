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
        self.message = message
        super().__init__(message)

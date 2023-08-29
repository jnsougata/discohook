from aiohttp import ClientResponse
from typing import Any, Dict


__all__ = [
    'Unauthorized',
    'NotFound',
    'BadRequest',
    'KeyConflict',
    'PayloadTooLarge',
    'DetaUnknownError',
    'IncompleteUpload',
    '_raise_or_return',
]


class Unauthorized(Exception):
    """
    Raised when the API key is invalid
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotFound(Exception):
    """
    Raised when a resource is not found
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BadRequest(Exception):
    """
    Raised when a request body is invalid
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class KeyConflict(Exception):
    """
    Raised when a key already exists in the base
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class PayloadTooLarge(Exception):
    """
    Raised when the payload size exceeds the limit of 10MB
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class IncompleteUpload(Exception):
    """
    Raised when a chunked upload is finalized without uploading all the chunks
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DetaUnknownError(Exception):
    """
    Raised when a generic error occurs
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


async def _raise_or_return(response: ClientResponse, ok: int = 200) -> Dict[str, Any]:
    if response.status == ok:
        return await response.json()
    if response.status == 401:
        raise Unauthorized("Invalid API key")
    if response.status == 413:
        raise PayloadTooLarge("Payload size exceeds the limit of 10MB")
    if response.status == 404:
        raise NotFound("Resource not found")
    errors = await response.json()
    message = ". ".join(errors['errors'])
    if response.status == 400:
        raise BadRequest(message)
    elif response.status == 409:
        raise KeyConflict(message)
    else:
        raise DetaUnknownError(message)



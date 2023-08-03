import hashlib
import secrets
from typing import Any, Callable, Coroutine

AsyncFunc = Callable[..., Coroutine[Any, Any, Any]]


def compare_password(local: str, remote: str) -> bool:
    return secrets.compare_digest(hashlib.sha256(local.encode()).hexdigest(), remote)


def auto_description(description: Any, callback: AsyncFunc) -> str:
    if description and isinstance(description, str):
        return description
    if callback.__doc__:
        return callback.__doc__.strip().split("\n")[0]
    raise TypeError("description is required")

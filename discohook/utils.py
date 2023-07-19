import hashlib
import secrets
from typing import Any, Callable, Coroutine

AsyncFunc = Callable[..., Coroutine[Any, Any, Any]]


def compare_password(local: str, remote: str) -> bool:
    return secrets.compare_digest(hashlib.sha256(local.encode()).hexdigest(), remote)

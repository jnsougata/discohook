import time
from typing import Optional, Protocol, runtime_checkable


@runtime_checkable
class RatelimitMux(Protocol):
    """
    A protocol that defines the methods and properties of a rate limit bucket.
    """

    def insert(
        self,
        path: str,
        *,
        limit: int,
        remaining: int,
        reset: float,
        reset_after: float,
        bucket: str,
    ) -> str: ...

    def reset(self, path: str) -> None: ...

    def get(self, path: str) -> Optional[dict]: ...

    def is_rate_limited(self, path: str) -> bool: ...

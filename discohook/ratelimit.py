from dataclasses import dataclass
from typing import Optional, Protocol, runtime_checkable


@dataclass
class Bucket:
    """
    A dataclass that represents a rate limit bucket.
    """

    limit: int
    remaining: int
    reset: float
    reset_after: float
    bucket: str


@runtime_checkable
class RatelimitMux(Protocol):
    """
    A protocol that defines the methods and properties of a rate limit bucket.
    """

    async def insert(
        self,
        path: str,
        *,
        limit: int,
        remaining: int,
        reset: float,
        reset_after: float,
        bucket: str,
    ) -> str: ...

    async def reset(self, path: str) -> None:
        """
        Reset the rate limit bucket for the given path.
        """
        ...

    async def get(self, path: str) -> Optional[Bucket]:
        """
        Get the rate limit bucket for the given path.
        """
        ...

    async def is_rate_limited(self, path: str) -> bool:
        """
        Check if the rate limit bucket for the given path is rate limited.
        """
        ...

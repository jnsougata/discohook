import asyncio
from typing import TYPE_CHECKING, Callable, List, Any, Optional

if TYPE_CHECKING:
    from .interaction import Interaction


class Interactable:

    def __init__(self):
        self.checks: List[Callable[["Interaction"], bool]] = []
        self._error_handler: Optional[Callable[["Interaction", Exception], Any]] = None

    def check(self):
        """
        A decorator that adds a check to a specific command or component.
        """
        def decorator(coro: Callable[["Interaction"], bool]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("check must be a coroutine")
            self.checks.append(coro)

        return decorator

    def error_handler(self):
        """
        A decorator that adds an error handler to a specific command or component.
        """
        def decorator(coro: Callable[["Interaction", Exception], None]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("error handler must be a coroutine")
            self._error_handler = coro

        return decorator

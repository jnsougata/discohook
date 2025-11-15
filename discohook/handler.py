import asyncio
from typing import TYPE_CHECKING, Any, Callable, List, Optional

if TYPE_CHECKING:
    from .interaction import Interaction


# noinspection PyShadowingBuiltins
class Handler:
    """
    A class to handle interactions from a component or command.
    """

    def __init__(self, id: str, callback: Callable[["Interaction", Any], Any]):
        """
        Initialize the handler.

        Parameters
        ----------
        id: str
            The ID of the component or unique key for the command.
        callback : Callable[["Interaction", Any], Any]
            The callback function to be called when the interaction is received.
        """
        self.id = id
        if not asyncio.iscoroutinefunction(callback):
            raise TypeError("Callback must be a coroutine.")
        self.callback = callback
        self.checks: List[Callable[["Interaction"], bool]] = []
        self._error_handler: Optional[Callable[["Interaction"], Any]] = None

    def fork(self, suffix: str, separator: str = "::") -> "Handler":
        """
        Forks a generic handler into a new handler with a different ID.

        Parameters
        ----------
        suffix: str
            The new ID suffix to append to the original ID.
        separator: str
            The separator to use between the original ID and the suffix. Default is "::".
        """
        return Handler(f"{self.id}{separator}{suffix}", ...)  # type: ignore

    def check(self):
        """
        A decorator that adds a check to a specific command or component.
        """

        def decorator(coro: Callable[["Interaction"], bool]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("check must be a coroutine")
            self.checks.append(coro)  # noqa
            return coro

        return decorator

    def on_error(self):
        """
        A decorator that adds an error handler to a specific command or component.
        """

        def decorator(coro: Callable[["Interaction"], None]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("error handler must be a coroutine")
            self._error_handler = coro

        return decorator

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning("No callback registered for this component.")
        return self.callback(*args, **kwargs)


# noinspection PyShadowingBuiltins
def handler(id: str) -> Callable[[Callable[["Interaction", Any], Any]], Handler]:
    """
    A decorator that creates a handler.

    Parameters
    ----------
    id: str
        The ID of the component or command.
    """

    def decorator(callback: Callable[["Interaction", Any], Any]):
        return Handler(id, callback)

    return decorator

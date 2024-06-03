import asyncio
import secrets
from typing import TYPE_CHECKING, Any, Callable, List, Optional

from .enums import ComponentType

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
            return coro

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


# noinspection PyShadowingBuiltins
class Component(Interactable):
    """
    Represents a discord component.

    Parameters
    ----------
    type: :class:`ComponentType`
        The type of the component.
    """

    def __init__(
        self, type: Optional[ComponentType] = None, custom_id: Optional[str] = None
    ):
        super().__init__()
        self.type = type
        self.callback: Optional[Callable[["Interaction", Any], Any]] = None
        self.custom_id = custom_id or secrets.token_urlsafe(8)

    def on_interaction(self):
        """
        Decorator that registers a callback to be called when the component is interacted with.

        Raises
        ------
        TypeError
            If the callback is not a coroutine.
        """

        def decorator(coro: Callable[["Interaction", Any], Any]):
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("Callback must be a coroutine.")
            self.callback = coro

        return decorator

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning("No callback registered for this component.")
        return self.callback(*args, **kwargs)

    def to_dict(self):
        """
        Convert the component to a dict to be sent to discord. For internal use only.
        """
        ...

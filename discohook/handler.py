import inspect
from typing import Callable, List, Optional

from .types import CallbackType, CheckType, ErrorHandlerType



# noinspection PyShadowingBuiltins
class Handler:
    """
    A class to handle interactions from a component or command.
    """

    def __init__(self, id: str, callback: CallbackType):
        """
        Initialize the handler.

        Args:
            id (str): The ID of the component or unique key for the command.
            callback (CallbackType): The callback function to be called when the interaction is received.
        """
        self.id = id
        if not inspect.iscoroutinefunction(callback):
            raise TypeError("Callback must be a coroutine.")
        self.callback = callback
        self.checks: List[CheckType] = []
        self._error_handler: Optional[ErrorHandlerType] = None

    def fork(self, suffix: str, separator: str = "::") -> "Handler":
        """
        Forks a generic handler into a new handler with a different ID.

        Args:
            suffix (str): The suffix to append to the original ID.
            separator (str): The separator to use between the original ID and the suffix. Default is "::".

        Returns:
            Handler: A new handler with the modified ID and the same callback.
        """
        return Handler(f"{self.id}{separator}{suffix}", self.callback)

    def check(self):
        """
        A decorator that adds a check to a specific command or component.
        """

        def decorator(coro: CheckType):
            if not inspect.iscoroutinefunction(coro):
                raise TypeError("check must be a coroutine")
            self.checks.append(coro)  # noqa
            return coro

        return decorator

    def on_error(self, coro: ErrorHandlerType):
        """
        A decorator that adds an error handler to a specific command or component.
        """
        if not inspect.iscoroutinefunction(coro):
            raise TypeError("error handler must be a coroutine")
        self._error_handler = coro  # noqa

    def __call__(self, *args, **kwargs):
        if not self.callback:
            raise RuntimeWarning("No callback registered for this component.")
        return self.callback(*args, **kwargs)


# noinspection PyShadowingBuiltins
def handler(id: str) -> Callable[[CallbackType], Handler]:
    """
    A decorator that creates a handler.

    Args:
        id (str): The unique key for the handler.
    """

    def decorator(callback: CallbackType) -> Handler:
        return Handler(id, callback)

    return decorator

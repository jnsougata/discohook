from typing import Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from .interaction import Interaction


CallbackType = Callable[["Interaction", Any], Any]
CheckType = Callable[["Interaction"], bool]
ErrorHandlerType = Callable[["Interaction"], None]
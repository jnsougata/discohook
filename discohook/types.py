from typing import TYPE_CHECKING, Any, Callable, List

if TYPE_CHECKING:
    from .interaction import Interaction


CallbackType = Callable[["Interaction", Any], Any]
ButtonCallbackType = Callable[["Interaction", str], Any]
SelectCallbackType = Callable[["Interaction", List[Any]], Any]
CheckType = Callable[["Interaction"], bool]
ErrorHandlerType = Callable[["Interaction"], None]

try:
    from typing import TypedDict, NotRequired
except (ModuleNotFoundError, ImportError):
    from typing_extensions import TypedDict, NotRequired

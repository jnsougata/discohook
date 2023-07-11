from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .interaction import Interaction


class InteractionTypeMismatch(Exception):
    """Raised when the interaction type is not the expected type."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class GlobalException(Exception):
    """Base exception class for discohook."""

    def __init__(self, message: str, interaction: "Interaction"):
        self.message = message
        self.interaction = interaction
        super().__init__(message)

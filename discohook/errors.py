

class TokenError(Exception):
    """Raised when the token is invalid or not found in memory."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

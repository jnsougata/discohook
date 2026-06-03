from typing import Optional


# noinspection PyShadowingBuiltins
class PartialEmoji:
    """
    Represents a discord PartialEmoji object.

    Args:
        name (str | None): Name of the emoji.
        id (str | None): ID of the emoji.
        animated (bool | None): Whether the emoji is animated.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,
        animated: Optional[bool] = None
    ):
        self.name = name
        self.id = id
        self.animated = animated

    @classmethod
    def from_str(cls, value: str) -> "PartialEmoji":
        """
        Creates a partial emoji from a string formatted emoji.

        Args:
            value (str): Emoji string.

        Returns:
            PartialEmoji: PartialEmoji object.
        """
        animated, name, id = value.strip("<>").split(":")
        return cls(name=name, id=id, animated=bool(animated))

    def to_dict(self) -> dict:
        data = {"name": self.name}
        if self.id:
            data["id"] = self.id
        if self.animated:
            data["animated"] = self.animated
        return data

from typing import Optional


# noinspection PyShadowingBuiltins
class PartialEmoji:
    """
    Represents a discord PartialEmoji object.

    Parameters
    ----------
    name: :class:`str`
        The name of the emoji.
    id: :class:`str`
        The unique id of the emoji.
    animated: :class:`bool`
        Whether the emoji is animated.
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

        Parameters
        ----------
        value: :class:`str`
            The string formatted emoji.
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

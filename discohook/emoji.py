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

    def __init__(self, *, name: Optional[str] = None, id: Optional[str] = None, animated: Optional[bool] = None):
        self.name = name
        self.id = id
        self.animated = animated

    @classmethod
    def from_str(cls, value: str):
        values = value.strip('<>').split(':')
        return cls(name=values[1], id=values[2], animated=bool(values[0]))

    def to_dict(self) -> dict:
        data = {"name": self.name}
        if self.id:
            data["id"] = self.id
        if self.animated:
            data["animated"] = self.animated
        return data

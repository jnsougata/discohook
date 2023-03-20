from typing import Optional


class PartialEmoji:
    """
    Represents a discord PartialEmoji object.

    Parameters
    ----------
    name: :class:`str`
        The name of the emoji.
    id: :class:`int`
        The ID of the emoji.
    animated: Optional[:class:`bool`]
        Whether the emoji is animated.
    """
    def __init__(self, name: str, id: int, animated: Optional[bool] = False):  # noqa
        self.name = name
        self.id = id
        self.animated = animated

    def to_dict(self):
        """
        Returns a dict representation of the PartialEmoji object.

        This is used internally by the library. You will rarely need to use it.

        Returns
        -------
        """
        return {"name": self.name, "id": self.id, "animated": self.animated}

from typing import Any, Dict, Optional


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
    def __init__(self, name: str, id: Optional[str] = None, animated: bool = False):  # noqa
        self.id = id
        self.name = name
        self.animated = animated

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dict representation of the PartialEmoji object.

        This is used internally by the library. You will rarely need to use it.

        Returns
        -------
        :class:`dict`
        """
        return {"name": self.name, "id": self.id, "animated": self.animated}

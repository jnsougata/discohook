from typing_extensions import TypedDict, NotRequired


class PartialEmoji(TypedDict):
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
    id: NotRequired[str]
    name: str
    animated: NotRequired[bool]

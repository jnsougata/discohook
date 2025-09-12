from typing import List, Union

from .components import Label, TextDisplay
from .handler import Handler


class Modal:
    """
    A modal for discord.

    Parameters
    ----------
    title: :class:`str`
        The title of the modal.
    handler: Handler
        The handler to control the modal submission.
    """

    def __init__(
        self,
        title: str,
        *,
        handler: Handler,
    ):
        self.handler = handler
        self.title = title
        self.components: List[Union[Label, TextDisplay]] = []

    def append(self, *components: Union[Label, TextDisplay]):
        self.components.extend(components)

    def to_dict(self):
        """
        Convert the modal to a dict to be sent to discord. For internal use only.
        """
        return {
            "title": self.title,
            "custom_id": self.handler.id,
            "components": [label.to_dict() for label in self.components],
        }

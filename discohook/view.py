from typing import Any, Dict, List, Union

from .button import Button
from .enums import ComponentType
from .select import Select


class View:
    """
    Represents a discord message component tree.

    This is used to create actions rows and add buttons and select menus to them without having tree conflicts.

    Attributes
    ----------
    components: List[:class:`dict`]
        The list of components to be sent to discord. Do not modify this directly.
    children: List[Union[:class:`Button`, :class:`Select`]]
        The list of children to be sent to discord. Do not modify this directly.
    """

    def __init__(self):
        self.components: List[Dict[str, Any]] = []
        self.children: List[Union[Button, Select]] = []

    def add_buttons(self, *buttons: Union[Button, Any]):
        """
        Adds a row of buttons to the view.
        Each row can only contain up to 5 buttons.
        Action rows having buttons can not have select menus.

        Parameters
        ----------
        *buttons: :class:`Button`
            The buttons to be added to the view.
        """
        batches = [buttons[i : i + 5] for i in range(0, len(buttons), 5)]
        for batch in batches:
            self.components.append(
                {
                    "type": ComponentType.action_row,
                    "components": [btn.to_dict() for btn in batch],
                }
            )
            self.children.extend(batch)

    # noinspection PyShadowingNames
    def add_select(self, select: Union[Select, Any]):
        """
        Adds a row of select to the view.
        Each row can only contain up to 1 select menu.
        Action rows having select menu can not have buttons.

        Parameters
        ----------
        select: :class:`Select`
            The select menu to be added to the view.
        """
        self.components.append(
            {
                "type": ComponentType.action_row,
                "components": [select.to_dict()],
            }
        )
        self.children.append(select)

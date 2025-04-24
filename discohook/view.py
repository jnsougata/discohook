from typing import Any, Dict, List, Optional, Union

import aiohttp

from .button import Button
from .components import *
from .enums import ComponentType, InteractionCallbackType
from .file import File
from .select import Select


# noinspection PyShadowingBuiltins
class View:
    """
    Represents a discord message component.
    """

    def __init__(self):
        self.children: List[
            Union[ActionRow, Section, Container, Separator, FileAttachment]
        ] = []
        self.attachments: List[FileAttachment] = []

    def file(
        self,
        file: Optional[File] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        spoiler: bool = False,
        id: Optional[int] = None,
    ):
        """
        Appends a FileAttachment to the view.

        Parameters
        ----------
        file: Optional[:class:`File`]
            The file to be attached. This is used to identify the file when it is submitted.
        url: Optional[:class:`str`]
            The url of the file.
        description: Optional[:class:`str`]
            The description of the file.
        spoiler: bool
            Whether the file is a spoiler.
        id: Optional[:class:`int`]
            The id of the file. This is used to identify the file when it is submitted.
        """
        assert file or url, "Either file or url must be provided."
        assert not (file and url), "Either file or url must be provided, not both."
        if file:
            attachment = FileAttachment.from_file(file, id=id)
            self.attachments.append(attachment)
        else:
            attachment = FileAttachment.from_url(
                url, description=description, spoiler=spoiler, id=id
            )
        self.children.append(attachment)

    def separator(self, id: Optional[int] = None, spacing: int = 1):
        """
        Appends a Separator to the view.
        """
        self.children.append(Separator(id=id, spacing=spacing))

    def row(self, *components: Union[Button, Select], id: Optional[int] = None):
        """
        Appends an ActionRow to the view.

        Parameters
        ----------
        components: :class:`Button` or :class:`Select`
            The components to be added to the row.
        id: Optional[:class:`str`]
            The id of the row. This is used to identify the row when it is submitted.
        """
        self.children.append(ActionRow(*components, id=id))

    def section(
        self,
        *components: TextDisplay,
        accessory: Optional[Union[Button, Thumbnail]] = None,
        id: Optional[int] = None
    ):
        """
        Appends a Section to the view.

        Parameters
        ----------
        components: :class:`Button` or :class:`Select`
            The components to be added to the section.
        accessory: Optional[Union[:class:`Button`, :class:`Thumbnail`]]
            The accessory to be added to the section. This can be a button or a thumbnail.
        id: Optional[:class:`str`]
            The id of the section. This is used to identify the section when it is submitted.
        """
        self.children.append(Section(*components, accessory=accessory, id=id))

    def container(
        self,
        *components: Union[ActionRow, TextDisplay, Section, MediaGallery, Separator],
        accent_color: Optional[int] = None,
        id: Optional[int] = None
    ):
        """
        Appends a Container to the view.

        Parameters
        ----------
        components: :class:`Button` or :class:`Select`
            The components to be added to the container.
        accent_color: Optional[:class:`int`]
            The accent color of the container. This is used to identify the container when it is submitted.
        id: Optional[:class:`str`]
            The id of the container. This is used to identify the container when it is submitted.
        """
        self.children.append(Container(*components, accent_color=accent_color, id=id))


class LegacyView:
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

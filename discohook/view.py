from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

if TYPE_CHECKING:
    from .common import Component

from .button import Button
from .components import *
from .enums import ComponentType
from .file import File
from .select import Select


# noinspection PyShadowingBuiltins
class View:
    """
    Represents a discord message component.
    """

    def __init__(self):
        self.children: List[
            Union[ActionRow, Section, Container, Separator, File, MediaGallery]
        ] = []
        self.attachments: List[File] = []
        self.interactables: Dict[str, "Component"] = {}

    def add_gallery(self, *media: Media, id: Optional[int] = None):
        """
        Appends a MediaGallery to the view.

        Parameters
        ----------
        media: :class:`Media`
            The media to be added to the gallery.
        id: Optional[:class:`int`]
        """
        self.children.append(MediaGallery(*media, id=id))
        return self

    def add_file(self, *file: File):
        """
        Appends a FileAttachment to the view.

        Parameters
        ----------
        *file: :class:`File`
            The file to be attached. This is used to identify the file when it is submitted.
        """
        for f in file:
            if f.content:
                self.attachments.append(f)
        self.children.extend(file)
        return self

    def add_separator(self, id: Optional[int] = None, spacing: int = 1):
        """
        Appends a Separator to the view.
        """
        self.children.append(Separator(id=id, spacing=spacing))
        return self

    def add_row(self, *components: Union[Button, Select], id: Optional[int] = None):
        """
        Appends an ActionRow to the view.

        Parameters
        ----------
        components: :class:`Button` or :class:`Select`
            The components to be added to the row.
        id: Optional[:class:`str`]
            The id of the row. This is used to identify the row when it is submitted.
        """
        for component in components:
            self.interactables[component.custom_id] = component
        self.children.append(ActionRow(*components, id=id))
        return self

    def add_section(
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
        if isinstance(components, Button):
            self.interactables[components.custom_id] = components
        self.children.append(Section(*components, accessory=accessory, id=id))

    def add_container(
        self,
        *components: Union[
            ActionRow, TextDisplay, Section, MediaGallery, Separator, File
        ],
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
        for component in components:
            if isinstance(component, Button) or isinstance(component, Select):
                self.interactables[component.custom_id] = component
        container = Container(*components, accent_color=accent_color, id=id)
        self.attachments.extend(container.attachments)
        self.children.append(container)
        return self


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

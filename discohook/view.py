from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

if TYPE_CHECKING:
    from .common import Component

from .button import Button
from .components import *
from .file import File
from .select import Select


# noinspection PyShadowingBuiltins
class View:
    """
    Represents a discord message component.
    """

    def __init__(self):
        self.children: List[
            Union[
                TextDisplay,
                ActionRow,
                Section,
                Container,
                Separator,
                File,
                MediaGallery,
            ]
        ] = []
        self.attachments: List[File] = []
        self.interactables: Dict[str, "Component"] = {}

    @classmethod
    def from_children(
        cls,
        *children: Union[
            TextDisplay, ActionRow, Section, Container, Separator, File, MediaGallery
        ]
    ):
        self = cls()
        for child in children:
            if isinstance(child, ActionRow):
                self.add_row(*child.components, id=child.id)
            elif isinstance(child, Section):
                self.add_section(
                    *child.components, accessory=child.accessory, id=child.id
                )
            elif isinstance(child, Container):
                self.add_container(
                    *child.components, accent_color=child.accent_color, id=child.id
                )
            elif isinstance(child, Separator):
                self.add_separator(id=child.id, spacing=child.spacing)
            elif isinstance(child, File):
                self.add_file(child)
            elif isinstance(child, MediaGallery):
                self.add_gallery(*child.items, id=child.id)
            else:
                self.children.append(child)
        return self

    def add_gallery(self, *media: Media, id: Optional[int] = None):
        """
        Appends a MediaGallery to the view.

        Parameters
        ----------
        media: :class:`Media`
            The media to be added to the gallery.
        id: Optional[:class:`int`]
        """
        gallery = MediaGallery(*media, id=id)
        self.attachments.extend(gallery.attachments)
        self.children.append(gallery)
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
            if component.handler:
                self.interactables[component.handler.id] = component  # noqa
        self.children.append(ActionRow(*components, id=id))
        return self

    def add_section(
        self,
        *components: TextDisplay,
        accessory: Union[Button, Thumbnail],
        id: Optional[int] = None
    ):
        """
        Appends a Section to the view.

        Parameters
        ----------
        *components: Tuple[TextDisplay]
            The components to be added to the section.
        accessory: Union[:class:`Button`, :class:`Thumbnail`]
            The accessory to be added to the section. This can be a button or a thumbnail.
        id: Optional[:class:`str`]
            The id of the section. This is used to identify the section when it is submitted.
        """
        if isinstance(accessory, Button):
            self.interactables[accessory.handler.id] = accessory  # noqa
        if isinstance(accessory, Thumbnail):
            self.attachments.append(accessory.attachment)
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
        components: Tuple[ActionRow | TextDisplay | Section | MediaGallery | Separator | File]
            The components to be added to the container.
        accent_color: Optional[:class:`int`]
            The accent color of the container. This is used to identify the container when it is submitted.
        id: str | None
            The id of the container. This is used to identify the container when it is submitted.
        """
        for component in components:
            if isinstance(component, Button) or isinstance(component, Select):
                self.interactables[component.handler.id] = component  # noqa
        container = Container(*components, accent_color=accent_color, id=id)
        self.attachments.extend(container.attachments)
        self.children.append(container)
        return self

from typing import List, Optional, Union

from .components import (Checkbox, CheckboxGroup, CheckboxGroupOption,
                         FileUpload, Label, RadioGroup, RadioGroupOption,
                         TextDisplay, TextInput)
from .enums import ChannelType, SelectType, TextInputFieldLength
from .handler import Handler
from .select import Select, SelectDefaultValue, SelectOption


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
        self.components: List[Union[Label, TextDisplay, FileUpload]] = []

    # noinspection PyShadowingBuiltins
    def display(self, markdown: str, *, id: Optional[int] = None):
        """
        Appends a text display component to the modal.

        Parameters
        ----
        """
        self.components.append(TextDisplay(markdown=markdown, id=id))

    # noinspection PyShadowingBuiltins
    def input(
        self,
        *,
        custom_id: str,
        label: str,
        description: Optional[str] = None,
        id: Optional[int] = None,
        required: bool = True,
        placeholder: Optional[str] = None,
        value: Optional[str] = None,
        min_length: int = 0,
        max_length: int = 4000,
        style: TextInputFieldLength = TextInputFieldLength.short,
    ):
        """
        Appends a text input component to the modal.
        """
        self.components.append(
            Label(
                label=label,
                child=TextInput(
                    custom_id=custom_id,
                    required=required,
                    placeholder=placeholder,
                    value=value,
                    min_length=min_length,
                    max_length=max_length,
                    style=style,
                ),
                id=id,
                description=description,
            )
        )

    # noinspection PyShadowingBuiltins
    def select_menu(
        self,
        *,
        custom_id: str,
        label: str,
        type: SelectType,
        description: Optional[str] = None,
        id: Optional[int] = None,
        placeholder: Optional[str] = None,
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        options: Optional[List[SelectOption]] = None,
        channel_types: Optional[List[ChannelType]] = None,
        default_values: Optional[List[SelectDefaultValue]] = None,
    ):
        """
        Appends a select menu component to the modal.
        """

        async def dummy(): ...

        handler = Handler(id=custom_id, callback=dummy)  # noqa
        select = Select(
            type=type,
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            handler=handler,
        )
        select.options = options
        select.channel_types = channel_types
        select.default_values = default_values
        self.components.append(
            Label(label=label, child=select, id=id, description=description)
        )

    def file_upload(
        self,
        *,
        label: str,
        custom_id: str,
        id: Optional[int] = None,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
    ):
        """
        Appends a file upload component to the modal.
        """

        self.components.append(
            Label(
                label=label,
                child=FileUpload(
                    custom_id=custom_id,
                    min_values=min_values,
                    max_values=max_values,
                    required=required,
                ),
                id=id,
            )
        )

    # noinspection PyShadowingBuiltins
    def checkbox(
        self,
        *,
        custom_id: str,
        label: str,
        id: Optional[int] = None,
        default: bool = False,
    ):
        """
        Appends a checkbox component to the modal.
        """
        self.components.append(
            Label(
                label=label, child=Checkbox(custom_id=custom_id, default=default), id=id
            )
        )

    def checkbox_group(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        label: str,
        options: List[CheckboxGroupOption],
        min_values: Optional[int] = None,
        max_values: Optional[int] = None,
        required: bool = True,
    ):
        """
        Appends a checkbox group component to the modal.
        """
        if len(options) < 1:
            raise ValueError("Checkbox group must have at least one option.")
        self.components.append(
            Label(
                label=label,
                child=CheckboxGroup(
                    custom_id=custom_id,
                    options=options,
                    min_values=min_values,
                    max_values=max_values,
                    required=required,
                ),
                id=id,
            )
        )

    def radio_group(
        self,
        *,
        id: Optional[int] = None,
        custom_id: str,
        label: str,
        options: List[RadioGroupOption],
        required: bool = True,
    ):
        """
        Appends a radio group component to the modal.
        """
        if len(options) < 2:
            raise ValueError("Radio group must have at least two options.")
        self.components.append(
            Label(
                label=label,
                child=RadioGroup(
                    custom_id=custom_id, options=options, required=required
                ),
                id=id,
            )
        )

    def to_dict(self):
        """
        Convert the modal to a dict to be sent to discord. For internal use only.
        """
        return {
            "title": self.title,
            "custom_id": self.handler.id,
            "components": [label.to_dict() for label in self.components],
        }

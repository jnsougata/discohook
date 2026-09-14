---
title: discohook.components
---

# `discohook.components`

## Classes

- [ActionRow](#class-actionrow)
- [Checkbox](#class-checkbox)
- [CheckboxGroup](#class-checkboxgroup)
- [CheckboxGroupOption](#class-checkboxgroupoption)
- [Container](#class-container)
- [FileUpload](#class-fileupload)
- [Label](#class-label)
- [Media](#class-media)
- [MediaGallery](#class-mediagallery)
- [RadioGroup](#class-radiogroup)
- [RadioGroupOption](#class-radiogroupoption)
- [Section](#class-section)
- [Separator](#class-separator)
- [TextDisplay](#class-textdisplay)
- [TextInput](#class-textinput)
- [Thumbnail](#class-thumbnail)

<a id="class-actionrow"></a>
## ActionRow

`discohook.components.ActionRow`

Action row component.
#### _Arguments_

- _**components** (`Tuple[Button | Select]`): Components to include in the action row. Must be between 1 and 5 components._
- _**id** (`int | None`): Unique id for the action row._
#### _Attributes_

- _**id** (`int`): Action row id._
- _**type** (`ComponentType`): Action row type._
- _**components** (`List[Component]`): Action row components._


<a id="class-checkbox"></a>
## Checkbox

`discohook.components.Checkbox`

Represents a checkbox component in a modal.
#### _Arguments_

- _**custom_id** (`str`): A unique id of the checkbox field. Must be a valid python identifier._
- _**id** (`int | None`): A unique id of the checkbox field. Must be a valid python identifier._
- _**default** (`bool`): Whether this checkbox is checked by default (defaults to false)._


<a id="class-checkboxgroup"></a>
## CheckboxGroup

`discohook.components.CheckboxGroup`

Represents a group of checkboxes in a modal.
#### _Arguments_

- _**custom_id** (`str`): A unique id of the checkbox group. Must be a valid python identifier._
- _**options** (`List[CheckboxGroupOption]`): A list of checkbox options in the group._
- _**min_values** (`int | None`): Minimum number of checkboxes that must be checked (defaults to None)._
- _**max_values** (`int | None`): Maximum number of checkboxes that can be checked (defaults to None)._
- _**required** (`bool`): Whether this component is required to be filled (defaults to true)._


<a id="class-checkboxgroupoption"></a>
## CheckboxGroupOption

`discohook.components.CheckboxGroupOption`

Represents an option in a checkbox group.
#### _Arguments_

- _**label** (`str`): The label of the checkbox option._
- _**value** (`str`): The value of the checkbox option._
- _**description** (`str | None`): The description of the checkbox option._
- _**default** (`bool`): Whether this checkbox option is checked by default (defaults to false)._


<a id="class-container"></a>
## Container

`discohook.components.Container`

Container component.
#### _Arguments_

*components (Tuple[ActionRow | TextDisplay | Section | MediaGallery | Separator | File]): Components to include in the container. Must be between 1 and 10 components.
- _**accent_color** (`int | None`): Optional accent color for the container._
- _**id** (`int | None`): Unique id for the container._
#### _Attributes_

- _**attachments** (`List[File]`): List of attachments in the container._


<a id="class-fileupload"></a>
## FileUpload

`discohook.components.FileUpload`

Represents a file upload component in a modal.
#### _Arguments_

- _**id** (`int`): A unique id of the file upload field. Must be a valid python identifier._
- _**min_values** (`int`): Minimum number of items that must be uploaded (defaults to 1)_
- _**max_values** (`int`): Maximum number of items that must be uploaded (defaults to 1)_
- _**required** (`bool`): Whether this component is required to be filled (defaults to true)._


<a id="class-label"></a>
## Label

`discohook.components.Label`

Represents a label component in a modal.
#### _Arguments_

- _**label** (`str`): The text of the label._
- _**child** (`Select | TextInput | FileUpload | Checkbox | CheckboxGroup | RadioGroup`): Child component for the label._
- _**id** (`int | None`): Optional unique id of the label._
- _**description** (`str | None`): The description of the label._


<a id="class-media"></a>
## Media

`discohook.components.Media`

Media component.
#### _Arguments_

- _**media** (`str | File`): Media to include in the media component._
- _**description** (`str | None`): Media description._
- _**spoiler** (`bool`): Whether the media should be spoiler or not._


<a id="class-mediagallery"></a>
## MediaGallery

`discohook.components.MediaGallery`

Media gallery component.
#### _Arguments_

*media (Media): Media items to include in the gallery.
- _**id** (`int | None`): Unique id for the media gallery._
#### _Attributes_

- _**id** (`int`): Media gallery id._
- _**type** (`ComponentType`): Media gallery type._
- _**items** (`Tuple[Media]`): Media items in the gallery._
- _**attachments** (`List[File]`): Attachments for the media items._


<a id="class-radiogroup"></a>
## RadioGroup

`discohook.components.RadioGroup`

Represents a group of radio buttons in a modal.
#### _Arguments_

- _**custom_id** (`str`): A unique id of the radio group. Must be a valid python identifier._
- _**options** (`List[RadioGroupOption]`): A list of radio options in the group._
- _**required** (`bool`): Whether this component is required to be filled (defaults to true)._


<a id="class-radiogroupoption"></a>
## RadioGroupOption

`discohook.components.RadioGroupOption`

Represents an option in a radio group.
#### _Arguments_

- _**label** (`str`): Label of the radio option._
- _**value** (`str`): Value of the radio option._
- _**description** (`str | None`): Description of the radio option._
- _**default** (`bool`): Whether this radio option is selected by default (defaults to false)._


<a id="class-section"></a>
## Section

`discohook.components.Section`

Section component.
#### _Arguments_

*components (Tuple[TextDisplay]): Text display components to include in the section.
- _**accessory** (`Button | Thumbnail`): Accessory component for the section._
- _**id** (`int | None`): Unique id for the section._
#### _Attributes_

- _**attachment** (`File | None`): Attachment for the accessory if it is a File._


<a id="class-separator"></a>
## Separator

`discohook.components.Separator`

Separator component.
#### _Arguments_

- _**id** (`int | None`): Optional separator id._
- _**spacing** (`int`): The spacing of the separator. Must be either 1 or 2._
#### _Raises_

- **AssertionError**: If spacing is not 1 or 2.


<a id="class-textdisplay"></a>
## TextDisplay

`discohook.components.TextDisplay`

Text display component.
#### _Arguments_

- _**markdown** (`str`): Markdown content to display._
- _**id** (`int | None`): Unique id for the text display._
#### _Attributes_

- _**id** (`int | None`): Optional text display id._
- _**type** (`ComponentType`): Text display type._
- _**content** (`str`): Markdown content to display._


<a id="class-textinput"></a>
## TextInput

`discohook.components.TextInput`

Represents a text input field in a modal.
#### _Arguments_

- _**custom_id** (`str`): Custom id of the text input field. Must be a valid python identifier._
- _**id** (`int | None`): Optional unique id of the text input field._
- _**required** (`bool`): Whether this component is required to be filled (defaults to true)._
- _**placeholder** (`str | None`): Custom placeholder text if the input is empty; max 100 characters._
- _**value** (`str | None`): Pre-filled value for this component; max 4000 characters._
- _**min_length** (`int`): Minimum length of the text input field._
- _**max_length** (`int`): Maximum length of the text input field._
- _**style** (`TextInputFieldLength`): The style of the text input field._


<a id="class-thumbnail"></a>
## Thumbnail

`discohook.components.Thumbnail`

Thumbnail component.
#### _Arguments_

- _**media** (`str | File`): Media to include in the thumbnail._
- _**description** (`str | None`): Thumbnail description._
- _**spoiler** (`bool`): Whether the thumbnail should be spoiler or not._
- _**id** (`int | None`): Unique id for the thumbnail._
#### _Attributes_

- _**attachment** (`File | None`): Attachment for the thumbnail if media is a File._


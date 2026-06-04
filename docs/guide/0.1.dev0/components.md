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


<a id="class-checkboxgroup"></a>
## CheckboxGroup

`discohook.components.CheckboxGroup`


<a id="class-checkboxgroupoption"></a>
## CheckboxGroupOption

`discohook.components.CheckboxGroupOption`


<a id="class-container"></a>
## Container

`discohook.components.Container`


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


<a id="class-radiogroup"></a>
## RadioGroup

`discohook.components.RadioGroup`


<a id="class-radiogroupoption"></a>
## RadioGroupOption

`discohook.components.RadioGroupOption`


<a id="class-section"></a>
## Section

`discohook.components.Section`


<a id="class-separator"></a>
## Separator

`discohook.components.Separator`


<a id="class-textdisplay"></a>
## TextDisplay

`discohook.components.TextDisplay`


<a id="class-textinput"></a>
## TextInput

`discohook.components.TextInput`

Represents a text input field in a modal.
#### _Arguments_

- _**custom_id** (`str`): The label of the text input field. Must be a valid python identifier._
- _**id** (`int | None`): A unique id of the text input field. Must be a valid python identifier._
- _**required** (`bool`): Whether this component is required to be filled (defaults to true)._
- _**placeholder** (`str | None`): Custom placeholder text if the input is empty; max 100 characters._
- _**value** (`str | None`): Pre-filled value for this component; max 4000 characters._
- _**min_length** (`int`): The minimum length of the text input field._
- _**max_length** (`int`): The maximum length of the text input field._
- _**style** (`TextInputFieldLength`): The style of the text input field._


<a id="class-thumbnail"></a>
## Thumbnail

`discohook.components.Thumbnail`


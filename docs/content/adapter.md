---
title: discohook.adapter
---

# `discohook.adapter`

## Classes

- [FollowupResponse](#class-followupresponse)
- [InteractionResponse](#class-interactionresponse)
- [ResponseAdapter](#class-responseadapter)

<a id="class-followupresponse"></a>
## Class `FollowupResponse`

**Qualified Name:** `discohook.adapter.FollowupResponse`

Represents a followup message sent by an interaction.

### Method Index

- [delete](#followupresponse-delete)
- [edit](#followupresponse-edit)

### Methods

<a id="followupresponse-delete"></a>
#### `delete`

```python
async delete(self)
```

Deletes the followup message.

<a id="followupresponse-edit"></a>
#### `edit`

```python
async edit(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Edits the followup response message.

### Arguments

- **components** (`Tuple[TopLevelComponent]`): Components to use in the edited response.

### Returns

- **Type:** `Message`
  - Edited response message.


<a id="class-interactionresponse"></a>
## Class `InteractionResponse`

**Qualified Name:** `discohook.adapter.InteractionResponse`

Represents a response message sent by an interaction

### Method Index

- [delete](#interactionresponse-delete)
- [edit](#interactionresponse-edit)

### Methods

<a id="interactionresponse-delete"></a>
#### `delete`

```python
async delete(self)
```

Deletes the response message.

<a id="interactionresponse-edit"></a>
#### `edit`

```python
async edit(self, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container)
```

Edits an interaction response.

### Arguments

- **components**: Components to use in the edited response.

### Returns

- **Type:** `Message`
  - Edited response message.


<a id="class-responseadapter"></a>
## Class `ResponseAdapter`

**Qualified Name:** `discohook.adapter.ResponseAdapter`

Interface for sending responses to interactions

### Method Index

- [autocomplete](#responseadapter-autocomplete)
- [defer](#responseadapter-defer)
- [edit_origin](#responseadapter-edit-origin)
- [followup](#responseadapter-followup)
- [require_premium](#responseadapter-require-premium)
- [send](#responseadapter-send)
- [send_modal](#responseadapter-send-modal)

### Methods

<a id="responseadapter-autocomplete"></a>
#### `autocomplete`

```python
async autocomplete(self, choices: List[discohook.option.Choice], with_response: bool = False)
```

Sends autocomplete choices to the interaction (max 25)

### Arguments

- **choices** (`List[Choice]`): Choices to send with autocomplete response.
- **with_response** (`bool`): Whether to get a response message or not.

### Raises

- **InteractionTypeMismatch**: If the method is not supported for the current interaction type.

<a id="responseadapter-defer"></a>
#### `defer`

```python
async defer(self, ephemeral: bool = False, thinking: bool = False, with_response: bool = False) -> discohook.adapter.InteractionResponse
```

Defers the interaction.

### Arguments

- **ephemeral** (`bool`): Whether the successive responses should be ephemeral or not (only for Application Commands or `thinking` is `True`)
- **thinking** (`bool`): Whether to send a new "is thinking..." message to be edited later (DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE) or do nothing to edit the original message later (DEFERRED_UPDATE_MESSAGE). Not available for application commands.
- **with_response** (`bool`): Whether to get a response message or not.

### Returns

- **Type:** `InteractionResponse`
  - Interaction response object for further actions.

<a id="responseadapter-edit-origin"></a>
#### `edit_origin`

```python
async edit_origin(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, with_response: bool = False) -> discohook.adapter.InteractionResponse
```

Edits the original message of the interaction.
Only available for buttons, select menus, and modal submission interactions.

### Arguments

- **with_response** (`bool`): Whether to get a response message or not.

### Returns

- **Type:** `InteractionResponse`
  - Interaction response object for further actions.

<a id="responseadapter-followup"></a>
#### `followup`

```python
async followup(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery) -> discohook.adapter.FollowupResponse
```

Sends a followup message to the interaction.

### Arguments


### Returns

- **Type:** `FollowupResponse`
  - Followup response object for further actions.

<a id="responseadapter-require-premium"></a>
#### `require_premium`

```python
async require_premium(self, with_response: bool = False)
```

Prompts the user that a premium purchase is required for this interaction.
This method is only available for applications with a premium SKU set up.

<a id="responseadapter-send"></a>
#### `send`

```python
async send(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, with_response: bool = False, ephemeral: bool = False)
```

Sends a response to the interaction

### Arguments

- **components**: Components to use in the response.
- **with_response** (`bool`): Whether to get a response message or not.
- **ephemeral** (`bool`): Whether the response should be ephemeral or not (only for application commands).

### Returns

- **Type:** `InteractionResponse`
  - Interaction response object for further actions.

<a id="responseadapter-send-modal"></a>
#### `send_modal`

```python
async send_modal(self, modal: discohook.modal.Modal | Any, with_response: bool = False) -> discohook.adapter.InteractionResponse
```

Sends a modal to the interaction

### Arguments

- **modal** (`Modal`): Modal to send.
- **with_response** (`bool`): Whether to get a response message or not.

### Returns

- **Type:** `InteractionResponse`
  - Interaction response object for further actions.


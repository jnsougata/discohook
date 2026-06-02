---
title: discohook.adapter
---

# `discohook.adapter`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/adapter.py`

## Classes

- [FollowupResponse](#class-followupresponse)
- [InteractionResponse](#class-interactionresponse)
- [ResponseAdapter](#class-responseadapter)

## Class `FollowupResponse`

Represents a followup message sent by an interaction, subclassed from :class:`Message`.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/adapter.py`
- Line: `59`

### Methods

#### `delete`

```python
delete(self)
```

Deletes the followup message.

#### `edit`

```python
edit(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery)
```

Edits the followup response message.

Args:
    components (Tuple[TopLevelComponent]): Components to use in the edited response.

Returns:
    Message: Edited response message.


## Class `InteractionResponse`

Represents a response message sent by an interaction

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/adapter.py`
- Line: `17`

### Methods

#### `delete`

```python
delete(self)
```

Deletes the response message.

#### `edit`

```python
edit(self, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container)
```

Edits an interaction response.

Args:
    components: Components to use in the edited response.

Returns:
    Message: Edited response message.


## Class `ResponseAdapter`

Interface for sending responses to interactions

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/adapter.py`
- Line: `99`

### Methods

#### `autocomplete`

```python
autocomplete(self, choices: List[discohook.option.Choice], with_response: bool = False)
```

Sends autocomplete choices to the interaction (max 25)

Args:
    choices (List[Choice]): Choices to send with autocomplete response.
    with_response (bool): Whether to get a response message or not.

Raises:
    InteractionTypeMismatch: If the method is not supported for the current interaction type.

#### `defer`

```python
defer(self, ephemeral: bool = False, thinking: bool = False, with_response: bool = False) -> discohook.adapter.InteractionResponse
```

Defers the interaction.

Args:
    ephemeral (bool): Whether the successive responses should be ephemeral or not
        (only for Application Commands or `thinking` is `True`)
    thinking (bool): Whether to send a new "is thinking..." message to be edited later
        (DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE) or do nothing to edit the original message later
        (DEFERRED_UPDATE_MESSAGE). Not available for application commands.
    with_response (bool): Whether to get a response message or not.

Returns:
    InteractionResponse: Interaction response object for further actions.

#### `edit_origin`

```python
edit_origin(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, with_response: bool = False) -> discohook.adapter.InteractionResponse
```

Edits the original message of the interaction.
Only available for buttons, select menus, and modal submission interactions.

Args:
    components (Tuple(TopLevelComponent)): Components to include in the response message.
    with_response (bool): Whether to get a response message or not.

Returns:
    InteractionResponse: Interaction response object for further actions.

#### `followup`

```python
followup(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery) -> discohook.adapter.FollowupResponse
```

Sends a followup message to the interaction.

Args:
    components (Tuple(TopLevelComponent)): Components to include in the response message.

Returns:
    FollowupResponse: Followup response object for further actions.

#### `require_premium`

```python
require_premium(self, with_response: bool = False)
```

Prompts the user that a premium purchase is required for this interaction.
This method is only available for applications with a premium SKU set up.

#### `send`

```python
send(self, *components: str | discohook.components.TextDisplay | discohook.components.ActionRow | discohook.components.Section | discohook.components.Container | discohook.components.Separator | discohook.file.File | discohook.components.MediaGallery, with_response: bool = False, ephemeral: bool = False)
```

Sends a response to the interaction

Args:
    components: Components to use in the response.
    with_response (bool): Whether to get a response message or not.
    ephemeral (bool): Whether the response should be ephemeral or not (only for application commands).

Returns:
    InteractionResponse: Interaction response object for further actions.

#### `send_modal`

```python
send_modal(self, modal: discohook.modal.Modal | Any, with_response: bool = False) -> discohook.adapter.InteractionResponse
```

Sends a modal to the interaction

Args:
    modal (Modal): Modal to send.
    with_response (bool):  Whether to get a response message or not.

Returns:
    InteractionResponse: Interaction response object for further actions.


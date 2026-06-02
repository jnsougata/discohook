---
title: discohook.enums
---

# `discohook.enums`

## Classes

- [AllowedMentionsType](#class-allowedmentionstype)
- [ApplicationCommandOptionType](#class-applicationcommandoptiontype)
- [ApplicationCommandType](#class-applicationcommandtype)
- [ApplicationIntegrationType](#class-applicationintegrationtype)
- [ButtonStyle](#class-buttonstyle)
- [ChannelType](#class-channeltype)
- [ComponentType](#class-componenttype)
- [InteractionCallbackType](#class-interactioncallbacktype)
- [InteractionContextType](#class-interactioncontexttype)
- [InteractionType](#class-interactiontype)
- [ModalFieldType](#class-modalfieldtype)
- [PollLayoutType](#class-polllayouttype)
- [SelectDefaultValueType](#class-selectdefaultvaluetype)
- [SelectType](#class-selecttype)
- [TextInputFieldLength](#class-textinputfieldlength)
- [WebhookType](#class-webhooktype)

## Functions

- [try_enum](#try-enum)

<a id="class-allowedmentionstype"></a>
## Class `AllowedMentionsType`

**Qualified Name:** `discohook.enums.AllowedMentionsType`

The type of mentions allowed in a message.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.str`
- `enum.Enum`


<a id="class-applicationcommandoptiontype"></a>
## Class `ApplicationCommandOptionType`

**Qualified Name:** `discohook.enums.ApplicationCommandOptionType`

The type of application command option.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-applicationcommandtype"></a>
## Class `ApplicationCommandType`

**Qualified Name:** `discohook.enums.ApplicationCommandType`

The type of application command.

Attributes
----------
slash: :class:`int`
Used to specify a slash command.
user: :class:`int`
Used to specify a user command.
message: :class:`int`
Used to specify a message command.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-applicationintegrationtype"></a>
## Class `ApplicationIntegrationType`

**Qualified Name:** `discohook.enums.ApplicationIntegrationType`

Installation context(s) where the command is available.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-buttonstyle"></a>
## Class `ButtonStyle`

**Qualified Name:** `discohook.enums.ButtonStyle`

Represents the style of a button.

Attributes
----------
blurple: :class:`int`
Used to specify a blurple button.
grey: :class:`int`
Used to specify a grey button.
green: :class:`int`
Used to specify a green button.
red: :class:`int`
Used to specify a red button.
link: :class:`int`
Used to specify a link type button.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-channeltype"></a>
## Class `ChannelType`

**Qualified Name:** `discohook.enums.ChannelType`

Use to specify discord channel type in application command Option.

Attributes
----------
guild_text: :class:`int`
Used to specify a guild text channel.
dm: :class:`int`
Used to specify a dm channel.
guild_voice: :class:`int`
Used to specify a guild voice channel.
group_dm: :class:`int`
Used to specify a group dm channel.
guild_category: :class:`int`
Used to specify a guild category channel.
guild_announcement: :class:`int`
Used to specify a guild announcement channel.
guild_announcement_thread: :class:`int`
Used to specify a guild announcement thread channel.
public_thread: :class:`int`
Used to specify a guild public thread channel.
private_thread: :class:`int`
Used to specify a guild private thread channel.
guild_stage_voice: :class:`int`
Used to specify a guild stage voice channel.
guild_directory: :class:`int`
Used to specify a guild directory channel.
guild_forum: :class:`int`
Used to specify a guild forum channel.
guild_media: :class:`int`
Used to specify a guild media channel.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-componenttype"></a>
## Class `ComponentType`

**Qualified Name:** `discohook.enums.ComponentType`

The type of message component.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactioncallbacktype"></a>
## Class `InteractionCallbackType`

**Qualified Name:** `discohook.enums.InteractionCallbackType`

The type of interaction callback.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactioncontexttype"></a>
## Class `InteractionContextType`

**Qualified Name:** `discohook.enums.InteractionContextType`

The type of interaction context.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactiontype"></a>
## Class `InteractionType`

**Qualified Name:** `discohook.enums.InteractionType`

The type of interaction received from discord.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-modalfieldtype"></a>
## Class `ModalFieldType`

**Qualified Name:** `discohook.enums.ModalFieldType`

The type of field in a modal.

Used internally by the library. You should not need to use this.

Attributes
----------
text_input: :class:`int`
Used to specify a text input field.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-polllayouttype"></a>
## Class `PollLayoutType`

**Qualified Name:** `discohook.enums.PollLayoutType`

The type of layout for a poll.

Attributes
----------
default: :class:`int`
Used to specify the default layout.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-selectdefaultvaluetype"></a>
## Class `SelectDefaultValueType`

**Qualified Name:** `discohook.enums.SelectDefaultValueType`

The type of default value for a select menu.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.str`
- `enum.Enum`


<a id="class-selecttype"></a>
## Class `SelectType`

**Qualified Name:** `discohook.enums.SelectType`

The type of select menu.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-textinputfieldlength"></a>
## Class `TextInputFieldLength`

**Qualified Name:** `discohook.enums.TextInputFieldLength`

The length of a text input field for a modal.

Attributes
----------
short: :class:`int`
Used to specify a short length text input field (up to 100 characters).
long: :class:`int`
Used to specify a long length text input field (up to 3000 characters).

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-webhooktype"></a>
## Class `WebhookType`

**Qualified Name:** `discohook.enums.WebhookType`

The type of webhook.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="try-enum"></a>
## `try_enum`

**Qualified Name:** `discohook.enums.try_enum`

### Signature

```python
try_enum(enum_class, value)
```


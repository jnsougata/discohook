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

### Attributes

- **roles** (`int`): Used to specify a role mentions allowed in a message.
- **users** (`int`): Used to specify a user mentions allowed in a message.
- **everyone** (`int`): Used to specify everyone mentions allowed in a message.

### Inheritance

- `builtins.str`
- `enum.Enum`


<a id="class-applicationcommandoptiontype"></a>
## Class `ApplicationCommandOptionType`

**Qualified Name:** `discohook.enums.ApplicationCommandOptionType`

Type of application command option.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-applicationcommandtype"></a>
## Class `ApplicationCommandType`

**Qualified Name:** `discohook.enums.ApplicationCommandType`

Type of application command.

### Attributes

- **slash** (`int`): Used to specify a slash command.
- **user** (`int`): Used to specify a user command.
- **message** (`int`): Used to specify a message command.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-applicationintegrationtype"></a>
## Class `ApplicationIntegrationType`

**Qualified Name:** `discohook.enums.ApplicationIntegrationType`

Installation context(s) where the command is available.

### Attributes

- **guild** (`int`): Used to specify a guild context.
- **user** (`int`): Used to specify a user context.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-buttonstyle"></a>
## Class `ButtonStyle`

**Qualified Name:** `discohook.enums.ButtonStyle`

Represents the style of a button.

### Attributes

- **blurple** (`int`): Used to specify a blurple button.
- **gray** (`int`): Used to specify a gray button.
- **green** (`int`): Used to specify a green button.
- **red** (`int`): Used to specify a red button.
- **link** (`int`): Used to specify a link type button.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-channeltype"></a>
## Class `ChannelType`

**Qualified Name:** `discohook.enums.ChannelType`

Use to specify discord channel type in application command Option.

### Attributes

- **guild_text** (`int`): Used to specify a guild text channel.
- **dm** (`int`): Used to specify a dm channel.
- **guild_voice** (`int`): Used to specify a guild voice channel.
- **group_dm** (`int`): Used to specify a group dm channel.
- **guild_category** (`int`): Used to specify a guild category channel.
- **guild_announcement** (`int`): Used to specify a guild announcement channel.
- **guild_announcement_thread** (`int`): Used to specify a guild announcement thread channel.
- **public_thread** (`int`): Used to specify a guild public thread channel.
- **private_thread** (`int`): Used to specify a guild private thread channel.
- **guild_stage_voice** (`int`): Used to specify a guild stage voice channel.
- **guild_directory** (`int`): Used to specify a guild directory channel.
- **guild_forum** (`int`): Used to specify a guild forum channel.
- **guild_media** (`int`): Used to specify a guild media channel.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-componenttype"></a>
## Class `ComponentType`

**Qualified Name:** `discohook.enums.ComponentType`

Type of message component.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactioncallbacktype"></a>
## Class `InteractionCallbackType`

**Qualified Name:** `discohook.enums.InteractionCallbackType`

Type of interaction callback.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactioncontexttype"></a>
## Class `InteractionContextType`

**Qualified Name:** `discohook.enums.InteractionContextType`

Type of interaction context.

### Attributes

- **guild** (`int`): Used to specify a guild context.
- **bot_dm** (`int`): Used to specify a bot dm context.
- **private_channel** (`int`): Used to specify a private channel context.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactiontype"></a>
## Class `InteractionType`

**Qualified Name:** `discohook.enums.InteractionType`

Type of interaction received from discord.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-modalfieldtype"></a>
## Class `ModalFieldType`

**Qualified Name:** `discohook.enums.ModalFieldType`

Type of field in a modal.
Used internally by the library. You should not need to use this.

### Attributes

- **text_input** (`int`): Used to specify a text input field.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-polllayouttype"></a>
## Class `PollLayoutType`

**Qualified Name:** `discohook.enums.PollLayoutType`

Type of layout for a poll.

### Attributes

- **default** (`int`): Used to specify a default layout for a poll.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-selectdefaultvaluetype"></a>
## Class `SelectDefaultValueType`

**Qualified Name:** `discohook.enums.SelectDefaultValueType`

Type of default values for a select menu.

### Attributes

- **user** (`str`): Used to specify a user default value for a select menu.
- **role** (`str`): Used to specify a role default value for a select menu.
- **channel** (`str`): Used to specify a channel default value for a select menu.

### Inheritance

- `builtins.str`
- `enum.Enum`


<a id="class-selecttype"></a>
## Class `SelectType`

**Qualified Name:** `discohook.enums.SelectType`

The type of select menu.

### Attributes

- **text** (`int`): Used to specify a text select menu.
- **user** (`int`): Used to specify a user select menu.
- **role** (`int`): Used to specify a role select menu.
- **mentionable** (`int`): Used to specify a mentionable select menu.
- **channel** (`int`): Used to specify a channel select menu.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-textinputfieldlength"></a>
## Class `TextInputFieldLength`

**Qualified Name:** `discohook.enums.TextInputFieldLength`

Length of a text input field for a modal.

### Attributes

- **short** (`int`): Used to specify a short text input field.
- **long** (`int`): Used to specify a long text input field.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-webhooktype"></a>
## Class `WebhookType`

**Qualified Name:** `discohook.enums.WebhookType`

Type of webhook.
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


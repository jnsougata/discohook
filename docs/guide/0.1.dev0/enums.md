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

<a id="class-allowedmentionstype"></a>
## AllowedMentionsType

`discohook.enums.AllowedMentionsType`

The type of mentions allowed in a message.
#### _Attributes_

- _**roles** (`int`): Used to specify a role mentions allowed in a message._
- _**users** (`int`): Used to specify a user mentions allowed in a message._
- _**everyone** (`int`): Used to specify everyone mentions allowed in a message._

### Inheritance

- `builtins.str`
- `enum.Enum`


<a id="class-applicationcommandoptiontype"></a>
## ApplicationCommandOptionType

`discohook.enums.ApplicationCommandOptionType`

Type of application command option.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-applicationcommandtype"></a>
## ApplicationCommandType

`discohook.enums.ApplicationCommandType`

Type of application command.
#### _Attributes_

- _**slash** (`int`): Used to specify a slash command._
- _**user** (`int`): Used to specify a user command._
- _**message** (`int`): Used to specify a message command._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-applicationintegrationtype"></a>
## ApplicationIntegrationType

`discohook.enums.ApplicationIntegrationType`

Installation context(s) where the command is available.
#### _Attributes_

- _**guild** (`int`): Used to specify a guild context._
- _**user** (`int`): Used to specify a user context._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-buttonstyle"></a>
## ButtonStyle

`discohook.enums.ButtonStyle`

Represents the style of a button.
#### _Attributes_

- _**blurple** (`int`): Used to specify a blurple button._
- _**gray** (`int`): Used to specify a gray button._
- _**green** (`int`): Used to specify a green button._
- _**red** (`int`): Used to specify a red button._
- _**link** (`int`): Used to specify a link type button._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-channeltype"></a>
## ChannelType

`discohook.enums.ChannelType`

Use to specify discord channel type in application command Option.
#### _Attributes_

- _**guild_text** (`int`): Used to specify a guild text channel._
- _**dm** (`int`): Used to specify a dm channel._
- _**guild_voice** (`int`): Used to specify a guild voice channel._
- _**group_dm** (`int`): Used to specify a group dm channel._
- _**guild_category** (`int`): Used to specify a guild category channel._
- _**guild_announcement** (`int`): Used to specify a guild announcement channel._
- _**guild_announcement_thread** (`int`): Used to specify a guild announcement thread channel._
- _**public_thread** (`int`): Used to specify a guild public thread channel._
- _**private_thread** (`int`): Used to specify a guild private thread channel._
- _**guild_stage_voice** (`int`): Used to specify a guild stage voice channel._
- _**guild_directory** (`int`): Used to specify a guild directory channel._
- _**guild_forum** (`int`): Used to specify a guild forum channel._
- _**guild_media** (`int`): Used to specify a guild media channel._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-componenttype"></a>
## ComponentType

`discohook.enums.ComponentType`

Type of message component.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactioncallbacktype"></a>
## InteractionCallbackType

`discohook.enums.InteractionCallbackType`

Type of interaction callback.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactioncontexttype"></a>
## InteractionContextType

`discohook.enums.InteractionContextType`

Type of interaction context.
#### _Attributes_

- _**guild** (`int`): Used to specify a guild context._
- _**bot_dm** (`int`): Used to specify a bot dm context._
- _**private_channel** (`int`): Used to specify a private channel context._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-interactiontype"></a>
## InteractionType

`discohook.enums.InteractionType`

Type of interaction received from discord.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-modalfieldtype"></a>
## ModalFieldType

`discohook.enums.ModalFieldType`

Type of field in a modal.
Used internally by the library. You should not need to use this.
#### _Attributes_

- _**text_input** (`int`): Used to specify a text input field._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-polllayouttype"></a>
## PollLayoutType

`discohook.enums.PollLayoutType`

Type of layout for a poll.
#### _Attributes_

- _**default** (`int`): Used to specify a default layout for a poll._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-selectdefaultvaluetype"></a>
## SelectDefaultValueType

`discohook.enums.SelectDefaultValueType`

Type of default values for a select menu.
#### _Attributes_

- _**user** (`str`): Used to specify a user default value for a select menu._
- _**role** (`str`): Used to specify a role default value for a select menu._
- _**channel** (`str`): Used to specify a channel default value for a select menu._

### Inheritance

- `builtins.str`
- `enum.Enum`


<a id="class-selecttype"></a>
## SelectType

`discohook.enums.SelectType`

The type of select menu.
#### _Attributes_

- _**text** (`int`): Used to specify a text select menu._
- _**user** (`int`): Used to specify a user select menu._
- _**role** (`int`): Used to specify a role select menu._
- _**mentionable** (`int`): Used to specify a mentionable select menu._
- _**channel** (`int`): Used to specify a channel select menu._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-textinputfieldlength"></a>
## TextInputFieldLength

`discohook.enums.TextInputFieldLength`

Length of a text input field for a modal.
#### _Attributes_

- _**short** (`int`): Used to specify a short text input field._
- _**long** (`int`): Used to specify a long text input field._

### Inheritance

- `builtins.int`
- `enum.Enum`


<a id="class-webhooktype"></a>
## WebhookType

`discohook.enums.WebhookType`

Type of webhook.
Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`


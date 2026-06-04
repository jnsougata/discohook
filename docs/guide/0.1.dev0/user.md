---
title: discohook.user
---

# `discohook.user`

## Classes

- [User](#class-user)

<a id="class-user"></a>
## User

`discohook.user.User`

Represents a discord user.
Properties
----------
id: :class:`str`
The unique ID of the user.
name: :class:`str`
The name of the user.
discriminator: :class:`str`
The discriminator of the user.
accent_color: Optional[:class:`int`]
The accent color of the user.
avatar: :class:`Asset`
The avatar of the user.
system: :class:`bool`
Whether the user is a system user.
bot: :class:`bool`
Whether the user is a bot.
mfa_enabled: :class:`bool`
Whether the user has MFA enabled.
locale: Optional[:class:`str`]
The locale of the user.
verified: :class:`bool`
Whether the user is verified.
email: Optional[:class:`str`]
The email of the user.
premium_type: Optional[:class:`int`]
The premium type of the user.
public_flags: Optional[:class:`int`]
The public flags of the user.
mention: :class:`str`
Returns a string that allows you to mention the user.

### Method Index

- [send](#user-send)

### Methods

<a id="user-send"></a>
#### `send`

```python
async send(self, *components: discohook.components.TextDisplay | discohook.components.Section | discohook.file.File | discohook.components.MediaGallery | discohook.components.ActionRow | discohook.components.Separator | discohook.components.Container) -> aiohttp.client_reqrep.ClientResponse
```

Sends a message to the user.
Parameters
----------
*components: Union[TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container]
The components to send in the message.


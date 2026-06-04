---
title: discohook.command
---

# `discohook.command`

## Classes

- [ApplicationCommand](#class-applicationcommand)
- [SubCommand](#class-subcommand)
- [SubCommandGroup](#class-subcommandgroup)

## Functions

- [message](#message)
- [slash](#slash)
- [user](#user)

<a id="class-applicationcommand"></a>
## ApplicationCommand

`discohook.command.ApplicationCommand`

Discord application command class.
#### _Arguments_

- _**name** (`str`): Name of the command._
- _**description** (`str | None`): Description of the command. Does not apply to user and message commands._
- _**options** (`List[Option] | None`): Options of the command. Does not apply to user & message commands._
- _**nsfw** (`bool`): Whether the command is nsfw. Defaults to False._
- _**permissions** (`List[Permission] | None`): Permissions of the command. Defaults to None._
- _**type** (`ApplicationCommandType`): Type of the command. Defaults to slash commands._
- _**integration_types** (`List[ApplicationIntegrationType] | None`): Integrations of the command. Defaults to None._
- _**contexts** (`List[InteractionContextType] | None`): Contexts of the command. Defaults to None._

### Method Index

- [check](#applicationcommand-check)
- [on_autocomplete](#applicationcommand-on-autocomplete)
- [on_error](#applicationcommand-on-error)
- [subcommand](#applicationcommand-subcommand)
- [to_dict](#applicationcommand-to-dict)

### Methods

<a id="applicationcommand-check"></a>
#### `check`

```python
check(self)
```

Decorator that adds a check to the command.

<a id="applicationcommand-on-autocomplete"></a>
#### `on_autocomplete`

```python
on_autocomplete(self, coro: Callable[[ForwardRef('Interaction'), Any], Coroutine[Any, Any, Any]])
```

Decorator to register a callback for the command's autocomplete options.

<a id="applicationcommand-on-error"></a>
#### `on_error`

```python
on_error(self)
```

Decorator that adds an error handler to a specific command or component.

<a id="applicationcommand-subcommand"></a>
#### `subcommand`

```python
subcommand(self, name: str | None = None, *, description: str | None = None, options: List[discohook.option.Option] | None = None)
```

Decorator to register a subcommand for the command.
#### _Arguments_

- _**name** (`str`): Name of the subcommand._
- _**description** (`str`): Description of the subcommand._ If not provided, it will be resolved from the callback's name.
- _**options** (`List[Option] | None`): Options of the subcommand._
#### _Raises_

- **TypeError**: If the callback is not a coroutine.

<a id="applicationcommand-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Converts the command to a dictionary. Not intended for use by end-users.
#### _Returns_

- **Type:** `dict`
  - Dictionary of the command object.


<a id="class-subcommand"></a>
## SubCommand

`discohook.command.SubCommand`

Discord application command subcommand class.
#### _Arguments_

- _**name** (`str`): Name of the subcommand._
- _**description** (`str`): Description of the subcommand._
- _**options** (`List[Option] | None`): Options of the subcommand._
- _**handler** (`Handler`): Handler for the subcommand._

### Method Index

- [check](#subcommand-check)
- [on_autocomplete](#subcommand-on-autocomplete)
- [on_error](#subcommand-on-error)

### Methods

<a id="subcommand-check"></a>
#### `check`

```python
check(self)
```

Decorator that adds a check to the command.

<a id="subcommand-on-autocomplete"></a>
#### `on_autocomplete`

```python
on_autocomplete(self, coro: Callable[[ForwardRef('Interaction'), Any], Coroutine[Any, Any, Any]])
```

Decorator to register a callback for a subcommand's autocomplete options.

<a id="subcommand-on-error"></a>
#### `on_error`

```python
on_error(self)
```

Decorator that adds an error handler to a specific command or component.


<a id="class-subcommandgroup"></a>
## SubCommandGroup

`discohook.command.SubCommandGroup`

Barely need it.


<a id="message"></a>
## `message`

**Qualified Name:** `discohook.command.message`

### Signature

```python
message(name: str | None = None, *, nsfw: bool = False, permissions: List[discohook.permission.Permission] | None = None, guild_id: str | None = None, integration_types: List[discohook.enums.ApplicationIntegrationType] | None = None, contexts: List[discohook.enums.InteractionContextType] | None = None)
```

Decorator to create a message command with its callback.


<a id="slash"></a>
## `slash`

**Qualified Name:** `discohook.command.slash`

### Signature

```python
slash(name: str | None = None, *, description: str | None = None, options: List[discohook.option.Option] | None = None, nsfw: bool = False, permissions: List[discohook.permission.Permission] | None = None, guild_id: str | None = None, integration_types: List[discohook.enums.ApplicationIntegrationType] | None = None, contexts: List[discohook.enums.InteractionContextType] | None = None)
```

Decorator to create a slash command with its callback.


<a id="user"></a>
## `user`

**Qualified Name:** `discohook.command.user`

### Signature

```python
user(name: str | None = None, *, nsfw: bool = False, permissions: List[discohook.permission.Permission] | None = None, guild_id: str | None = None, integration_types: List[discohook.enums.ApplicationIntegrationType] | None = None, contexts: List[discohook.enums.InteractionContextType] | None = None)
```

Decorator to create a user command with its callback.


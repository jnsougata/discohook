---
title: discohook.command
---

# `discohook.command`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`

## Classes

- [ApplicationCommand](#class-applicationcommand)
- [SubCommand](#class-subcommand)
- [SubCommandGroup](#class-subcommandgroup)

## Class `ApplicationCommand`

Discord application command class.

Args:
    name (str): Name of the command.
    description (str | None): Description of the command. Does not apply to user and message commands.
    options (List[Option] | None): Options of the command. Does not apply to user & message commands.
    nsfw (bool): Whether the command is nsfw. Defaults to False.
    permissions (List[Permission] | None): Permissions of the command. Defaults to None.
    type (ApplicationCommandType): Type of the command. Defaults to slash commands.
    integration_types (List[ApplicationIntegrationType] | None): Integrations of the command. Defaults to None.
    contexts (List[InteractionContextType] | None): Contexts of the command. Defaults to None.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`
- Line: `102`

### Methods

#### `check`

```python
check(self)
```

Decorator that adds a check to the command.

#### `on_autocomplete`

```python
on_autocomplete(self, coro: Callable[[ForwardRef('Interaction'), Any], Coroutine[Any, Any, Any]])
```

Decorator to register a callback for the command's autocomplete options.

#### `on_error`

```python
on_error(self)
```

Decorator that adds an error handler to a specific command or component.

#### `subcommand`

```python
subcommand(self, name: str | None = None, *, description: str | None = None, options: List[discohook.option.Option] | None = None)
```

Decorator to register a subcommand for the command.

Args:
    name (str): Name of the subcommand.
    description (str): Description of the subcommand.
        If not provided, it will be resolved from the callback's name.
    options (List[Option] | None): Options of the subcommand.

Raises:
    TypeError: If the callback is not a coroutine.

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Converts the command to a dictionary. Not intended for use by end-users.

Returns:
    Dictionary of the command object.


## Class `SubCommand`

Discord application command subcommand class.

Args:
    name (str): Name of the subcommand.
    description (str): Description of the subcommand.
    options (List[Option] | None): Options of the subcommand.
    handler (Handler): Handler for the subcommand.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`
- Line: `16`

### Methods

#### `check`

```python
check(self)
```

Decorator that adds a check to the command.

#### `on_autocomplete`

```python
on_autocomplete(self, coro: Callable[[ForwardRef('Interaction'), Any], Coroutine[Any, Any, Any]])
```

Decorator to register a callback for a subcommand's autocomplete options.

#### `on_error`

```python
on_error(self)
```

Decorator that adds an error handler to a specific command or component.

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `SubCommandGroup`

Barely need it.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`
- Line: `94`


## Functions

- [message](#message)
- [slash](#slash)
- [user](#user)

## `message`

### Signature

```python
message(name: str | None = None, *, nsfw: bool = False, permissions: List[discohook.permission.Permission] | None = None, guild_id: str | None = None, integration_types: List[discohook.enums.ApplicationIntegrationType] | None = None, contexts: List[discohook.enums.InteractionContextType] | None = None)
```

Decorator to create a message command with its callback.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`
- Line: `312`


## `slash`

### Signature

```python
slash(name: str | None = None, *, description: str | None = None, options: List[discohook.option.Option] | None = None, nsfw: bool = False, permissions: List[discohook.permission.Permission] | None = None, guild_id: str | None = None, integration_types: List[discohook.enums.ApplicationIntegrationType] | None = None, contexts: List[discohook.enums.InteractionContextType] | None = None)
```

Decorator to create a slash command with its callback.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`
- Line: `253`


## `user`

### Signature

```python
user(name: str | None = None, *, nsfw: bool = False, permissions: List[discohook.permission.Permission] | None = None, guild_id: str | None = None, integration_types: List[discohook.enums.ApplicationIntegrationType] | None = None, contexts: List[discohook.enums.InteractionContextType] | None = None)
```

Decorator to create a user command with its callback.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/command.py`
- Line: `284`


# Client

---
It is the core abstraction of discohook built on top of [Starlette](https://starlette.dev/). Unlike gateway-based Discord libraries it represents your Discord application as a web server that:

- Receives and verifies incoming interactions from Discord
- Registers and synchronizes application commands
- Manages HTTP communication with the Discord API
- Provides high-level methods for interacting with Discord resources

## Instantiation
To create a `Client`, simply import it from the `discohook` package and instantiate it:

```python
import discohook

app = discohook.Client.from_env()
```
## Methods
The `Client` class provides a variety of methods for interacting with Discord API.

## _def from_env()_
It is a class method that creates a client instance using environment variables for configuration. It expects the following environment variables to be set:
- `APPLICATION_ID`: Your Discord application's client ID
- `PUBLIC_KEY`: Your Discord application's public key for verifying interactions
- `BOT_TOKEN`: Your Discord bot token for authentication
- `APPLICATION_PASSWORD`: The dashboard password for your application

## _def on_error(self)_
This is a decorator method that allows you to register an error handler for your client. You can use it to define a function that will be called whenever an error occurs during the processing of any server request.

```python
from starlette.requests import Request


@app.on_error()
async def handle_error(request: Request, exc: Exception):
    # Handle the error here
    ...
```

## _def register(self, item)_
This method is used to register a command or event handler with the client. You can pass an instance of a command or event handler to this method, and it will be registered with the client.
```python
@app.register  # Registering a slash command
@discohook.command.slash()
async def ping(interaction: discohook.Interaction):
    ...

@app.register  # Registering a button handler
@discohook.handler("delete_button")
async def handle_delete_button(interaction: discohook.Interaction):
    await interaction.message.delete()
```

## _def commands(self, *commands: ApplicationCommand)_
This method is used to add one or more application commands to the client's command registry. You can pass any number of `ApplicationCommand` instances to this method, and they will be added to the client's command registry.

```python
ping = discohook.ApplicationCommand(
    name="ping",
    description="Responds with Pong!",
    handler_func=...
)

app.commands(ping)
```
> This method is typically used when you want to define your commands separately from their handlers, allowing for more modular code organization.
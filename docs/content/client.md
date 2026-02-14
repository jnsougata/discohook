from starlette.applications import Starlette

# Client

---
`Client` is the core abstraction of discohook built on top of [Starlette](https://starlette.dev/). Unlike gateway-based Discord libraries it represents your Discord application as a web server that:

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
It is a class method that creates a `Client` instance using environment variables for configuration. It expects the following environment variables to be set:
- `APPLICATION_ID`: Your Discord application's client ID
- `PUBLIC_KEY`: Your Discord application's public key for verifying interactions
- `BOT_TOKEN`: Your Discord bot token for authentication
- `APPLICATION_PASSWORD`: The dashboard password for your application

## _def on_error(self)_
This is a decorator method that allows you to register an error handler for your `Client`. You can use it to define a function that will be called whenever an error occurs during the processing of any server request.

```python
from starlette.requests import Request


@app.on_error()
async def handle_error(request: Request, exc: Exception):
    # Handle the error here
    ...
```
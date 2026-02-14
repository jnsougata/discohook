# 🚀 Getting Started

Discohook can be installed using **pip** or from a local source distribution.

---

## 📦 Installation

### Option 1 — Install via pip (Recommended)

```bash
pip install discohook
```
or

```bash
pip install git+https://github.com/jnsougata/discohook.git
```
## ⚙️ Environment Configuration
Create a `.env` file in the root of your project and add the following environment variables:

```env
DISCORD_TOKEN=<your_bot_token_here>
PUBLIC_KEY=<your_public_key_here>
APPLICATION_ID=<your_application_id_here>
APPLICATION_PASSWORD=<your_application_password_here>
```
## ▶️ Basic Usage
Import the library and initialize the client:

```python
import discohook


app = discohook.Client.from_env()  # This will automatically read the environment variables from the .env file and initialize the client.
```
## 🤖Creating a Slash Command
```python
@app.register
@discohook.command.slash()
async def ping(i: discohook.Interaction):
    """
    A simple slash command that responds with "pong!" when invoked.
    """
    await i.response.send(discohook.TextDisplay(
        markdown="pong!"
    ))
```
> The command name is automatically derived from the function name (`ping` in this case), and the command description is taken from the function's docstring if not explicitly provided.


## 🛠️ Error Handling
You can add error handlers for both interaction errors and server-side exceptions.
```python
@app.on_interaction_error()
async def interaction_error_handler(i: discohook.Interaction):
    await app.send("<channel_id>", f"Error: {i.error}")  # send error to a channel in development server.

@app.on_error()
async def server_error_handler(request, error: Exception):
    # (request) is starlette.requests.Request object representing the incoming HTTP request that caused the error.
    # (error) is the error occurred on the server side, which is not related to any interaction.
    await app.send("12345678910", f"Error: {error}")  # send error to a channel in development server.
```
> The `on_interaction_error` handler will catch any exceptions that occur during the processing of an interaction, while the `on_error` handler will catch any server-side exceptions that are not related to interactions. You can customize the error handling logic as needed, such as sending error messages to a specific channel or logging them for debugging purposes.

## 🔄 Running the Bot
Finally, start the bot by running the script:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
```
## ⚠️ Wait! where are you going?
There are few more shenanigans you have to do to make the command work. 
### 1. Setting up the Interaction Endpoint URL
> You need to deploy your bot to a serverless environment (ex: AWS Lambda, Google Cloud Functions, etc.) or any hosting service, and you will get a `public URL` for your bot.

For example if your URL is `https://my-bot-url.com`, then you need to set the **Interaction Endpoint URL** in your Discord Developer Portal to `https://my-bot-url.com/interactions`.

### 2. Syncing Commands
After setting up the endpoint URL, you need to sync your commands with Discord. After you set up the endpoint URL, you can register your commands just by visiting the dashboard at `https://my-bot-url.com/api/dash`.
> It will ask you to enter a password, which is the `APPLICATION_PASSWORD` you set in the environment variable if you are visiting the dashboard for the first time.

### 3. Testing the Command
After syncing the commands, you can test the command in your Discord server. Just type `/ping` in any channel where the bot has access, and you should see the response "pong!".
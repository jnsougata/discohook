import os
import discohook
from component import random_num


DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
APPLICATION_ID = os.environ["APPLICATION_ID"]
APPLICATION_PASSWORD = os.environ["APPLICATION_PASSWORD"]

app = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    token=DISCORD_TOKEN,
    password=APPLICATION_PASSWORD,
    default_help_command=True,  # This will enable your bot to use  default help command (/help).
)

app.load_modules("modules")  # load a command from a module in a directory named modules

app.add_commands(random_num)  # import a command from another file


# adding a error handler
@app.on_interaction_error()
async def on_error(i: discohook.Interaction, err: Exception):
    user_response = "Some error occurred! Please contact the developer."
    if i.responded:
        await i.response.followup(user_response, ephemeral=True)
    else:
        await i.response.send(user_response, ephemeral=True)

    await app.send("12345678910", f"Error: {err}")


@app.load
@discohook.ApplicationCommand.slash()
async def ping(i: discohook.Interaction):
    """Ping the bot."""
    await i.response.send("Pong!")

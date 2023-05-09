import os
import discohook
from button import random_num


TOKEN = os.environ["TOKEN"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
APPLICATION_ID = os.environ["APPLICATION_ID"]

app = discohook.Client(application_id=APPLICATION_ID, public_key=PUBLIC_KEY, token=TOKEN)

app.load_modules("modules.avatar")  # load a command from a file

app.add_commands(random_num)  # import a command from another file


# adding a error handler
@app.on_error
async def on_error(i: discohook.Interaction, err: Exception):
    if i.responded:
        await i.followup(f"```py\nError: {err}\n```", ephemeral=True)
    else:
        await i.response(f"```py\nError: {err}\n```", ephemeral=True)
    # the above is not recommended as it might leak secret tokens
    # you can get a logging channel and push the traceback there


@app.command(name="help", description="sample help command")
async def callback(i: discohook.Interaction):
    embed = discohook.Embed("Help Command")
    embed.add_field("/help", "Shows this message", inline=True)
    embed.add_field("/do", "Does something", inline=True)

    await i.response(embed=embed)

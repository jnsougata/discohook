import os
import random
import traceback

import deta
import discohook


PASSWORD = os.environ["PASSWORD"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
APPLICATION_ID = os.environ["APPLICATION_ID"]
LOG_CHANNEL_ID = os.environ["LOG_CHANNEL_ID"]


app = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    password=PASSWORD,
    token=DISCORD_TOKEN,
    default_help_command=True,
)


@app.preload("delete")
@discohook.button("Delete", style=discohook.ButtonStyle.red)
async def delete_button(i: discohook.Interaction):
    await i.response.defer()
    await i.message.delete()


@app.on_error()
async def debugger(_, err: Exception):
    stack = "\n".join(traceback.format_exception(type(err), err, err.__traceback__))
    embed = discohook.Embed(title="Exception", description=f"```py\n{stack}```")
    view = discohook.View()
    view.add_buttons(delete_button)
    await app.send(LOG_CHANNEL_ID, embed=embed, view=view)


@app.on_interaction_error()
async def interaction_error(i: discohook.Interaction, err: Exception):
    if i.responded:
        await i.response.followup("An error occurred while processing your interaction.", ephemeral=True)
    else:
        await i.response.send("An error occurred while processing your interaction.", ephemeral=True)
    stack = "\n".join(traceback.format_exception(type(err), err, err.__traceback__))
    embed = discohook.Embed(title="Exception", description=f"```py\n{stack}\n```")
    view = discohook.View()
    view.add_buttons(delete_button)
    await app.send(LOG_CHANNEL_ID, embed=embed, view=view)


def make_random_color_card(i: discohook.Interaction) -> discohook.Embed:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    _hex = f"{red:02x}{green:02x}{blue:02x}"
    embed = discohook.Embed(description=f"**`color: #{_hex}`**", color=_hex)
    embed.set_image(f"https://singlecolorimage.com/get/{_hex}/1280x720")
    embed.author(name=i.author.name, icon_url=i.author.avatar.url)
    return embed


@app.preload("regenerate")
@discohook.button("Regenerate")
async def generate_button(i: discohook.Interaction):
    await i.response.update_message(embed=make_random_color_card(i))


@app.command()
async def color(i: discohook.Interaction):
    """Generate a random color."""
    view = discohook.View()
    view.add_buttons(generate_button)
    await i.response.send(embed=make_random_color_card(i), view=view)


@app.command(
    options=[
        discohook.IntegerOption(
            "limit",
            "The number of messages to purge.",
            required=True,
            max_value=100,
            min_value=2
        )
    ],
    dm_access=False,
    permissions=[discohook.Permission.manage_messages],
)
async def purge(i: discohook.Interaction, limit: int):
    """Purge messages from the channel."""
    await i.response.send(f"Purging {limit} messages.", ephemeral=True)
    await i.channel.purge(limit)


@app.user_command()
async def avatar(i: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed()
    embed.set_image(url=user.avatar.url)
    await i.response.send(embed=embed)


@app.message_command(guild_id=os.environ["GUILD_ID"])
async def echo(i: discohook.Interaction, message: discohook.Message):
    if message.content:
        await i.response.send(message.content)
    else:
        await i.response.send("Message does not have text content.", ephemeral=True)


@app.command(
    options=[
        discohook.AttachmentOption("file", "The file to upload.", required=True)
    ]
)
async def upload(i: discohook.Interaction, file: discohook.Attachment):
    """Upload a file to Deta Drive."""
    drive = deta.Deta(env="DETA_PROJECT_KEY").drive("files")
    await i.response.defer()
    await drive.put(await file.read(), save_as=file.filename, content_type=file.content_type)
    await i.response.followup(f"File `{file.filename}` uploaded to drive.")


@app.command(
    options=[
        discohook.StringOption("filename", "The file to download.", autocomplete=True, required=True)
    ]
)
async def download(i: discohook.Interaction, filename: str):
    """Download a file from Deta Drive."""
    drive = deta.Deta(env="DETA_PROJECT_KEY").drive("files")
    await i.response.defer()
    file = await drive.get(filename)
    await i.response.followup(file=discohook.File(filename, content=await file.read()))


@download.autocomplete("filename")
async def download_autocomplete(i: discohook.Interaction, filename: str):
    if not filename:
        return
    drive = deta.Deta(env="DETA_PROJECT_KEY").drive("files")
    files = await drive.files(prefix=filename)
    choices = [discohook.Choice(name=file, value=file) for file in files["names"]]
    await i.response.autocomplete(choices)

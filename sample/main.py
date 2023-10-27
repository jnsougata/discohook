import os
import random
import secrets
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


async def exec_code_and_respond(i: discohook.Interaction, code: str):
    from io import StringIO
    import re
    import sys
    import os

    os.environ.clear()

    await i.response.defer()

    view = discohook.View()
    view.add_buttons(delete_button)

    pattern = re.compile("```(?:python|py)?\n([\s\S]*?)\n```")  # noqa
    code = pattern.search(i.message.content)
    if not code:
        return await i.response.followup("No code to execute.")
    orig = sys.stdout
    sys.stdout = stdout = StringIO()
    try:
        exec(f'async def aexec(): ' + "".join(f"\n {line}" for line in code.group(1).split("\n")))
        await locals()["aexec"]()
        sys.stdout = orig
    except Exception as err:
        await i.response.followup(f"```py\n{err}\n```", view=view)
    else:
        value = stdout.getvalue()
        if len(value) > 2000:
            file = discohook.File("output.txt", content=value.encode("utf-8"))
            return await i.response.followup(file=file, view=view)
        embed = discohook.Embed("Output")
        embed.set_author(name=str(i.author), icon_url=i.author.avatar.url)
        embed.description = f"```\n{value}\n```"
        await i.response.followup(embed=embed, view=view)


@app.preload("delete")
@discohook.button.new("Delete", style=discohook.ButtonStyle.red)
async def delete_button(i: discohook.Interaction):
    await i.response.defer()
    await i.message.delete()


@app.preload("execute_code")
@discohook.button.new("Execute", style=discohook.ButtonStyle.green)
async def exec_button(i: discohook.Interaction):
    await exec_code_and_respond(i, i.message.content)


@discohook.modal.new(
    "Code Runner",
    fields=[
        discohook.TextInput("code", "field", required=True, style=discohook.TextInputFieldLength.long)
    ]
)
async def code_input_modal(i: discohook.Interaction, field: str):
    view = discohook.View()
    view.add_buttons(rewrite_code_button, exec_button, delete_button)
    if i.message:
        await i.response.update_message(content=f"```py\n{field}\n```", view=view)
    else:
        await i.response.send(f"```py\n{field}\n```", view=view)


@app.preload("rewrite_code")
@discohook.button.new("Rewrite")
async def rewrite_code_button(i: discohook.Interaction):
    await i.response.send_modal(code_input_modal)


@app.load
@discohook.command.slash()
async def run(i: discohook.Interaction):
    """Run python code snippets"""
    await i.response.send_modal(code_input_modal)


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
    color_hex = f"{red:02x}{green:02x}{blue:02x}"
    embed = discohook.Embed(description=f"**`color: #{color_hex}`**", color=color_hex)
    embed.set_image(f"https://singlecolorimage.com/get/{color_hex}/1280x720")
    embed.set_author(name=i.author.name, icon_url=i.author.avatar.url)
    return embed


@app.preload("regenerate")
@discohook.button.new("Regenerate")
async def generate_button(i: discohook.Interaction):
    await i.response.update_message(embed=make_random_color_card(i))


@app.load
@discohook.command.slash()
async def color(i: discohook.Interaction):
    """Generate a random color."""
    view = discohook.View()
    view.add_buttons(generate_button)
    await i.response.send(embed=make_random_color_card(i), view=view)


@app.load
@discohook.command.slash(
    options=[
        discohook.Option.integer(
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


@app.load
@discohook.command.user()
async def avatar(i: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed()
    embed.set_image(user.avatar.url)
    await i.response.send(embed=embed)


@app.load
@discohook.command.message(guild_id=os.environ["GUILD_ID"])
async def echo(i: discohook.Interaction, message: discohook.Message):
    if message.content:
        await i.response.send(message.content)
    else:
        await i.response.send("Message does not have text content.", ephemeral=True)


@app.load
@discohook.command.slash(
    options=[
        discohook.Option.attachment("file", "The file to upload.", required=True)
    ]
)
async def upload(i: discohook.Interaction, file: discohook.Attachment):
    """Upload a file to Deta Drive."""
    drive = deta.Deta(env="DETA_PROJECT_KEY").drive("files")
    await i.response.defer()
    parts = file.filename.split(".", maxsplit=1)
    name = f"{parts[0]}_{secrets.token_urlsafe(4)}"
    if len(parts) > 1:
        name += f".{parts[1]}"
    await drive.put(await file.read(), save_as=name, folder=i.author.id, content_type=file.content_type)
    embed = discohook.Embed()
    embed.set_author(name=str(i.author), icon_url=i.author.avatar.url)
    embed.description = f"Uploaded ` {name} ` to drive."
    await i.response.followup(embed=embed)


async def filename_autocomplete(i: discohook.Interaction, filename: str):
    drive = deta.Deta(env="DETA_PROJECT_KEY").drive("files")
    if not filename:
        files = await drive.files(prefix=f"{i.author.id}")
    else:
        files = await drive.files(prefix=f"{i.author.id}/{filename}")
    names = files.get("names", [])[:25]
    await i.response.autocomplete([discohook.Choice(name=name, value=name) for name in names])


@app.load
@discohook.command.slash(
    options=[
        discohook.Option.string("filename", "The file to download.", autocomplete=True, required=True)
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
    await filename_autocomplete(i, filename)


@app.load
@discohook.command.slash(
    options=[
        discohook.Option.string("filename", "The file to delete.", autocomplete=True, required=True)
    ]
)
async def delete(i: discohook.Interaction, filename: str):
    """Delete a file from Deta Drive."""
    drive = deta.Deta(env="DETA_PROJECT_KEY").drive("files")
    await i.response.defer()
    await drive.delete(filename)
    embed = discohook.Embed()
    embed.set_author(name=str(i.author), icon_url=i.author.avatar.url)
    embed.description = f"Deleted ` {filename} ` from drive."
    await i.response.followup(embed=embed)


@delete.autocomplete("filename")
async def delete_autocomplete(i: discohook.Interaction, filename: str):
    await filename_autocomplete(i, filename)


@app.load
@discohook.command.message("exec")
async def _exec(i: discohook.Interaction, message: discohook.Message):
    """Execute a python script."""
    await exec_code_and_respond(i, message.content)

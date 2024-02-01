import os
import random
import discohook

from debugger import tracer


PASSWORD = os.environ["PASSWORD"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
APPLICATION_ID = os.environ["APPLICATION_ID"]


app = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    password=PASSWORD,
    token=DISCORD_TOKEN,
    default_help_command=True,
)

app.on_interaction_error()(tracer)


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
        exec(f'async def _a_exec(): ' + "".join(f"\n {line}" for line in code.group(1).split("\n")))
        await locals()["_a_exec"]()
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
async def regenerate_button(i: discohook.Interaction):
    await i.response.update_message(embed=make_random_color_card(i))


@app.load
@discohook.command.slash()
async def color(i: discohook.Interaction):
    """Generate a random color."""
    view = discohook.View()
    view.add_buttons(regenerate_button)
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
@discohook.command.message("exec")
async def _exec(i: discohook.Interaction, message: discohook.Message):
    """Execute a python script."""
    await exec_code_and_respond(i, message.content)


@app.load
@discohook.command.slash(
    options=[
        discohook.Option.integer(
            "red",
            "The red value of the color.",
            required=True,
            max_value=255,
            min_value=0,
            autocomplete=True
        ),
        discohook.Option.integer(
            "green",
            "The green value of the color.",
            required=True,
            max_value=255,
            min_value=0,
            autocomplete=True
        ),
        discohook.Option.integer(
            "blue",
            "The blue value of the color.",
            required=True,
            max_value=255,
            min_value=0,
            autocomplete=True
        ),
    ]
)
async def colormix(i: discohook.Interaction, red: int, green: int, blue: int):
    """Generates a range of numbers."""
    hex_value = f"{red:02x}{green:02x}{blue:02x}"
    embed = discohook.Embed(title=f"0x{hex_value}")
    embed.set_image(f"https://singlecolorimage.com/get/{hex_value}/1280x720")
    embed.set_author(name=i.author.name, icon_url=i.author.avatar.url)
    await i.response.send(embed=embed)


@colormix.on_autocomplete
async def handler(i: discohook.Interaction, red: int, green: int, blue: int):

    choices = []

    if i.focused_option_name == "red":
        green = green or '_'
        blue = blue or '_'
        original_color = f"RGB({red}, {green}, {blue})"
        random_colors = [f"RGB({red}, {green}, {blue})" for red in range(0, 256, 24)]
        random_colors = [original_color] + random_colors
        choices = [discohook.Choice(name=_color, value=red) for _color in random_colors]
    if i.focused_option_name == "green":
        red = red or '_'
        blue = blue or '_'
        original_color = f"RGB({red}, {green}, {blue})"
        random_colors = [f"RGB({red}, {green}, {blue})" for green in range(0, 256, 24)]
        random_colors = [original_color] + random_colors
        choices = [discohook.Choice(name=_color, value=green) for _color in random_colors]
    if i.focused_option_name == "blue":
        red = red or '_'
        green = green or '_'
        original_color = f"RGB({red}, {green}, {blue})"
        random_colors = [f"RGB({red}, {green}, {blue})" for blue in range(0, 256, 24)]
        random_colors = [original_color] + random_colors
        choices = [discohook.Choice(name=_color, value=blue) for _color in random_colors]

    await i.response.autocomplete(choices)

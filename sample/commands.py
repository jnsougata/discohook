import random

import discohook


command_tree = discohook.CommandTree()


@command_tree.preload("regenerate")
@discohook.button.new("Regenerate")
async def regenerate_button(i: discohook.Interaction):
    await i.response.update_message(embed=make_random_color_card(i))


@command_tree.preload("delete")
@discohook.button.new("Delete", style=discohook.ButtonStyle.red)
async def delete_button(i: discohook.Interaction):
    await i.response.defer()
    await i.message.delete()


def make_random_color_card(i: discohook.Interaction) -> discohook.Embed:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_hex = f"{red:02x}{green:02x}{blue:02x}"
    embed = discohook.Embed(description=f"**`color: #{color_hex}`**", color=color_hex)
    embed.set_image(f"https://singlecolorimage.com/get/{color_hex}/1280x720")
    embed.set_author(name=i.author.name, icon_url=i.author.avatar.url)
    return embed


@command_tree.slash()
async def color(i: discohook.Interaction):
    """Generate a random color."""
    view = discohook.View()
    view.add_buttons(regenerate_button)
    await i.response.send(embed=make_random_color_card(i), view=view)


@command_tree.slash(
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
    permissions=[discohook.Permission.manage_messages]
)
async def purge(i: discohook.Interaction, limit: int):
    """Purge messages from the channel."""
    await i.response.send(f"Purging {limit} messages.", ephemeral=True)
    await i.channel.purge(limit)


@command_tree.user()
async def avatar(i: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed()
    embed.set_image(user.avatar.url)
    embed.set_thumbnail(i.author.avatar.url)
    await i.response.send(embed=embed)


async def exec_and_respond(i: discohook.Interaction, content: str):
    from io import StringIO
    import os
    import re
    import sys

    os.environ.clear()

    await i.response.defer()

    view = discohook.View()
    view.add_buttons(delete_button)

    pattern = re.compile("```(?:python|py)?\n([\s\S]*?)\n```")  # noqa
    code = pattern.search(content)
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


@command_tree.message("exec")
async def _exec(i: discohook.Interaction, message: discohook.Message):
    """Execute a python script."""
    await exec_and_respond(i, message.content)

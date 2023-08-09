from .command import command
from .embed import Embed
from .enums import ApplicationCommandType
from .interaction import Interaction


@command("help", "Shows this message.")
async def _help(i: Interaction):
    embed = Embed()
    embed.author(name=i.author.name, icon_url=i.author.avatar.url)
    embed.description = "Here are the commands you can use:\n"
    commands = i.client.application_commands.values()
    sorted_commands = sorted(commands, key=lambda x: x.category.value)
    for cmd in sorted_commands:
        if cmd.category == ApplicationCommandType.slash:
            embed.description += f"\n**` /{cmd.name} `**  {cmd.description}\n"
        else:
            category = "user" if cmd.category == ApplicationCommandType.user else "message"
            embed.description += f"\n**` {cmd.name} `**  (A {category} command)\n"

    await i.response.send(embed=embed)

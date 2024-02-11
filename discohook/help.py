from .command import slash
from .embed import Embed
from .enums import ApplicationCommandType
from .interaction import Interaction


@slash("help")
async def _help(i: Interaction):
    """Shows help message."""
    embed = Embed()
    embed.set_author(name=i.author.name, icon_url=i.author.avatar.url)
    embed.description = "Here are the commands you can use\n"
    commands = i.client.commands.values()
    commands = sorted(sorted(commands, key=lambda x: x.name), key=lambda x: x.type.value)
    for cmd in commands:
        if cmd.guild_id and cmd.guild_id != i.guild_id:
            continue
        if cmd.kind == ApplicationCommandType.slash:
            embed.description += f"\n**` /{cmd.name} `** {cmd.description}\n"
        else:
            category = "user" if cmd.kind == ApplicationCommandType.user else "message"
            embed.description += f"\n**` {cmd.name} `** {category.capitalize()} Command\n"

    await i.response.send(embed=embed)

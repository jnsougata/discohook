from .command import ApplicationCommand
from .embed import Embed
from .enums import ApplicationCommandType
from .interaction import Interaction


async def help_callback(i: Interaction):
    embed = Embed()
    embed.author(name=i.author.name, icon_url=i.author.avatar.url)
    embed.description = "Here are the commands you can use:\n"
    commands = i.client.application_commands.values()
    sorted_commands = sorted(commands, key=lambda x: x.category.value)
    for command in sorted_commands:
        if command.category == ApplicationCommandType.slash:
            embed.description += f"\n**` /{command.name} `**  {command.description}\n"
        else:
            category = "user" if command.category == ApplicationCommandType.user else "message"
            embed.description += f"\n**` {command.name} `**  (a {category} command)\n"

    await i.response.send(embed=embed)


def help_command() -> ApplicationCommand:
    command = ApplicationCommand(
        name="help",
        description="Shows this message.",
    )
    command.callback = help_callback
    return command

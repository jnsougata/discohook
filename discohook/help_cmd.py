from .command import ApplicationCommand
from .embed import Embed
from .enums import ApplicationCommandType
from .interaction import Interaction


async def help_cmd_callback(i: Interaction):
    embed = Embed(title="Help")
    embed.author(name=i.author.name, icon_url=i.author.avatar.url)
    embed.description = "Here are the commands you can use:\n"
    commands = i.client.application_commands.values()
    sorted_commands = sorted(commands, key=lambda x: x.category.value)
    for command in sorted_commands:
        if command.category == ApplicationCommandType.slash:
            embed.description += f"\n**` /{command.name} `**  {command.description}\n"
        else:
            cmd_category_str = str(command.category).split(".")[1]
            embed.description += f"\n**` {command.name} `**  This is {cmd_category_str} command.\n"

    await i.response.send(embed=embed)


def default_help_command() -> ApplicationCommand:
    command = ApplicationCommand(
        name="help",
        description="Shows this message.",
    )
    command.callback = help_cmd_callback
    return command

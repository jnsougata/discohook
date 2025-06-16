from .command import slash
from .components import Container, Separator, TextDisplay
from .enums import ApplicationCommandType
from .interaction import Interaction


@slash("help")
async def _help(interaction: Interaction):
    """Shows help message."""
    commands = interaction.client.active_commands.values()
    commands = sorted(
        sorted(commands, key=lambda x: x.name), key=lambda x: x.type.value
    )
    widgets = []
    for cmd in commands:
        if cmd.guild_id and cmd.guild_id != interaction.guild_id:
            continue
        if cmd.type == ApplicationCommandType.slash:
            widgets.append(TextDisplay(f"- **`/{cmd.name}`**  {cmd.description}"))
            widgets.append(Separator(spacing=1))
        else:
            category = "user" if cmd.type == ApplicationCommandType.user else "message"
            widgets.append(
                TextDisplay(f"- **`{cmd.name}`**  {category.capitalize()} Command")
            )
            widgets.append(Separator(spacing=1))
        if len(widgets) > 0 and isinstance(widgets[-1], Separator):
            widgets.pop()
    await interaction.response.send(
        Container(
            TextDisplay("**Commands you can use**"),
            Separator(spacing=2),
            *widgets,
        )
    )

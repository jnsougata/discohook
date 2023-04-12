import discohook


avatar_command = discohook.ApplicationCommand(
    name="avatar",
    category=discohook.ApplicationCommandType.user,
    permissions=[discohook.Permissions.send_messages],
    dm_access=False,
)


@avatar_command.on_interaction
async def callback(inter: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed(title=f"{user.name}#{user.discriminator}")
    embed.image(user.avatar.url)
    await inter.response(embed=embed)


# don't forget to add setup function
def setup(client: discohook.Client):
    client.add_commands(avatar_command)

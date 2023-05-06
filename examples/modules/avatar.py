import discohook


@discohook.command(
    name="avatar",
    category=discohook.ApplicationCommandType.user,
    permissions=[discohook.Permissions.send_messages],
    dm_access=False,
)
async def avatar(inter: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed(title=f"{user.name}#{user.discriminator}")
    embed.image(user.avatar.url)
    await inter.response(embed=embed)


# don't forget to add setup function
def setup(client: discohook.Client):
    client.add_commands(avatar)

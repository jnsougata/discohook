import discohook

# invite command

'''
Command that showcases the use of permissions, as well as the Discord REST API
to create an invite to the current channel.

Parameters
----------
duration: int
    Duration of the invite (in days), write "0" for no expiration.
'''


@discohook.command(
    name="invite",
    description="Sends an invite link to the current channel.",
    options=[
        discohook.IntegerOption(
            name="duration",
            description="Duration of the invite (in days), write \"0\" for no expiration",
            max_value=7,  # Discord only allows up to 7 days
            min_value=0
        )
    ],
    permissions=[
        discohook.Permissions.create_instant_invite
    ]
)
async def invite(interaction: discohook.Interaction):
    # Get duration
    duration = interaction.data.get('options')

    # Check if duration was provided
    if duration != None:
        duration = duration[0].get('value')
    else:
        duration = 1

    # Send request to Discord API to create a new invite to the current channel
    params = {
        "max_age": duration*86400,
        "unique": "true"
    }
    invite = await interaction.client.http.request(method="POST", path=f"/channels/{interaction.channel_id}/invites", use_auth=True, json=params)
    invite = await invite.json()

    # Send result
    await interaction.response(
        content=f"https://discord.gg/{invite['code']}"
    )

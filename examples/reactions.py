import asyncio
import discohook

# vote command
"""
Command that showcases the use of options, as well as the Discord REST API
to create reactions on a poll.

Parameters
----------
statement: str (*Required*)
    The poll's question
option_1: str (*Required*)
    The first option
option_2: str
    The second option
option_3: str
    The third option
option_4: str
    The fourth option
"""


@discohook.command(
    name="vote",
    description="Create a new poll",
    options=[
        discohook.StringOption(
            name="enunciado",
            description="The motive of the poll",
            required=True
        ),
        discohook.StringOption(
            name="option_1",
            description="The first option",
            required=True
        ),
        discohook.StringOption(
            name="option_2",
            description="The second option",
            required=False
        ),
        discohook.StringOption(
            name="option_3",
            description="The third option",
            required=False
        ),
        discohook.StringOption(
            name="option_4",
            description="The fourth option",
            required=False
        )
    ]
)
async def vote(interaction: discohook.Interaction, enunciado: str):
    # Get options and remove empty ones
    options = list(filter(None, interaction.data['options'][1:]))

    # Get all values into a list
    options = [option['value'] for option in options]

    # Format options with emojis (a, b, c, d)
    formatted = [f":regional_indicator_{chr(97+i)}: {item}" for i, item in enumerate(options)]

    # Create embed
    embed = discohook.Embed(title=f"{enunciado}", description="\n\n".join(formatted), color=0xb51ed4)

    # Add footer with author name and avatar
    embed.footer("Poll created by " + interaction.author.name, icon_url=interaction.author.avatar.url)

    # Send result
    await interaction.response.send(embed=embed)

    # Calling the internal Discord API to add the reactions for each option
    # To find your unicode emoji as Encoded URL use this website: https://www.urlencoder.org/
    # To do this for components use "interaction.message.id" instead of "interaction.original_response_message().id"
    encoded_emojis = ["%F0%9F%87%A6", "%F0%9F%87%A7", "%F0%9F%87%A8", "%F0%9F%87%A9"]
    msg = await interaction.original_response()

    for emoji in encoded_emojis:

        # Create new reaction for the message
        await interaction.client.http.request(
            method="PUT",
            path=f"/channels/{interaction.channel_id}/messages/{msg.id}/reactions/{emoji}/@me", use_auth=True)

        # Wait a moment between each reaction to avoid rate limit
        await asyncio.sleep(0.2)

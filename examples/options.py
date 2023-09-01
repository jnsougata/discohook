import random
import discohook


# roll command
"""
Command that showcases how to use integer options. It also shows how to use
embeds and how to send them with the response method.

The command takes one option, which is the number of faces of the dice. It
then rolls the dice and sends the result in an embed.

Note: the IntegerOption parameter "name" must be in lowercase.
"""


@discohook.ApplicationCommand.slash(
    name="roll",
    description="Roll a dice",
    options=[
        discohook.Option.integer(
            name="dice",
            description="Number of faces of the dice",
            required=True,
            min_value=3,
            max_value=100
        )
    ]
)
async def roll(interaction: discohook.Interaction, dice: int):

    # Roll the dice
    result = random.randint(1, dice)

    # Initialize embed
    embed = discohook.Embed(title=f"The result was: **{result}**", color=0xffffff)
    embed.set_image("https://i.gifer.com/2eRd.gif")
    embed.add_field(name="Dice used", value=f"{dice} faces (d{dice})")

    # Send result
    await interaction.response.send(embed=embed)


# gamechoice command
"""
Command that showcases how to use string select options. It
just sends a message with the selected option. It also shows
how to use the Choice class.

Note: the StringOption parameter "name" must be in lowercase and a valid python identifier.
"""


@discohook.ApplicationCommand.slash(
    name="gamechoice",
    description="Test command for string select options",
    options=[
        discohook.Option.string(
            name="videogame",
            description="Choose a videogame",
            required=True,
            choices=[
                discohook.Choice(name="Persona 5", value="Persona 5"),
                discohook.Choice(name="Zero Escape", value="Zero Escape"),
                discohook.Choice(name="Danganronpa", value="Danganronpa")
            ]
        )
    ]
)
async def gamechoice(interaction: discohook.Interaction, videogame: str):
    await interaction.response.send(content=f"You have chosen `{videogame}`")


# coinflip command
"""
Command that showcases how to use embeds and how to send them with the
response method. It also shows how to use the random module. It doesn't
take any options. It just flips a coin and sends the result in an embed.
"""


@discohook.ApplicationCommand.slash(
    name="coinflip",
    description="Flip a coin"
)
async def coinflip(interaction: discohook.Interaction):
    # Throw the coin
    result = random.choice(["heads", "tails"])

    # Initialize embed
    embed = discohook.Embed(title=f"The result was: **{result}**", color=0xaba924)
    embed.set_image("https://i.gifer.com/Fw3P.gif")

    # Send result
    await interaction.response.send(embed=embed)

import random
import discohook

# roll command

'''
Command that showcases how to use integer options. It also shows how to use
embeds and how to send them with the response method.

The command takes one option, which is the number of faces of the dice. It
then rolls the dice and sends the result in an embed.

Note: the IntegerOption parameter "name" must be in lowercase.
'''

@discohook.command(
    name="roll",
    description="Roll a dice",
    options=[discohook.IntegerOption(
        name="dice",
        description="Number of faces of the dice",
        required=True,
        min_value=3,
        max_value=100
    )]
)
async def roll(interaction: discohook.Interaction):
    # Get number of faces
    faces = interaction.data['options'][0]['value']

    # Roll the dice
    result = random.randint(1, faces)

    # Initialize embed
    dice_embed = discohook.Embed(
        title=f"The result was: **{result}**",
        color=0xffffff
    )
    dice_embed.image("https://i.gifer.com/2eRd.gif")
    dice_embed.add_field(
        name="Dice used",
        value=f"{faces} faces (d{faces})"
    )

    # Send result
    await interaction.response(
        embed=dice_embed
    )

# gamechoice command

'''
Command that showcases how to use string select options. It
just sends a message with the selected option. It also shows
how to use the Choice class.

Note: the StringOption parameter "name" must be in lowercase.
'''

@discohook.command(
    name="gamechoice",
    description="Test command for string select options",
    options=[
    discohook.StringOption(
        name="videogame",
        description="Choose a videogame",
        required=True,
        choices=[discohook.Choice(name="Persona 5", value="Persona 5"),
                 discohook.Choice(name="Zero Escape", value="Zero Escape"),
                 discohook.Choice(name="Danganronpa", value="Danganronpa")]
    )]
)
async def gamechoice(interaction: discohook.Interaction):
    choice = interaction.data['options'][0]['value']
    await interaction.response(
        content=f"You have chosen \"{choice}\""
    )

# coinflip command

'''
Command that showcases how to use embeds and how to send them with the
response method. It also shows how to use the random module. It doesn't
take any options. It just flips a coin and sends the result in an embed.
'''

@discohook.command(
    name="coinflip",
    description="Flip a coin"
)
async def coinflip(interaction: discohook.Interaction):
    # Throw the coin
    result = random.choice(["heads", "tails"])

    # Initialize embed
    coin_embed = discohook.Embed(
        title=f"The result was: **{result}**",
        color=0xaba924
        )
    coin_embed.image("https://i.gifer.com/Fw3P.gif")

    # Send result
    await interaction.response(
        embed=coin_embed
    )

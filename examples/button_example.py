import random
import discohook


@discohook.button("Delete", style=discohook.ButtonStyle.red)
async def delete(i: discohook.ComponentInteraction):
    if i.from_originator:
        await i.message.delete()
    else:
        await i.response("You can't delete this message!", ephemeral=True)


random_num = discohook.ApplicationCommand(
    name="randint",
    description="Get a random number within a range",
    options=[
        discohook.IntegerOption("min_num", "The minimum number", required=True),
        discohook.IntegerOption("max_num", "The maximum number", required=True),
    ],
)


@random_num.on_interaction
async def randint_command(i: discohook.Interaction, min_num: int, max_num: int):
    num = random.randint(min_num, max_num)
    view = discohook.View()
    view.add_button_row(delete)
    await i.response(f"Your random number is {num}", view=view)

import random
import discohook


@discohook.button("Delete", style=discohook.ButtonStyle.red)
async def delete(i: discohook.Interaction):
    if i.from_originator:
        await i.message.delete()
    else:
        await i.response.send("You can't delete this message!", ephemeral=True)


@discohook.command(
    name="randint",
    description="Get a random number within a range",
    options=[
        discohook.IntegerOption("min_num", "The minimum number", required=True),
        discohook.IntegerOption("max_num", "The maximum number", required=True),
    ]
)
async def random_num(i: discohook.Interaction, min_num: int, max_num: int):
    if min_num > max_num:
        return await i.response.send("The minimum number cannot be greater than the maximum number!", ephemeral=True)
    num = random.randint(min_num, max_num)
    view = discohook.View()
    view.add_buttons(delete)
    await i.response.send(f"Your random number is {num}", view=view)

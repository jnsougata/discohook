import random

import discohook


@discohook.button.new("Delete", style=discohook.ButtonStyle.red)
async def delete(i: discohook.Interaction):
    if i.from_originator:
        await i.message.delete()
    else:
        await i.response.send("You can't delete this message!", ephemeral=True)


@discohook.select.user("Select a user to poke", max_values=1)
async def user_select(i: discohook.Interaction, users: list[discohook.User]):
    await i.response.update_message(f"You selected {users[0].mention}")


@discohook.command.slash()
async def poke(i: discohook.Interaction):
    """Poke a user."""
    view = discohook.View()
    view.add_select(user_select)
    await i.response.send(view=view)


@discohook.command.slash(
    name="randint",
    description="Get a random number within a range",
    options=[
        discohook.Option.integer("min_num", "The minimum number", required=True),
        discohook.Option.integer("max_num", "The maximum number", required=True),
    ]
)
async def random_num(i: discohook.Interaction, min_num: int, max_num: int):
    if min_num > max_num:
        return await i.response.send("The minimum number cannot be greater than the maximum number!", ephemeral=True)
    num = random.randint(min_num, max_num)
    view = discohook.View()
    view.add_buttons(delete)
    await i.response.send(f"Your random number is {num}", view=view)

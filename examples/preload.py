import os
import random

import discohook


DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
APPLICATION_ID = os.environ["APPLICATION_ID"]
APPLICATION_PASSWORD = os.environ["APPLICATION_PASSWORD"]


app = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    token=DISCORD_TOKEN,
    password=APPLICATION_PASSWORD
)


def make_random_color_card(i: discohook.Interaction) -> discohook.Embed:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    _hex = f"{red:02x}{green:02x}{blue:02x}"
    embed = discohook.Embed(description=f"**`color: #{_hex}`**")
    embed.set_image(f"https://singlecolorimage.com/get/{_hex}/500x500")
    embed.color = _hex
    embed.author(name=i.author.name, icon_url=i.author.avatar.url)
    return embed


# preloading the button is necessary for the button to work forever.
# the button will be loaded when the bot cold starts with a predefined id.
# changing the button's id will cause the older buttons with the same id to stop working.
# changing the button's style, label, color will not affect the functionality of older buttons with the same id.
@app.preload("regenerate")
@discohook.button("Regenerate")
async def regenerate_button(i: discohook.Interaction):
    await i.response.defer()  # you should always defer the response if you are not planning to respond in 4s.
    await i.message.edit(embed=make_random_color_card(i))


@app.command()
async def color(i: discohook.Interaction):
    """Generate a random color."""
    view = discohook.View()
    view.add_buttons(regenerate_button)  # adding the button to the view.
    await i.response.send(embed=make_random_color_card(i), view=view)

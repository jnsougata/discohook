import os

import discohook
from debugger import send_error
from wrapper import (
    regenerate_button,
    delete_button,
    color,
    purge,
    avatar,
    _exec,
    translate
)

PASSWORD = os.environ["PASSWORD"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
APPLICATION_ID = os.environ["APPLICATION_ID"]

app = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    password=PASSWORD,
    token=DISCORD_TOKEN,
    default_help_command=True,
)

app.on_interaction_error()(send_error)
app.preload("regenerate")(regenerate_button)
app.preload("delete")(delete_button)
app.add_commands(color, purge, avatar, _exec, translate)

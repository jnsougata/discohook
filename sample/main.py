import os
import discohook

from commands import tree
from debugger import tracer


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

app.on_interaction_error()(tracer)
app.load_trees(tree)

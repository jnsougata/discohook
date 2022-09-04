# discohook

# Quickstart

```python
from discohook import Bot
import os


bot = Bot(
    int(os.getenv("APPLICATION_ID")),
    public_key=os.getenv("PUBLIC_KEY"),
    token=os.getenv("DISCORD_TOKEN")
)


@bot.command(name="abc", description="abc command")
async def abc(context):
    pass


@abc.subcommand(name="xyz", description="subcommand of abc")
async def xyz(context):
    pass


@test.subcommand(name="another", description="sub command")
async def sub(context):
    pass


bot.sync()

```
# discohook

### Quickstart

```python
import discohook
import os


APPLICATION_ID = int(os.getenv("APPLICATION_ID"))
APPLICATION_TOKEN = os.getenv("DISCORD_TOKEN")
APPLICATION_PUBLIC_KEY = os.getenv("PUBLIC_KEY")

client = discohook.Client(application_id=APPLICATION_ID, token=APPLICATION_TOKEN, public_key=APPLICATION_PUBLIC_KEY)


@client.command(name="help", description="basic help command for the bot")
async def help_command(interaction: discohook.Interaction):
    return await interaction.command.response(
        "Hello, World!",
        embed=discohook.Embed(title="Help", description="This is a help command"),
        ephemeral=True,
    )
```

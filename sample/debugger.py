import os
import traceback

import discohook

LOG_CHANNEL_ID = os.environ["LOG_CHANNEL_ID"]


async def send_error(i: discohook.Interaction, err: Exception):

    e_str = "\n".join(traceback.format_exception(type(err), err, err.__traceback__))
    embed = discohook.Embed(title="Exception", description=f"```py\n{e_str}\n```")
    if i.responded:
        await i.response.followup("An error occurred while processing your interaction.", ephemeral=True)
    else:
        await i.response.send("An error occurred while processing your interaction.", ephemeral=True)
    await i.client.send(LOG_CHANNEL_ID, embed=embed)

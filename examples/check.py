# Example of using a check on a button

import os
import discohook

app = discohook.Client(
  application_id = os.getenv('APPLICATION_ID'),
  public_key = os.getenv('PUBLIC_KEY'),
  token = os.getenv('DISCORD_TOKEN'),
  password = os.getenv('APPLICATION_PASSWORD')
)

async def interaction_owner_check(interaction):
  if interaction.from_originator:
    return True
  await interaction.response.send('{} This is not your interaction!'.format(interaction.author.mention), ephemeral = True)

@discohook.Button.new('Say hello')
async def hello_button(interaction):
  await interaction.response.send('hello')
hello_button.checks.append(interaction_owner_check)

@discohook.ApplicationCommand.slash('hello', description = 'a button that makes the bot say hello')
async def hello_command(interaction):
  view = discohook.View()
  view.add_buttons(hello_button)
  await interaction.response.send('Click the button below.', view = view)

# How to check if the user that clicked the button is the original user that ran the command, and make it still work forever?

# You can't store the user id in variable/attribute because serverless functions get unloaded after some mins of inactivity.
# Instead store it in a custom id of a component (button), since they can be 100 chars long and user ids are usually 17-19 chars long.

# Below is an example. The original custom id of the test button is 'test:v0.0', and the component is loaded into the app on startup. 
# Each time you run the command, it makes a copy of the button (no need to worry about a callback) with an adjusted custom id, like
# 'test:v0.0:364487161250316289:dynamic'. '364487161250316289' is my user id for example. Purposely ending the custom id with 'dynamic' 
# helps with a check in custom id parser to trim the custom id and make it look like 'test:v0.0' to point to the loaded test button's callback.



import os
import discohook


# commands/test.py

@discohook.Button.new('Test Label', custom_id = 'test:v0.0')
async def test_button(interaction):
  original_author_id = interaction.data['custom_id'].split(':')[2]
  if interaction.author.id == original_author_id:
    await interaction.response.send('You are the original owner of this interaction.')
  else:
    await interaction.response.send('This is not your interaction, run your own command!')

class TestView(discohook.View):
  def __init__(self, interaction = None):
    super().__init__()
    if interaction:
      custom_id = '{}:{}:dynamic'.format(test_button.custom_id, interaction.author.id)
      button = discohook.Button(test_button.label, custom_id = custom_id)
    else:
      button = test_button
    self.add_buttons(button)

@discohook.ApplicationCommand.slash('test', description = 'test stuff')
async def test_command(interaction):
  view = TestView(interaction)
  await interaction.response.send('Click the button below to do the test.', view = view)


# main.py

app = discohook.Client(
  application_id = os.getenv('APPLICATION_ID'),
  public_key = os.getenv('PUBLIC_KEY'),
  token = os.getenv('DISCORD_TOKEN'),
  password = os.getenv('APPLICATION_PASSWORD')
)

@app.custom_id_parser()
async def parser(interaction, custom_id):
  if custom_id.endswith('dynamic'):
    return ':'.join(custom_id.split(':')[:2]) # e.g. test:v0.0 returned from test:v0.0:364487161250316289:dynamic
  return custom_id

app.load_components(TestView())
app.add_commands(test_command)

# discohook

### Installation

```bash
pip install git+https://github.com/jnsougata/discohook
```

### Quickstart

```python
import discohook


APPLICATION_ID = "YOUR_APPLICATION_ID"
APPLICATION_TOKEN = "YOUR_APPLICATION_TOKEN"
APPLICATION_PUBLIC_KEY = "YOUR_APPLICATION_PUBLIC_KEY"

app = discohook.Client(
    application_id=APPLICATION_ID,
    token=APPLICATION_TOKEN,
    public_key=APPLICATION_PUBLIC_KEY
)

@app.command(
    id="", # leave empty for now
    name="help", 
    description="basic help command for the bot"
)
async def help_command(interaction: discohook.Interaction):
    await interaction.response(
        "Hello, World!",
        embed=discohook.Embed(title="Help", description="This is a help command"),
        ephemeral=True,
    )
```
### Deployment
Deploy the snippet above to your serverless function, and you're good to go to the next step.
Remember to replace the variables with your own.
Command will not be automatically registered.
We provide a dashboard to register commands.
We will talk about it later.

### Devportal Setup
**1.** Head over to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Once you've created the application, go to the "Bot" tab and create a new bot. Generate new token by using `Reset Token` and copy the bot token and paste it in the `APPLICATION_TOKEN` variable.
![image](https://user-images.githubusercontent.com/53375272/205481601-934f7304-96a1-493f-82ed-91a3890e6352.png)
**2.** Then go to the `General Information` tab and copy the `Application ID` and paste it in the `APPLICATION_ID` variable and copy the `Public Key` and paste it in the `APPLICATION_PUBLIC_KEY` variable.

![image](https://user-images.githubusercontent.com/53375272/205481675-5e2f338f-7524-4e70-af65-bacfa48d1541.png)

**3.** Then take you serverless instance `URL` i.e. `https://example.io` and add `/interactions` to it (i.e. `https://example.io/interactions`). Then head over to the general information tab and paste it in the `Interactions Endpoint URL` field. If everything is correct, you should see a confirmation message. Make sure you deploy the above code to your serverless instance before doing this.

![image](https://user-images.githubusercontent.com/53375272/205481706-3ecae6ba-1c98-4b55-bcfd-bf42ac1ad10e.png)


#### Registering Commands
You can sync commands by just visiting the dashboard.
The dashboard will be available at `https://example.io/api/dash/<bot_token_here> `. 

![image](https://user-images.githubusercontent.com/53375272/229229047-38102ff8-16ea-4f57-8e33-4e00fed939a2.png)

Once you visit the dashboard, it will automatically register all the commands. 
You can also register commands manually by using the bash command below.   
```bash
curl -X GET https://example.io/api/sync/<bot_token_here>
```

### Adding the `id` to the local command
Now that you've registered the command,
you can get the `id` of the command by visiting the dashboard and clicking `Copy Id` button.
Once you have the `id`, you can add it to the command in the code.
Then your command should look like this
```python
@app.command(
    id="1047575834602520586", # add id like this
    name="help", 
    description="basic help command for the bot"
)
async def help_command(interaction: discohook.Interaction):
    await interaction.response(
        "Hello, World!",
        embed=discohook.Embed(title="Help", description="This is a help command"),
        ephemeral=True,
    )
```
⚠️ Command without the `id` will not work as the library will consider it as a non-registered command.

### 📚 Get more examples [here](examples/)

### 📕 Why we didn't add auto registration?
As this library is meant to be used in serverless functions,
we didn't add auto registration as at each invocation the scripts will be reloaded
and the commands will be re-registered again.
This will cause rate limit issues and also due to command registration being a slow process,
it will cause significant latency.
So we decided to add a dashboard to register commands.
Which is a lot faster and also doesn't cause any rate limit issues if used properly.
Through the dashboard, you can also delete commands and sync the edited commands.

##  [📕 Read documentation](https://discohook.readthedocs.io/en/latest/)

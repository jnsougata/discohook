# discohook

### Installation

```bash
pip install git+https://github.com/jnsougata/discohook
```
- ⚠️ `pip install discohook` won't install this library. Use the git method mentioned above.

### Links

- [Docs](https://discohook.readthedocs.io/en/latest/)
- [Discord](https://discord.gg/5PwqKbM7wu)
- [Examples](examples)

## Quickstart

```python
import os

import discohook

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
APPLICATION_ID = os.environ["APPLICATION_ID"]
APPLICATION_PASSWORD = os.environ["APPLICATION_PASSWORD"]

app = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    token=DISCORD_TOKEN,
    password=APPLICATION_PASSWORD,  # Must be provided if you want to use the dashboard.
    default_help_command=True,  # This will enable your bot to use  default help command (/help).
)


# adding a error handler
@app.on_interaction_error()
async def on_error(i: discohook.Interaction, err: Exception):
    user_response = "Some error occurred! Please contact the developer."
    if i.responded:
        await i.response.followup(user_response, ephemeral=True)
    else:
        await i.response.send(user_response, ephemeral=True)

    await app.send("12345678910", f"Error: {err}")  # send error to a channel in development server


# If description is not provided, it will look for function's docstring.
# If description is not provided and function's docstring is not found, it will raise ValueError.
# If name is not provided, it will use the function name as the command name. (in this case, "ping")
# If category is not provided, it will use ApplicationCommandType.slash as the command category.
@app.command()
async def ping(i: discohook.Interaction):
    """Ping the bot."""
    await i.response.send("Pong!")


# Making user command
@app.user_command()
async def avatar(i: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed()
    embed.set_image(url=user.avatar.url)
    await i.response.send(embed=embed)

```
### Deployment
Deploy the snippet above to your serverless function, and you're good to go to the next step.
Remember to replace the variables with your own.
Command will not be automatically registered.
We provide a dashboard to register commands.
We will talk about it later.

### Developer Portal Setup
**1.** Head over to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Once you've created the application, go to the "Bot" tab and create a new bot. Generate new token by using `Reset Token` and copy the bot token and paste it in the `APPLICATION_TOKEN` variable.
![image](https://user-images.githubusercontent.com/53375272/205481601-934f7304-96a1-493f-82ed-91a3890e6352.png)
**2.** Then go to the `General Information` tab and copy the `Application ID` and paste it in the `APPLICATION_ID` variable and copy the `Public Key` and paste it in the `APPLICATION_PUBLIC_KEY` variable.

![image](https://user-images.githubusercontent.com/53375272/205481675-5e2f338f-7524-4e70-af65-bacfa48d1541.png)

**3.** Then take you serverless instance `URL` i.e. `https://example.io` and add `/interactions` to it (i.e. `https://example.io/interactions`). Then head over to the general information tab and paste it in the `Interactions Endpoint URL` field. If everything is correct, you should see a confirmation message. Make sure you deploy the above code to your serverless instance before doing this.

![image](https://user-images.githubusercontent.com/53375272/205481706-3ecae6ba-1c98-4b55-bcfd-bf42ac1ad10e.png)


#### Registering Commands
You can sync commands by just visiting the dashboard.
The dashboard will be available at `https://example.io/api/dash `. 

![image](https://github.com/jnsougata/discohook/assets/53375272/b174878b-7aac-4e05-83cc-62f00dfa8c80)

Once you visit the dashboard, it will automatically register all the commands. 
You can also register commands manually by using the bash command below.   
```bash
curl -d '{"password":  <sha256 hashed password>}' -X POST https://example.io/api/sync  
```

**🎉 Boom!** You're done. Now you can test your bot by using ` /help ` command in your server.

#### Why we didn't add auto registration?
As this library is meant to be used in serverless functions,
we didn't add auto registration as at each invocation the scripts will be reloaded
and the commands will be re-registered again.
This will cause rate limit issues and also due to command registration being a slow process,
it will cause significant latency.
So we decided to add a dashboard to register commands.
Which is a lot faster and also doesn't cause any rate limit issues if used properly.
Through the dashboard, you can also delete commands and sync the edited commands.

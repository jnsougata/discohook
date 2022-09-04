from discord import DiscordOverHTTP, Request

PUB_KEY = "3a7cdb965f8b20fdb4becb83eacb8eda9388e97f0752ad98e3b269b103b584e1"
http = DiscordOverHTTP()

@http.command(name="ping")
async def ping(request: Request):
    pass

@http.command()
async def echo(request: Request):
    pass


app = http.get_app(PUB_KEY)


@app.get("/")
async def root(request: Request):
    return {"version": "0.0.1", "developer": "jnsouagata", "commands": app.factory}

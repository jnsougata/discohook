import aiohttp
from .embed import Embed
from .user import ClientUser
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def init_session(self):
    if not self.token:
        raise ValueError("Token is not provided")
    headers = {"Authorization": f"Bot {self.token}"}
    self._session = aiohttp.ClientSession(base_url="https://discord.com", headers=headers)
    
async def cache_client(self):
    data = await (await self._session.get(f"/api/v10/oauth2/applications/@me")).json()
    self.user = ClientUser(data)
    self.owner = self.user.owner
    
async def sync_cmds(self):
    done = []
    for command in self._qualified_commands:
        if command.guild_id:
            url = f"/api/v10/applications/{self.application_id}/guilds/{command.guild_id}/commands"
        else:
            url = f"/api/v10/applications/{self.application_id}/commands"
        resp = await (await self._session.post(url, json=command.json())).json()
        try:
            command.id = resp['id']
        except KeyError:
            raise ValueError(str(resp))
        else:
            self.application_commands[command.id] = command
            done.append(f"` name ` {command.name}   ` id ` {command.id}")
    self._qualified_commands.clear()
    if self.log_channel_id:
        embed = Embed(
            title="✅ Commands Synced",
            description="\n\n".join(done)
        )
        await self.send_message(self.log_channel_id, {"embeds": [embed.json()]})

async def sync_handler(request: Request, token: str = ""):
    if token == "":
        return JSONResponse({"error": "TokenRequired"}, status_code=400)
    if token != request.app.token:
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    await init_session(request.app)
    await cache_client(request.app)
    await sync_cmds(request.app)
    return JSONResponse({"success": True}, status_code=200)
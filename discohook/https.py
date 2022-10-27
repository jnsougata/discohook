import aiohttp


ROOT = "https://discord.com/api/v10"


async def request(method: str, path: str, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, f"{ROOT}{path}", **kwargs) as resp:
            try:
                return await resp.json()
            except Exception:
                return await resp.text()

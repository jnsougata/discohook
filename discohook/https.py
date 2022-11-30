import aiohttp


async def request(session: aiohttp.ClientSession, path: str, method: str = "GET", **kwargs):
    r =  await session.request(method, f'/api/v10/{path}', **kwargs)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}

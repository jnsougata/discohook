import aiohttp


async def request(method: str = "GET", *, path: str, session: aiohttp.ClientSession, **kwargs):
    r = await session.request(method, f'/api/v10/{path}', **kwargs)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}

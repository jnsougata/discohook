import aiohttp


async def request(
    method: str = "GET", *, path: str, session: aiohttp.ClientSession, **kwargs
):
    r = await session.request(method, f"/api/v10/{path}", **kwargs)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}

async def multipart_request(
    method: str = "POST", 
    *, 
    path: str, 
    session: aiohttp.ClientSession, 
    form: aiohttp.MultipartWriter, 
):
    r = await session.request(method, f"/api/v10/{path}", data=form, headers=form.headers)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}
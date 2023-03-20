import aiohttp


async def request(
    method: str = "GET", *, path: str, session: aiohttp.ClientSession, **kwargs
):
    """
    Makes authenticated request to the discord api

    This function is used internally by the library and should be used carefully.

    Parameters
    ----------
    method: str
        The http method to use
    path: str
        The path to the endpoint
    session: aiohttp.ClientSession
        The session to use
    kwargs: dict
        The kwargs to pass to the request
    """
    r = await session.request(method, f"/api/v10/{path}", **kwargs)
    try:
        return await r.json()
    except aiohttp.ContentTypeError:
        return {"content": await r.text()}

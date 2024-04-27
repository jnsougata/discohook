import aiohttp
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request


class SingleUseSession(BaseHTTPMiddleware):
    """
    This middleware creates a new aiohttp.ClientSession to handle this request.
    This is helpful for some serverless providers
    that handle each request in a new event loop but keep the same app instance.
    """

    async def dispatch(self, request: Request, rre: RequestResponseEndpoint):
        await request.app.http.session.close()
        request.app.http.session = aiohttp.ClientSession('https://discord.com')
        return await rre(request)

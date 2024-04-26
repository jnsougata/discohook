import aiohttp
from starlette.middleware.base import BaseHTTPMiddleware

class SingleUseSessionMiddleware(BaseHTTPMiddleware):
    """ This middleware creates a new aiohttp.ClientSession
        to handle this request.
        This is helpful for some serverless prviders
        that handle each request in a new event loop
        but keep the same app instance
    """
    async def dispatch(self, request, call_next):
        await request.app.http.session.close()
        request.app.http.session = aiohttp.ClientSession('https://discord.com')
        return await call_next(request)

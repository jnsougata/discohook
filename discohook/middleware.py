import aiohttp
from starlette.middleware.base import BaseHTTPMiddleware

class SingleUseSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        await request.app.http.session.close()
        request.app.http.session = aiohttp.ClientSession('https://discord.com')
        return await call_next(request)

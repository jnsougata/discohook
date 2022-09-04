import asyncio
import typing
import fastapi
from models import *
from functools import wraps
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi.responses import JSONResponse, Response


handler = fastapi.FastAPI()
handler.public_key = ""
handler.factory = {}


@handler.post("/interactions")
async def interactions(request: fastapi.Request):
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = await request.body()
    key = VerifyKey(bytes.fromhex(app.PUBKEY))
    smessage = timestamp.encode() + body
    try:
        key.verify(smessage, bytes.fromhex(signature))
    except BadSignatureError:
        return Response(content='invalid request signature', status_code=401)
    else:
        interaction = Interaction(await request.json())
        if interaction.type == InteractionType.PING:
            return JSONResponse(status_code=200, content={'type': CallbackType.PONG.value})
        elif interaction.type == InteractionType.APPLICATION_COMMAND:
            return JSONResponse(
                status_code=200,
                content={
                    'type': CallbackType.CHANNEL_MESSAGE_WITH_SOURCE.value,
                    'data': {'content': interaction.token}
                }
            )

Request = fastapi.Request


class DiscordOverHTTP:

    def get_app(self, key: str) -> fastapi.FastAPI:
        handler.public_key = key
        return handler

    def command(self, name: str = None, guild_id: int = None) -> None:

        def decorator(coro):
            @wraps(coro)
            def wrapper(*args, **kwargs):
                if asyncio.iscoroutinefunction(coro):
                    if guild_id and name:
                        handler.factory[f'{guild_id}*{name}'] = coro
                    elif guild_id:
                        handler.factory[f'{guild_id}*{coro.__name__}'] = coro
                    elif name:
                        handler.factory[name] = coro
                    else:
                        handler.factory[coro.__name__] = coro
                return coro
            return wrapper()
        return decorator

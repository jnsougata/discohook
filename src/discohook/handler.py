from __future__ import annotations
import asyncio
from fastapi import Request
from .interaction import *
from .command import *
from functools import wraps
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi.responses import JSONResponse, Response
from typing import Optional, List, Dict, Any, Union, Callable
from .enums import CallbackType, InteractionType, ComponentType, CommandType


async def handler(request: Request):
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = await request.body()
    key = VerifyKey(bytes.fromhex(request.app.public_key))
    try:
        key.verify(stimestamp.encode() + body, bytes.fromhex(signature))
    except BadSignatureError:
        return Response(content='invalid request signature', status_code=401)
    else:
        interaction = Interaction(await request.json())
        if interaction.type is InteractionType.PING:
            return JSONResponse(status_code=200, content={'type': CallbackType.PONG.value})
        elif interaction.type is InteractionType.APPLICATION_COMMAND:
            return JSONResponse(
                status_code=200,
                content={
                    'type': CallbackType.CHANNEL_MESSAGE_WITH_SOURCE.value,
                    'data': {'content': interaction.token}
                }
            )



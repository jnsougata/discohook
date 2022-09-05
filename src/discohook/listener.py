from __future__ import annotations
import asyncio
from fastapi import Request
from .interaction import Interaction
from .command import *
from functools import wraps
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi.responses import JSONResponse, Response
from typing import Optional, List, Dict, Any, Union, Callable
from .enums import callback_types, interaction_types, component_type, command_types


async def listener(request: Request):
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = await request.body()
    key = VerifyKey(bytes.fromhex(request.app.public_key))
    try:
        key.verify(timestamp.encode() + body, bytes.fromhex(signature))
    except BadSignatureError:
        return Response(content='invalid request signature', status_code=401)
    else:
        interaction = Interaction(**(await request.json()))
        if interaction.type == interaction_types.ping.value:
            return JSONResponse({'type': callback_types.pong.value}, status_code=200, )
        elif interaction.type is interaction_types.app_command.value:
            command: ApplicationCommand = request.app.application_commands.get(interaction.app_command_data.id)
            if not command:
                return interaction.response.send(content='Command not Implemented!', ephemeral=True)
            else:
                # TODO: use parser to make sufficient arguments later
                return await command.callback(interaction)


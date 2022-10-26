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
from .enums import callback_types, interaction_types, command_types, component_types
from .parser import build_prams, build_options, build_modal_params


async def listener(request: Request):
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    try:
        key = VerifyKey(bytes.fromhex(request.app.public_key))
        key.verify(str(timestamp).encode() + await request.body(), bytes.fromhex(str(signature)))
    except BadSignatureError:
        return Response(content='request validation failed', status_code=401)
    else:
        interaction = Interaction(**(await request.json()))
        interaction.app = request.app
        if interaction.type == interaction_types.ping.value:
            return JSONResponse({'type': callback_types.pong.value}, status_code=200)

        elif interaction.type == interaction_types.app_command.value:
            command: ApplicationCommand = request.app.application_commands.get(interaction.app_command_data.id)
            if not command:
                return interaction.response(content='command not implemented!', ephemeral=True)
            else:
                options = build_options(interaction)
                args, kwargs = build_prams(options, command._callback)  # noqa
                return await command._callback(interaction, *args, **kwargs) # noqa

        elif interaction.type == interaction_types.component.value:
            component_data = interaction.data
            custom_id = component_data.get('custom_id')
            component = request.app.ui_factory.get(custom_id, None)
            if not (custom_id and component):
                return JSONResponse({'error': 'component not found!'}, status_code=404)
            if component_data['component_type'] == component_types.select_menu.value:
                values = component_data['values']
                return await component._callback(interaction, values) # noqa
            return await component._callback(interaction)  # noqa

        elif interaction.type == interaction_types.modal_submit.value:
            component = request.app.ui_factory.get(interaction.data['custom_id'], None)
            if not component:
                return JSONResponse({'error': 'component not found!'}, status_code=404)
            params = build_modal_params(interaction.data)
            return await component._callback(interaction, **params)  # noqa

        else:
            return JSONResponse({'message': "unhandled interaction type"}, status_code=300)

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
from .parser import build_prams, build_options, build_modal_params
from .enums import InteractionCallbackType, InteractionType, AppCmdType, SelectMenuType
from .models import Channel, User, Role


async def listener(request: Request):
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    try:
        key = VerifyKey(bytes.fromhex(request.app.public_key))
        key.verify(str(timestamp).encode() + await request.body(), bytes.fromhex(str(signature)))
    except BadSignatureError:
        return Response(content='request validation failed', status_code=401)
    else:
        interaction = Interaction(await request.json())
        interaction.app = request.app
        if interaction.type == InteractionType.ping.value:
            return JSONResponse({'type': InteractionCallbackType.pong.value}, status_code=200)

        elif interaction.type == InteractionType.app_command.value:
            command: ApplicationCommand = request.app.application_commands.get(interaction.app_command_data.id)
            if not command:
                return interaction.response(content='command not implemented!', ephemeral=True)
            else:
                options = build_options(interaction)
                args, kwargs = build_prams(options, command._callback)  # noqa
                return await command._callback(interaction, *args, **kwargs) # noqa

        elif interaction.type == InteractionType.component.value:
            custom_id = interaction.data.get('custom_id')
            component = request.app.ui_factory.get(custom_id, None)
            if not (custom_id and component):
                return JSONResponse({'error': 'component not found!'}, status_code=404)
            if interaction.data['component_type'] == SelectMenuType.text.value:
                return await component._callback(interaction, interaction.data['values']) # noqa
            elif interaction.data['component_type'] == SelectMenuType.channel.value:
                raw_channels = interaction.data['resolved']['channels']
                values = [Channel(raw_channels.get(channel_id, {}))
                          for channel_id in interaction.data['values']]
                return await component._callback(interaction, values)  # noqa
            elif interaction.data['component_type'] == SelectMenuType.user.value:
                raw_users = interaction.data['resolved']['users']
                values = [User(raw_users.get(user_id, {}))
                          for user_id in interaction.data['values']]
                return await component._callback(interaction, values)  # noqa
            elif interaction.data['component_type'] == SelectMenuType.role.value:
                raw_roles = interaction.data['resolved']['roles']
                values = [Role(raw_roles.get(role_id, {}))
                          for role_id in interaction.data['values']]
                return await component._callback(interaction, values)  # noqa
            elif interaction.data['component_type'] == SelectMenuType.mentionable.value:
                raw_values = interaction.data['values']
                raw_resolved_roles = interaction.data['resolved'].get('roles', {})
                raw_resolved_users = interaction.data['resolved'].get('users', {})
                user_values = [User(raw_resolved_users[user_id])
                               for user_id in raw_values if user_id in raw_resolved_users]
                role_values = [Role(raw_resolved_roles[role_id])
                               for role_id in raw_values if role_id in raw_resolved_roles]
                values = user_values + role_values  # noqa
                return await component._callback(interaction, values)  # noqa
            else:
                return await component._callback(interaction, [])  # noqa

        elif interaction.type == InteractionType.modal_submit.value:
            component = request.app.ui_factory.get(interaction.data['custom_id'], None)
            if not component:
                return JSONResponse({'error': 'component not found!'}, status_code=404)
            params = build_modal_params(interaction)
            return await component._callback(interaction, **params)  # noqa

        else:
            return JSONResponse({'message': "unhandled interaction type"}, status_code=300)

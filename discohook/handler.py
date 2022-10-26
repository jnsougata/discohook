import asyncio
from fastapi import Request
from .interaction import Interaction, CommandContext, ComponentContext
from .command import *
from functools import wraps
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi.responses import JSONResponse, Response
from .parser import (
    build_slash_command_prams,
    build_modal_params,
    build_context_menu_param
)
from .enums import (
    InteractionCallbackType,
    InteractionType,
    AppCmdType,
    SelectMenuType
)
from typing import Optional, List, Dict, Any, Union, Callable
from .models import Channel, User, Role
from .debugger import build_traceback_embed


async def handler(request: Request):
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    try:
        key = VerifyKey(bytes.fromhex(request.app.public_key))
        key.verify(str(timestamp).encode() + await request.body(), bytes.fromhex(str(signature)))
    except BadSignatureError:
        return Response(content='request validation failed', status_code=401)
    else:
        data = await request.json()
        interaction = Interaction(data)
        interaction.app = request.app
        try:
            if interaction.type == InteractionType.ping.value:
                return JSONResponse({'type': InteractionCallbackType.pong.value}, status_code=200)

            elif interaction.type == InteractionType.app_command.value:
                ctx = CommandContext(request.app, data)
                command: ApplicationCommand = request.app.application_commands.get(interaction.app_command_data.id)
                if not command:
                    return interaction.response(content='command not implemented', ephemeral=True)
                if not (interaction.data['type'] == AppCmdType.slash.value):
                    target_object = build_context_menu_param(interaction)
                    return await command._callback(ctx, target_object)  # noqa
                else:
                    args, kwargs = build_slash_command_prams(command._callback, interaction)  # noqa
                    return await command._callback(ctx, *args, **kwargs) # noqa

            elif interaction.type == InteractionType.component.value:
                cctx = ComponentContext(request.app, data)
                custom_id = interaction.data.get('custom_id')
                component = request.app.ui_factory.get(custom_id, None)
                if not (custom_id and component):
                    return JSONResponse({'error': 'component not found!'}, status_code=404)
                if interaction.data['component_type'] == SelectMenuType.text.value:
                    return await component._callback(cctx, interaction.data['values']) # noqa
                elif interaction.data['component_type'] == SelectMenuType.channel.value:
                    raw_channels = interaction.data['resolved']['channels']
                    values = [Channel(raw_channels.get(channel_id, {}))
                              for channel_id in interaction.data['values']]
                    return await component._callback(cctx, values)  # noqa
                elif interaction.data['component_type'] == SelectMenuType.user.value:
                    raw_users = interaction.data['resolved']['users']
                    values = [User(raw_users.get(user_id, {}))
                              for user_id in interaction.data['values']]
                    return await component._callback(cctx, values)  # noqa
                elif interaction.data['component_type'] == SelectMenuType.role.value:
                    raw_roles = interaction.data['resolved']['roles']
                    values = [Role(raw_roles.get(role_id, {}))
                              for role_id in interaction.data['values']]
                    return await component._callback(cctx, values)  # noqa
                elif interaction.data['component_type'] == SelectMenuType.mentionable.value:
                    raw_values = interaction.data['values']
                    raw_resolved_roles = interaction.data['resolved'].get('roles', {})
                    raw_resolved_users = interaction.data['resolved'].get('users', {})
                    user_values = [User(raw_resolved_users[user_id])
                                   for user_id in raw_values if user_id in raw_resolved_users]
                    role_values = [Role(raw_resolved_roles[role_id])
                                   for role_id in raw_values if role_id in raw_resolved_roles]
                    values = user_values + role_values  # noqa
                    return await component._callback(cctx, values)  # noqa
                else:
                    return await component._callback(cctx, [])  # noqa

            elif interaction.type == InteractionType.modal_submit.value:
                ctx = CommandContext(request.app, data)
                component = request.app.ui_factory.get(interaction.data['custom_id'], None)
                if not component:
                    return JSONResponse({'error': 'component not found!'}, status_code=404)
                args, kwargs = build_modal_params(component._callback, interaction) # noqa
                return await component._callback(ctx, *args, **kwargs)  # noqa
            else:
                return JSONResponse({'message': "unhandled interaction type"}, status_code=300)
        except Exception as e:
            if request.app.express_debug:
                return JSONResponse({
                    "data": {"embeds": [build_traceback_embed(e)]},
                    "type": InteractionCallbackType.channel_message_with_source.value
                }, status_code=200)
            return JSONResponse({'error': str(e)}, status_code=500)

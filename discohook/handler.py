from fastapi import Request
from .interaction import Interaction
from .command import *
from functools import wraps
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi.responses import JSONResponse, Response
from .parser import (
    build_modal_params,
    build_slash_command_prams,
    build_context_menu_param,
    build_select_menu_values,
)
from .enums import (
    InteractionCallbackType,
    InteractionType,
    AppCmdType,
    SelectMenuType,
    MessageComponentType
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
        interaction.client = request.app
        try:
            if interaction.type == InteractionType.ping.value:
                return JSONResponse({'type': InteractionCallbackType.pong.value}, status_code=200)

            elif interaction.type == InteractionType.app_command.value:
                command: ApplicationCommand = request.app.application_commands.get(interaction._app_command_data.id)  # noqa
                if not command:
                    return await interaction.command.response(content='command not implemented', ephemeral=True)
                if not (interaction.data['type'] == AppCmdType.slash.value):
                    target_object = build_context_menu_param(interaction)
                    if command.cog:
                        return await command._callback(command.cog, interaction, target_object)  # noqa
                    else:
                        return await command._callback(interaction, target_object)  # noqa
                else:
                    if interaction.data.get('options') and interaction.data['options'][0].get('type') == AppCmdOptionType.subcommand.value:
                        subcommand = command._subcommand_callbacks.get(interaction.data['options'][0]['name'])
                        if command.cog:
                            args, kwargs = build_slash_command_prams(subcommand, interaction, 2)
                            return await subcommand(command.cog, interaction, *args, **kwargs)
                        else:
                            args, kwargs = build_slash_command_prams(subcommand, interaction)
                            return await subcommand(interaction, *args, **kwargs)
                            
                    if command.cog:
                        args, kwargs = build_slash_command_prams(command._callback, interaction, 2)  # noqa
                        return await command._callback(command.cog, interaction, *args, **kwargs)  # noqa
                    else:
                        args, kwargs = build_slash_command_prams(command._callback, interaction)  # noqa
                        return await command._callback(interaction, *args, **kwargs) # noqa

            elif interaction.type == InteractionType.component.value:
                custom_id = interaction.data['custom_id']
                component = request.app.ui_factory.get(custom_id, None)
                if not component:
                    return JSONResponse({'error': 'component not found!'}, status_code=404)
                if interaction.data['component_type'] == MessageComponentType.button.value:
                    return await component._callback(interaction)  # noqa
                return await component._callback(interaction, build_select_menu_values(interaction))  # noqa

            elif interaction.type == InteractionType.modal_submit.value:
                component = request.app.ui_factory.get(interaction.data['custom_id'], None)
                if not component:
                    return JSONResponse({'error': 'component not found!'}, status_code=404)
                args, kwargs = build_modal_params(component._callback, interaction) # noqa
                return await component._callback(interaction, *args, **kwargs)  # noqa
            else:
                return JSONResponse({'message': "unhandled interaction type"}, status_code=300)
        except Exception as e:
            if request.app.express_debug:
                return JSONResponse({
                    "data": {"embeds": [build_traceback_embed(e).json()], 'flags': 64},
                    "type": InteractionCallbackType.channel_message_with_source.value
                }, status_code=200)
            return JSONResponse({'error': str(e)}, status_code=500)

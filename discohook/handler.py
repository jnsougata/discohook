from fastapi import Request
from .interaction import Interaction, ComponentInteraction, CommandInteraction
from .command import *
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi.responses import JSONResponse, Response
from .resolver import (
    build_modal_params,
    build_slash_command_prams,
    build_context_menu_param,
    build_select_menu_values,
)
from .enums import (
    AppCmdType,
    InteractionType,
    MessageComponentType,
    InteractionCallbackType,
)
from .errors import NotImplemented


# noinspection PyProtectedMember
async def handler(request: Request):
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    try:
        key = VerifyKey(bytes.fromhex(request.app.public_key))
        key.verify(
            str(timestamp).encode() + await request.body(),
            bytes.fromhex(str(signature)),
        )
    except BadSignatureError:
        return Response(content="BadSignature", status_code=401)

    data = await request.json()
    try:
        if data["type"] == InteractionType.ping.value:
            return JSONResponse({"type": InteractionCallbackType.pong.value}, status_code=200)

        elif data["type"] == InteractionType.app_command.value:
            interaction = CommandInteraction(data, request)
            command: ApplicationCommand = request.app.application_commands.get(interaction.command_data.id)
            if not command:
                raise NotImplemented(data)

            elif not (interaction.data["type"] == AppCmdType.slash.value):
                target_object = build_context_menu_param(interaction)
                if command.cog:
                    await command._callback(command.cog, interaction, target_object)
                else:
                    await command._callback(interaction, target_object)

            elif interaction.data.get("options") and (
                interaction.data["options"][0].get("type") == AppCmdOptionType.subcommand.value
            ):
                subcommand = command._subcommand_callbacks.get(interaction.data["options"][0]["name"])
                if command.cog:
                    args, kwargs = build_slash_command_prams(subcommand, interaction, 2)
                    await subcommand(command.cog, interaction, *args, **kwargs)
                else:
                    args, kwargs = build_slash_command_prams(subcommand, interaction)
                    await subcommand(interaction, *args, **kwargs)

            elif command.cog:
                args, kwargs = build_slash_command_prams(command._callback, interaction, 2)
                await command._callback(command.cog, interaction, *args, **kwargs)

            else:
                args, kwargs = build_slash_command_prams(command._callback, interaction)
                await command._callback(interaction, *args, **kwargs)

        elif data["type"] == InteractionType.component.value:
            interaction = ComponentInteraction(data, request)
            custom_id = interaction.data["custom_id"]
            component = request.app.ui_factory.get(custom_id, None)
            if not component:
                return JSONResponse({"error": "component not found!"}, status_code=404)
            if interaction.data["component_type"] == MessageComponentType.button.value:
                await component._callback(interaction)
            if interaction.data["component_type"] == MessageComponentType.select_menu.value:
                await component._callback(interaction, build_select_menu_values(interaction))

        elif data["type"] == InteractionType.modal_submit.value:
            interaction = Interaction(data, request)
            component = request.app.ui_factory.get(interaction.data["custom_id"], None)
            if not component:
                return JSONResponse({"error": "component not found!"}, status_code=404)
            args, kwargs = build_modal_params(component._callback, interaction)
            await component._callback(interaction, *args, **kwargs)

        elif data["type"] == InteractionType.autocomplete.value:
            interaction = Interaction(data, request)
            command: ApplicationCommand = request.app.application_commands.get(interaction.data["id"])
            if not command:
                return JSONResponse({"error": "command not found!"}, status_code=404)
            callback = command._autocomplete_callback
            option_name = interaction.data["options"][0]["name"]
            option_value = interaction.data["options"][0]["value"]
            if option_value:
                await callback(interaction, option_name, option_value)

        else:
            return JSONResponse({"message": "unhandled interaction type"}, status_code=300)

    except Exception as e:
        if request.app._global_error_handler:
            await request.app._global_error_handler(e, data)

    return JSONResponse({"ack": 1}, status_code=200)

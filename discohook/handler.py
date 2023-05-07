import traceback
from .command import *
from fastapi import Request
from .resolver import (
    build_modal_params,
    build_slash_command_prams,
    build_context_menu_param,
    build_select_menu_values,
)
from .enums import (
    ApplicationCommandType,
    InteractionType,
    MessageComponentType,
    InteractionCallbackType,
)
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from .interaction import Interaction, ComponentInteraction
from fastapi.responses import JSONResponse, Response


# noinspection PyProtectedMember
async def handler(request: Request):
    """
    Handles all interactions from discord

    Note: This is not a public API and should not be used outside the library
    """
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    try:
        key = VerifyKey(bytes.fromhex(request.app.public_key))
        key.verify(str(timestamp).encode() + await request.body(), bytes.fromhex(str(signature)))
    except BadSignatureError:
        return Response(content="BadSignature", status_code=401)

    data = await request.json()
    interaction = Interaction(data, request.app)
    try:
        if data["type"] == InteractionType.ping.value:
            return JSONResponse({"type": InteractionCallbackType.pong.value}, status_code=200)

        elif data["type"] == InteractionType.app_command.value:
            key = f"{interaction.data['name']}:{interaction.data['type']}"
            cmd: ApplicationCommand = request.app.application_commands.get(key)
            if not cmd:
                raise RuntimeError(f"command `{interaction.data['name']}` ({interaction.data['id']}) not found")

            elif not (interaction.data["type"] == ApplicationCommandType.slash.value):
                target_object = build_context_menu_param(interaction)
                await cmd.__call__(interaction, target_object)

            elif interaction.data.get("options") and (
                interaction.data["options"][0].get("type") == ApplicationCommandOptionType.subcommand.value
            ):
                subcommand = cmd.subcommands.get(interaction.data["options"][0]["name"])
                args, kwargs = build_slash_command_prams(subcommand, interaction)
                await subcommand.__call__(interaction, *args, **kwargs)
            else:
                args, kwargs = build_slash_command_prams(cmd.callback, interaction)
                await cmd.__call__(interaction, *args, **kwargs)

        elif data["type"] == InteractionType.component.value:
            interaction = ComponentInteraction(data, request.app)
            custom_id = interaction.data["custom_id"]
            if request.app._custom_id_parser:
                custom_id = await request.app._custom_id_parser(custom_id)
            component = request.app.active_components.get(custom_id, None)
            if not component:
                return JSONResponse({"error": "component not found"}, status_code=404)
            if interaction.data["component_type"] == MessageComponentType.button.value:
                await component.__call__(interaction)
            menu_types = [
                MessageComponentType.text_select_menu.value,
                MessageComponentType.user_select_menu.value,
                MessageComponentType.role_select_menu.value,
                MessageComponentType.mentionable_select_menu.value,
                MessageComponentType.channel_select_menu.value,
            ]
            if interaction.data["component_type"] in menu_types:
                await component.__call__(interaction, build_select_menu_values(interaction))

        elif data["type"] == InteractionType.modal_submit.value:
            component = request.app.active_components.get(interaction.data["custom_id"])
            if not component:
                return JSONResponse({"error": "component not found!"}, status_code=404)
            args, kwargs = build_modal_params(component.callback, interaction)
            await component.__call__(interaction, *args, **kwargs)

        elif data["type"] == InteractionType.autocomplete.value:
            key = f"{interaction.data['name']}:{interaction.data['type']}"
            cmd: ApplicationCommand = request.app.application_commands.get(key)
            if not cmd:
                return JSONResponse({"error": "command not found"}, status_code=404)
            name = interaction.data["options"][0]["name"]
            value = interaction.data["options"][0]["value"]
            callback = cmd.autocompletes.get(name)
            if callback:
                await callback(interaction, value)

        else:
            return JSONResponse({"message": "unhandled interaction type"}, status_code=300)
    except Exception as e:
        if request.app.error_handler:
            await request.app.error_handler(interaction, e)
            return JSONResponse({"message": "internal server error"}, status_code=500)
        else:
            err = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
            raise RuntimeError(err) from None
    else:
        return JSONResponse({"message": "acknowledged"}, status_code=200)

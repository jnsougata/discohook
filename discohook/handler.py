import traceback

from fastapi import Request
from fastapi.responses import JSONResponse, Response
from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey

from .command import ApplicationCommand, ApplicationCommandOptionType
from .enums import (
    ApplicationCommandType,
    InteractionCallbackType,
    InteractionType,
    MessageComponentType,
)
from .interaction import Interaction
from .resolver import (
    build_context_menu_param,
    build_modal_params,
    build_select_menu_values,
    build_slash_command_prams,
)


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
        if interaction.type == InteractionType.ping:
            return JSONResponse({"type": InteractionCallbackType.pong.value}, status_code=200)

        elif interaction.type == InteractionType.app_command:
            key = f"{interaction.data['name']}:{interaction.data['type']}"
            cmd: ApplicationCommand = request.app.application_commands.get(key)
            if not cmd:
                raise RuntimeError(f"command `{interaction.data['name']}` ({interaction.data['id']}) not found")

            elif not (interaction.data["type"] == ApplicationCommandType.slash.value):
                target_object = build_context_menu_param(interaction)
                await cmd.__call__(interaction, target_object)

            elif interaction.data.get("options") and (
                interaction.data["options"][0]["type"] == ApplicationCommandOptionType.subcommand.value
            ):
                subcommand = cmd.subcommands[interaction.data["options"][0]["name"]]
                args, kwargs = build_slash_command_prams(subcommand.callback, interaction)
                await subcommand.__call__(interaction, *args, **kwargs)
            else:
                args, kwargs = build_slash_command_prams(cmd.callback, interaction)
                await cmd.__call__(interaction, *args, **kwargs)

        elif interaction.type == InteractionType.component:
            custom_id = interaction.data["custom_id"]
            if request.app._custom_id_parser:
                custom_id = await request.app._custom_id_parser(custom_id)
            component = request.app.active_components.get(custom_id)
            if not component:
                return JSONResponse({"error": "component not found"}, status_code=404)
            if interaction.data["component_type"] == MessageComponentType.button.value:
                await component.__call__(interaction)
            menu_types = [
                MessageComponentType.text_select.value,
                MessageComponentType.user_select.value,
                MessageComponentType.role_select.value,
                MessageComponentType.channel_select.value,
                MessageComponentType.mentionable_select.value,
            ]
            if interaction.data["component_type"] in menu_types:
                await component.__call__(interaction, build_select_menu_values(interaction))

        elif interaction.type == InteractionType.modal_submit:
            component = request.app.active_components.get(interaction.data["custom_id"])
            if not component:
                return JSONResponse({"error": "component not found!"}, status_code=404)
            args, kwargs = build_modal_params(component.callback, interaction)
            await component.__call__(interaction, *args, **kwargs)

        elif interaction.type == InteractionType.autocomplete:
            key = f"{interaction.data['name']}:{interaction.data['type']}"
            cmd: ApplicationCommand = request.app.application_commands.get(key)
            if not cmd:
                return JSONResponse({"error": "command not found"}, status_code=404)
            option_type = interaction.data["options"][0]["type"]
            if option_type == ApplicationCommandOptionType.subcommand.value:
                subcommand_name = interaction.data["options"][0]["name"]
                option = interaction.data["options"][0]["options"][0]
                callback = cmd.subcommands[subcommand_name].autocompletes.get(option["name"])
            else:
                option = interaction.data["options"][0]
                callback = cmd.autocompletes.get(option["name"])
            if callback:
                await callback(interaction, option["value"])
        else:
            return JSONResponse({"message": "unhandled interaction type"}, status_code=300)
    except Exception as exc:
        stack_trace = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
        if request.app.error_handler:
            await request.app.error_handler(interaction, exc)
            return JSONResponse({"errors": stack_trace}, status_code=500)
        raise RuntimeError(stack_trace) from None
    return Response(status_code=200)

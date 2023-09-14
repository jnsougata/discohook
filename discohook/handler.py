import asyncio

import ed25519
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from .command import ApplicationCommand, ApplicationCommandOptionType
from .enums import (
    ApplicationCommandType,
    InteractionCallbackType,
    InteractionType,
    ComponentType
)
from .errors import CheckFailure, UnknownInteractionType
from .interaction import Interaction
from .resolver import (
    build_context_menu_param,
    build_modal_params,
    build_select_menu_values,
    build_slash_command_params,
)


def _command_key(interaction: Interaction) -> str:
    specific_source_guild = interaction.data.get("guild_id")
    if specific_source_guild:
        return f"{interaction.data['name']}:{specific_source_guild}:{interaction.data['type']}"
    return f"{interaction.data['name']}:{interaction.data['type']}"


# noinspection PyProtectedMember
async def _handler(request: Request):
    """
    Handles all interactions from discord

    Note: This is not a public API and should not be used outside the library
    """
    signature = bytes.fromhex(request.headers.get("X-Signature-Ed25519", ""))
    timestamp = request.headers.get("X-Signature-Timestamp", "")
    message = timestamp.encode() + await request.body()
    public_key = bytes.fromhex(request.app.public_key)
    try:
        ed25519.VerifyingKey(public_key).verify(signature, message)
    except ed25519.BadSignatureError:
        return Response(content="BadSignature", status_code=401)
    data = await request.json()
    interaction = Interaction(request.app, data)
    try:
        if interaction.kind == InteractionType.ping:
            return JSONResponse({"type": InteractionCallbackType.pong}, status_code=200)

        elif interaction.kind == InteractionType.app_command:
            cmd: ApplicationCommand = request.app.commands.get(_command_key(interaction))
            if not cmd:
                raise NotImplementedError(f"command `{interaction.data['name']}` ({interaction.data['id']}) not found")
            try:
                if cmd.checks:
                    results = await asyncio.gather(*[check(interaction) for check in cmd.checks])
                    for result in results:
                        if not isinstance(result, bool):
                            raise CheckFailure(f"check returned {type(result)}, expected bool")
                    if not all(results):
                        raise CheckFailure(f"command checks failed")

                if not (interaction.data["type"] == ApplicationCommandType.slash):
                    target_object = build_context_menu_param(interaction)
                    await cmd(interaction, target_object)

                elif interaction.data.get("options") and (
                    interaction.data["options"][0]["type"] == ApplicationCommandOptionType.subcommand
                ):
                    subcommand = cmd.subcommands[interaction.data["options"][0]["name"]]
                    args, kwargs = build_slash_command_params(subcommand.callback, interaction)
                    await subcommand(interaction, *args, **kwargs)
                else:
                    args, kwargs = build_slash_command_params(cmd.callback, interaction)
                    await cmd(interaction, *args, **kwargs)
            except Exception as e:
                if not cmd._error_handler:
                    raise e
                await cmd._error_handler(interaction, e)

        elif interaction.kind == InteractionType.autocomplete:
            cmd: ApplicationCommand = request.app.commands.get(_command_key(interaction))
            if not cmd:
                raise Exception(f"command `{interaction.data['name']}` ({interaction.data['id']}) not found")
            if interaction.data["options"][0]["type"] == ApplicationCommandOptionType.subcommand:
                subcommand_name = interaction.data["options"][0]["name"]
                option = interaction.data["options"][0]["options"][0]
                callback = cmd.subcommands[subcommand_name].autocompletes.get(option["name"])
            else:
                option = interaction.data["options"][0]
                callback = cmd.autocompletes.get(option["name"])
            if callback:
                await callback(interaction, option["value"])

        elif interaction.kind in (InteractionType.component, InteractionType.modal_submit):
            custom_id = interaction.data["custom_id"]
            if request.app._custom_id_parser:
                custom_id = await request.app._custom_id_parser(interaction, custom_id)
            component = request.app.active_components.get(custom_id)
            if not component:
                raise NotImplementedError(f"component `{custom_id}` not found")
            try:
                if component.checks:
                    results = await asyncio.gather(*[check(interaction) for check in component.checks])
                    for result in results:
                        if not isinstance(result, bool):
                            raise CheckFailure(f"check returned {type(result)}, expected bool")
                    if not all(results):
                        raise CheckFailure("component checks failed")

                if interaction.kind == InteractionType.component:
                    if interaction.data["component_type"] == ComponentType.button:
                        await component(interaction)
                    else:
                        await component(interaction, build_select_menu_values(interaction))
                elif interaction.kind == InteractionType.modal_submit:
                    args, kwargs = build_modal_params(component.callback, interaction)
                    await component(interaction, *args, **kwargs)
            except Exception as e:
                if not component._error_handler:
                    raise e
                await component._error_handler(interaction, e)
        else:
            raise UnknownInteractionType(f"unknown interaction type {interaction.kind}")
    except Exception as e:
        if request.app._interaction_error_handler:
            await request.app._interaction_error_handler(interaction, e)
            return Response(status_code=500)
        else:
            raise e from None
    else:
        return Response(status_code=200)

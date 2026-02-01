import asyncio

from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from .command import ApplicationCommand, ApplicationCommandOptionType
from .enums import (ApplicationCommandType, ComponentType,
                    InteractionCallbackType, InteractionType)
from .errors import CheckFailure, UnknownInteractionType
from .interaction import Interaction
from .resolver import (build_context_menu_param, build_modal_params,
                       build_slash_command_params, resolve_select_menu_values)


def _build_key(interaction: Interaction) -> str:
    specific_source_guild = interaction.data.get("guild_id")
    key = f"{interaction.data['name']}:{interaction.data['type']}"
    if specific_source_guild:
        key += f":{specific_source_guild}"
    return key


# noinspection PyProtectedMember
async def _engine(request: Request):
    """
    Handles all interactions from discord

    Note: This is not a public API and should not be used outside the library
    """
    signature = bytes.fromhex(request.headers.get("X-Signature-Ed25519", ""))
    timestamp = request.headers.get("X-Signature-Timestamp", "")
    message = timestamp.encode() + await request.body()
    public_key = bytes.fromhex(request.app.public_key)
    try:
        VerifyKey(public_key).verify(message, signature)
    except BadSignatureError:
        return Response(content="BadSignature", status_code=401)
    data = await request.json()
    interaction = Interaction(request.app, data)
    try:
        if interaction.type == InteractionType.ping:
            return JSONResponse({"type": InteractionCallbackType.pong}, status_code=200)

        elif interaction.type == InteractionType.app_command:
            command: ApplicationCommand = request.app.active_commands.get(
                _build_key(interaction)
            )
            if not command:
                raise NotImplementedError(
                    f"command `{interaction.data['name']}` ({interaction.data['id']}) not found"
                )
            try:
                if command.handler.checks:
                    results = await asyncio.gather(
                        *[check(interaction) for check in command.handler.checks]
                    )
                    for result in results:
                        if not isinstance(result, bool):
                            raise CheckFailure(
                                f"Any of the checks for command `{command.name}` "
                                f"returned {type(result)}, expected bool.",
                            )
                    if not all(results):
                        raise CheckFailure(
                            f"Checks for command `{command.name}` failed."
                        )

                if not (interaction.data["type"] == ApplicationCommandType.slash):
                    await command.handler(
                        interaction, build_context_menu_param(interaction)
                    )

                elif interaction.data.get("options") and (
                    interaction.data["options"][0]["type"]
                    == ApplicationCommandOptionType.subcommand
                ):
                    subcommand = command.subcommands[
                        interaction.data["options"][0]["name"]
                    ]
                    results = await asyncio.gather(
                        *[check(interaction) for check in subcommand.handler.checks]
                    )
                    for result in results:
                        if not isinstance(result, bool):
                            raise CheckFailure(
                                f"Any of the checks for subcommand `{command.name}.{subcommand.name}` "
                                f"returned {type(result)}, expected bool."
                            )
                    if not all(results):
                        raise CheckFailure(
                            f"Checks for subcommand `{command.name}.{subcommand.name}` failed."
                        )
                    args, kwargs = build_slash_command_params(
                        subcommand.handler.callback, interaction
                    )
                    try:
                        # noinspection PyUnresolvedReferences
                        await subcommand.handler(interaction, *args, **kwargs)
                    except Exception as e:
                        if not subcommand.handler._error_handler:
                            raise e
                        interaction._error = e
                        await subcommand.handler._error_handler(interaction)
                else:
                    args, kwargs = build_slash_command_params(
                        command.handler.callback, interaction
                    )
                    await command.handler(interaction, *args, **kwargs)
            except Exception as e:
                if not command.handler._error_handler:
                    raise e
                interaction._error = e
                await command.handler._error_handler(interaction)

        elif interaction.type == InteractionType.autocomplete:
            command: ApplicationCommand = request.app.active_commands.get(
                _build_key(interaction)
            )
            if not command:
                raise Exception(
                    f"Command `{interaction.data['name']}` ({interaction.data['id']}) was not found."
                )
            if (
                interaction.data["options"][0]["type"]
                == ApplicationCommandOptionType.subcommand
            ):
                subcommand = command.subcommands[interaction.data["options"][0]["name"]]
                args, kwargs = build_slash_command_params(
                    subcommand.autocompletion_handler.callback, interaction
                )
                await subcommand.autocompletion_handler.callback(
                    interaction, *args, **kwargs
                )
            elif not command.autocompletion_handler:
                raise Exception(
                    f"Command `{interaction.data['name']}` ({interaction.data['id']}) has no autocompletion handler."
                )
            else:
                args, kwargs = build_slash_command_params(
                    command.autocompletion_handler.callback, interaction
                )
                await command.autocompletion_handler.callback(
                    interaction, *args, **kwargs
                )

        elif interaction.type in (
            InteractionType.component,
            InteractionType.modal_submit,
        ):
            original_custom_id = interaction.data["custom_id"]
            parsed_custom_id = None
            if request.app._custom_id_parser:
                parsed_custom_id = await request.app._custom_id_parser(
                    interaction, original_custom_id
                )
            handler = request.app.active_handlers.get(
                parsed_custom_id or original_custom_id
            )
            if not handler:
                raise NotImplementedError(
                    f"Component with custom_id `{original_custom_id}` was not found."
                )
            try:
                if handler.checks:
                    results = await asyncio.gather(
                        *[check(interaction) for check in handler.checks]
                    )
                    for result in results:
                        if not isinstance(result, bool):
                            raise CheckFailure(
                                f"Any of the checks for component with custom_id `{original_custom_id}` "
                                f"returned {type(result)}, expected bool."
                            )
                    if not all(results):
                        raise CheckFailure(
                            f"Checks for component with custom_id `{original_custom_id}` failed."
                        )

                if interaction.type == InteractionType.component:
                    if interaction.data["component_type"] == ComponentType.button:
                        await handler(interaction, original_custom_id)
                    else:
                        await handler(
                            interaction, resolve_select_menu_values(interaction)
                        )
                elif interaction.type == InteractionType.modal_submit:
                    args, kwargs = build_modal_params(handler.callback, interaction)
                    await handler(interaction, *args, **kwargs)
            except Exception as e:
                if not handler._error_handler:
                    raise e
                interaction._error = e
                await handler._error_handler(interaction)
        else:
            raise UnknownInteractionType(
                f"Unknown interaction type {interaction.type} encountered."
            )
    except Exception as e:
        if not request.app._interaction_error_handler:
            raise e
        interaction._error = e
        await request.app._interaction_error_handler(interaction)
        return Response(status_code=500)
    else:
        return Response(status_code=200)

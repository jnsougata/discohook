import inspect
from typing import Any, Callable, Dict, List, Tuple

from .attachment import Attachment
from .channel import Channel
from .enums import (
    ApplicationCommandOptionType,
    ApplicationCommandType,
    ComponentType,
)
from .interaction import Interaction
from .member import Member
from .message import Message
from .role import Role
from .user import User
from .utils import unwrap_user


def handle_params_by_signature(
    func: Callable,
    options: Dict[str, Any],
    skips: int = 1,
) -> Tuple[List[Any], Dict[str, Any]]:
    if not func:
        return [], {}
    params = inspect.getfullargspec(func)
    default_args = params.defaults or []
    default_kwargs = params.kwonlydefaults or {}

    args = []
    positional_args = [None for _ in range(len(params.args[skips:]) - len(default_args))]
    positional_args.extend(default_args)
    for param, default in zip(params.args[skips:], positional_args):
        option = options.get(param)
        if option is not None:
            args.append(option)
        else:
            args.append(default)

    kwargs = {}
    for kw in params.kwonlyargs:
        option = options.get(kw)
        if option is not None:
            kwargs[kw] = option
        else:
            kwargs[kw] = default_kwargs.get(kw)
    return args, kwargs


def parse_generic_options(payload: List[Dict[str, Any]], interaction: Interaction):
    options = {}
    for option in payload:
        name = option["name"]
        value = option["value"]
        option_type = option["type"]
        if option_type == ApplicationCommandOptionType.string:
            options[name] = value
        elif option_type == ApplicationCommandOptionType.integer:
            options[name] = int(value)
        elif option_type == ApplicationCommandOptionType.boolean:
            options[name] = bool(value)
        elif option_type == ApplicationCommandOptionType.number:
            options[name] = float(value)
        elif option_type == ApplicationCommandOptionType.user:
            user_data = interaction.data["resolved"]["users"][value]
            if interaction.guild_id:
                member_data = interaction.data["resolved"]["members"][value]
                member_data["user"] = user_data
                member_data = unwrap_user(member_data, interaction.guild_id)
                options[name] = Member(interaction.client, member_data)
            else:
                options[name] = User(interaction.client, user_data)
        elif option_type == ApplicationCommandOptionType.channel:
            options[name] = Channel(interaction.client, interaction.data["resolved"]["channels"][value])
        elif option_type == ApplicationCommandOptionType.role:
            options[name] = Role(interaction.client, interaction.data["resolved"]["roles"][value])
        elif option_type == ApplicationCommandOptionType.mentionable:
            # TODO: this is a shit option type, not enough motivation to implement it
            pass
        elif option_type == ApplicationCommandOptionType.attachment:
            options[name] = Attachment(interaction.data["resolved"]["attachments"][value])
    return options


def build_slash_command_prams(func: Callable, interaction: Interaction, skips: int = 1):
    command_options = interaction.data.get("options")
    if not command_options:
        return [], {}
    if command_options[0]["type"] == ApplicationCommandOptionType.subcommand:
        subcommand_options = command_options[0].get("options") or []
        parsed = parse_generic_options(subcommand_options, interaction)
    else:
        parsed = parse_generic_options(interaction.data["options"], interaction)
    return handle_params_by_signature(func, parsed, skips)


def build_context_menu_param(interaction: Interaction):
    if interaction.data["type"] == ApplicationCommandType.user:
        user_id = interaction.data["target_id"]
        user_resolved = interaction.data["resolved"]["users"][user_id]
        member_resolved = interaction.data["resolved"]["members"][user_id] if interaction.guild_id else {}
        if member_resolved:
            member_resolved["avatar"] = user_resolved["avatar"]
            user_resolved.update(member_resolved)
        return User(interaction.client, user_resolved)

    if interaction.data["type"] == ApplicationCommandType.message:
        message_id = interaction.data["target_id"]
        message_data = interaction.data["resolved"]["messages"][message_id]
        return Message(interaction.client, message_data)


def build_modal_params(func: Callable, interaction: Interaction):
    options = {}
    for row in interaction.data["components"]:
        comp = row["components"][0]
        if comp["type"] == 4:
            options[comp["custom_id"]] = comp["value"]
    return handle_params_by_signature(func, options)


def build_select_menu_values(interaction: Interaction) -> List[Any]:
    if interaction.data["component_type"] == ComponentType.select_text:
        return interaction.data["values"]
    if interaction.data["component_type"] == ComponentType.select_channel:
        resolved = interaction.data["resolved"]["channels"]
        return [Channel(interaction.client, resolved.pop(channel_id)) for channel_id in interaction.data["values"]]
    if interaction.data["component_type"] == ComponentType.select_user:
        resolved = interaction.data["resolved"]["users"]
        return [User(interaction.client, resolved.pop(user_id)) for user_id in interaction.data["values"]]
    if interaction.data["component_type"] == ComponentType.select_role:
        resolved = interaction.data["resolved"]["roles"]
        roles = [resolved.pop(role_id) for role_id in interaction.data["values"]]
        for role in roles:
            role["guild_id"] = interaction.guild_id
        return [Role(interaction.client, role) for role in roles]
    if interaction.data["component_type"] == ComponentType.select_mentionable:
        raw_values = interaction.data["values"]
        resolved_roles = interaction.data["resolved"].get("roles", {})
        resolved_users = interaction.data["resolved"].get("users", {})
        users = [
            User(interaction.client, resolved_users.pop(user_id))
            for user_id in raw_values
            if user_id in resolved_users
        ]
        roles = [
            Role(interaction.client, resolved_roles.pop(role_id))
            for role_id in raw_values
            if role_id in resolved_roles
        ]
        return users + roles  # type: ignore
    return []

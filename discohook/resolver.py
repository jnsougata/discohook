import inspect
from .user import User
from .role import Role
from .member import Member
from .channel import Channel
from .message import Message
from .attachment import Attachment
from .interaction import Interaction, CommandData
from typing import List, Dict, Any, Callable, Tuple
from .enums import ApplicationCommandOptionType, SelectMenuType, ApplicationCommandType


def handle_params_by_signature(
    func: Callable, options: Dict[str, Any], skips: int = 1
) -> Tuple[List[Any], Dict[str, Any]]:
    params = inspect.getfullargspec(func)
    default_args = params.defaults
    default_kwargs = params.kwonlydefaults
    args = []
    if default_args:
        defaults = list(default_args)
        for i in range(len(params.args[:skips]) - len(defaults)):
            defaults.insert(i, None)  # noqa
        for arg, value in zip(params.args[skips:], defaults):
            option = options.get(arg)
            if option:
                args.append(option)
            else:
                args.append(value)
    else:
        for arg in params.args[skips:]:
            option = options.get(arg)
            if option:
                args.append(option)
            else:
                args.append(None)
    kwargs = {}
    for kw in params.kwonlyargs:
        option = options.get(kw)
        if option:
            kwargs[kw] = option
        elif default_kwargs:
            kwargs[kw] = default_kwargs.get(kw)
        else:
            kwargs[kw] = None
    return args, kwargs


def parse_generic_options(payload: List[Dict[str, Any]], interaction: Interaction):
    options = {}
    for option in payload:
        name = option["name"]
        value = option["value"]
        option_type = option["type"]
        if option_type == ApplicationCommandOptionType.string.value:
            options[name] = value
        elif option_type == ApplicationCommandOptionType.integer.value:
            options[name] = int(value)
        elif option_type == ApplicationCommandOptionType.boolean.value:
            options[name] = bool(value)
        elif option_type == ApplicationCommandOptionType.user.value:
            user_data = interaction.data["resolved"]["users"][value]
            if interaction.guild_id:
                member_data = interaction.data["resolved"]["members"][value]
                if not member_data["avatar"]:
                    member_data["avatar"] = user_data["avatar"]
                user_data.update(member_data)
                options[name] = Member(user_data, interaction.client)
            else:
                options[name] = User(user_data, interaction.client)
        elif option_type == ApplicationCommandOptionType.channel.value:
            options[name] = Channel(interaction.data["resolved"]["channels"][value], interaction.client)
        elif option_type == ApplicationCommandOptionType.role.value:
            options[name] = Role(interaction.data["resolved"]["roles"][value], interaction.client)
        elif option_type == ApplicationCommandOptionType.mentionable.value:
            # TODO: this is a shit option type, not enough motivation to implement it
            pass
        elif option_type == ApplicationCommandOptionType.attachment.value:
            options[name] = Attachment(
                interaction.data["resolved"]["attachments"][value]
            )
    return options


def resolve_command_options(interaction: Interaction):
    data = CommandData(interaction.data)
    if not data.options:
        return {}
    for option in data.options:
        if option["type"] == ApplicationCommandOptionType.subcommand.value:
            return parse_generic_options(option["options"], interaction)
        else:
            return parse_generic_options(data.options, interaction)


def build_slash_command_prams(func: Callable, interaction: Interaction, skips: int = 1):
    options = resolve_command_options(interaction)
    if not options:
        return [], {}
    return handle_params_by_signature(func, options, skips)


def build_context_menu_param(interaction: Interaction):
    if interaction.data["type"] == ApplicationCommandType.user.value:
        user_id = interaction.data["target_id"]
        user_resolved = interaction.data["resolved"]["users"][user_id]
        member_resolved = (
            interaction.data["resolved"]["members"][user_id]
            if interaction.guild_id
            else {}
        )
        if member_resolved:
            member_resolved["avatar"] = user_resolved["avatar"]
            user_resolved.update(member_resolved)
        return User(user_resolved, interaction.client)

    if interaction.data["type"] == ApplicationCommandType.message.value:
        message_id = interaction.data["target_id"]
        message_data = interaction.data["resolved"]["messages"][message_id]
        return Message(message_data, interaction.client)


def build_modal_params(func: Callable, interaction: Interaction):
    options = {}
    for row in interaction.data["components"]:
        comp = row["components"][0]
        if comp["type"] == 4:
            options[comp["custom_id"]] = comp["value"]
    return handle_params_by_signature(func, options)


def build_select_menu_values(interaction: Interaction) -> List[Any]:
    if interaction.data["component_type"] == SelectMenuType.text.value:
        return interaction.data["values"]
    if interaction.data["component_type"] == SelectMenuType.channel.value:
        resolved = interaction.data["resolved"]["channels"]
        return [Channel(resolved.pop(channel_id), interaction.client) for channel_id in interaction.data["values"]]
    if interaction.data["component_type"] == SelectMenuType.user.value:
        resolved = interaction.data["resolved"]["users"]
        return [User(resolved.pop(user_id), interaction.client) for user_id in interaction.data["values"]]
    if interaction.data["component_type"] == SelectMenuType.role.value:
        resolved = interaction.data["resolved"]["roles"]
        return [Role(resolved.pop(role_id), interaction.client) for role_id in interaction.data["values"]]
    if interaction.data["component_type"] == SelectMenuType.mentionable.value:
        raw_values = interaction.data["values"]
        resolved_roles = interaction.data["resolved"].get("roles", {})
        resolved_users = interaction.data["resolved"].get("users", {})
        users = [
            User(resolved_users.pop(user_id), interaction.client) for user_id in raw_values if user_id in resolved_users
        ]
        roles = [
            Role(resolved_roles.pop(role_id), interaction.client) for role_id in raw_values if role_id in resolved_roles
        ]
        return users + roles  # type: ignore
    return []

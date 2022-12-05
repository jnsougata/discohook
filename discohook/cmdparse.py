import inspect
from .user import User
from .role import Role
from .member import Member 
from .channel import Channel
from .attachment import Attachment
from .interaction import Interaction
from typing import List, Dict, Any, Callable, Tuple
from .enums import AppCmdOptionType, SelectMenuType, AppCmdType


def handle_params_by_signature(
    func: Callable, 
    options: Dict[str, Any], 
    skips: int = 1
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
        name = option['name']
        value = option['value']
        option_type = option['type']
        if option_type == AppCmdOptionType.string.value:
            options[name] = value
        elif option_type == AppCmdOptionType.integer.value:
            options[name] = int(value)
        elif option_type == AppCmdOptionType.boolean.value:
            options[name] = bool(value)
        elif option_type == AppCmdOptionType.user.value:
            user_data = interaction.data['resolved']['users'][value]
            if interaction.guild_id:
                member_data = interaction.data['resolved']['members'][value]
                if not member_data['avatar']:
                    member_data['avatar'] = user_data['avatar']
                user_data.update(member_data)
                options[name] = Member(user_data)
            else:
                options[name] = User(user_data)
        elif option_type == AppCmdOptionType.channel.value:
            options[name] = Channel(interaction.data['resolved']['channels'][value])
        elif option_type == AppCmdOptionType.role.value:
            options[name] = Role(interaction.data['resolved']['roles'][value])
        elif option_type == AppCmdOptionType.mentionable.value:
            # TODO: this is a shit option
            pass
        elif option_type == AppCmdOptionType.attachment.value:
            options[name] = Attachment(interaction.data['resolved']['attachments'][value])
    return options


def resolve_command_options(interaction: Interaction):
    if not interaction.command_data.options:  # noqa
        return {}
    for option in interaction.command_data.options:  # noqa
        if option['type'] == AppCmdOptionType.subcommand.value:
            return parse_generic_options(option['options'], interaction)
        else:
            return parse_generic_options(interaction.command_data.options, interaction)  # noqa


def build_slash_command_prams(func: Callable, interaction: Interaction, skips: int = 1):
    options = resolve_command_options(interaction)
    if not options:
        return [], {}
    return handle_params_by_signature(func, options, skips)


def build_context_menu_param(interaction: Interaction):
    if interaction.data['type'] == AppCmdType.user.value:
        user_id = interaction.data['target_id']
        user_resolved = interaction.data['resolved']['users'][user_id]
        member_resolved = interaction.data['resolved']['members'][user_id] if interaction.guild_id else {}
        if member_resolved:
            member_resolved['avatar'] = user_resolved['avatar']
            user_resolved.update(member_resolved)
        return User(user_resolved)

    if interaction.data['type'] == AppCmdType.message.value:
        message_id = interaction.data['target_id']
        message_dict = interaction.data['resolved']['messages'][message_id]
        # TODO: objectify
        return message_dict


def build_modal_params(func: Callable, interaction: Interaction):
    options = {}
    for row in interaction.data['components']:
        comp = row['components'][0]
        if comp['type'] == 4:
            options[comp['custom_id']] = comp['value']
    return handle_params_by_signature(func, options)


def build_select_menu_values(interaction: Interaction) -> List[Any]:
    if interaction.data['component_type'] == SelectMenuType.text.value:
        return interaction.data['values']
    if interaction.data['component_type'] == SelectMenuType.channel.value:
        resolved = interaction.data['resolved']['channels']
        return [Channel(resolved.pop(channel_id)) for channel_id in interaction.data['values']]
    if interaction.data['component_type'] == SelectMenuType.user.value:
        resolved = interaction.data['resolved']['users']
        return [User(resolved.pop(user_id)) for user_id in interaction.data['values']]
    if interaction.data['component_type'] == SelectMenuType.role.value:
        resolved = interaction.data['resolved']['roles']
        return [Role(resolved.pop(role_id)) for role_id in interaction.data['values']]
    if interaction.data['component_type'] == SelectMenuType.mentionable.value:
        raw_values = interaction.data['values']
        resolved_roles = interaction.data['resolved'].get('roles', {})
        resolved_users = interaction.data['resolved'].get('users', {})
        users = [User(resolved_users.pop(user_id)) for user_id in raw_values if user_id in resolved_users]
        roles = [Role(resolved_roles.pop(role_id)) for role_id in raw_values if role_id in resolved_roles]
        return users + roles  # type: ignore
    return []

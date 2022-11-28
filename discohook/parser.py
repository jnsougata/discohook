import inspect
from .user import User
from .channel import Channel
from .member import Member  
from .role import Role
from .interaction import Interaction
from typing import List, Dict, Any, Callable, Tuple
from .enums import AppCmdOptionType, SelectMenuType, AppCmdType


def handle_params_by_signature(
    func: Callable, 
    options: Dict[str, Any], 
    skips: int = 1
) -> Tuple[List[Any], Dict[str, Any]]:
    params = inspect.getfullargspec(func)
    defaults = params.defaults
    default_kwargs = params.kwonlydefaults
    args = []
    if defaults:
        for i in range(len(params.args[:skips]) - len(defaults) - 1):
            defaults.insert(i, None)
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
        if option['type'] == AppCmdOptionType.string.value:
            options[option['name']] = option['value']
        elif option['type'] == AppCmdOptionType.integer.value:
            options[option['name']] = int(option['value'])
        elif option['type'] == AppCmdOptionType.boolean.value:
            options[option['name']] = bool(option['value'])
        elif option['type'] == AppCmdOptionType.user.value:
            user_data = interaction.data['resolved']['users'][option['value']]
            if interaction.guild_id:
                member_data = interaction.data['resolved']['members'][option['value']]
                if not member_data['avatar']:
                    member_data['avatar'] = user_data['avatar']
                user_data.update(member_data)
                options[option['name']] = Member(user_data)
            else:
                options[option['name']] = User(user_data)
        elif option['type'] == AppCmdOptionType.channel.value:
            options[option['name']] = Channel(interaction.data['resolved']['channels'][option['value']])
        elif option['type'] == AppCmdOptionType.role.value:
            # TODO: objectify
            options[option['name']] = interaction.data['resolved']['roles'][option['value']]
        elif option['type'] == AppCmdOptionType.mentionable.value:
            # TODO: this is a shit option
            # IDK if someone uses this shit
            # I mean what's the use case of this shi**
            pass
    return options


def resolve_command_options(interaction: Interaction):
    if not interaction._app_command_data.options:  # noqa
        return {}
    for option in interaction._app_command_data.options:
        if option['type'] == AppCmdOptionType.subcommand.value:
            return parse_generic_options(option['options'], interaction)
        else:
            return parse_generic_options(interaction._app_command_data.options, interaction)


def build_slash_command_prams(func: Callable, interaction: Interaction, skips: int = 1):
    options = resolve_command_options(interaction)
    if not options:
        return [], {}
    return handle_params_by_signature(func, options, skips)


def build_context_menu_param(interaction: Interaction):
    if interaction.data['type'] == AppCmdType.user.value:
        user_id = interaction.data['target_id']
        user_dict = interaction.data['resolved']['users'][user_id]
        member_dict = interaction.data['resolved']['members'][user_id] if interaction.guild_id else {}
        if member_dict:
            member_dict['avatar'] = user_dict['avatar']
            user_dict.update(member_dict)
        return User(user_dict)

    if interaction.data['type'] == AppCmdType.message.value:
        message_id = interaction.data['target_id']
        message_dict = interaction.data['resolved']['messages'][message_id]
        # TODO: objectify
        return message_dict


def build_modal_params(func: Callable, interaction: Interaction):
    options = {}
    for comp in interaction.data['components']:
        c = comp['components'][0]
        if c['type'] == 4:
            options[c['custom_id']] = c['value']
    return handle_params_by_signature(func, options)


def build_select_menu_values(interaction: Interaction) -> List[Any]:
    if interaction.data['component_type'] == SelectMenuType.text.value:
        return interaction.data['values']
    elif interaction.data['component_type'] == SelectMenuType.channel.value:
        raw_channels = interaction.data['resolved']['channels']
        return [Channel(raw_channels.get(channel_id, {})) for channel_id in interaction.data['values']]
    elif interaction.data['component_type'] == SelectMenuType.user.value:
        raw_users = interaction.data['resolved']['users']
        return [User(raw_users.get(user_id, {})) for user_id in interaction.data['values']]
    elif interaction.data['component_type'] == SelectMenuType.role.value:
        raw_roles = interaction.data['resolved']['roles']
        return [Role(raw_roles.get(role_id, {})) for role_id in interaction.data['values']]
    elif interaction.data['component_type'] == SelectMenuType.mentionable.value:
        raw_values = interaction.data['values']
        raw_resolved_roles = interaction.data['resolved'].get('roles', {})
        raw_resolved_users = interaction.data['resolved'].get('users', {})
        user_values = [User(raw_resolved_users[user_id]) for user_id in raw_values if user_id in raw_resolved_users]
        role_values = [Role(raw_resolved_roles[role_id]) for role_id in raw_values if role_id in raw_resolved_roles]
        return user_values + role_values  # type: ignore
    else:
        return []

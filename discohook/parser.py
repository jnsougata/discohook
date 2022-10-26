import inspect
from .enums import AppCmdType
from .interaction import Interaction
from .models import User, Member
from .enums import AppCmdOptionType
from typing import List, Dict, Any, Optional, Union, Callable


def handle_params_by_signature(func: Callable, options: Dict[str, Any]) -> (List[Any], Dict[str, Any]):
    params = inspect.getfullargspec(func)
    defaults = params.defaults
    default_kwargs = params.kwonlydefaults
    args = []
    if defaults:
        for i in range(len(params.args[:1]) - len(defaults) - 1):
            defaults.insert(i, None)
        for arg, value in zip(params.args[1:], defaults):
            option = options.get(arg)
            if option:
                args.append(option)
            else:
                args.append(value)
    else:
        for arg in params.args[1:]:
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


def resolve_command_options(interaction: Interaction):
    if not interaction.app_command_data.options:
        return {}
    options = {}
    for option in interaction.app_command_data.options:
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
            # TODO: objectify
            options[option['name']] = interaction.data['resolved']['channels'][option['value']]
        elif option['type'] == AppCmdOptionType.role.value:
            # TODO: objectify
            options[option['name']] = interaction.data['resolved']['roles'][option['value']]
        elif option['type'] == AppCmdOptionType.mentionable.value:
            # TODO: this is a shit option
            # IDK if someone uses this shit
            # I mean what's the use case of this shi**
            pass
        elif option['type'] == AppCmdOptionType.sub_command.value:
            # TODO: handle later
            pass
        elif option['type'] == AppCmdOptionType.sub_command_group.value:
            # TODO: Handle later
            pass
    return options


def build_slash_command_prams(func: Callable, interaction: Interaction):
    options = resolve_command_options(interaction)
    if not options:
        return [], {}
    return handle_params_by_signature(func, options)


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
    root_comps = interaction.data['components']
    options = {}
    for comp in root_comps:
        c = comp['components'][0]
        if c['type'] == 4:
            options[c['custom_id']] = c['value']
    return handle_params_by_signature(func, options)


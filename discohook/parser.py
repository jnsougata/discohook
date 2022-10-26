import inspect
from .enums import AppCmdType
from .interaction import Interaction
from .models import User, Member
from .enums import AppCmdOptionType
from typing import List, Dict, Any, Optional, Union, Callable


def build_prams(cmd_ops: Dict[str, Any], func: Callable):
    if not cmd_ops:
        return [], {}
    params = inspect.getfullargspec(func)
    defaults = params.defaults
    default_kwargs = params.kwonlydefaults
    args = []
    if defaults:
        for i in range(len(params.args[:1]) - len(defaults) - 1):
            defaults.insert(i, None)
        for arg, value in zip(params.args[1:], defaults):
            option = cmd_ops.get(arg)
            if option:
                args.append(option)
            else:
                args.append(value)
    else:
        for arg in params.args[1:]:
            option = cmd_ops.get(arg)
            if option:
                args.append(option)
            else:
                args.append(None)
    kwargs = {}
    for kw in params.kwonlyargs:
        option = cmd_ops.get(kw)
        if option:
            kwargs[kw] = option
        elif default_kwargs:
            kwargs[kw] = default_kwargs.get(kw)
        else:
            kwargs[kw] = None
    return args, kwargs


def build_options(interaction: Interaction):
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
                options[option['name']] = Member(**user_data)
            else:
                options[option['name']] = User(**user_data)
        elif option['type'] == AppCmdOptionType.channel.value:
            pass
        elif option['type'] == AppCmdOptionType.role.value:
            pass
        elif option['type'] == AppCmdOptionType.mentionable.value:
            pass
        elif option['type'] == AppCmdOptionType.sub_command.value:
            pass
        elif option['type'] == AppCmdOptionType.sub_command_group.value:
            pass
    return options


def build_modal_params(interaction: Interaction) -> dict:
    root_comps = interaction.data['components']
    params = {}
    for comp in root_comps:
        c = comp['components'][0]
        if c['type'] == 4:
            params[c['custom_id']] = c['value']
    return params

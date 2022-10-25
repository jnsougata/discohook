import inspect
from .enums import command_types
from .interaction import Interaction
from .resolved import User, Member
from .enums import option_types
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
        if option['type'] == option_types.string.value:
            options[option['name']] = option['value']
        elif option['type'] == option_types.integer.value:
            options[option['name']] = int(option['value'])
        elif option['type'] == option_types.boolean.value:
            options[option['name']] = bool(option['value'])
        elif option['type'] == option_types.user.value:
            user_data = interaction.data['resolved']['users'][option['value']]
            if interaction.guild_id:
                member_data = interaction.data['resolved']['members'][option['value']]
                if not member_data['avatar']:
                    member_data['avatar'] = user_data['avatar']
                user_data.update(member_data)
                options[option['name']] = Member(**user_data)
            else:
                options[option['name']] = User(**user_data)
        elif option['type'] == option_types.channel.value:
            pass
        elif option['type'] == option_types.role.value:
            pass
        elif option['type'] == option_types.mentionable.value:
            pass
        elif option['type'] == option_types.sub_command.value:
            pass
        elif option['type'] == option_types.sub_command_group.value:
            pass
    return options

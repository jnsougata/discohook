import inspect
from .interaction import Interaction
from .enums import command_types
from typing import List, Dict, Any, Optional, Union, Callable


def build_prams(cmd_ops: List[Dict[str, Any]], func: Callable):
    cmd_ops = {option['name']: option for option in cmd_ops}
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
                args.append(option.get('value'))
            else:
                args.append(value)
    else:
        for arg in params.args[1:]:
            option = cmd_ops.get(arg)
            if option:
                args.append(option.get('value'))
            else:
                args.append(None)
    kwargs = {}
    for kw in params.kwonlyargs:
        option = cmd_ops.get(kw)
        if option:
            kwargs[kw] = option.get('value')
        elif default_kwargs:
            kwargs[kw] = default_kwargs.get(kw)
        else:
            kwargs[kw] = None
    return args, kwargs

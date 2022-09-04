import inspect
from .context import Context
from .enums import CommandType
from typing import List, Dict, Any, Optional, Union, Callable


def _build_prams(options: Dict[str, Any], func: Callable):
    args = []
    kwargs = {}
    params = inspect.getfullargspec(func)
    default_args = params.defaults
    default_kwargs = params.kwonlydefaults
    if default_args:
        default_list = [*default_args]
        for i in range(len(params.args[:2]) - len(default_list) - 1):
            default_list.insert(i, None)

        for arg, default_value in zip(params.args[2:], default_list):
            option = options.get(arg)
            if option:
                args.append(option.value)
            else:
                args.append(default_value)
    else:
        for arg in params.args[2:]:
            option = options.get(arg)
            if option:
                args.append(option.value)
            else:
                args.append(None)

    for kw in params.kwonlyargs:
        option = options.get(kw)
        if option:
            kwargs[kw] = option.value
        elif default_kwargs:
            kwargs[kw] = default_kwargs.get(kw)
        else:
            kwargs[kw] = None
    return args, kwargs


def _build_ctx_menu_param(c: Context):
    if c.type is CommandType.USER:
        return c._target_user
    elif c.type is CommandType.MESSAGE:
        return c._target_message


def _build_modal_prams(options: Dict[str, Any], func: Callable):
    args = []
    kwargs = {}
    params = inspect.getfullargspec(func)
    default_args = params.defaults
    default_kwargs = params.kwonlydefaults
    if default_args:
        default_list = [*default_args]
        for i in range(len(params.args[:1]) - len(default_list) - 1):
            default_list.insert(i, None)

        for arg, default_value in zip(params.args[1:], default_list):
            option = options.get(arg)
            if option:
                args.append(option)
            else:
                args.append(default_value)
    else:
        for arg in params.args[1:]:
            option = options.get(arg)
            if option:
                args.append(option)
            else:
                args.append(None)

    for kw in params.kwonlyargs:
        option = options.get(kw)
        if option:
            kwargs[kw] = option
        elif default_kwargs:
            kwargs[kw] = default_kwargs.get(kw)
        else:
            kwargs[kw] = None
    return args, kwargs


def _build_autocomplete_prams(options: Dict[str, Any], func: Callable):
    args = []
    kwargs = {}
    params = inspect.getfullargspec(func)
    default_args = params.defaults
    default_kwargs = params.kwonlydefaults
    if default_args:
        default_list = [*default_args]
        for i in range(len(params.args[:1]) - len(default_list) - 1):
            default_list.insert(i, None)

        for arg, default_value in zip(params.args[1:], default_list):
            option = options.get(arg)
            if option:
                args.append(option.value)
            else:
                args.append(default_value)
    else:
        for arg in params.args[1:]:
            option = options.get(arg)
            if option:
                args.append(option.value)
            else:
                args.append(None)

    for kw in params.kwonlyargs:
        option = options.get(kw)
        if option:
            kwargs[kw] = option.value
        elif default_kwargs:
            kwargs[kw] = default_kwargs.get(kw)
        else:
            kwargs[kw] = None
    return args, kwargs

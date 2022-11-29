import inspect
from functools import wraps
from .enums import AppCmdType
from .option import Option
from typing import List
from .command import ApplicationCommand


class Cog(metaclass=type):
    commands = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.private_commands = cls.commands.copy()
        for command in instance.private_commands:
            command.cog = instance
        cls.commands.clear()
        return instance

    @classmethod
    def command(
        cls,
        name: str,
        description: str = None,
        *,
        options: List[Option] = None,
        permissions: str = None,
        dm_access: bool = True,
        guild_id: int = None,
        category: AppCmdType = AppCmdType.slash,
    ):
        def decorator(func):
            @wraps(func)
            def wrapper(*_, **__):
                if inspect.iscoroutinefunction(func):
                    command = ApplicationCommand(
                        name=name,
                        description=description,
                        options=options,
                        permissions=permissions,
                        dm_access=dm_access,
                        guild_id=guild_id,
                        category=category
                    )
                    command._callback = func
                    cls.commands.append(command)
                    return command
            return wrapper()
        return decorator

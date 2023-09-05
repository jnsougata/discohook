import hashlib
import json
import secrets
from typing import Any, Callable, Coroutine, Union


AsyncFunc = Callable[["Interaction", Any], Coroutine[Any, Any, Any]]


def compare_password(local: str, remote: str) -> bool:
    return secrets.compare_digest(hashlib.sha256(local.encode()).hexdigest(), remote)


def color_parser(color: Union[int, str]) -> int:
    if isinstance(color, int):
        if not (color < 0 or color > 0xFFFFFF):
            return color
        raise ValueError("Color must be in the range [0, 16777215]")
    if color.startswith("#"):
        color = color[1:]
    return int(color, 16)


def try_description(name: str, description: Any, callback: AsyncFunc) -> str:
    if description and isinstance(description, str):
        return description
    if callback.__doc__:
        return callback.__doc__.strip().split("\n")[0]
    raise TypeError(f"description is required for slash command `{name}`")


def unwrap_user(data: dict, guild_id: str) -> dict:
    member = json.loads(json.dumps(data))
    user: dict = member.pop("user")
    member.update(user)
    member["guild_id"] = guild_id
    return member

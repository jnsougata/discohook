import asyncio
import hashlib
import json
import secrets
from typing import Any, Callable, Coroutine, Union

Handler = Callable[["Interaction", Any], Coroutine[Any, Any, Any]]


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


def snowflake_time(snowflake_id: str) -> float:
    discord_epoch = 1420070400000
    return ((int(snowflake_id) >> 22) + discord_epoch) / 1000


def find_description(name: str, description: Any, callback: Handler) -> str:
    if description and isinstance(description, str):
        return description
    if callback.__doc__:
        return callback.__doc__.strip().split("\n")[0]
    raise ValueError(f"description is required for slash command `{name}`")


def unwrap_user(data: dict, guild_id: str) -> dict:
    member = json.loads(json.dumps(data))
    user: dict = member.pop("user")
    member.update(user)
    member["guild_id"] = guild_id
    return member


run_sync = asyncio.get_event_loop().run_until_complete

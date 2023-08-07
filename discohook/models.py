from typing import List
from typing_extensions import NotRequired, TypedDict
from .enums import AllowedMentionsTypes


class AllowedMentions(TypedDict):
    parse: NotRequired[List[AllowedMentionsTypes]]
    roles: NotRequired[List[str]]
    users: NotRequired[List[str]]
    replied_user: NotRequired[bool]


class MessageReference(TypedDict):
    message_id: NotRequired[str]
    channel_id: NotRequired[str]
    guild_id: NotRequired[str]
    fail_if_not_exists: NotRequired[bool]



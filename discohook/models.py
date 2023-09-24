from typing import List, Optional

from .enums import AllowedMentionsType


class AllowedMentions:
    """
    Represents a discord allowed mentions object.

    Parameters
    ----------
    parse: List[AllowedMentionsType] | None
        The types of mentions to parse from the message content.
    roles: List[str] | None
        The roles to mention.
    users: List[str] | None
        The users to mention.
    replied_user: bool | None
        Whether to mention the user the message is replying to.
    """

    def __init__(
        self,
        parse: Optional[List[AllowedMentionsType]] = None,
        roles: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        replied_user: Optional[bool] = None
    ):
        self.parse = parse
        self.roles = roles
        self.users = users
        self.replied_user = replied_user

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the allowed mentions object.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the allowed mentions object.
        """
        data = {}
        if self.parse:
            data["parse"] = [mention.value for mention in self.parse]
        if self.roles:
            data["roles"] = self.roles
        if self.users:
            data["users"] = self.users
        if self.replied_user:
            data["replied_user"] = self.replied_user
        return data


class MessageReference:
    """
    Represents a discord message reference object.

    Parameters
    ----------
    message_id: str | None
        The id of the message.
    channel_id: str | None
        The id of the channel where the message was sent.
    guild_id: str | None
        The id of the guild where the message was sent.
    fail_if_not_exists: bool | None
        Whether to throw an error if the message does not exist.
    """

    def __init__(
        self,
        message_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        guild_id: Optional[str] = None,
        fail_if_not_exists: Optional[bool] = None
    ):
        self.message_id = message_id
        self.channel_id = channel_id
        self.guild_id = guild_id
        self.fail_if_not_exists = fail_if_not_exists

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the message reference object.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the message reference object.
        """

        data = {}
        if self.message_id:
            data["message_id"] = self.message_id
        if self.channel_id:
            data["channel_id"] = self.channel_id
        if self.guild_id:
            data["guild_id"] = self.guild_id
        if self.fail_if_not_exists:
            data["fail_if_not_exists"] = self.fail_if_not_exists
        return data


# noinspection PyShadowingBuiltins
class PermissionOverwrite:
    """
    Represents a permission overwrite object.

    Parameters
    ----------
    id: str
        The id of the role or user.
    type: str
        The type of the overwrite.
    allow: int
        The permissions allowed by the overwrite.
    deny: int
        The permissions denied by the overwrite.
    """

    def __init__(self, id: str, type: str, allow: int, deny: int):
        self.id = id
        self.type = type
        self.allow = int(allow)
        self.deny = int(deny)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the permission overwrite object.

        This is used internally by the library. You should not need to use this method.

        Returns
        -------
        :class:`dict`
            The dictionary representation of the permission overwrite object.
        """

        return {
            "id": self.id,
            "type": self.type,
            "allow": self.allow,
            "deny": self.deny
        }

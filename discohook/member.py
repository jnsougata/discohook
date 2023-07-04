from typing import TYPE_CHECKING, Any, Dict

from .user import User

if TYPE_CHECKING:
    from .client import Client


class Member(User):
    """
    Represents a member of a guild sent with an interaction, subclassed from :class:`User`.
    """

    def __init__(self, client: "Client", data: Dict[str, Any]):
        super().__init__(client, data)
        self.nick = data.get("nick")
        self.roles = data.get("roles")
        self.joined_at = data.get("joined_at")
        self.premium_since = data.get("premium_since")
        self.pending = data.get("pending")
        self.is_pending = data.get("is_pending")
        self.flags = data.get("flags")
        self.guild_id = data.get("guild_id")
        self.communication_disabled_until = data.get("communication_disabled_until")

    @property
    def mention(self) -> str:
        """
        Returns a string that allows you to mention the member.
        """
        return f"<@!{self.id}>"

    async def add_role(self, role_id: str):
        """
        Add a role to the member.

        Parameters
        ----------
        role_id : str
            The ID of the role.
        """
        return await self.client.http.add_role(self.guild_id, self.id, role_id)

    async def remove_role(self, role_id: str):
        """
        Remove a role from the member.

        Parameters
        ----------
        role_id : str
            The ID of the role.
        """
        return await self.client.http.remove_role(self.guild_id, self.id, role_id)

    async def kick(self):
        """
        Kick the member.
        """
        return await self.client.http.kick_user(self.guild_id, self.id)

    async def ban(self, *, delete_message_seconds: int = 0):
        """
        Ban the member.

        Parameters
        ----------
        delete_message_seconds: int
            The number of days to delete messages for.
        """
        if delete_message_seconds > 604800:
            raise ValueError("You can only delete messages for up to last 7 days.")
        return await self.client.http.ban_user(self.guild_id, self.id, delete_message_seconds)

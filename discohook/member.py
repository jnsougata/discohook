from .user import User
from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .client import Client


class Member(User):
    """
    Represents a member of a guild sent with an interaction, subclassed from :class:`User`.
    """
    def __init__(self, data: Dict[str, Any], client: "Client"):
        super().__init__(data, client)
        self.nick = data.get("nick")
        self.roles = data.get("roles")
        self.joined_at = data.get("joined_at")
        self.premium_since = data.get("premium_since")
        self.pending = data.get("pending")
        self.is_pending = data.get("is_pending")
        self.communication_disabled_until = data.get("communication_disabled_until")
        self.flags = data.get("flags")
        self.guild_id = data.get("guild_id")

    @property
    def mention(self) -> str:
        """
        Returns a string that allows you to mention the member.
        """
        return f"<@!{self.id}>"

    async def add_role(self, role_id: str) -> None:
        """
        Add a role to the member.

        Parameters
        ----------
        role_id : str
            The ID of the role.
        """
        return await self.client.session.put(f"/api/v10/guilds/{self.guild_id}/members/{self.id}/roles/{role_id}")

    async def remove_role(self, role_id: str) -> None:
        """
        Remove a role from the member.

        Parameters
        ----------
        role_id : str
            The ID of the role.
        """
        return await self.client.session.delete(f"/api/v10/guilds/{self.guild_id}/members/{self.id}/roles/{role_id}")
    
    async def kick(self) -> None:
        """
        Kick the member.
        """
        return await self.client.session.delete(f"/api/v10/guilds/{self.guild_id}/members/{self.id}")

    async def ban(self, *, delete_message_seconds: int = 0) -> None:
        """
        Ban the member.

        Parameters
        ----------
        reason : str
            The reason for the ban.
        delete_message_days : int
            The number of days to delete messages for.
        """
        if delete_message_seconds > 604800:
            raise ValueError("You can only delete messages for up to last 7 days.")
        return await self.client.session.put(
            f"/api/v10/guilds/{self.guild_id}/bans/{self.id}", 
            json={"delete_message_seconds": delete_message_seconds}
        )
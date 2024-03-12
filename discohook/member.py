from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .asset import Asset
from .permission import Permission
from .role import PartialRole
from .user import User

if TYPE_CHECKING:
    from .client import Client


class Member(User):
    """
    Represents a member of a guild, subclassed from :class:`User`.
    """

    def __init__(self, client: "Client", data: Dict[str, Any]):
        super().__init__(client, data["user"])

    @property
    def guild_id(self) -> str:
        return self.data["guild_id"]

    @property
    def nick(self) -> str:
        return self.data.get("nick") or self.name

    @property
    def roles(self) -> List[PartialRole]:
        ids = self.data.get("roles")
        return [PartialRole(self.client, {"id": i, "guild_id": self.guild_id}) for i in ids]

    @property
    def joined_at(self) -> str:
        return self.data["joined_at"]

    @property
    def premium_since(self) -> Optional[str]:
        return self.data.get("premium_since")

    @property
    def permissions(self) -> int:
        return int(self.data.get("permissions", "0"))

    @property
    def pending(self) -> bool:
        return self.data.get("pending", False)

    @property
    def disabled_until(self) -> Optional[str]:
        return self.data.get("communication_disabled_until")

    @property
    def flags(self) -> int:
        return self.data["flags"]

    @property
    def avatar(self) -> Asset:
        av_hash = self.data.get("avatar")
        if not av_hash:
            return super().avatar
        return Asset(hash=av_hash, fragment=f"avatars/{self.id}")

    @property
    def mention(self) -> str:
        """
        Returns a string that allows you to mention the member.
        """
        return f"<@{self.id}>"

    def has_permission(self, permission: Permission) -> bool:
        return Permission.check(self.permissions, permission)

    async def add_role(self, role_id: str, *, reason: Optional[str] = None):
        """
        Add a role to the member.

        Parameters
        ----------
        role_id : str
            The ID of the role.
        reason: Optional[str]
            The reason for adding the role to be logged.
        """
        return await self.client.http.add_role(self.guild_id, self.id, role_id, reason=reason)

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

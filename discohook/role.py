from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .permission import Permission

if TYPE_CHECKING:
    from .client import Client


class PartialRole:
    def __init__(self, client: "Client", data: Dict[str, Any], ):
        self.client = client
        self.id = data["id"]
        self.guild_id = data.get("guild_id")

    @property
    def mention(self) -> str:
        """
        Returns a string that allows you to mention the role.

        Returns
        -------
        :class:`str`
        """
        return f"<@&{self.id}>"

    async def edit(
        self,
        *,
        name: Optional[str] = None,
        permissions: Optional[List[Permission]] = None,
        color: Optional[int] = None,
        hoist: Optional[bool] = None,
        mentionable: Optional[bool] = None,
        description: Optional[str] = None,
        unicode_emoji: Optional[str] = None,
        icon_data_uri: Optional[str] = None,
    ) -> "Role":
        """
        Edits the role.

        Parameters
        ----------
        name: Optional[:class:`str`]
            The name of the role.
        permissions: Optional[:class:`Permission`]
            The permissions of the role.
        color: Optional[:class:`int`]
            The color of the role.
        hoist: Optional[:class:`bool`]
            Whether the role has separability in the member list.
        mentionable: Optional[:class:`bool`]
            Whether the role is mentionable.
        description: Optional[:class:`str`]
            The description of the role.
        unicode_emoji: Optional[:class:`str`]
            The unicode emoji of the role.
        icon_data_uri: Optional[:class:`str`]
            The icon of the role. Must be a data URI (base64 encoded).

        Returns
        -------
        :class:`Role`
        """
        payload = {}
        if name:
            payload["name"] = name
        if permissions:
            base = 0
            for permission in permissions:
                base |= permission.value
            payload["permissions"] = str(base)
        if color:
            payload["color"] = color
        if hoist:
            payload["hoist"] = hoist
        if mentionable:
            payload["mentionable"] = mentionable
        if description:
            payload["description"] = description
        if unicode_emoji:
            payload["unicode_emoji"] = unicode_emoji
        if icon_data_uri:
            payload["icon"] = icon_data_uri
        resp = await self.client.http.edit_guild_role(self.guild_id, self.id, payload)
        data = await resp.json()
        return Role(self.client, data)

    async def edit_position(self, role_id: str, *, position: int) -> List["Role"]:
        """
        Changes the position of the role.
        Parameters
        ----------
        role_id: :class:`str`
            The id of the role to move.
        position: :class:`int`
            The new position of the role.

        Returns
        -------
        :class:`Role`
        """
        payload = {"id": role_id, "position": position}
        resp = await self.client.http.edit_guild_role_position(self.guild_id, payload)
        data = await resp.json()
        return [Role(self.client, role) for role in data]


class Role(PartialRole):
    """
    Represents a discord Role.

    Attributes
    ----------
    id: :class:`str`
        The unique ID of the role.
    name: :class:`str`
        The name of the role.
    color: :class:`int`
        The color of the role.
    hoist: :class:`bool`
        Whether the role has separability in the member list.
    position: :class:`int`
        The position of the role.
    permissions: :class:`str`
        The permissions of the role.
    managed: :class:`bool`
        Whether the role is managed by an integration.
    mentionable: :class:`bool`
        Whether the role is mentionable.
    description: Optional[:class:`str`]
        The description of the role.
    unicode_emoji: Optional[:class:`str`]
        The unicode emoji of the role.
    icon: Optional[:class:`str`]
        The icon of the role.
    flags: :class:`int`
        The flags of the role.
    """

    def __init__(self, client: "Client", data: dict):
        super().__init__(client, data)
        self.id: str = data.get("id")
        self.name: str = data.get("name")
        self.color: int = data.get("color")
        self.hoist: bool = data.get("hoist")
        self.position: int = data.get("position")
        self.permissions: str = data.get("permissions")
        self.managed: bool = data.get("managed")
        self.mentionable: bool = data.get("mentionable")
        self.description: Optional[str] = data.get("description")
        self.unicode_emoji: Optional[str] = data.get("unicode_emoji")
        self.icon: Optional[str] = data.get("icon")
        self.flags: int = data.get("flags")

    def __eq__(self, other):
        return self.id == other.id

    def has_permission(self, permission: Permission) -> bool:
        """
        Checks if the role has the given permissions.

        Parameters
        ----------
        permission: :class:`Permission`
            The permissions to check.

        Returns
        -------
        :class:`bool`
        """
        return Permission.check(int(self.permissions), permission)

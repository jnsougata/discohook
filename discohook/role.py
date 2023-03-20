from typing import Optional
from .permissions import Permissions


class Role:
    """
    Represents a role.

    Attributes
    ----------
    id: :class:`str`
        The unique ID of the role.
    name: :class:`str`
        The name of the role.
    color: :class:`int`
        The color of the role.
    hoist: :class:`bool`
        Whether the role is separelty displayed in the member list.
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
    def __init__(self, data: dict):
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

    @property
    def mention(self) -> str:
        """
        Returns a string that allows you to mention the role.

        Returns
        -------
        :class:`str`
        """
        return f"<@&{self.id}>"

    def has_permission(self, permissions: Permissions) -> bool:
        """
        Checks if the role has the given permissions.

        Parameters
        ----------
        permissions: :class:`Permissions`
            The permissions to check.

        Returns
        -------
        :class:`bool`
        """
        return int(self.permissions) & permissions.value == permissions.value


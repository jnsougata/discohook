from typing import Optional


class Role:
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

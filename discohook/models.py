from typing import Optional


class User:
    def __init__(self, data):
        self.id = data.get("id")
        self.username = data.get("username")
        self.discriminator = data.get("discriminator")
        self.avatar = data.get("avatar")
        self.bot = data.get("bot")
        self.system = data.get("system")
        self.mfa_enabled = data.get("mfa_enabled")
        self.locale = data.get("locale")
        self.verified = data.get("verified")
        self.email = data.get("email")
        self.premium_type = data.get("premium_type")
        self.public_flags = data.get("public_flags")

    def avatar_url(
            self,
            *,
            size: int = 1024,
            extension: str = "png",
            static_extension: str = "webp",
            dynamic_extension: str = "gif"
    ) -> str:
        if self.avatar is None:
            return f"https://cdn.discordapp.com/embed/avatars/{int(self.discriminator) % 5}.{extension}"
        if self.avatar.startswith("a_"):
            return f"https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.{dynamic_extension}?size={size}"
        return f"https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.{static_extension}?size={size}"

    def __eq__(self, other):
        return self.id == other.id


class Member(User):
    def __init__(self, data):
        super().__init__(data)
        self.nick = data.get("nick")
        self.roles = data.get("roles")
        self.joined_at = data.get("joined_at")
        self.premium_since = data.get("premium_since")
        self.pending = data.get("pending")
        self.is_pending = data.get("is_pending")
        self.communication_disabled_until = data.get("communication_disabled_until")
        self.flags = data.get("flags")


class Channel:
    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.type: int = data.get("type")
        self.name: str = data.get("name")
        self.parent_id: str = data.get("parent_id")
        self.permissions: str = data.get("permissions")

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f"<PartialChannel id={self.id} name={self.name} type={self.type}>"


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

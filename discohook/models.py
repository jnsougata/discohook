from typing import Optional


class User:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.username = kwargs.get("username")
        self.discriminator = kwargs.get("discriminator")
        self.avatar = kwargs.get("avatar")
        self.bot = kwargs.get("bot")
        self.system = kwargs.get("system")
        self.mfa_enabled = kwargs.get("mfa_enabled")
        self.locale = kwargs.get("locale")
        self.verified = kwargs.get("verified")
        self.email = kwargs.get("email")
        self.premium_type = kwargs.get("premium_type")
        self.public_flags = kwargs.get("public_flags")

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nick = kwargs.get("nick")
        self.roles = kwargs.get("roles")
        self.joined_at = kwargs.get("joined_at")
        self.premium_since = kwargs.get("premium_since")
        self.pending = kwargs.get("pending")
        self.is_pending = kwargs.get("is_pending")
        self.communication_disabled_until = kwargs.get("communication_disabled_until")
        self.flags = kwargs.get("flags")

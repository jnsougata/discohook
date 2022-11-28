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
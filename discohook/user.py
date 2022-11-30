from typing import Optional


class User:
    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.username: str = data["username"]
        self.discriminator: str = data["discriminator"]
        self.avatar: Optional[str] = data.get("avatar")
        self.bot: bool = data.get("bot", False)
        self.system: bool = data.get("system", False)
        self.mfa_enabled: bool = data.get("mfa_enabled", False)
        self.locale: Optional[str] = data.get("locale")
        self.verified: bool = data.get("verified", False)
        self.email: Optional[str] = data.get("email")
        self.premium_type: Optional[int] = data.get("premium_type")
        self.public_flags: Optional[int] = data.get("public_flags")

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
    
    @property
    def mention(self) -> str:
        return f"<@{self.id}>"


class ClientUser:
    def __init__(self, data: dict) -> None:
        self._data = data
    
    @property
    def id(self) -> str:
        return self._data["id"]
    
    @property
    def name(self) -> str:
        return self._data["name"]
    
    @property
    def icon_hash(self) -> Optional[str]:
        return self._data.get("icon")
    
    @property
    def icon_url(self) -> Optional[str]:
        return f"https://cdn.discordapp.com/app-icons/{self.id}/{self.icon_hash}.png"
    
    @property
    def public(self) -> bool:
        return self._data["bot_public"]
    
    @property
    def require_code_grant(self) -> bool:
        return self._data["bot_require_code_grant"]
    
    @property
    def permissions(self) -> str:
        return self._data["install_params"]["permissions"]
    
    @property
    def scopes(self) -> str:
        return self._data["install_params"]["scopes"]
    
    @property
    def owner(self) -> User:
        return User(self._data["owner"])
    
    @property
    def flags(self) -> int:
        return self._data["flags"]

from typing import Optional
from .asset import Asset
from .permissions import Permissions


class User:
    def __init__(self, data: dict):
        self.data = data

    @property
    def id(self) -> str:
        return self.data["id"]
    
    @property
    def name(self) -> str:
        return self.data["username"]
    
    @property
    def discriminator(self) -> str:
        return self.data["discriminator"]

    # noinspection PyShadowingBuiltins
    @property
    def avatar(self) -> Asset:
        hash = self.data.get("avatar")
        if not hash:
            fragment = f"embed/avatars/"
            hash = str({int(self.discriminator) % 5})
            return Asset(hash=hash, fragment=fragment)
        return Asset(hash=hash, fragment=f"avatars/{self.id}")
    
    @property
    def system(self) -> bool:
        return self.data.get("system", False)
    
    @property
    def bot(self) -> bool:
        return self.data.get("bot", False)
    
    @property
    def mfa_enabled(self) -> bool:
        return self.data.get("mfa_enabled", False)
    
    @property
    def locale(self) -> Optional[str]:
        return self.data.get("locale")
    
    @property
    def verified(self) -> bool:
        return self.data.get("verified", False)
    
    @property
    def email(self) -> Optional[str]:
        return self.data.get("email")
    
    @property
    def premium_type(self) -> Optional[int]:
        return self.data.get("premium_type")
    
    @property
    def public_flags(self) -> Optional[int]:
        return self.data.get("public_flags")
    
    def __str__(self) -> str:
        return f"{self.name}#{self.discriminator}"
    
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
    
    def has_permission(self, permission: Permissions) -> bool:
        return permission.value & int(self.permissions) == permission.value
        
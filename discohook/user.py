from typing import Optional


class User:

    id: str
    username: str
    discriminator: str
    avatar: Optional[str] = None
    bot: Optional[bool] = False
    system: Optional[bool] = False
    mfa_enabled: Optional[bool] = False
    banner: Optional[str] = None
    accent_color: Optional[int] = None
    locale: Optional[str] = None
    verified: Optional[bool] = False
    email: Optional[str] = None
    flags: Optional[int] = None
    premium_type: Optional[int] = None
    public_flags: Optional[int] = None

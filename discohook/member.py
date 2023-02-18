from .user import User


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

    @property
    def mention(self) -> str:
        return f"<@!{self.id}>"

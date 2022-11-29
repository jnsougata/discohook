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

    @property
    def mention(self) -> str:
        return f"<#{self.id}>"

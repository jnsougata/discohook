from typing import Optional


class PartialEmoji:
    def __init__(self, name: str, id: int,  animated: Optional[bool] = False):  # noqa
        self.name = name
        self.id = id
        self.animated = animated

    def to_dict(self):
        return {"name": self.name, "id": self.id, "animated": self.animated}

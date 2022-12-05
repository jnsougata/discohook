from .https import HTTPClient
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .interaction import Interaction

class Message:
    def __init__(self, payload: dict) -> None:
        self.data = payload
        self.id = payload["id"]

class Followup:
    def __init__(self, payload: dict, interaction: "Interaction") -> None:
        self.data = payload
        self.id = payload["id"]

    
    async def delete(self):
        await self.data["channel"].delete_message(self.id)

        
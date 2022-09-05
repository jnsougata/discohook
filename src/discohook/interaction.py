from .enums import interaction_types
from typing import Any, Dict, Optional, List
from pydantic import BaseModel
from .webhook import Webhook


class CommandData(BaseModel):
    id: str
    name: str
    type: int
    guild_id: Optional[str] = None
    target_id: Optional[str] = None
    resolved: Optional[Dict[str, Any]] = None
    options: Optional[List[Dict[str, Any]]] = None


class Interaction(BaseModel):
    id: str
    type: int
    token: str
    version: int
    application_id: str
    data: Optional[Dict[str, Any]] = None
    guild_id: Optional[str] = None
    channel_id: Optional[str] = None
    member: Optional[Dict[str, Any]] = None
    user: Optional[Dict[str, Any]] = None
    message: Optional[Dict[str, Any]] = None
    app_permissions: Optional[int] = None
    locale: Optional[str] = None
    guild_locale: Optional[str] = None

    @property
    def app_command_data(self) -> Optional[CommandData]:
        if self.type == interaction_types.app_command.value:
            return CommandData(**self.data)
        return None

    @property
    def response(self) -> Webhook:
        return Webhook(
            id=self.application_id,
            type=self.type,
            token=self.token,
            application_id=self.application_id,
            guild_id=self.guild_id,
            channel_id=self.channel_id
        )


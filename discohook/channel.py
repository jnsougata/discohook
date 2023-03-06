from .view import View
from .embed import Embed
from .https import request
from .params import handle_send_params
from typing import Optional, List, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client


class PartialChannel:
    def __init__(self, data: dict, client: "Client"):
        self.client = client
        self.id: str = data.get("id")

    async def send(
            self,
            content: Optional[str] = None,
            *,
            embed: Optional[Embed] = None,
            embeds: Optional[List[Embed]] = None,
            view: Optional[View] = None,
            tts: Optional[bool] = False,
            file: Optional[Dict[str, Any]] = None,
            files: Optional[List[Dict[str, Any]]] = None,
            ephemeral: Optional[bool] = False,
            supress_embeds: Optional[bool] = False,
    ):
        if view:
            for component in view.children:  # noqa
                self.client.load_component(component)  # noqa
        return await request(
            "POST",
            path=f"/channels/{self.id}/messages",
            session=self.client.session,
            json=handle_send_params(
                content=content,
                embed=embed,
                embeds=embeds,
                view=view,
                tts=tts,
                file=file,
                files=files,
                ephemeral=ephemeral,
                supress_embeds=supress_embeds,
            ),
        )


class Channel(PartialChannel):
    def __init__(self, data: dict, client: "Client"):
        super().__init__(data, client)
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

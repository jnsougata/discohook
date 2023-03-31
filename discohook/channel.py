from .file import File
from .view import View
from .embed import Embed
from .message import Message
from .multipart import create_form
from .params import handle_send_params, merge_fields
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client


class PartialChannel:
    """
    Represents a partial discord channel object.

    Parameters
    ----------
    data: :class:`dict`
        The data of the channel.
    client: :class:`Client`
        The client that the channel belongs to.
    """
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
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
    ):
        """
        Sends a message to the channel.

        Parameters
        ----------
        content: Optional[:class:`str`]
            The content of the message.
        embed: Optional[:class:`Embed`]
            The embed to send with the message.
        embeds: Optional[List[:class:`Embed`]]
            A list of embeds to send with the message.
        view: Optional[:class:`View`]
            The view to send with the message.
        tts: Optional[:class:`bool`]
            Whether the message should be sent with text-to-speech.
        file: Optional[File]
            A file to send with the message.
        files: Optional[List[File]]
            A list of files to send with the message.
        """
        if view:
            for component in view.children:
                self.client.load_component(component)
        payload = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
        )
        resp = await self.client.http.send_message(self.id, create_form(payload, merge_fields(file, files)))
        data = await resp.json()
        return Message(data, self.client)


class Channel(PartialChannel):
    """
    Represents a discord channel object subclassed from :class:`PartialChannel`.

    Parameters
    ----------
    data: :class:`dict`
        The data of the channel.
    client: :class:`Client`
        The client that the channel belongs to.
    """
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
        """
        Returns the channel mentionable string.

        Returns
        -------
        :class:`str`
        """
        return f"<#{self.id}>"

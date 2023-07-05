from .embed import Embed
from .file import File
from .view import View
from .params import MISSING, handle_edit_params, handle_send_params, merge_fields
from .enums import InteractionCallbackType, InteractionType, try_enum
from .multipart import create_form
from typing import TYPE_CHECKING, Optional, List
from .message import Message
if TYPE_CHECKING:
    from .client import Client
    from .interaction import Interaction


class InteractionResponse:
    """
    Represents a response message sent by an interaction
    """

    def __init__(self, interaction: "Interaction") -> None:
        self.interaction = interaction

    async def delete(self):
        """
        Deletes the response message.
        """
        await self.interaction.client.http.delete_webhook_message(
            self.interaction.application_id, self.interaction.token, "@original"
        )

    async def edit(
        self,
        content: Optional[str] = MISSING,
        *,
        embed: Optional[Embed] = MISSING,
        embeds: Optional[List[Embed]] = MISSING,
        view: Optional[View] = MISSING,
        tts: Optional[bool] = MISSING,
        file: Optional[File] = MISSING,
        files: Optional[List[File]] = MISSING,
        suppress_embeds: Optional[bool] = MISSING,
    ) -> Message:
        """
        Edits the response message.

        Parameters
        ----------
        same as :meth:`Message.edit`
        """
        data = handle_edit_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )
        if view and view is not MISSING:
            self.interaction.client.load_components(view)
        self.interaction.client.store_inter_token(self.interaction.id, self.interaction.token)
        resp = await self.interaction.client.http.edit_webhook_message(
            self.interaction.application_id,
            self.interaction.token,
            "@original",
            create_form(data, merge_fields(file, files)),
        )
        data = await resp.json()
        return Message(data, self.interaction.client)


class ResponseAdapter:
    """
    Represents a response message sent by an interaction
    """

    def __init__(self, interaction: "Interaction") -> None:
        self.inter = interaction

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
        ephemeral: Optional[bool] = False,
        suppress_embeds: Optional[bool] = False,
    ) -> InteractionResponse:
        """
        Sends a response to the interaction

        Parameters
        ----------
        content: Optional[str]
            The content of the message to send
        embed: Optional[Embed]
            The embed to send with the message
        embeds: Optional[List[Embed]]
            The list of embeds to send with the message (max 10)
        view: Optional[View]
            The view to send with the message
        tts: Optional[bool]
            Whether the message should be sent as tts or not
        file: Optional[File]
            The file to send with the message
        files: Optional[List[File]]
            The list of files to send with the message
        ephemeral: Optional[bool]
            Whether the message should be ephemeral or not
        suppress_embeds: Optional[bool]
            Whether the embeds should be suppressed or not

        Returns
        -------
        InteractionResponse
        """
        data = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            suppress_embeds=suppress_embeds,
        )
        if view:
            self.inter.client.store_inter_token(self.inter.id, self.inter.token)
            self.inter.client.load_components(view)

        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        await self.inter.client.http.send_interaction_mp_callback(
            self.inter.id, self.inter.token, create_form(payload, merge_fields(file, files))
        )
        self.inter.__responded = True
        return InteractionResponse(self.inter)

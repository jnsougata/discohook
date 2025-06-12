from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from .embed import Embed
from .enums import InteractionCallbackType, InteractionType
from .errors import InteractionTypeMismatch
from .file import File
from .message import Message
from .modal import Modal
from .models import AllowedMentions
from .option import Choice
from .params import (UNSPECIFIED, _prepare_editing_payload,
                     _prepare_sending_payload)
from .poll import Poll
from .view import LegacyView, View

if TYPE_CHECKING:
    from .interaction import Interaction


class InteractionResponse:
    """
    Represents a response message sent by an interaction
    """

    def __init__(self, interaction: "Interaction") -> None:
        self.inter = interaction

    async def delete(self):
        """
        Deletes the response message.
        """
        await self.inter.client.http.delete_webhook_message(
            self.inter.application_id, self.inter.token, "@original"
        )

    async def patch(self, view: View):
        """
        Patches the response message.
        """
        await self.inter.client.http.edit_webhook_message(
            self.inter.application_id, self.inter.token, "@original",
            _prepare_sending_payload(component=view))

    async def edit(
        self,
        content: Optional[str] = UNSPECIFIED,
        *,
        embed: Optional[Embed] = UNSPECIFIED,
        embeds: Optional[List[Embed]] = UNSPECIFIED,
        view: Optional[LegacyView] = UNSPECIFIED,
        tts: Optional[bool] = UNSPECIFIED,
        file: Optional[File] = UNSPECIFIED,
        files: Optional[List[File]] = UNSPECIFIED,
        suppress_embeds: Optional[bool] = UNSPECIFIED,
    ) -> Message:
        """
        Edits the response message.

        Parameters
        ----------
        same as :meth:`Message.edit`
        """
        payload = _prepare_editing_payload(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )
        resp = await self.inter.client.http.edit_webhook_message(
            self.inter.application_id,
            self.inter.token,
            "@original",
            payload,
        )
        data = await resp.json()
        return Message(self.inter.client, data)


class FollowupResponse:
    """
    Represents a followup message sent by an interaction, subclassed from :class:`Message`.
    """

    def __init__(self, payload: Dict[str, Any], interaction: "Interaction") -> None:
        self.message = Message(interaction.client, payload)
        self.interaction = interaction

    async def delete(self):
        """
        Deletes the followup message.
        """
        return await self.interaction.client.http.delete_webhook_message(
            self.interaction.application_id,
            self.interaction.token,
            self.message.id,
        )

    async def edit(
        self,
        content: Optional[str] = UNSPECIFIED,
        *,
        embed: Optional[Embed] = UNSPECIFIED,
        embeds: Optional[List[Embed]] = UNSPECIFIED,
        view: Optional[LegacyView] = UNSPECIFIED,
        tts: Optional[bool] = UNSPECIFIED,
        file: Optional[File] = UNSPECIFIED,
        files: Optional[List[File]] = UNSPECIFIED,
        suppress_embeds: Optional[bool] = UNSPECIFIED,
    ) -> Message:
        """
        Edits the followup message.

        Parameters
        ----------
        same as :meth:`Message.edit`
        """
        payload = _prepare_editing_payload(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
        )
        resp = await self.interaction.client.http.edit_webhook_message(
            self.interaction.application_id,
            self.interaction.token,
            self.message.id,
            payload,
        )
        data = await resp.json()
        return Message(self.interaction.client, data)


class ResponseAdapter:
    """
    Interface for sending responses to interactions
    """

    def __init__(self, interaction: "Interaction") -> None:
        self.inter = interaction

    async def post(self, view: View, with_response: bool = False):
        await self.inter.client.http.create_interaction_response(
            self.inter.id,
            self.inter.token,
            _prepare_sending_payload(
                component=view,
                payload_type=InteractionCallbackType.channel_message_with_source,
            ),
            with_response=with_response,
        )
        self.inter._responded = True
        return InteractionResponse(self.inter)

    async def send(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[LegacyView] = None,
        tts: Optional[bool] = False,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
        allowed_mentions: Optional[AllowedMentions] = None,
        ephemeral: Optional[bool] = False,
        suppress_embeds: Optional[bool] = False,
        poll: Optional[Poll] = None,
        with_response: bool = False,
    ) -> InteractionResponse:
        """
        Sends a response to the interaction

        Parameters
        ----------
        content: str | None
            The content of the message to send
        embed: Embed | None
            The embed to send with the message
        embeds: List[Embed] | None
            The list of embeds to send with the message (max 10)
        view: LegacyView | None
            The view to send with the message
        tts: bool
            Whether the message should be sent as tts or not, defaults to False
        file: File | None
            The file to send with the message
        files: List[File] | None
            The list of files to send with the message
        allowed_mentions: AllowedMentions | None
            The allowed_mentions object to send with the message
        ephemeral: bool
            Whether the message should be ephemeral or not, defaults to False
        suppress_embeds: bool
            Whether the embeds should be suppressed or not, defaults to False
        poll: Poll | None
            The poll to send with the message
        with_response: bool
            Whether to include an interaction callback object as the response, defaults to False
        Returns
        -------
        InteractionResponse
        """
        payload = _prepare_sending_payload(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            suppress_embeds=suppress_embeds,
            allowed_mentions=allowed_mentions,
            poll=poll,
            payload_type=InteractionCallbackType.channel_message_with_source,
        )
        self.inter._responded = True
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )
        return InteractionResponse(self.inter)

    async def send_modal(
        self, modal: Union[Modal, Any], with_response: bool = False
    ) -> InteractionResponse:
        """
        Sends a modal to the interaction

        Parameters
        ----------
        modal: Modal
            The modal to send
        with_response: bool
            Whether to include an interaction callback object as the response.

        Returns
        -------
        InteractionResponse
        """
        if self.inter.type not in (
            InteractionType.component,
            InteractionType.app_command,
        ):
            raise InteractionTypeMismatch(
                f"Method not supported for {self.inter.type}", self.inter
            )
        payload = {
            "data": modal.to_dict(),
            "type": InteractionCallbackType.modal,
        }
        self.inter._responded = True
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )
        return InteractionResponse(self.inter)

    async def autocomplete(self, choices: List[Choice], with_response: bool = False):
        """
        Sends autocomplete choices to the interaction (max 25)

        Parameters
        ----------
        choices: List[Choice]
            The choices to send
        with_response: bool
            Whether to include an interaction callback object as the response.
        """
        if self.inter.type != InteractionType.autocomplete:
            raise InteractionTypeMismatch(
                f"Method not supported for {self.inter.type}", self.inter
            )
        choices = choices[:25]
        payload = {
            "type": InteractionCallbackType.autocomplete,
            "data": {"choices": [i.to_dict() for i in choices]},
        }
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )

    async def defer(
        self,
        ephemeral: bool = False,
        thinking: bool = False,
        with_response: bool = False,
    ) -> InteractionResponse:
        """
        Defers the interaction

        Parameters
        ----------
        ephemeral: bool
            Whether the successive responses should be ephemeral or not
            (only for Application Commands or `thinking` is `True`)
        thinking: bool
            Whether to send a new "is thinking..." message to be edited later
            (DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE) or do nothing to edit the original message later
            (DEFERRED_UPDATE_MESSAGE). Not available for application commands.
        with_response: bool
            Whether to include an interaction callback object as the response.
        """
        payload = {}
        if (
            self.inter.type is InteractionType.component
            or self.inter.type is InteractionType.modal_submit
        ):
            if thinking:
                payload["type"] = (
                    InteractionCallbackType.deferred_channel_message_with_source
                )
                if ephemeral:
                    payload["data"] = {"flags": 64}
            else:
                payload["type"] = (
                    InteractionCallbackType.deferred_update_component_message
                )
        elif self.inter.type == InteractionType.app_command:
            payload["type"] = (
                InteractionCallbackType.deferred_channel_message_with_source
            )
            if ephemeral:
                payload["data"] = {"flags": 64}
        else:
            raise InteractionTypeMismatch(
                f"Method not supported for {self.inter.type}", self.inter
            )

        self.inter._responded = True
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )
        return InteractionResponse(self.inter)

    async def require_premium(self, with_response: bool = False):
        """
        Prompts the user that a premium purchase is required for this interaction
        This method is only available for applications with a premium SKU set up
        """
        if self.inter.type == InteractionType.autocomplete:
            raise InteractionTypeMismatch(
                f"Method not supported for {self.inter.type}", self.inter
            )
        payload = {
            "data": {},
            "type": InteractionCallbackType.premium_required,
        }
        self.inter._responded = True
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )
        return InteractionResponse(self.inter)

    async def update_message(
        self,
        content: Optional[str] = UNSPECIFIED,
        *,
        embed: Optional[Embed] = UNSPECIFIED,
        embeds: Optional[List[Embed]] = UNSPECIFIED,
        view: Optional[LegacyView] = UNSPECIFIED,
        tts: Optional[bool] = UNSPECIFIED,
        file: Optional[File] = UNSPECIFIED,
        files: Optional[List[File]] = UNSPECIFIED,
        suppress_embeds: Optional[bool] = UNSPECIFIED,
        with_response: bool = False,
    ) -> InteractionResponse:
        """
        Edits the message, the component was attached to.
        This method is only available for component interactions.

        Parameters
        ----------
        content: Optional[str]
            The new content of the message.
        embed: Optional[Embed]
            The new embed of the message.
        embeds: Optional[List[Embed]]
            The new embeds of the message.
        view: Optional[LegacyView]
            The new view of the message.
        tts: Optional[bool]
            Whether the message should be sent with text-to-speech.
        file: Optional[File]
            A file to send with the message.
        files: Optional[List[File]]
            A list of files to send with the message.
        suppress_embeds: Optional[bool]
            Whether the embeds should be suppressed.
        with_response: bool
            Whether to include an interaction callback object as the response.

        Returns
        -------
        InteractionResponse
        """
        if not (
            self.inter.type == InteractionType.component
            or self.inter.type == InteractionType.modal_submit
        ):
            raise InteractionTypeMismatch(
                f"Method not supported for {self.inter.type}", self.inter
            )

        payload = _prepare_editing_payload(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            suppress_embeds=suppress_embeds,
            payload_type=InteractionCallbackType.update_component_message,
        )
        self.inter._responded = True
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )
        return InteractionResponse(self.inter)

    async def followup(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        view: Optional[LegacyView] = None,
        tts: Optional[bool] = False,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
        allowed_mentions: Optional[AllowedMentions] = None,
        ephemeral: Optional[bool] = False,
        suppress_embeds: Optional[bool] = False,
        poll: Optional[Poll] = None,
    ) -> FollowupResponse:
        """
        Sends a follow-up message to a deferred interaction

        Parameters
        ----------
        content: str | None
            The content of the message to send
        embed: Embed | None
            The embed to send with the message
        embeds: List[Embed] | None
            The list of embeds to send with the message (max 10)
        view: LegacyView | None
            The view to send with the message
        tts: bool
            Whether the message should be sent as tts or not, defaults to False
        file: File | None
            The file to send with the message
        files: List[File] | None
            The list of files to send with the message
        allowed_mentions: AllowedMentions | None
            The allowed_mentions object to send with the message
        ephemeral: bool
            Whether the message should be ephemeral or not, defaults to False
        suppress_embeds: bool
            Whether the message should suppress embeds or not, defaults to False
        poll: Poll | None
            The poll to send with the message
        """
        payload = _prepare_sending_payload(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            ephemeral=ephemeral,
            suppress_embeds=suppress_embeds,
            allowed_mentions=allowed_mentions,
            poll=poll,
        )
        resp = await self.inter.client.http.execute_webhook(
            self.inter.application_id, self.inter.token, payload
        )
        data = await resp.json()
        return FollowupResponse(data, self.inter)

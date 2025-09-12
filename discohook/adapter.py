from typing import TYPE_CHECKING, Any, Dict, List, Union

from .components import *
from .enums import InteractionCallbackType, InteractionType
from .errors import InteractionTypeMismatch
from .file import File
from .message import Message
from .modal import Modal
from .option import Choice
from .params import _prepare_payload
from .view import View

if TYPE_CHECKING:
    from .interaction import Interaction


class InteractionResponse:
    """
    Represents a response message sent by an interaction
    """

    def __init__(self, interaction: "Interaction") -> None:
        self.inter = interaction

    async def edit(
        self,
        *components: Union[
            TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container
        ],
    ):
        """
        Patches the response message.
        """
        resp = await self.inter.client.http.edit_webhook_message(
            self.inter.application_id,
            self.inter.token,
            "@original",
            _prepare_payload(View.from_children(*components)),
        )
        data = await resp.json()
        self.inter._responded = True
        return Message(self.inter.client, data)

    async def delete(self):
        """
        Deletes the response message.
        """
        await self.inter.client.http.delete_webhook_message(
            self.inter.application_id, self.inter.token, "@original"
        )


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
        *components: Union[
            TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container
        ],
    ):
        """
        Edits the followup response message.
        """
        resp = await self.interaction.client.http.edit_webhook_message(
            self.interaction.application_id,
            self.interaction.token,
            self.message.id,
            _prepare_payload(View.from_children(*components)),
        )
        data = await resp.json()
        self.message = Message(self.interaction.client, data)


class ResponseAdapter:
    """
    Interface for sending responses to interactions
    """

    def __init__(self, interaction: "Interaction") -> None:
        self.inter = interaction

    async def send(
        self,
        *components: Union[
            TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container
        ],
        with_response: bool = False,
        ephemeral: bool = False,
    ):
        await self.inter.client.http.create_interaction_response(
            self.inter.id,
            self.inter.token,
            _prepare_payload(
                View.from_children(*components),
                ephemeral=ephemeral,
                payload_type=InteractionCallbackType.channel_message_with_source,
            ),
            with_response=with_response,
        )
        self.inter._responded = True
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

    async def edit_origin(
        self,
        *components: Union[
            TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container
        ],
        with_response: bool = False,
    ) -> InteractionResponse:
        """
        Edits the original message of the interaction.
        Only available for buttons, select menus, and modal submission interactions.

        Parameters
        ----------
        *components:
            The components to include in the response message.
        with_response: bool
            Whether to return the original message as a response object.

        Returns
        -------
        InteractionResponse
            The response object containing the edited message.

        """
        if not (
            self.inter.type == InteractionType.component
            or self.inter.type == InteractionType.modal_submit
        ):
            raise InteractionTypeMismatch(
                f"Method not supported for {self.inter.type}", self.inter
            )

        payload = _prepare_payload(
            View.from_children(*components),
            payload_type=InteractionCallbackType.update_component_message,
        )
        self.inter._responded = True
        await self.inter.client.http.create_interaction_response(
            self.inter.id, self.inter.token, payload, with_response
        )
        return InteractionResponse(self.inter)

    async def followup(
        self,
        *components: Union[
            TextDisplay, Section, File, MediaGallery, ActionRow, Separator, Container
        ],
    ) -> FollowupResponse:
        """
        Sends a followup message to the interaction.

        Parameters
        ----------
        components:
            The components to include in the followup message.

        Returns
        -------
        FollowupResponse
            The followup response object containing the sent message.

        """
        payload = _prepare_payload(View.from_children(*components))
        resp = await self.inter.client.http.execute_webhook(
            self.inter.application_id, self.inter.token, payload
        )
        data = await resp.json()
        return FollowupResponse(data, self.inter)

from .embed import Embed
from .file import File
from .user import User
from .member import Member
from .view import View
from .modal import Modal
from .option import Choice
from .channel import PartialChannel
from fastapi.requests import Request
from .multipart import create_form
from .guild import Guild, PartialGuild
from .enums import InteractionType, InteractionCallbackType
from .message import Message, ResponseMessage, FollowupMessage
from typing import Any, Dict, Optional, List, Union, TYPE_CHECKING
from .params import handle_edit_params, handle_send_params, MISSING, merge_fields

if TYPE_CHECKING:
    from .client import Client


class CommandData:
    """
    Represents the data of a command interaction

    This is used internally by the library and should not be used by the user.
    """
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data["id"]
        self.name: str = data["name"]
        self.type: int = data["type"]
        self.guild_id: Optional[str] = data.get("guild_id")
        self.target_id: Optional[str] = data.get("target_id")
        self.resolved: Optional[Dict[str, Any]] = data.get("resolved")
        self.options: Optional[List[Dict[str, Any]]] = data.get("options")


class Interaction:
    """
    Base interaction class for all interactions

    Attributes
    ----------
    id: str
        The unique id of the interaction
    type: int
        The type of the interaction
    token: str
        The token of the interaction
    version: int
        The version of the interaction
    application_id: str
        The id of the application that the interaction was triggered for
    data: Optional[Dict[str, Any]]
        The command data payload (if the interaction is a command)
    guild_id: Optional[str]
        The guild id of the interaction
    channel_id: Optional[str]
        The channel id of the interaction
    app_permissions: Optional[int]
        The permissions of the application
    locale: Optional[str]
        The locale of the interaction
    guild_locale: Optional[str]
        The guild locale of the interaction
    
    Parameters
    ----------
    data: Dict[str, Any]
        The interaction data payload
    req: Request
        The request object from fastapi
    """
    def __init__(self, data: Dict[str, Any], req: Request):
        self._payload = data
        self.request: Request = req
        self.client: "Client" = req.app
        self.id: str = data["id"]
        self.type: int = data["type"]
        self.token: str = data["token"]
        self.version: int = data["version"]
        self.application_id: str = data["application_id"]
        self.data: Optional[Dict[str, Any]] = data.get("data")
        self.guild_id: Optional[str] = data.get("guild_id")
        self.channel_id: Optional[str] = data.get("channel_id")
        self.app_permissions: Optional[int] = data.get("app_permissions")
        self.locale: Optional[str] = data.get("locale")
        self.guild_locale: Optional[str] = data.get("guild_locale")

    @property
    def channel(self) -> PartialChannel:
        """
        The channel where the interaction was triggered

        Returns
        -------
        PartialChannel
        """
        return PartialChannel({"id": self.channel_id}, self.client)

    @property
    def author(self) -> Optional[Union[User, Member]]:
        """
        The author of the interaction

        If the interaction was triggered in a guild, this will return a member object else it will return user object.

        Returns
        -------
        Optional[Union[User, Member]]
        """
        member = self._payload.get("member")
        user = self._payload.get("user")
        if member:
            member.update(member.pop("user", {}))
            member["guild_id"] = self.guild_id
            return Member(member, self.client)
        else:
            return User(user, self.client)

    @property
    def partial_guild(self) -> Optional[PartialGuild]:
        if not self.guild_id:
            return
        return PartialGuild(self.guild_id, self.client)
    
    async def fetch_guild(self) -> Optional[Guild]:
        """
        Fetches the guild of the interaction

        Returns
        -------
        Guild
        """
        if self.guild_id:
            resp = await self.client.http.fetch_guild(self.guild_id)
            data = await resp.json()
            return Guild(data, self.client)

    async def send_modal(self, modal: Modal):
        """
        Sends a modal to the interaction

        Parameters
        ----------
        modal: Modal
            The modal to send
        """
        self.client.active_components[modal.custom_id] = modal
        payload = {
            "data": modal.to_dict(),
            "type": InteractionCallbackType.modal.value,
        }
        await self.client.http.send_modal(self.id, self.token, payload)

    async def send_autocomplete(self, choices: List[Choice]):
        """
        Sends autocomplete choices to the interaction

        Parameters
        ----------
        choices: List[Choice]
            The choices to send
        """
        payload = {
            "type": InteractionCallbackType.autocomplete_result.value,
            "data": {"choices": [choice.to_dict() for choice in choices]},
        }
        await self.client.http.send_interaction_callback(self.id, self.token, payload)

    async def defer(self, ephemeral: bool = False):
        """
        Defers the interaction

        Parameters
        ----------
        ephemeral: bool
            Whether the successive responses should be ephemeral or not
        """
        payload = {
            "type": InteractionCallbackType.deferred_channel_message_with_source.value,
        }
        if ephemeral:
            payload["data"] = {"flags": 64}
        await self.client.http.send_interaction_callback(self.id, self.token, payload)

    async def response(
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
    ) -> None:
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

        Notes
        -----
        Multipart files are not supported yet, will be added in the future.
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
            self.client.store_inter_token(self.id, self.token)
            self.client.load_components(view)

        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        files = merge_fields(file, files)
        await self.client.http.send_interaction_mp_callback(self.id, self.token, create_form(payload, files))

    async def follow_up(
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
    ) -> FollowupMessage:
        """
        Sends a follow-up message to a deferred interaction

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
            Whether the message should suppress embeds or not

        Notes
        -----
        Multipart files are not supported yet, will be added in the future.
        """
        payload = handle_send_params(
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
            self.client.store_inter_token(self.id, self.token)
            self.client.load_components(view)
        resp = await self.client.http.send_webhook_message(
            self.application_id, self.token, create_form(payload, merge_fields(file, files))
        )
        data = await resp.json()
        return FollowupMessage(data, self)

    async def original_response(self) -> ResponseMessage:
        """
        Gets the original response message of the interaction

        Returns
        -------
        ResponseMessage
            The original response message
        """
        resp = await self.client.http.fetch_original_webhook_message(self.application_id, self.token)
        data = await resp.json()
        return ResponseMessage(data, self)


class ComponentInteraction(Interaction):
    """
    Represents a component interaction subclassed from :class:`Interaction`
    """
    def __init__(self, data: Dict[str, Any], req: Request):
        super().__init__(data, req)

    @property
    def message(self) -> Optional[Message]:
        """
        The message that the component was clicked on

        Returns
        -------
        Optional[Message]
            The message that the component was clicked on
        """
        return Message(self._payload["message"], self.client)

    @property
    def originator(self) -> User:
        """
        The user that used the component

        Returns
        -------
        User
        """
        return User(self.message.interaction["user"], self.client)

    @property
    def from_originator(self) -> bool:
        """
        Whether the interaction was from the original author of the message

        Returns
        -------
        bool
        """
        return self.originator == self.author

    async def follow_up(
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
        suppress_embeds: Optional[bool] = False,
    ) -> FollowupMessage:
        """
        Sends a follow-up message to a deferred interaction

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
            Whether the message should suppress embeds or not
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
            self.client.store_inter_token(self.id, self.token)
            self.client.load_components(view)

        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        resp = await self.client.http.send_interaction_mp_callback(
            self.id, self.token, create_form(payload, merge_fields(file, files))
        )
        data = await resp.json()
        return FollowupMessage(data, self)

    async def edit_original(
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
    ):
        """
        Edits the original response message of the interaction

        Parameters
        ----------
        content: Optional[str]
            The edited content of the message
        embed: Optional[Embed]
            The edited embed of the message
        embeds: Optional[List[Embed]]
            The edited list of embeds of the message
        view: Optional[View]
            The edited view of the message
        tts: Optional[bool]
            Whether the message should be sent as tts or not
        file: Optional[File]
            The edited file of the message
        files: Optional[List[File]]
            The edited list of files of the message
        suppress_embeds: Optional[bool]
            Whether the message should suppress embeds or not
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
        if view is not MISSING and view:
            self.client.store_inter_token(self.id, self.token)
            self.client.load_components(view)

        payload = {
            "data": data,
            "type": InteractionCallbackType.update_message.value,
        }
        await self.client.http.edit_interaction_mp_callback(
            self.id, self.token, create_form(payload, merge_fields(file, files))
        )

    @property
    def origin(self) -> Optional[str]:
        """
        The original token of the interaction (if it is a follow up)

        Returns
        -------
        Optional[str]
        """
        if not self.message:
            return
        parent_id = self.message.interaction["id"]
        return self.client.cached_inter_tokens.get(parent_id, "")

    async def original_message(self) -> Optional[Message]:
        """
        Gets the original message of the interaction

        Returns
        -------
        Optional[Message]
        """
        if not self.origin:
            return
        resp = await self.client.http.fetch_original_webhook_message(self.application_id, self.origin)
        data = await resp.json()
        return Message(data, self.client)

    async def delete_original(self):
        """
        Deletes the original message of the interaction
        """
        if not self.origin:
            return
        self.client.cached_inter_tokens.pop(self.id, None)
        await self.client.http.delete_webhook_message(self.application_id, self.origin, "@original")


class CommandInteraction(Interaction):
    """
    Represents a command interaction, subclassed from :class:`Interaction`

    Attributes
    ----------
    data: Optional[CommandData]
        Raw data of the command
    """
    def __init__(self, data: Dict[str, Any], req: Request):
        super().__init__(data, req)

    @property
    def command_data(self) -> Optional[CommandData]:
        if self.type == InteractionType.app_command.value:
            return CommandData(self.data)
        return None

    async def response(
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
    ) -> None:
        """
        Sends a response to the interaction

        Parameters
        ----------
        content: Optional[str]
            The content of the message
        embed: Optional[Embed]
            The embed of the message
        embeds: Optional[List[Embed]]
            The list of embeds of the message
        view: Optional[View]
            The view of the message
        tts: Optional[bool]
            Whether the message should be sent as tts or not
        file: Optional[File]
            The file of the message
        files: Optional[List[File]]
            The list of files of the message
        ephemeral: Optional[bool]
            Whether the message should be ephemeral or not
        suppress_embeds: Optional[bool]
            Whether the message should suppress embeds or not
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
            self.client.store_inter_token(self.id, self.token)
            self.client.load_components(view)
        payload = {
            "data": data,
            "type": InteractionCallbackType.channel_message_with_source.value,
        }
        await self.client.http.send_interaction_mp_callback(
            self.id, self.token, create_form(payload, merge_fields(file, files))
        )

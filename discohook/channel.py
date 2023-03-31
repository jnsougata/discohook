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
    Represents a discord channel object.

    Attributes
    ----------
    id: :class:`str`
        The id of the channel.
    type: Optional[:class:`int`]
        The type of the channel.
    guild_id: Optional[:class:`str`]
        The id of the guild the channel belongs to.
    position: Optional[:class:`int`]
        The position of the channel.
    permission_overwrites: Optional[List[:class:`dict`]]
        A list of permission overwrites for the channel.
    name: Optional[:class:`str`]
        The name of the channel.
    topic: Optional[:class:`str`]
        The topic of the channel.
    nsfw: Optional[:class:`bool`]
        Whether the channel is nsfw.
    last_message_id: Optional[:class:`str`]
        The id of the last message sent in the channel.
    bitrate: Optional[:class:`int`]
        The bitrate of the channel if it is a voice channel.
    user_limit: Optional[:class:`int`]
        The user limit of the channel if it is a voice channel.
    rate_limit_per_user: Optional[:class:`int`]
        The rate limit per user of the channel if it is a text channel.
    recipients: Optional[List[:class:`dict`]]
        A list of recipients of the channel if it is a dm channel.
    icon: Optional[:class:`str`]
        The icon of the channel if it is a dm channel.
    owner_id: Optional[:class:`str`]
        The id of the owner of the channel if it is a dm channel.
    application_id: Optional[:class:`str`]
        The id of the application of the channel if it is a group dm channel.
    parent_id: Optional[:class:`str`]
        The id of the parent category of the channel.
    last_pin_timestamp: Optional[:class:`str`]
        The timestamp of the last pinned message in the channel.
    rtc_region: Optional[:class:`str`]
        The rtc region of the channel.
    video_quality_mode: Optional[:class:`int`]
        The video quality mode of the channel.
    message_count: Optional[:class:`int`]
        The message count of the channel.
    member_count: Optional[:class:`int`]
        The member count of the channel.
    thread_metadata: Optional[:class:`dict`]
        The thread metadata of the channel.
    member: Optional[:class:`dict`]
        The member of the channel.Appears in thread channels.
    default_auto_archive_duration: Optional[:class:`int`]
        The default auto archive duration of the channel.Appears in thread channels.
    permissions: Optional[:class:`str`]
        The permissions of the channel.
    flags: Optional[:class:`int`]
        The flags of the channel.
    total_message_sent: Optional[:class:`int`]
        The total message sent of the channel.
    available_tags: Optional[List[:class:`str`]]
        A list of available tags of the channel.Appears in thread channels.
    default_reaction_emoji: Optional[:class:`dict`]
        The default reaction emoji of the channel.Appears in thread channels.
    default_thread_rate_limit_per_user: Optional[:class:`int`]
        The default rate limit per user of the channel.Appears in thread channels.
    default_sort_order: Optional[:class:`int`]
        The default sort order of the channel.Appears in forum channels.
    default_forum_layout: Optional[:class:`int`]
        The default channel layout of the channel.Appears in forum channels.

    """
    def __init__(self, data: dict, client: "Client"):
        super().__init__(data, client)
        self.type = data.get("type")
        self.guild_id = data.get("guild_id")
        self.position = data.get("position")
        self.permission_overwrites = data.get("permission_overwrites")
        self.name = data.get("name")
        self.topic = data.get("topic")
        self.nsfw = data.get("nsfw")
        self.last_message_id = data.get("last_message_id")
        self.bitrate = data.get("bitrate")
        self.user_limit = data.get("user_limit")
        self.rate_limit_per_user = data.get("rate_limit_per_user")
        self.recipients = data.get("recipients")
        self.icon = data.get("icon")
        self.owner_id = data.get("owner_id")
        self.application_id = data.get("application_id")
        self.managed = data.get("managed")
        self.parent_id = data.get("parent_id")
        self.last_pin_timestamp = data.get("last_pin_timestamp")
        self.rtc_region = data.get("rtc_region")
        self.video_quality_mode = data.get("video_quality_mode")
        self.message_count = data.get("message_count")
        self.member_count = data.get("member_count")
        self.thread_metadata = data.get("thread_metadata")
        self.member = data.get("member")
        self.default_auto_archive_duration = data.get("default_auto_archive_duration")
        self.permissions = data.get("permissions")
        self.flags = data.get("flags")
        self.total_message_sent = data.get("total_message_sent")
        self.available_tags = data.get("available_tags")
        self.applied_tags = data.get("applied_tags")
        self.default_reaction_emoji = data.get("default_reaction_emoji")
        self.default_thread_rate_limit_per_user = data.get("default_thread_rate_limit_per_user")
        self.default_sort_order = data.get("default_sort_order")
        self.default_forum_layout = data.get("default_forum_layout")

    def __eq__(self, other):
        return self.id == other.id

    @property
    def mention(self) -> str:
        """
        Returns the channel-mentionable string.

        Returns
        -------
        :class:`str`
        """
        return f"<#{self.id}>"

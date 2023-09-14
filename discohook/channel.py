from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .embed import Embed
from .emoji import PartialEmoji
from .enums import ChannelType
from .file import File
from .message import Message
from .models import AllowedMentions, MessageReference
from .multipart import create_form
from .params import handle_send_params, merge_fields
from .view import View

if TYPE_CHECKING:
    from .client import Client


class PartialChannel:
    """
    Represents a partial discord channel object.

    Parameters
    ----------
    channel_id: str
        The channel's ID.
    guild_id: str | None
        The guild's ID.
    client: :class:`Client`
        The client that the channel belongs to.
    """

    def __init__(self, client: "Client", channel_id: str, guild_id: Optional[str] = None):
        self.client = client
        self.id: str = channel_id
        self.guild_id = guild_id

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
        allowed_mentions: Optional[AllowedMentions] = None,
        message_reference: Optional[MessageReference] = None,
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
        allowed_mentions: Optional[:class:`AllowedMentions`]
            The allowed mentions for the message.
        message_reference: Optional[:class:`MessageReference`]
            The message reference for the message.
        """
        if view:
            self.client.load_components(view)

        payload = handle_send_params(
            content=content,
            embed=embed,
            embeds=embeds,
            view=view,
            tts=tts,
            file=file,
            files=files,
            allowed_mentions=allowed_mentions,
            message_reference=message_reference,
        )

        resp = await self.client.http.send_message(self.id, create_form(payload, merge_fields(file, files)))
        data = await resp.json()
        return Message(self.client, data)

    async def edit(
        self,
        *,
        name: Optional[str] = None,
        kind: Optional[ChannelType] = None,
        position: Optional[int] = None,
        topic: Optional[str] = None,
        nsfw: Optional[bool] = None,
        rate_limit_per_user: Optional[int] = None,
        bitrate: Optional[int] = None,
        user_limit: Optional[int] = None,
        permission_overwrites: Optional[List[Dict[str, Any]]] = None,
        parent_id: Optional[str] = None,
        rtc_region: Optional[str] = None,
        video_quality_mode: Optional[int] = None,
        default_auto_archive_duration: Optional[int] = None,
        flags: Optional[int] = None,
        available_tags: Optional[List[Dict[str, Any]]] = None,
        icon: Optional[str] = None,
        default_reaction_emoji: Optional[PartialEmoji] = None,
        default_thread_rate_limit_per_user: Optional[int] = None,
        default_sort_order: Optional[int] = None,
        default_forum_layout: Optional[int] = None,
    ) -> "Channel":
        """
        Edits all kinds of channels.

        Parameters
        ----------
        name: Optional[:class:`str`]
            The new name of the channel.
        kind: Optional[:class:`ChannelType`]
            The new type of the channel.
        position: Optional[:class:`int`]
            The new position of the channel.
        topic: Optional[:class:`str`]
            The new topic of the channel.
        nsfw: Optional[:class:`bool`]
            Whether the channel should be marked as nsfw.
        rate_limit_per_user: Optional[:class:`int`]
            The duration of the slowmode in seconds. Must be between 0 and 21600. Applies to text and forum channels.
        bitrate: Optional[:class:`int`]
            The new bitrate of the channel. Must be between 8000 and 96000. Applies to voice channels.
        user_limit: Optional[:class:`int`]
            The new user limit of the channel. Must be between 0 and 99. Applies to voice channels.
        permission_overwrites: Optional[List[:class:`dict`]]
            A list of permission overwrites to apply to the channel. Applies to all channel types.
        parent_id: Optional[:class:`str`]
            The id of the parent category to move the channel to. Applies to all channel types.
        rtc_region: Optional[:class:`str`]
            The new region of the channel. Applies to voice channels.
        video_quality_mode: Optional[:class:`int`]
            The new video quality mode of the channel. Applies to voice channels.
        default_auto_archive_duration: Optional[:class:`int`]
            The new default auto archive duration of the channel. Applies to text and forum channels.
        flags: Optional[:class:`int`]
            The new flags of the channel. Applies to all channel types.
        available_tags: Optional[List[:class:`dict`]]
            The new available tags of the channel. Applies to text and forum channels.
        icon: Optional[:class:`str`]
            The new icon of the channel. Applies to Group DMs. Must be a base64 encoded string.
        default_reaction_emoji: Optional[:class:`PartialEmoji`]
            The new default reaction emoji of the channel. Applies to text and forum channels.
        default_thread_rate_limit_per_user: Optional[:class:`int`]
            The new default thread rate limit per user of the channel. Applies to text and forum channels.
        default_sort_order: Optional[:class:`int`]
            The new default sort order of the channel. Applies to text and forum channels.
        default_forum_layout: Optional[:class:`int`]
            The new default forum layout of the channel. Applies to text and forum channels.

        Returns
        -------
        :class:`Channel`
            The edited channel.
        """
        payload = {}
        if name:
            payload["name"] = name
        if kind:
            payload["type"] = kind
        if position:
            payload["position"] = position
        if topic:
            payload["topic"] = topic
        if nsfw:
            payload["nsfw"] = nsfw
        if rate_limit_per_user:
            payload["rate_limit_per_user"] = rate_limit_per_user
        if bitrate:
            payload["bitrate"] = bitrate
        if user_limit:
            payload["user_limit"] = user_limit
        if permission_overwrites:
            payload["permission_overwrites"] = permission_overwrites
        if parent_id:
            payload["parent_id"] = parent_id
        if rtc_region:
            payload["rtc_region"] = rtc_region
        if video_quality_mode:
            payload["video_quality_mode"] = video_quality_mode
        if default_auto_archive_duration:
            payload["default_auto_archive_duration"] = default_auto_archive_duration
        if flags:
            payload["flags"] = flags
        if available_tags:
            payload["available_tags"] = available_tags
        if icon:
            payload["icon"] = icon
        if default_reaction_emoji:
            payload["default_reaction_emoji"] = default_reaction_emoji.to_dict()
        if default_thread_rate_limit_per_user:
            payload["default_thread_rate_limit_per_user"] = default_thread_rate_limit_per_user
        if default_sort_order:
            payload["default_sort_order"] = default_sort_order
        if default_forum_layout:
            payload["default_forum_layout"] = default_forum_layout
        resp = await self.client.http.edit_channel(self.id, payload)
        data = await resp.json()
        return Channel(self.client, data)

    async def fetch_message(self, message_id: str) -> Optional[Message]:
        """
        Fetches a message from the channel.

        Parameters
        ----------
        message_id: :class:`str`
            The id of the message to fetch.

        Returns
        -------
        :class:`Message`
            The fetched message.
        """
        resp = await self.client.http.fetch_channel_message(self.id, message_id)
        data = await resp.json()
        return Message(self.client, data)

    async def fetch_messages(
        self,
        limit: int = 50,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        around: Optional[str] = None,
    ) -> List[Message]:
        """
        Fetches messages from the channel.

        Parameters
        ----------
        limit: Optional[:class:`int`]
            The maximum amount of messages to fetch.
        before: Optional[:class:`str`]
            The id of the message to fetch before.
        after: Optional[:class:`str`]
            The id of the message to fetch after.
        around: Optional[:class:`str`]
            The id of the message to fetch around.

        Returns
        -------
        List[:class:`Message`]
            The fetched messages.
        """
        params = {"limit": limit}
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if around:
            params["around"] = around
        resp = await self.client.http.fetch_channel_messages(self.id, params=params)
        data = await resp.json()
        return [Message(self.client, msg) for msg in data]

    async def purge(
        self,
        limit: int = 50,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        around: Optional[str] = None,
    ) -> List[Message]:
        """
        Deletes messages from the channel in bulk.

        Parameters
        ----------
        limit: Optional[:class:`int`]
            The maximum amount of messages to delete.
        before: Optional[:class:`str`]
            The id of the message to delete before.
        after: Optional[:class:`str`]
            The id of the message to delete after.
        around: Optional[:class:`str`]
            The id of the message to delete around.

        Returns
        -------
        List[:class:`Message`]
            The deleted messages.
        """
        messages = await self.fetch_messages(limit=limit, before=before, after=after, around=around)
        ids = [msg.id for msg in messages]
        if len(ids) < 2:
            await self.client.http.delete_channel_message(self.id, ids[0])
            return messages
        await self.client.http.delete_channel_messages(self.id, {"messages": ids})
        return messages

    async def delete(self):
        await self.client.http.delete_channel(self.id)

    async def crosspost(self, message_id: str):
        resp = await self.client.http.crosspost_channel_message(self.id, message_id)
        data = await resp.json()
        return Message(self.client, data)


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

    def __init__(self, client: "Client", data: dict):
        super().__init__(client, data["id"], data.get("guild_id"))
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

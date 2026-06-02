from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

import aiohttp

from .components import TopLevelComponent
from .emoji import PartialEmoji
from .enums import ChannelType
from .message import Message
from .params import _prepare_payload
from .view import View

if TYPE_CHECKING:
    from .client import Client


class PartialChannel:
    """
    Represents a partial discord channel object.

    Args:
        channel_id (str): ID of the channel.
        guild_id (str | None): Guild id of the channel.
        client (Client): Client that the channel belongs to.
    """

    def __init__(
        self, client: "Client", channel_id: str, guild_id: Optional[str] = None
    ):
        self.client = client
        self.id: str = channel_id
        self.guild_id = guild_id

    def __eq__(self, other):
        return self.id == other.id

    @property
    def mention(self) -> str:
        """
        Builds channel mention formatting.

        Returns:
            str: String representation of the channel mention.
        """
        return f"<#{self.id}>"

    async def send(self, *components: TopLevelComponent):
        """
        Sends a message to the channel.

        Args:
            components (Tuple(TopLevelComponent)): The components to send in the message.

        Returns:
            Message: Message object returned by the API.
        """

        payload = _prepare_payload(View.from_children(*components))
        resp = await self.client.http.create_message(self.id, payload)
        data = await resp.json()
        return Message(self.client, data)

    # noinspection PyShadowingBuiltins
    async def edit(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[ChannelType] = None,
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
        reason: Optional[str] = None,
    ) -> "Channel":
        """
        Edits all kinds of channels.

        Args:
            name (str | None): Updated name of the channel.
            type (ChannelType): Updated type of the channel.
            position (int | None): Updated position of the channel.
            topic (str | None): Updated topic of the channel.
            nsfw (bool | None): Whether the channel should be marked as NSFW.
            rate_limit_per_user (int | None): Updated rate limit per user.
                Must be between 0 and 21600. Applies to text and forum channels.
            bitrate (int | None): Updated bitrate of the channel.
                Must be between 8000 and 96000. Applies to voice channels.
            user_limit (int | None): Updated user limit of the channel.
                Must be between 0 and 99. Applies to voice channels.
            permission_overwrites (List[dict] | None): Updated list permission overwrites to apply.
            parent_id (str | None): ID of the parent category to move the channel to.
            rtc_region (str | None): Updated region of the channel. Applies to voice channels.
            video_quality_mode (int | None): New video quality mode of the channel. Applies to voice channels.
            default_auto_archive_duration (int | None): Updated default auto archive duration of the channel.
                Applies to text and forum channels.
            flags (int | None): Updated flags of the channel. Applies to all channel types.
            available_tags (List[dict] | None): Updated available tags of the channel.
                Applies to text and forum channels.
            icon (str | None): Updated icon of the channel. Applies to Group DMs. Must be a base64 encoded string.
            default_reaction_emoji (PartialEmoji | None): Updated default reaction emoji of the channel.
                Applies to text and forum channels.
            default_thread_rate_limit_per_user (int | None): Updated default thread rate limit per user of the channel.
                Applies to text and forum channels.
            default_sort_order (int | None): Updated default sort order of the channel.
                Applies to text and forum channels.
            default_forum_layout (int | None): Updated default forum layout of the channel.
                Applies to text and forum channels.
            reason (str | None): The reason for the edit. This will be shown in the audit log.

        Returns:
            Channel: Updated channel.
        """
        payload = {}
        if name:
            payload["name"] = name
        if type:
            payload["type"] = type
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
            payload["default_thread_rate_limit_per_user"] = (
                default_thread_rate_limit_per_user
            )
        if default_sort_order:
            payload["default_sort_order"] = default_sort_order
        if default_forum_layout:
            payload["default_forum_layout"] = default_forum_layout
        resp = await self.client.http.modify_channel(self.id, payload, reason=reason)
        data = await resp.json()
        return Channel(self.client, data)

    async def fetch_message(self, message_id: str) -> Optional[Message]:
        """
        Fetches a message by its id from the channel.

        Args:
            message_id (str): The id of the message to fetch.

        Returns:
            Message: Message fetched from the channel.
        """
        resp = await self.client.http.get_channel_message(self.id, message_id)
        data = await resp.json()
        return Message(self.client, data)

    async def fetch_messages(
        self,
        limit: int = 50,
        *,
        around: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
    ) -> List[Message]:
        """
        Fetch multiple messages from the channel.

        Args:
            limit (int): Maximum number of messages to fetch.
            around (str): ID of the message to fetch around.
            before (str): ID of the message to fetch before.
            after (str): ID of the message to fetch after.

        Returns:
            List[Message]: Messages fetched from the channel.
        """
        params = {"limit": limit}
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if around:
            params["around"] = around
        resp = await self.client.http.get_channel_messages(self.id, **params)
        data = await resp.json()
        return [Message(self.client, msg) for msg in data]

    async def purge(
        self,
        limit: int = 50,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        around: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> List[Message]:
        """
        Delete messages from the channel in bulk.

        Args:
            limit (int): Maximum number of messages to purge.
            around (str): ID of the message to purge around.
            before (str): ID of the message to purge before.
            after (str): ID of the message to purge after.
            reason (str): The reason for the purge. This will be shown in the audit log.

        Returns:
            List[Message]: Messages purged from the channel.
        """
        messages = await self.fetch_messages(
            limit=limit, before=before, after=after, around=around
        )
        ids = [msg.id for msg in messages]
        if len(ids) < 2:
            await self.client.http.delete_message(self.id, ids[0], reason=reason)
            return messages
        await self.client.http.bulk_delete_messages(
            self.id, {"messages": ids}, reason=reason
        )
        return messages

    async def delete(self, *, reason: Optional[str] = None):
        """
        Deletes the channel.

        Args:
            reason (str): The reason for the purge. This will be shown in the audit log.
        """
        await self.client.http.delete_or_close_channel(self.id, reason=reason)

    async def crosspost(self, message_id: str):
        """
        Crosspost a message in the channel.

        Args:
            message_id (str): The id of the message to crosspost.

        Returns:
            Message: Message crossposted from the channel.
        """
        resp = await self.client.http.crosspost_message(self.id, message_id)
        data = await resp.json()
        return Message(self.client, data)

    async def start_thread(
        self,
        name: str,
        *,
        auto_archive_duration: int = 60,
        invitable: bool = True,
        rate_limit_per_user: int = 0,
        reason: Optional[str] = None,
    ) -> "Channel":
        """
        Creates a thread from the channel.

        Args:
            name (str): Name of the thread.
            auto_archive_duration (int): The duration in minutes to automatically archive the thread.
                Defaults to 60.
            invitable (bool): Whether non-moderators can add other non-moderators to the thread.
                Defaults to True.
            rate_limit_per_user (int): Amount of seconds a user has to wait before
                sending another message (0-21600). Defaults to 0.
            reason (str | None): The reason for the action. This will be shown in the audit log.

        Returns:
            Channel: Thread channel.
        """
        payload = {
            "name": name,
            "auto_archive_duration": auto_archive_duration,
            "type": ChannelType.private_thread,
            "invitable": invitable,
            "rate_limit_per_user": rate_limit_per_user,
        }
        resp = await self.client.http.start_thread_without_message(
            self.id, payload, reason=reason
        )
        data = await resp.json()
        return Channel(self.client, data)

    async def fetch_webhooks(self):
        return await self.client.http.fetch_channel_webhooks(self.id)


class Channel(PartialChannel):
    """
    Represents a discord channel object.

    Attributes:
        id (str): ID of the channel.
        type (int): Type of the channel.
        guild_id (str): ID of the guild the channel belongs to.
        position (int): Position of the channel in the guild.
        permission_overwrites (List[dict]): A list of permission overwrites for the channel.
        name (str): Name of the channel.
        topic (str): Topic of the channel.
        nsfw (bool): Whether the channel is NSFW.
        last_message_id (str): ID of the last message sent in the channel.
        bitrate (int): Bitrate of the channel if it is a voice channel.
        user_limit (int): User limit of the channel if it is a voice channel.
        rate_limit_per_user (int): Rate limit per user of the channel if it is a text channel.
        recipients (List[dict]): A list of recipients of the channel if it is a DM channel.
        icon (str): Icon of the channel if it is a DM channel.
        owner_id (str): ID of the owner of the channel if it is a DM channel.
        application_id (str): ID of the application of the channel if it is a group DM channel.
        parent_id (str): ID of the parent category of the channel.
        last_pin_timestamp (str): Timestamp of the last pinned message in the channel.
        rtc_region (str): RTC region of the channel.
        video_quality_mode (int): Video quality mode of the channel.
        message_count (int): Message count of the channel.
        member_count (int): Member count of the channel.
        thread_metadata (dict): Thread metadata of the channel.
        member (dict): Member of the channel. Appears in thread channels.
        default_auto_archive_duration (int): Default auto archive duration of the channel. Appears in thread channels.
        permissions (str): Permissions of the channel.
        flags (int): Flags of the channel.
        total_message_sent (int): Total message sent of the channel.
        available_tags (List[str]): A list of available tags of the channel. Appears in thread channels.
        default_reaction_emoji (dict): Default reaction emoji of the channel. Appers in thread channels.
        default_thread_rate_limit_per_user (int): Default rate limit per user of the channel. Appears in thread channels.
        default_sort_order (int): Default sort order of the channel. Appears in forum channels.
        default_forum_layout (int): Default channel layout of the channel. Appears in forum channels.
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
        self.default_thread_rate_limit_per_user = data.get(
            "default_thread_rate_limit_per_user"
        )
        self.default_sort_order = data.get("default_sort_order")
        self.default_forum_layout = data.get("default_forum_layout")

    @classmethod
    async def from_response(cls, client: "Client", response: aiohttp.ClientResponse):
        """
        Create a channel object from an aiohttp response.

        Args:
            client (Client): Client object.
            response (aiohttp.ClientResponse): Response to create the channel from.

        Returns:
            Channel: Channel object.
        """
        return cls(client, await response.json())

    @classmethod
    def from_dict(cls, client: "Client", data: dict):
        """
        Create a channel object from a dictionary.

        Args:
            client (Client): Client object.
            data (dict): Dictionary to create the channel from.

        Returns:
            Channel: Channel object.
        """
        return cls(client, data)

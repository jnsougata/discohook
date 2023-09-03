from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .asset import Asset
from .embed import Embed
from .file import File
from .multipart import create_form
from .params import handle_send_params, merge_fields

if TYPE_CHECKING:
    from .client import Client


class User:
    """
    Represents a discord user.

    Properties
    ----------
    id: :class:`str`
        The unique ID of the user.
    name: :class:`str`
        The name of the user.
    discriminator: :class:`str`
        The discriminator of the user.
    accent_color: Optional[:class:`int`]
        The accent color of the user.
    avatar: :class:`Asset`
        The avatar of the user.
    system: :class:`bool`
        Whether the user is a system user.
    bot: :class:`bool`
        Whether the user is a bot.
    mfa_enabled: :class:`bool`
        Whether the user has MFA enabled.
    locale: Optional[:class:`str`]
        The locale of the user.
    verified: :class:`bool`
        Whether the user is verified.
    email: Optional[:class:`str`]
        The email of the user.
    premium_type: Optional[:class:`int`]
        The premium type of the user.
    public_flags: Optional[:class:`int`]
        The public flags of the user.
    mention: :class:`str`
        Returns a string that allows you to mention the user.
    """

    def __init__(self, client: "Client", data: Dict[str, Any]):
        self.data = data
        self.client = client

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def name(self) -> str:
        return self.data["username"]

    @property
    def global_name(self) -> Optional[str]:
        return self.data.get("global_name")

    @property
    def discriminator(self) -> int:
        return int(self.data["discriminator"])

    @property
    def accent_color(self) -> Optional[int]:
        return self.data.get("accent_color")

    @property
    def avatar(self) -> Asset:
        av_hash = self.data.get("avatar")
        if av_hash:
            return Asset(hash=av_hash, fragment=f"avatars/{self.id}")
        if self.discriminator == 0:
            av_hash = str({(int(self.id) >> 22) % 6})
        else:
            av_hash = str(int(self.discriminator) % 5)
        return Asset(hash=av_hash, fragment="embed/avatars")

    @property
    def system(self) -> bool:
        return self.data.get("system", False)

    @property
    def bot(self) -> bool:
        return self.data.get("bot", False)

    @property
    def mfa_enabled(self) -> bool:
        return self.data.get("mfa_enabled", False)

    @property
    def locale(self) -> Optional[str]:
        return self.data.get("locale")

    @property
    def verified(self) -> bool:
        return self.data.get("verified", False)

    @property
    def email(self) -> Optional[str]:
        return self.data.get("email")

    @property
    def premium_type(self) -> Optional[int]:
        return self.data.get("premium_type")

    @property
    def public_flags(self) -> Optional[int]:
        return self.data.get("public_flags")

    def __str__(self) -> str:
        if self.discriminator == 0:
            return self.global_name or self.name
        return f"{self.name}#{self.discriminator}"

    def __eq__(self, other):
        return self.id == other.id

    @property
    def mention(self) -> str:
        return f"<@{self.id}>"

    async def send(
        self,
        content: str,
        *,
        tts: bool = False,
        embed: Optional[Embed] = None,
        embeds: Optional[List[Embed]] = None,
        file: Optional[File] = None,
        files: Optional[List[File]] = None,
    ) -> Dict[str, Any]:
        """
        Sends a message to the user.

        Parameters
        ----------
        content: :class:`str`
            The content of the message.
        tts: :class:`bool`
            Whether the message should be sent using text-to-speech.
        embed: Optional[:class:`Embed`]
            The embed to be sent with the message.
        embeds: Optional[:class:`List`[:class:`Embed`]`]
            The embeds to be sent with the message.
        file: Optional[:class:`File`]
            The file to be sent with the message.
        files: Optional[:class:`List`[:class:`File`]`]
            The files to be sent with the message.
        """
        payload = handle_send_params(
            content=content,
            tts=tts,
            embed=embed,
            embeds=embeds,
            file=file,
            files=files,
        )
        resp = await self.client.http.create_dm_channel({"recipient_id": self.id})
        data = await resp.json()
        channel_id = data["id"]
        resp = await self.client.http.send_message(channel_id, create_form(payload, merge_fields(file, files)))
        return await resp.json()

from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client


class Guild:

    def __init__(self, data: Dict[str, Any], state: "Client") -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.icon = data.get("icon")
        self.icon_hash = data.get("icon_hash")
        self.splash = data.get("splash")
        self.discovery_splash = data.get("discovery_splash")
        self.owner = data.get("owner")
        self.owner_id = data["owner_id"]
        self.permissions = data.get("permissions")
        self.afk_channel_id = data.get("afk_channel_id")
        self.afk_timeout = data["afk_timeout"]
        self.widget_enabled = data.get("widget_enabled")
        self.widget_channel_id = data.get("widget_channel_id")
        self.verification_level = data["verification_level"]
        self.default_message_notifications = data["default_message_notifications"]
        self.explicit_content_filter = data["explicit_content_filter"]
        self.roles = data["roles"]
        self.emojis = data["emojis"]
        self.features = data["features"]
        self.mfa_level = data["mfa_level"]
        self.application_id = data.get("application_id")
        self.system_channel_id = data.get("system_channel_id")
        self.system_channel_flags = data["system_channel_flags"]
        self.rules_channel_id = data.get("rules_channel_id")
        self.max_presences = data.get("max_presences")
        self.max_members = data.get("max_members")
        self.vanity_url_code = data.get("vanity_url_code")
        self.description = data.get("description")
        self.banner = data.get("banner")
        self.premium_tier = data["premium_tier"]
        self.premium_subscription_count = data.get("premium_subscription_count")
        self.preferred_locale = data["preferred_locale"]
        self.public_updates_channel_id = data.get("public_updates_channel_id")
        self.max_video_channel_users = data.get("max_video_channel_users")
        self.approximate_member_count = data.get("approximate_member_count")
        self.approximate_presence_count = data.get("approximate_presence_count")
        self.welcome_screen = data.get("welcome_screen")
        self.nsfw_level = data["nsfw_level"]
        self.stickers = data.get("stickers")
        self.premium_progress_bar_enabled = data["premium_progress_bar_enabled"]
        self.state = state


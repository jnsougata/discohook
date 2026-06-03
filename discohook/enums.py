from enum import Enum

__all__ = (
    "ApplicationCommandOptionType",
    "ApplicationCommandType",
    "ButtonStyle",
    "ChannelType",
    "InteractionCallbackType",
    "InteractionType",
    "ComponentType",
    "ModalFieldType",
    "SelectType",
    "TextInputFieldLength",
    "AllowedMentionsType",
    "try_enum",
    "SelectDefaultValueType",
    "InteractionContextType",
    "ApplicationIntegrationType",
    "PollLayoutType",
)


def try_enum(enum_class, value):
    try:
        return enum_class(value)
    except ValueError:
        return None


class TextInputFieldLength(int, Enum):
    """
    Length of a text input field for a modal.

    Attributes:
        short (int): Used to specify a short text input field.
        long (int): Used to specify a long text input field.
    """

    short = 1
    long = 2


class ModalFieldType(int, Enum):
    """
    Type of field in a modal.
    Used internally by the library. You should not need to use this.

    Attributes:
        text_input (int): Used to specify a text input field.
    """

    text_input = 4


class ApplicationCommandType(int, Enum):
    """
    Type of application command.

    Attributes:
        slash (int): Used to specify a slash command.
        user (int): Used to specify a user command.
        message (int): Used to specify a message command.
    """

    slash = 1
    user = 2
    message = 3
    primary_entry_point = 4


class ApplicationCommandOptionType(int, Enum):
    """
    Type of application command option.
    Used internally by the library. You should not need to use this.
    """

    subcommand = 1
    subcommand_groups = 2
    string = 3
    integer = 4
    boolean = 5
    user = 6
    channel = 7
    role = 8
    mentionable = 9
    number = 10
    attachment = 11


class ChannelType(int, Enum):
    """
    Use to specify discord channel type in application command Option.

    Attributes:
        guild_text (int): Used to specify a guild text channel.
        dm (int): Used to specify a dm channel.
        guild_voice (int): Used to specify a guild voice channel.
        group_dm (int): Used to specify a group dm channel.
        guild_category (int): Used to specify a guild category channel.
        guild_announcement (int): Used to specify a guild announcement channel.
        guild_announcement_thread (int): Used to specify a guild announcement thread channel.
        public_thread (int): Used to specify a guild public thread channel.
        private_thread (int): Used to specify a guild private thread channel.
        guild_stage_voice (int): Used to specify a guild stage voice channel.
        guild_directory (int): Used to specify a guild directory channel.
        guild_forum (int): Used to specify a guild forum channel.
        guild_media (int): Used to specify a guild media channel.
    """

    guild_text = 0
    dm = 1
    guild_voice = 2
    group_dm = 3
    guild_category = 4
    guild_announcement = 5
    guild_announcement_thread = 10
    public_thread = 11
    private_thread = 12
    guild_stage_voice = 13
    guild_directory = 14
    guild_forum = 15
    guild_media = 16


class InteractionType(int, Enum):
    """
    Type of interaction received from discord.
    Used internally by the library. You should not need to use this.
    """

    ping = 1
    app_command = 2
    component = 3
    autocomplete = 4
    modal_submit = 5


class InteractionCallbackType(int, Enum):
    """
    Type of interaction callback.
    Used internally by the library. You should not need to use this.
    """

    pong = 1
    channel_message_with_source = 4
    deferred_channel_message_with_source = 5
    deferred_update_component_message = 6
    update_component_message = 7
    autocomplete = 8
    modal = 9
    premium_required = 10
    launch_activity = 12


class ComponentType(int, Enum):
    """
    Type of message component.
    Used internally by the library. You should not need to use this.
    """

    action_row = 1
    button = 2
    string_select = 3
    text_input = 4
    user_select = 5
    role_select = 6
    mentionable_select = 7
    channel_select = 8
    section = 9
    text_display = 10
    thumbnail = 11
    media_gallery = 12
    file = 13
    separator = 14
    container = 17
    label = 18
    file_upload = 19
    radio_group = 21
    checkbox_group = 22
    checkbox = 23


class SelectType(int, Enum):
    """
    The type of select menu.

    Attributes:
        text (int): Used to specify a text select menu.
        user (int): Used to specify a user select menu.
        role (int): Used to specify a role select menu.
        mentionable (int): Used to specify a mentionable select menu.
        channel (int): Used to specify a channel select menu.
    """

    text = 3
    user = 5
    role = 6
    mentionable = 7
    channel = 8


class ButtonStyle(int, Enum):
    """
    Represents the style of a button.

    Attributes:
        blurple (int): Used to specify a blurple button.
        gray (int): Used to specify a gray button.
        green (int): Used to specify a green button.
        red (int): Used to specify a red button.
        link (int): Used to specify a link type button.
    """

    blurple = 1
    gray = 2
    green = 3
    red = 4
    link = 5


class WebhookType(int, Enum):
    """
    Type of webhook.
    Used internally by the library. You should not need to use this.
    """

    incoming = 1
    channel_follower = 2
    application = 3


class AllowedMentionsType(str, Enum):
    """
    The type of mentions allowed in a message.

    Attributes:
        roles (int): Used to specify a role mentions allowed in a message.
        users (int): Used to specify a user mentions allowed in a message.
        everyone (int): Used to specify everyone mentions allowed in a message.
    """

    roles = "roles"
    users = "users"
    everyone = "everyone"


class SelectDefaultValueType(str, Enum):
    """
    Type of default values for a select menu.

    Attributes:
        user (str): Used to specify a user default value for a select menu.
        role (str): Used to specify a role default value for a select menu.
        channel (str): Used to specify a channel default value for a select menu.
    """

    user = "user"
    role = "role"
    channel = "channel"


class InteractionContextType(int, Enum):
    """
    Type of interaction context.

    Attributes:
        guild (int): Used to specify a guild context.
        bot_dm (int): Used to specify a bot dm context.
        private_channel (int): Used to specify a private channel context.
    """

    guild = 0
    bot_dm = 1
    private_channel = 2


class ApplicationIntegrationType(int, Enum):
    """
    Installation context(s) where the command is available.

    Attributes:
        guild (int): Used to specify a guild context.
        user (int): Used to specify a user context.
    """

    guild = 0
    user = 1


class PollLayoutType(int, Enum):
    """
    Type of layout for a poll.

    Attributes:
        default (int): Used to specify a default layout for a poll.
    """

    default = 1

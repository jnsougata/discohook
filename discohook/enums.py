from enum import Enum


def try_enum(enum_class, value):
    try:
        return enum_class(value)
    except ValueError:
        return None


class TextInputFieldLength(Enum):
    """
    The length of a text input field for a modal.

    Attributes
    ----------
    short: :class:`int`
        Used to specify a short length text input field (up to 100 characters).
    long: :class:`int`
        Used to specify a long length text input field (up to 3000 characters).
    """
    short = 1
    long = 2


class ModalFieldType(Enum):
    """
    The type of field in a modal.

    Used internally by the library. You should not need to use this.

    Attributes
    ----------
    text_input: :class:`int`
        Used to specify a text input field.
    """
    text_input = 4


class ApplicationCommandType(Enum):
    """
    The type of application command.

    Attributes
    ----------
    slash: :class:`int`
        Used to specify a slash command.
    user: :class:`int`
        Used to specify a user command.
    message: :class:`int`
        Used to specify a message command.
    """
    slash = 1
    user = 2
    message = 3


class ApplicationCommandOptionType(Enum):
    """
    The type of application command option.

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


class ChannelType(Enum):
    """
    Use to specify discord channel type in application command Option.

    Attributes
    ----------
    guild_text: :class:`int`
        Used to specify a guild text channel.
    dm: :class:`int`
        Used to specify a dm channel.
    guild_voice: :class:`int`
        Used to specify a guild voice channel.
    group_dm: :class:`int`
        Used to specify a group dm channel.
    guild_category: :class:`int`
        Used to specify a guild category channel.
    guild_news: :class:`int`
        Used to specify a guild news channel.
    guild_store: :class:`int`
        Used to specify a guild store channel.
    guild_news_thread: :class:`int`
        Used to specify a guild news thread channel.
    guild_public_thread: :class:`int`
        Used to specify a guild public thread channel.
    guild_private_thread: :class:`int`
        Used to specify a guild private thread channel.
    guild_stage_voice: :class:`int`
        Used to specify a guild stage voice channel.
    """
    guild_text = 0
    dm = 1
    guild_voice = 2
    group_dm = 3
    guild_category = 4
    guild_news = 5
    guild_store = 6
    guild_news_thread = 10
    guild_public_thread = 11
    guild_private_thread = 12
    guild_stage_voice = 13


class InteractionType(Enum):
    """
    The type of interaction received from discord.

    Used internally by the library. You should not need to use this.
    """
    ping = 1
    app_command = 2
    component = 3
    autocomplete = 4
    modal_submit = 5


class InteractionCallbackType(Enum):
    """
    The type of interaction callback.

    Used internally by the library. You should not need to use this.
    """
    pong = 1
    channel_message_with_source = 4
    deferred_channel_message_with_source = 5
    deferred_update_component_message = 6
    update_component_message = 7
    autocomplete = 8
    modal = 9


class MessageComponentType(Enum):
    """
    The type of message component.

    Used internally by the library. You should not need to use this.
    """
    action_row = 1
    button = 2
    text_select = 3
    text_input = 4
    user_select = 5
    role_select = 6
    mentionable_select = 7
    channel_select = 8


class SelectMenuType(Enum):
    """
    The type of select menu.

    """
    text = 3
    user = 5
    role = 6
    mentionable = 7
    channel = 8


class ButtonStyle(Enum):
    """
    Represents the style of a button.

    Attributes
    ----------
    blurple: :class:`int`
        Used to specify a blurple button.
    grey: :class:`int`
        Used to specify a grey button.
    green: :class:`int`
        Used to specify a green button.
    red: :class:`int`
        Used to specify a red button.
    link: :class:`int`
        Used to specify a link type button.
    """
    blurple = 1
    grey = 2
    green = 3
    red = 4
    link = 5


class WebhookType(Enum):
    """
    The type of webhook.

    Used internally by the library. You should not need to use this.
    """
    incoming = 1
    channel_follower = 2
    application = 3

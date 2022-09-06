from enum import Enum


def try_enum(enum_class, value):
    try:
        return enum_class(value)
    except ValueError:
        return None


class text_field_lengths(Enum):
    short = 1
    long = 2


class modal_field_types(Enum):
    text_input = 4


class command_types(Enum):
    slash = 1
    user = 2
    message = 3


class option_types(Enum):
    subcommand = 1
    subcommmand_groups = 2
    string = 3
    ineteger = 4
    boolean = 5
    user = 6
    channel = 7
    role = 8
    mentionable = 9
    number = 10
    attachment = 11


class channel_types(Enum):
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


class component_type(Enum):
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3
    TEXT_INPUT = 4


class interaction_types(Enum):
    ping = 1
    app_command = 2
    component = 3
    autocomplete = 4
    modal_submit = 5


class callback_types(Enum):
    pong = 1
    channel_message_with_source = 4
    deferred_channel_message_with_source = 5
    deferred_update_message = 6
    update_message = 7
    autocomplete_result = 8
    modal = 9


class component_types(Enum):
    action_row = 1
    button = 2
    select_menu = 3
    text_input = 4


class button_styles(Enum):
    blurple = 1
    grey = 2
    green = 3
    red = 4
    url = 5

from enum import Enum


class InteractionType(Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class CallbackType(Enum):
    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9


class Interaction:
    def __init__(self, payload: dict):
        self.id = int(payload['id'])
        self.application_id = int(payload['application_id'])
        self.type = InteractionType(payload['type'])
        self.data = payload.get('data', {})
        self.guild_id = int(payload.get('guild_id', 0))
        self.channel_id = int(payload.get('channel_id', 0))
        self.member = payload.get('member', {})
        self.user = payload.get('user', {})
        self.token = payload['token']
        self.version = payload['version']
        self.message = payload.get('message', {})
        self.locale = payload.get('locale')
        self.guild_locale = payload.get('guild_locale')

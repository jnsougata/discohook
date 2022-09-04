from .enums import InteractionType


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

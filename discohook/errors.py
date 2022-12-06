

# noinspection PyShadowingBuiltins
class NotImplemented(Exception):

    def __init__(self, payload: dict):
        self.data = payload
        self.name = payload['data']['name']
        self.id = payload['data']['id']
        self.type = payload['data']['type']
        super().__init__(f"Command `/{self.name}` (Id: {self.id} & Type: {self.type}) is not implemented")

class NoRightsException(Exception):
    def __init__(self, message="権限がありません"):
        self.body = message
        super().__init__(message)

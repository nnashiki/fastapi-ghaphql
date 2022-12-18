class MyException(Exception):
    def __init__(self, message="hoge"):
        self.body = message
        super().__init__(message)

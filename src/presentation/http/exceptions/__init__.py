class BaseHttpException(Exception):
    def __init__(self, message: str, status_code: int, class_name: str | None = None):
        self.message = message
        self.status_code = status_code
        self.class_name = class_name or self.__class__.__name__

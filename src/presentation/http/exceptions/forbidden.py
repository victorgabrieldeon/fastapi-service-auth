from presentation.http.exceptions.http_exception import BaseHttpException


class Forbidden(BaseHttpException):
    def __init__(self, message: str, class_name: str | None = None):
        super().__init__(message, 403, class_name)

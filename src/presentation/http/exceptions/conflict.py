from src.presentation.http.exceptions.http_exception import BaseHttpException


class Conflict(BaseHttpException):
    def __init__(self, message: str, class_name: str | None = None):
        super().__init__(message, 409, class_name)

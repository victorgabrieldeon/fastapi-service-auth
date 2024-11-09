from src.presentation.http.exceptions import BaseHttpException


class Unauthorized(BaseHttpException):
    def __init__(self, message: str, class_name: str | None = None):
        super().__init__(message, 401, class_name)

from src.presentation.http.exceptions import BaseHttpException


class NotFound(BaseHttpException):
    def __init__(self, message: str, class_name: str | None = None):
        super().__init__(message, 404, class_name)

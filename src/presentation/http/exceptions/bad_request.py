from src.presentation.http.exceptions import BaseHttpException


class BadRequest(BaseHttpException):
    def __init__(self, message: str, class_name: str | None = None):
        super().__init__(message, 400, class_name)

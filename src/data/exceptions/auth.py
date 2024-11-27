from data.exceptions.base import ApiException


class EmailNotAvailableError(ApiException): ...


class PasswordValidationError(ApiException): ...

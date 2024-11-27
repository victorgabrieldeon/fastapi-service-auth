from typing import Callable, Self

from data.validators.interface import Validator


class PasswordValidatorBuilder(Validator[str]):
    def __init__(self) -> None:
        self.validators: list[Callable[[str], bool]] = []

    def min_length(self, length: int) -> Self:
        self.validators.append(lambda data: len(data) >= length)
        return self

    def max_length(self, length: int) -> Self:
        self.validators.append(lambda data: len(data) <= length)
        return self

    def has_min_digits(self, digits: int) -> Self:
        self.validators.append(
            lambda data: len([char for char in data if char.isdigit()]) >= digits
        )
        return self

    def has_min_special_chars(self, special_chars: int) -> Self:
        self.validators.append(
            lambda data: len([char for char in data if not char.isalnum()])
            >= special_chars
        )
        return self

    def has_min_uppercase(self, uppercase: int) -> Self:
        self.validators.append(
            lambda data: len([char for char in data if char.isupper()]) >= uppercase
        )
        return self

    def no_spaces(self) -> Self:
        self.validators.append(lambda data: not any(char.isspace() for char in data))
        return self

    async def validate(self, data: str) -> bool:
        return all(validator(data) for validator in self.validators)

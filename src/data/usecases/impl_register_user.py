from data.exceptions.auth import EmailNotAvailableError, PasswordValidationError
from data.validators.string import StringValidator
from src.data.protocols.cryptography.hasher import Hasher
from src.data.protocols.repositories.create_user_repository import CreateUserRepository
from src.domain.usecases.register_user_usecase import (
    RegisterUserUseCase,
)
from src.domain.validators.email_available_validator import EmailAvailableValidator


class ImplRegisterUserUseCase(RegisterUserUseCase):
    def __init__(
        self,
        email_avaiable_validator: EmailAvailableValidator,
        hasher: Hasher,
        create_user_repository: CreateUserRepository,
    ) -> None:
        self.email_avaiable_validator = email_avaiable_validator
        self.hasher = hasher
        self.create_user_repository = create_user_repository

    async def execute(
        self, params: RegisterUserUseCase.Params
    ) -> RegisterUserUseCase.Response:
        if not await self.email_avaiable_validator.validate(params.email):
            raise EmailNotAvailableError

        MIN_LENGHT = 8
        MAX_LENGHT = 20
        MIN_SPECIAL_CHARS = 1
        MIN_UPPERCASE = 1
        MIN_DIGITS = 1

        password_validator = (
            StringValidator()
            .min_length(MIN_LENGHT)
            .no_spaces()
            .max_length(MAX_LENGHT)
            .has_min_digits(MIN_DIGITS)
            .has_min_special_chars(MIN_SPECIAL_CHARS)
            .has_min_uppercase(MIN_UPPERCASE)
        )

        if not await password_validator.validate(params.password):
            raise PasswordValidationError(
                f"Pasword must have at least {MIN_LENGHT} characters,"
                f" no spaces, at most {MAX_LENGHT} characters, {MIN_DIGITS} digits,"
                f" {MIN_SPECIAL_CHARS} special characters and {MIN_UPPERCASE} uppercase characters"
            )

        hashed_password = await self.hasher.hash(params.password)

        user = await self.create_user_repository.create(
            email=params.email, hashed_password=hashed_password
        )

        return RegisterUserUseCase.Response(
            user=user,
        )

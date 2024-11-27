from data.exceptions.auth import EmailNotAvailableError, PasswordValidationError
from data.validators.password import PasswordValidatorBuilder
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

        password_validator = (
            PasswordValidatorBuilder()
            .min_length(8)
            .no_spaces()
            .max_length(20)
            .has_min_digits(1)
            .has_min_special_chars(1)
            .has_min_uppercase(1)
        )

        if not await password_validator.validate(params.password):
            raise PasswordValidationError()

        hashed_password = await self.hasher.hash(params.password)

        user = await self.create_user_repository.create(
            email=params.email, hashed_password=hashed_password
        )

        return RegisterUserUseCase.Response(
            user=user,
        )

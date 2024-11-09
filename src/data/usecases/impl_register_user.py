from src.data.exceptions.email import EmailNotAvailableError
from src.data.protocols.cryptography.hasher import Hasher
from src.data.protocols.repositories.create_user_repository import CreateUserRepository
from src.domain.models.user import User
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

        hashed_password = await self.hasher.hash(params.password)

        user = User.create(email=params.email, hashed_password=hashed_password)

        user = await self.create_user_repository.create(user)

        return RegisterUserUseCase.Response(
            user=user,
        )

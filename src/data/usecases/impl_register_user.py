from uuid import uuid4

from data.protocols.cryptography.hasher import Hasher
from data.protocols.repositories.create_user_repository import CreateUserRepository
from domain.models.user import User
from domain.usecases.register_user_usecase import (
    RegisterUserUseCase,
)
from domain.validators.email_available_validator import EmailAvailableValidator


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
            raise ValueError("Email not available")

        hashed_password = await self.hasher.hash(params.password)

        user = User(
            id=str(uuid4()),
            email=params.email,
            hashed_password=hashed_password,
            is_active=True,
        )

        user = await self.create_user_repository.create(user)

        return RegisterUserUseCase.Response(**user.model_dump())

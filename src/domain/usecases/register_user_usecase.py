from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.user import User


class RegisterUserParams(BaseModel):
    email: str
    password: str


class RegisterUserResponse(User): ...


class RegisterUserUseCase(ABC):
    Params = RegisterUserParams
    Response = RegisterUserResponse

    @abstractmethod
    async def execute(self, params: Params) -> Response: ...

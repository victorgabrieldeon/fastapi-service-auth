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
    async def execute(self, params: Params) -> Response:
        """
        Register a new user in the system

        Rules:
        - Check if email is available

        ### Raises:
            ValueError: If email is not available

        ### Params:
            email: str - User email to register
            password: str - User password to register

        ### Returns:
            User - The user registered
        """

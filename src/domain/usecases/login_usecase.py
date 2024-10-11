from abc import ABC, abstractmethod

from pydantic import BaseModel


class LoginParams(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class LoginUseCase(ABC):
    Params = LoginParams
    Response = LoginResponse

    @abstractmethod
    async def execute(self, params: Params) -> Response:
        """
        Authenticate a user in the system

        ### Params:
            email: str - User email to authenticate
            password: str - User password to authenticate

        ### Returns:
            access_token: str - The access token to authenticate
            token_type: str - The token type
        """
        ...

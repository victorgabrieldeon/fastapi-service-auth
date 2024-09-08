from abc import ABC, abstractmethod

from src.domain.models.user import User


class CreateUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        raise NotImplementedError

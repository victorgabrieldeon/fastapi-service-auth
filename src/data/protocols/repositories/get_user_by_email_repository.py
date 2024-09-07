from abc import ABC, abstractmethod

from domain.models.user import User


class GetUserByEmailRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        raise NotImplementedError

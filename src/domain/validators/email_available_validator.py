from abc import ABC, abstractmethod


class EmailAvailableValidator(ABC):
    @abstractmethod
    async def validate(self, email: str) -> bool:
        """
        Check if email already exists in the system
        """

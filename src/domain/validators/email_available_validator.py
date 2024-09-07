from abc import ABC, abstractmethod


class EmailAvailableValidator(ABC):
    @abstractmethod
    async def validate(self, email: str) -> bool: ...

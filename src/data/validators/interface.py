from abc import ABC, abstractmethod


class Validator[T](ABC):
    @abstractmethod
    async def validate(self, data: T) -> bool:
        """
        Interface for validators
        """

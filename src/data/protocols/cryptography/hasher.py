from abc import ABC, abstractmethod


class Hasher(ABC):
    @abstractmethod
    async def hash(self, value: str) -> str:
        raise NotImplementedError

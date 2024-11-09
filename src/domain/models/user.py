from pydantic import EmailStr

from src.domain.models.base import BaseEntity


class User(BaseEntity):
    email: EmailStr
    hashed_password: str
    is_active: bool = True

    @classmethod
    def create(cls, email: str, hashed_password: str) -> "User":
        return User(email=email, hashed_password=hashed_password)

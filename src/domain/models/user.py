from pydantic import EmailStr

from domain.models.base import BaseEntity


class User(BaseEntity):
    email: EmailStr
    hashed_password: str
    is_active: bool

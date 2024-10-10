import datetime
import uuid

from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    """
    Class base for all entities in the domain layer.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    created_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.UTC)
    )

    updated_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.UTC)
    )

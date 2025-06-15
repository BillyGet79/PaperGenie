from typing import Optional, TypeVar

from sqlmodel import SQLModel, Field


class IdModel(SQLModel):
    __table_args__ = {"schema": "papergeniedb"}
    id: Optional[int] = Field(default=None, primary_key=True)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__str__()

T = TypeVar("T", bound=IdModel)
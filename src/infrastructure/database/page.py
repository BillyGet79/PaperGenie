from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlmodel import Field

M = TypeVar("M")

class PageData(BaseModel, Generic[M]):
    items: list[M]
    total: int
    page_size: int = Field(alias="pageSize")
    page_num: int = Field(alias="pageNum")
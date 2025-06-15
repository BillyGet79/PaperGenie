import sqlalchemy
from sqlalchemy import Column
from sqlmodel import Field

from infrastructure.db.base_model import IdModel


class TestModel(IdModel, table=True):
    __tablename__ = "test"

    name: str = Field(sa_column=Column(sqlalchemy.String(128), comment="测试名称"))
    description: str = Field(sa_column=Column(sqlalchemy.String(128), comment="<UNK>"))


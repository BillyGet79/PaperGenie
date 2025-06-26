import sqlalchemy
from sqlalchemy import Column
from sqlmodel import Field

from infrastructure.db.base_model import IdModel
from infrastructure.db.database import create_db_and_tables
from infrastructure.utils.log_utils import logger


class InitModel(IdModel, table=True):
    __tablename__ = "init"

    name: str = Field(sa_column=Column(sqlalchemy.String(128), comment="测试名称"))
    description: str = Field(sa_column=Column(sqlalchemy.String(128), comment="<UNK>"))

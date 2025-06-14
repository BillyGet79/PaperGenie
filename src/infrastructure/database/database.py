from config import get_config
from sqlmodel import create_engine, Session, SQLModel


def get_engine():
    database_config = get_config().database
    return create_engine(url=database_config.url, echo=False)

def create_session():
    return Session(get_engine())

def get_session():
    with Session(get_engine()) as session:
        yield session

def create_db_and_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)



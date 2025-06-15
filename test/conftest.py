import pytest
from sqlmodel import SQLModel
from starlette.testclient import TestClient

from infrastructure.database.database import get_engine, get_session
from main import app

engine = get_engine()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def session():
    with get_session() as session:
        yield session


@pytest.fixture(scope="module")
def override_get_session(session):
    def _override_get_session():
        return session

    app.dependency_overrides[get_session] = _override_get_session
    yield
    app.dependency_overrides.clear()

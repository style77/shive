import pytest
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from api.database import async_session

from api.settings import settings

DATABASE_NAME = settings.DATABASE_URL.split("/")[-1]

TEST_DATABASE_NAME = "test_" + DATABASE_NAME
TEST_DATABASE_URL = settings.DATABASE_URL.replace(
    DATABASE_NAME, TEST_DATABASE_NAME
)
engine = AsyncEngine(
    create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=True,
        future=True,
    )
)


@pytest.fixture
def setup_database():
    async_session.configure(bind=engine)

    SQLModel.metadata.create_all(bind=engine)

    yield

    SQLModel.metadata.drop_all(bind=engine)
    async_session.remove()

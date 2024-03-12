from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from api.database import async_session
from api.main import app
from api.settings import settings

DATABASE_NAME = settings.DATABASE_URL.rsplit("/", 1)[-1]

TEST_DATABASE_NAME = "test_" + DATABASE_NAME
TEST_DATABASE_PORT = "5433"
TEST_DATABASE_HOST = "test-database"
TEST_DATABASE_URL = settings.DATABASE_URL.rsplit("/", 1)[0] + "/" + TEST_DATABASE_NAME
TEST_DATABASE_URL = TEST_DATABASE_URL.replace("5432", TEST_DATABASE_PORT, 1)
TEST_DATABASE_URL = TEST_DATABASE_URL.replace("database", TEST_DATABASE_HOST, 1)

engine = AsyncEngine(
    create_engine(
        TEST_DATABASE_URL,
        echo=False,
        future=True,
    )
)


@pytest.fixture(scope="module")
def client() -> TestClient:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
async def setup_session():
    async_session.configure(bind=engine)

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    try:
        yield
    finally:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
        await engine.dispose()

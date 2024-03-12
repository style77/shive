from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from api.database import async_session
from api.main import app
from api.settings import settings

engine = AsyncEngine(
    create_engine(
        settings.TEST_DATABASE_URL,
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

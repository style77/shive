import asyncio
import pytest
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from httpx import AsyncClient
from api.database import async_session
from api.main import app
from api.settings import settings


@pytest.fixture(scope="module")
def event_loop():

    loop = asyncio.get_event_loop()

    yield loop


@pytest.fixture(scope="module")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://shive_test") as client:
        yield client


@pytest.fixture(scope="module")
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope="module", autouse=True)
async def setup_session():
    engine = AsyncEngine(
        create_engine(
            settings.TEST_DATABASE_URL,
            echo=False,
            future=True,
        )
    )

    async_session.configure(bind=engine)

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    try:
        yield
    finally:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
        await engine.dispose()

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from api.settings import settings

engine = AsyncEngine(create_engine(settings.DATABASE_URL, echo=True, future=True))
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_table() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

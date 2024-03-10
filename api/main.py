from contextlib import asynccontextmanager

from fastapi import FastAPI
from api.settings import settings
from api.router import router
from api.core.logs import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("startup: triggered")

    yield

    logger.info("shutdown: triggered")


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description=f"{settings.APP_NAME} API",
    lifespan=lifespan,
)

app.include_router(router=router)

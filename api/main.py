from contextlib import asynccontextmanager

import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from fastapi import FastAPI, APIRouter
from api.settings import settings
from api.core.logs import logger

from api.users.router import router as users_router
from api.health.router import router as health_router


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
# schema = graphene.Schema()

router = APIRouter(prefix="/api/v1")

router.include_router(users_router)
router.include_router(health_router)

app.include_router(router)

# app.mount("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))

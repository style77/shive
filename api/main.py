from contextlib import asynccontextmanager

import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, APIRouter
from api.settings import settings
from api.core.logs import logger

from api.users.router import router as users_router
from api.health.router import router as health_router
from api.auth.router import router as auth_router
from api.schema import Query, Mutation
from api.auth.middleware import RefreshTokenMiddleware


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RefreshTokenMiddleware)

router = APIRouter(prefix="/api/v1")

router.include_router(users_router)
router.include_router(health_router)
router.include_router(auth_router)

app.include_router(router)

schema = graphene.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLApp(schema, on_get=make_graphiql_handler())

app.mount("/graphql", graphql_app)

from fastapi import FastAPI
from api.users.router import router as users_router

app = FastAPI()

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])

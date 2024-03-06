from fastapi import FastAPI
from app.users.router import router as users_router

app = FastAPI()

app.add_api_route("/users", users_router)

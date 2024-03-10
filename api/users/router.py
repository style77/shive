from fastapi import APIRouter
from api.users.services import UserService

router = APIRouter(prefix="/users", tags=["users"])
service = UserService()

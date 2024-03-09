from fastapi import APIRouter
from api.users.models import UserCreate, User

router = APIRouter()


@router.post("/", response_model=User)
async def users(data: UserCreate):
    return data

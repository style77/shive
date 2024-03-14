from api.users.services import service
from api.users.models import User, UserCreate


async def create_test_user() -> User:
    user_create = UserCreate(
        username="test",
        email="test@test.com",
        full_name="Test Test",
        password="test",
    )

    user = await service.create_user(user_create)

    return user

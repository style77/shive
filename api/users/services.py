from api.users.models import UserCreate, User
from argon2 import PasswordHasher

from api.database import async_session


class UserService:
    hasher = PasswordHasher()

    def hash_password(self, password: str):
        return self.hasher.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        return self.hasher.verify(hashed_password, password)

    async def create_user(self, data: UserCreate):
        hashed_password = self.hash_password(data.password)

        user = User(**data.model_dump(), hashed_password=hashed_password)

        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)

        return user


service = UserService()

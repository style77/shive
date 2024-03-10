from api.users.models import UserCreate, User
from argon2 import PasswordHasher

from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    hasher = PasswordHasher()

    def hash_password(self, password: str):
        return self.hasher.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        return self.hasher.verify(hashed_password, password)

    async def create_user(self, data: UserCreate, session: AsyncSession):
        hashed_password = self.hash_password(data.password)

        user = User(**data.model_dump(), hashed_password=hashed_password)

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user

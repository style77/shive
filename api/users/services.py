from typing import Optional, Union
from sqlmodel import select
from api.users.models import UserCreate, User
from argon2 import PasswordHasher

from api.database import async_session


class UserService:
    hasher = PasswordHasher()

    def hash_password(self, password: str):
        return self.hasher.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        try:
            return self.hasher.verify(hashed_password, password)
        except Exception:
            return False

    async def get_user(self, email: str) -> Optional[User]:
        async with async_session() as session:
            user = await session.exec(select(User).where(User.email == email))
            user = user.first()

            return user

    async def create_user(self, data: UserCreate):
        hashed_password = self.hash_password(data.password)

        data = data
        data.password = hashed_password

        user = User(**data.model_dump())

        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)

        return user

    async def authenticate_user(
        self, email: str, password: str
    ) -> Union[Optional[User], bool]:
        user = await self.get_user(email)
        if user and self.verify_password(password, user.password):
            return user, True
        return None, False


service = UserService()

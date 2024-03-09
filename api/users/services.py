from api.users.models import UserCreate
from argon2 import PasswordHasher


class UserService:
    hasher = PasswordHasher()

    def hash_password(self, password: str):
        return self.hasher.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        return self.hasher.verify(hashed_password, password)

    async def create_user(self, data: UserCreate):
        hashed_password = self.hash_password(data.password)

from api.users.schemas import RegisterRequest
from api.users.models import User
from argon2 import PasswordHasher


class UserService:
    hasher = PasswordHasher()

    def hash_password(self, password: str):
        return self.hasher.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        return self.hasher.verify(hashed_password, password)

    async def create_user(self, data: RegisterRequest):
        hashed_password = self.hash_password(data.password)

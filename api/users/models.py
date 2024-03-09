from sqlmodel import Field, SQLModel

from api.common.models import GeneralModel


class UserBase(SQLModel):
    username: str
    email: str
    full_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase, GeneralModel):
    password: str  # hashed password
    is_active: bool = Field(default=True)

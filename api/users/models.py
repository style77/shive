from sqlmodel import Field, SQLModel

from api.common.models import GeneralModel


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    full_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase, GeneralModel, table=True):
    __tablename__ = "users"

    password: str  # hashed password
    is_active: bool = Field(default=True)

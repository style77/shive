from sqlmodel import Field, SQLModel, Column
from api.common.models import GeneralModel
from api.users.models import User

from enum import Enum


class OrganizationIcon(str, Enum):
    DEFAULT = "default"


class OrganizationBase(SQLModel):
    name: str = Field(max_length=50)
    icon: OrganizationIcon = Field(
        sa_column=Column(Enum(OrganizationIcon)), default=OrganizationIcon.DEFAULT
    )


class Organization(OrganizationBase, GeneralModel, table=True):
    __tablename__ = "organizations"
    owner: User

from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
import uuid


class GeneralModel(SQLModel):
    id: str = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None, nullable=True)

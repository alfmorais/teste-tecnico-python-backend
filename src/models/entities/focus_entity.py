from datetime import datetime

from sqlmodel import Field, SQLModel


class FocusTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    focus_level: int = Field(ge=1, le=5)
    duration_minutes: int = Field(gt=0)
    comment: str = Field(min_length=1)

    created_at: datetime = Field(default_factory=datetime.now)

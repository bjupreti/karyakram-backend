from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


# TODO:
# 1. Define relationship of user and group in events table
# 2. Rename the tablename to events -> done
# 3. Auto generate id, created_at and updated_at attributes
class Event(SQLModel, table=True):
    __tablename__ = "events"
    event_id: int | None = Field(default=None, primary_key=True, index=True)
    title: str
    description: str
    address_line_1: str
    address_line_2: str
    city: str
    province: str
    postal_code: str
    country: str
    is_owner: bool
    event_start_datetime: datetime
    event_end_datetime: datetime
    event_image_url: str
    event_image_thumb_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    # user_id: int = Field(default=None, foreign_key="user.id")

    # Foreign key relationship to User
    # user_id: int = Field(default=None, foreign_key="user.id")
    # user: User = Relationship(back_populates="events")

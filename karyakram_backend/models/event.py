from sqlmodel import SQLModel, Field
from datetime import datetime

class EventBase(SQLModel):
    title: str
    description: str
    address_line_1: str
    address_line_2: str
    # city: str
    # province: str
    # postal_code: str
    # country: str
    # is_owner: bool
    # event_datetime: datetime
    # event_image_url: str
    # event_image_thumb_url: str
    # created_at: datetime = Field(default_factory=datetime.utcnow)
    # updated_at: datetime = Field(default_factory=datetime.utcnow)

class Event(EventBase, table=True):
    __tablename__ = "events"
    event_id: int = Field(default=None, primary_key=True)
    # user_id: int
    # group_id: int

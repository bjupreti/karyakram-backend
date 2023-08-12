from pydantic import BaseModel
from datetime import datetime


class EventBase(BaseModel):
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
    created_at: datetime
    updated_at: datetime


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class EventResponse(EventBase):
    event_id: int

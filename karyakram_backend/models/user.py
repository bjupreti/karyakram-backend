from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class MFAOption(str, Enum):
    none = "none"
    phone = "phone"
    email = "email"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    country: str
    phone: str
    is_verified_email: bool
    is_verified_phone: bool
    mfa: MFAOption
    profile_pic_url: Optional[str] = None
    profile_pic_thumb_url: Optional[str] = None
    notification: bool
    is_admin: bool
    is_deleted: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

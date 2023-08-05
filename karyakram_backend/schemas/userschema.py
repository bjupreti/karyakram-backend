from typing import Optional
from pydantic import  BaseModel
from datetime import datetime
from ..models.user import MFAOption

class UserBase(BaseModel):
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

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


from typing import Optional
from pydantic import  BaseModel
from datetime import datetime
from karyakram_backend.models.user import MFAOption

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
    
    # Orm_mode tells Pydantic to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
    class Config:
        orm_mode = True


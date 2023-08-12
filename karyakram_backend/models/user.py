# from sqlmodel import SQLModel, Field, Relationship
# from datetime import datetime
# from enum import Enum
# from typing import Optional, List
# # from pydantic import EmailStr

# class MFAOption(str, Enum):
#     none = "none"
#     phone = "phone"
#     email = "email"

# # TODO:
# # 1. Create a relationship with events table
# # 2. Rename the tablename to users
# # 3. Maybe add indexing?
# # 4. Auto generate id, created_at and updated_at attributes
# class User(SQLModel, table=True):
#     id: Optional[int] = Field(nullable=False, primary_key=True,index=True)
#     first_name: str
#     last_name: str
#     email: str
#     country: str
#     phone: str
#     is_verified_email: bool
#     is_verified_phone: bool
#     mfa: MFAOption
#     profile_pic_url: Optional[str] = None
#     profile_pic_thumb_url: Optional[str] = None
#     notification: bool
#     is_admin: bool
#     is_deleted: bool
#     created_at: datetime = Field(default_factory=datetime.utcnow)
#     updated_at: datetime = Field(default_factory=datetime.utcnow)
    
#     # Relationship field to establish a one-to-many relationship
#     # events: list["Event"] = Relationship(back_populates="user")

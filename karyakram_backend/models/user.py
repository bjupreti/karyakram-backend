# from sqlmodel import SQLModel, Field, Relationship,Enum
# from datetime import datetime
# from enum import Enum as PyEnum
# from typing import Optional, List
# # from pydantic import EmailStr

# class MFAOption(str, PyEnum):
#     none = "none"
#     phone = "phone"
#     email = "email"

# # TODO:
# # 1. Create a relationship with events table
# # 2. Rename the tablename to users
# # 3. Maybe add indexing?
# # 4. Auto generate id, created_at and updated_at attributes
# class User(SQLModel, table=True):
#     __tablename__ = "users"
    
#     user_id: int = Field(default=None, primary_key=True,index=True)
#     first_name: str
#     last_name: str
#     email: str
#     country: str
#     phone: str
#     is_verified_email: bool
#     is_verified_phone: bool
#     mfa: MFAOption = Field(sa_column=Field(Enum(MFAOption)))
#     profile_pic_url: Optional[str] = None
#     profile_pic_thumb_url: Optional[str] = None
#     notification: bool
#     is_admin: bool
#     is_deleted: bool
#     created_at: datetime = Field(default_factory=datetime.utcnow)
#     updated_at: datetime = Field(default_factory=datetime.utcnow)
    
#     # Relationship field to establish a one-to-many relationship
#     # events: list["Event"] = Relationship(back_populates="user")

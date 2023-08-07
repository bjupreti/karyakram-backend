from sqlmodel import SQLModel, Field
from datetime import datetime


# TODO:
# 1. Create a relationship with events table
# 2. Rename the tablename to users
# 3. Maybe add indexing?
# 4. Auto generate id, created_at and updated_at attributes
class Group(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True,index=True)  
    title: str
    description: str
    group_image_url: str
    group_image_thumb_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

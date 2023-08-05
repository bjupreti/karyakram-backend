from sqlmodel import SQLModel, Field
from datetime import datetime

class Group(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True,index=True)  
    title: str
    description: str
    group_image_url: str
    group_image_thumb_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

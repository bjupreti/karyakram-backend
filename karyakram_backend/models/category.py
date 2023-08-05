from sqlmodel import SQLModel, Field
from datetime import datetime

class Category(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True,index=True)  
    title: str
    description: str
    image: str
    # created_by: User
    # last_updated_by: User
    is_deleted: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

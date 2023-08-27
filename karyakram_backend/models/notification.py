from sqlmodel import SQLModel, Field,Enum
from datetime import datetime
from enum import Enum as PyEnum


class NotificationTypeEnum(str, PyEnum):
    event = "event"
    admin = "admin"
    
class Notification(SQLModel, table=True):
    notification_id : int = Field(default=None, primary_key=True,index=True)  
    # user_id: User
    notification_text: str
    notification_type: NotificationTypeEnum = Field(sa_column=Field(Enum(NotificationTypeEnum)))
    is_read: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    

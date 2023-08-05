from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum


class NotificationTypeEnum(str, Enum):
    event = "event"
    admin = "admin"
    
class Notification(SQLModel, table=True):
    notification_id : int = Field(default=None, primary_key=True,index=True)  
    # user_id: User
    notification_text: str
    notification_type: NotificationTypeEnum
    is_read: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    

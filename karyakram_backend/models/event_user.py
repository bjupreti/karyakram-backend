from sqlmodel import SQLModel, Field
from enum import Enum

class StatusEnum(str, Enum):
    going = "going"
    maybe = "maybe"
    cancelled = "cancelled"
    
class EventUser(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True,index=True)  
    # event_id: Event
    # user_id: User
    status: StatusEnum

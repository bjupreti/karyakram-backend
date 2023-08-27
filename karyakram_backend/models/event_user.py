from sqlmodel import SQLModel, Field, Enum
from enum import Enum as PyEnum

class StatusEnum(str, PyEnum):
    going = "going"
    maybe = "maybe"
    cancelled = "cancelled"
    
class EventUser(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True,index=True)  
    # event_id: Event
    # user_id: User
    status: StatusEnum = Field(sa_column=Field(Enum(StatusEnum)))

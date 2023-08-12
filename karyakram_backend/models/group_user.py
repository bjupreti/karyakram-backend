# from sqlmodel import SQLModel, Field
# from datetime import datetime
# from enum import Enum
# from enum import Enum as PyEnum

# class NotificationEnum(str, PyEnum):
#     pending = "pending"
#     accepted = "accepted"
#     denied = "denied"

# class TypeEnum(str, PyEnum):
#     owner = "owner"
#     moderator = "moderator"
#     member = "member"
    
# class GroupUser(SQLModel, table=True):
#     id : int = Field(default=None, primary_key=True,index=True)  
#     group_id: int
#     user_id: int
#     send_notification: bool
#     status: NotificationEnum
#     type: TypeEnum
    

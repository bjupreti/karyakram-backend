from fastapi import FastAPI
from api import event

# from api import user
from db.database import create_db_and_tables

app = FastAPI()

app.include_router(event.router)
# app.include_router(user.router)

create_db_and_tables()

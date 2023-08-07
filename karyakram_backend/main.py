from fastapi import FastAPI
from api import event
from api import user

app = FastAPI()

app.include_router(event.router)
app.include_router(user.router)

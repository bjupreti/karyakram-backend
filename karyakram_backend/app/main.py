from fastapi import FastAPI
# from ..api.routes import hello
from ..api.routes import event
from ..api.routes import user

app = FastAPI()

app.include_router(event.router)
app.include_router(user.router)

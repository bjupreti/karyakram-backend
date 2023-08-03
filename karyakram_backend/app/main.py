from fastapi import FastAPI
# from ..api.routes import hello
from ..api.routes import event

app = FastAPI()

app.include_router(event.router)

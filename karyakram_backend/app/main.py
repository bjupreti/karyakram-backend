from fastapi import FastAPI
from karyakram_backend.api.routes import event
from karyakram_backend.api.routes import user

app = FastAPI()

app.include_router(event.router)
app.include_router(user.router)

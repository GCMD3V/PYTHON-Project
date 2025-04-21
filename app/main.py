from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db import init_db
from app.routes import login, register, dashboard

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(register.router)
app.include_router(login.router)
app.include_router(dashboard.router)

from fastapi import FastAPI

from app.config import settings
from app.routers.auth import router as auth_router

app = FastAPI(
    title=settings.app_name,
    description="A REST API for team and project management.",
    version="0.1.0",
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Welcome to ProjectHub API"}


@app.get("/status")
def status():
    return {"status": "healthy"}

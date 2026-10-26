from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.app_name,
    description="A REST API for team and project management.",
    version="0.1.0",
)


@app.get("/")
def home():
    return {"message": "Welcome to ProjectHub API"}


@app.get("/status")
def status():
    return {"status": "healthy"}

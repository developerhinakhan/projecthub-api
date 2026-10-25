from fastapi import FastAPI

app = FastAPI(
    title="ProjectHub API",
    description="A REST API for team and project management.",
    version="0.1.0", 
)

@app.get("/")
def home():
    return {"message":"Welcome to ProjectHub API"}


@app.get("/status")
def status():
    return {"status": "healthy"}

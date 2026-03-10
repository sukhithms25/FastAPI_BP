from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(title="FastAPI Boilerplate")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "backend running successfully"}

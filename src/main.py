from fastapi import FastAPI
from src.config import *
from src.api import ingestion

app = FastAPI()
app.include_router(ingestion.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

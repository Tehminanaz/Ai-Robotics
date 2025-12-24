from fastapi import FastAPI, Depends, Request, status
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from qdrant_client import QdrantClient
from loguru import logger

from backend.config.database import get_db
from backend.vector_db.qdrant_client import get_qdrant_client
from backend.utils.logger_config import configure_logging
from backend.api.ingestion import router as ingestion_router
from backend.api.chatbot import router as chatbot_router
from backend.api.personalization import router as personalization_router
from backend.api.auth import router as auth_router

# Configure logging at application startup
configure_logging()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(ingestion_router, prefix="/api/v1", tags=["ingestion"])
app.include_router(chatbot_router, prefix="/api/v1", tags=["chatbot"])
app.include_router(personalization_router, prefix="/api/v1", tags=["personalization"])
app.include_router(auth_router, prefix="/api/v1", tags=["auth"])

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "An unexpected error occurred.",
            "detail": str(exc),
        },
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    logger.info("Root endpoint accessed.")
    return {"message": "Hello from FastAPI backend!"}

@app.get("/check_db")
async def check_db(db: Session = Depends(get_db)):
    logger.info("Checking database connection...")
    try:
        db.execute("SELECT 1")
        logger.info("Database connection successful.")
        return {"status": "Database connection successful"}
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return {"status": f"Database connection failed: {e}"}

@app.get("/check_qdrant")
async def check_qdrant(qdrant_client: QdrantClient = Depends(get_qdrant_client)):
    logger.info("Checking Qdrant connection...")
    try:
        collections = qdrant_client.get_collections().collections
        logger.info("Qdrant connection successful.")
        return {"status": "Qdrant connection successful", "collections": [c.name for c in collections]}
    except Exception as e:
        logger.error(f"Qdrant connection failed: {e}")
        return {"status": f"Qdrant connection failed: {e}"}

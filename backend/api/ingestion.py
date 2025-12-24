from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.data.database import get_db
from backend.data.models import IngestRequest, IngestResponse
from backend.ingestion.ingestion_pipeline import process_and_ingest_content, initialize_qdrant_collection
from starlette.concurrency import run_in_threadpool # Import run_in_threadpool
import uuid

router = APIRouter()

@router.on_event("startup")
async def startup_event():
    try:
        await initialize_qdrant_collection()
    except Exception as e:
        print(f"Warning: Could not initialize Qdrant collection during startup: {e}")
        print("Qdrant connection will be retried on first use.")

@router.post("/ingest", response_model=IngestResponse)
async def ingest_content(request: IngestRequest, db: AsyncSession = Depends(get_db)):
    try:
        # Ensure blocking code runs in a thread pool
        db_content = await run_in_threadpool(process_and_ingest_content, db, request)
        return IngestResponse(status="success", content_id=db_content.id, message="Content ingestion initiated.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Content ingestion failed: {e}")

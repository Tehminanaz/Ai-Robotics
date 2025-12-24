from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from backend.services.rag_service import run_rag_query
from backend.data.database import get_db
from backend.data.models import QueryCreate, ResponseCreate

router = APIRouter(prefix="/chat", tags=["chatbot"])

class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = None
    context: Optional[str] = None  # For contextual queries based on selected text

class QueryResponse(BaseModel):
    response: str
    session_id: str
    sources: List[str] = []

class ClearSessionRequest(BaseModel):
    session_id: str

@router.post("/query", response_model=QueryResponse)
async def query_chatbot(request: QueryRequest):
    """
    Global Q&A based on the book content
    """
    try:
        # If context is provided, combine it with the query
        if request.context:
            query_text = f"Context: {request.context}\n\nQuestion: {request.query}"
        else:
            query_text = request.query

        response = await run_rag_query(query_text)

        # Generate a session ID if not provided
        session_id = request.session_id or str(uuid.uuid4())

        return QueryResponse(
            response=response,
            session_id=session_id,
            sources=[]  # In a full implementation, sources would be returned
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

@router.post("/query-highlighted", response_model=QueryResponse)
async def query_with_context(request: QueryRequest):
    """
    Contextual Q&A based on 'Selected Text' from the UI
    """
    if not request.context:
        raise HTTPException(status_code=400, detail="Context is required for contextual queries")

    try:
        # Combine the selected text context with the user's question
        enhanced_query = f"Based on this text: '{request.context}', answer this question: {request.query}"
        response = await run_rag_query(enhanced_query)

        session_id = request.session_id or str(uuid.uuid4())

        return QueryResponse(
            response=response,
            session_id=session_id,
            sources=[]  # In a full implementation, sources would be returned
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Contextual query failed: {str(e)}")

@router.get("/history/{session_id}")
async def get_conversation_history(session_id: str):
    """
    Retrieve conversation history for a specific session
    """
    # In a full implementation, this would retrieve from database
    # For now, returning an empty history
    return {"session_id": session_id, "history": []}

@router.delete("/clear/{session_id}")
async def clear_conversation_context(session_id: str):
    """
    Clear conversation context for a specific session
    """
    # In a full implementation, this would clear the session from database
    # For now, just returning success
    return {"message": f"Conversation context for session {session_id} cleared"}
import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Field
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB

from .database import Base

# SQLAlchemy models
class ContentORM(Base):
    __tablename__ = "content"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_url = Column(String, nullable=True)
    text_content = Column(Text, nullable=False)
    embedding_vector = Column(ARRAY(Text), nullable=True) # Storing as Text array for simplicity, consider a vector type if available/needed
    content_metadata = Column(JSONB, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)

class QueryORM(Base):
    __tablename__ = "queries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query_text = Column(Text, nullable=False)
    session_id = Column(UUID(as_uuid=True), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(UUID(as_uuid=True), nullable=True)

class ResponseORM(Base):
    __tablename__ = "responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query_id = Column(UUID(as_uuid=True), nullable=False)
    response_text = Column(Text, nullable=False)
    retrieved_chunks = Column(JSONB, nullable=True)
    generated_by_agent = Column(DateTime, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


# Pydantic models
class ContentBase(BaseModel):
    source_url: Optional[str] = None
    text_content: str
    content_metadata: Optional[Dict[str, Any]] = None

class ContentCreate(ContentBase):
    pass

class Content(ContentBase):
    id: uuid.UUID
    embedding_vector: Optional[List[float]] = None # Assuming float list for vector
    last_updated: datetime

    class Config:
        orm_mode = True

class QueryBase(BaseModel):
    query_text: str
    session_id: Optional[uuid.UUID] = None
    user_id: Optional[uuid.UUID] = None

class QueryCreate(QueryBase):
    pass

class Query(QueryBase):
    id: uuid.UUID
    timestamp: datetime

    class Config:
        orm_mode = True

class RetrievedChunk(BaseModel):
    content_id: uuid.UUID
    chunk_id: str
    score: float
    text_snippet: str

class ResponseBase(BaseModel):
    query_id: uuid.UUID
    response_text: str
    retrieved_chunks: Optional[List[RetrievedChunk]] = None
    generated_by_agent: Optional[bool] = False

class ResponseCreate(ResponseBase):
    pass

class Response(ResponseBase):
    id: uuid.UUID
    timestamp: datetime

    class Config:
        orm_mode = True

# Ingestion models
class IngestRequest(BaseModel):
    source_url: Optional[str] = None
    text_content: str
    content_metadata: Optional[Dict[str, Any]] = None

class IngestResponse(BaseModel):
    status: str
    content_id: uuid.UUID
    message: str

from typing import List
import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient, models
from sqlalchemy.ext.asyncio import AsyncSession

from src.data.models import ContentCreate, ContentORM
from src.embeddings.openai import generate_embeddings
from src.services.qdrant_client import get_qdrant_client
from src.services import content_service

COLLECTION_NAME = "rag_content"

async def initialize_qdrant_collection():
    client: QdrantClient = await get_qdrant_client()
    collections = await client.get_collections()
    if not any(c.name == COLLECTION_NAME for c in collections.collections):
        await client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
        )

async def process_and_ingest_content(
    db: AsyncSession, content_create: ContentCreate
) -> ContentORM:
    # 1. Store content metadata in Neon Postgres
    db_content = await content_service.create_content(db, content_create)

    # 2. Text extraction and chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(content_create.text_content)

    # 3. Generate embeddings and store in Qdrant
    client: QdrantClient = await get_qdrant_client()
    points = []
    for i, chunk in enumerate(chunks):
        embedding = await generate_embeddings(chunk)
        points.append(
            models.PointStruct(
                id=uuid.uuid4().hex,
                vector=embedding,
                payload={
                    "content_id": str(db_content.id),
                    "chunk_id": f"{db_content.id}-{i}",
                    "text": chunk,
                    "source_url": db_content.source_url,
                    ** (db_content.content_metadata if db_content.content_metadata else {})
                },
            )
        )

    if points:
        await client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)

    return db_content

from typing import List

from qdrant_client import QdrantClient
from src.embeddings.openai import generate_embeddings
from src.services.qdrant_client import get_qdrant_client
from src.ingestion.ingestion_pipeline import COLLECTION_NAME
from src.data.models import RetrievedChunk

async def retrieve_chunks(query_text: str, top_k: int = 4) -> List[RetrievedChunk]:
    client: QdrantClient = await get_qdrant_client()
    query_embedding = await generate_embeddings(query_text)

    search_result = await client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k,
        with_payload=True,
    )

    retrieved_chunks = []
    for hit in search_result:
        retrieved_chunks.append(
            RetrievedChunk(
                content_id=hit.payload["content_id"],
                chunk_id=hit.payload["chunk_id"],
                score=hit.score,
                text_snippet=hit.payload["text"],
            )
        )
    return retrieved_chunks

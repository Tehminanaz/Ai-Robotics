import os
from qdrant_client import QdrantClient, models

# Qdrant connection details from environment variables
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)

COLLECTION_NAME = "textbook_embeddings"

def get_qdrant_client():
    client = QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT,
        api_key=QDRANT_API_KEY,
    )
    return client

def ensure_collection_exists(client: QdrantClient):
    collections = client.get_collections().collections
    if not any(c.name == COLLECTION_NAME for c in collections):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE), # Assuming OpenAI embeddings size
        )
        print(f"Created Qdrant collection: {COLLECTION_NAME}")
    else:
        print(f"Qdrant collection {COLLECTION_NAME} already exists.")


if __name__ == "__main__":
    client = get_qdrant_client()
    ensure_collection_exists(client)
    print("Qdrant client initialized and collection checked.")

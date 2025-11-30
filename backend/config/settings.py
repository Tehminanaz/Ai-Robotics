from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost/robotics_db"

    # Qdrant settings
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION_NAME: str = "textbook_embeddings"

    # OpenAI settings (for RAG/LLM)
    OPENAI_API_KEY: str | None = None

settings = Settings()

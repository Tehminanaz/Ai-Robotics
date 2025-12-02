import os
from dotenv import load_dotenv, find_dotenv

# Use find_dotenv() to locate the .env file anywhere in the parent directories
load_dotenv(find_dotenv())

DATABASE_URL = os.getenv("DATABASE_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_URL = os.getenv("QDRANT_CLUSTER_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

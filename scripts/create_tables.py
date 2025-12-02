import asyncio
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import load_dotenv
load_dotenv() # Ensure .env is loaded

from src.data.database import create_db_and_tables, DATABASE_URL
from src.data.models import *

async def main():
    print(f"DEBUG (create_tables.py): DATABASE_URL = {DATABASE_URL}")
    print("Creating database tables...")
    await create_db_and_tables()
    print("Database tables created.")

if __name__ == "__main__":
    asyncio.run(main())

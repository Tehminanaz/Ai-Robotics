"""
Database migration script for adding the users table to support authentication.
"""
import asyncio
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from backend.config.database import DATABASE_URL
from backend.auth import Base


async def create_users_table():
    """Create the users table in the database."""
    # Create async engine
    engine = create_async_engine(DATABASE_URL)

    async with engine.begin() as conn:
        # Create the users table based on the UserORM model
        await conn.run_sync(Base.metadata.create_all)

    # Dispose of the engine
    await engine.dispose()

    print("Users table created successfully!")


async def check_users_table():
    """Check if the users table exists in the database."""
    engine = create_async_engine(DATABASE_URL)

    async with engine.begin() as conn:
        # Check if the users table exists
        result = await conn.execute(
            text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_name = 'users'
                );
            """)
        )
        table_exists = result.scalar()

    await engine.dispose()

    return table_exists


if __name__ == "__main__":
    print("Checking if users table exists...")
    table_exists = asyncio.run(check_users_table())

    if table_exists:
        print("Users table already exists.")
    else:
        print("Users table does not exist. Creating it now...")
        asyncio.run(create_users_table())
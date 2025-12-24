from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.data.models import ContentORM, ContentCreate, ContentBase
from typing import List, Optional
import uuid

async def create_content(db: AsyncSession, content: ContentCreate) -> ContentORM:
    db_content = ContentORM(**content.dict())
    db.add(db_content)
    await db.commit()
    await db.refresh(db_content)
    return db_content

async def get_content(db: AsyncSession, content_id: uuid.UUID) -> Optional[ContentORM]:
    result = await db.execute(select(ContentORM).filter(ContentORM.id == content_id))
    return result.scalar_one_or_none()

async def get_all_content(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[ContentORM]:
    result = await db.execute(select(ContentORM).offset(skip).limit(limit))
    return result.scalars().all()

async def update_content(db: AsyncSession, content_id: uuid.UUID, content: ContentBase) -> Optional[ContentORM]:
    db_content = await get_content(db, content_id)
    if db_content:
        for key, value in content.dict(exclude_unset=True).items():
            setattr(db_content, key, value)
        await db.commit()
        await db.refresh(db_content)
    return db_content

async def delete_content(db: AsyncSession, content_id: uuid.UUID) -> bool:
    db_content = await get_content(db, content_id)
    if db_content:
        await db.delete(db_content)
        await db.commit()
        return True
    return False

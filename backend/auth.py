"""
Authentication module for the Robotics course platform.
Implements user registration/login with custom fields for software/hardware background.
"""
from datetime import datetime, timedelta
from typing import Optional
import bcrypt
import os
import jwt
from uuid import uuid4
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Text, DateTime, Boolean
from backend.data.database import get_db

# Security schemes
security = HTTPBearer()
Base = declarative_base()

# Pydantic models
class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    software_background: Optional[str] = None
    hardware_background: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    software_background: Optional[str] = None
    hardware_background: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class UserORM(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    software_background = Column(Text, nullable=True)
    hardware_background = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    @classmethod
    async def get_user_by_email(cls, db: AsyncSession, email: str) -> Optional['UserORM']:
        """Get a user by email."""
        result = await db.execute(select(cls).filter(cls.email == email))
        return result.scalar_one_or_none()


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token."""
    from datetime import datetime, timedelta

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, os.getenv("BETTER_AUTH_SECRET", os.getenv("SECRET_KEY", "fallback_secret_key")), algorithm="HS256")
    return encoded_jwt

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[UserORM]:
    """Get a user by email."""
    result = await db.execute(select(UserORM).filter(UserORM.email == email))
    return result.scalar_one_or_none()

async def authenticate_user(db: AsyncSession, email: str, password: str) -> Optional[UserORM]:
    """Authenticate a user by email and password."""
    user = await get_user_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> UserORM:
    """Get the current user from the access token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(credentials.credentials, os.getenv("BETTER_AUTH_SECRET", os.getenv("SECRET_KEY", "fallback_secret_key")), algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = await get_user_by_email(db, email)
    if user is None:
        raise credentials_exception

    return user
"""
Middleware and security utilities for the Robotics course platform.
"""
from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from backend.auth import get_current_user
from backend.data.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession


class AuthMiddleware(BaseHTTPMiddleware):
    """
    Middleware to protect routes that require authentication.
    """
    def __init__(self, app, excluded_paths: list = None):
        super().__init__(app)
        self.excluded_paths = excluded_paths or []

    async def dispatch(self, request: Request, call_next: Callable) -> Awaitable:
        # Skip authentication for excluded paths
        if request.url.path in self.excluded_paths:
            response = await call_next(request)
            return response

        # Add your authentication logic here if needed
        # For now, this is a placeholder that passes through
        response = await call_next(request)
        return response


def require_auth():
    """
    Dependency to require authentication for specific endpoints.
    """
    async def auth_dependency():
        # This will be used as a dependency in route definitions
        # The actual authentication is handled by the get_current_user dependency
        pass
    return auth_dependency


def is_authorized_user(request: Request) -> bool:
    """
    Check if user is authorized based on session/token.
    """
    # This is a placeholder - actual implementation would check for valid token
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return True
    return False
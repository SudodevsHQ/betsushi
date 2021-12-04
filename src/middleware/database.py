from starlette.middleware.base import BaseHTTPMiddleware
from starlette.config import Config
from src.database.database import async_db_session


class DatabaseMiddleware(BaseHTTPMiddleware):
     async def dispatch(self, request, call_next):
        await async_db_session.flush()
        response = await call_next(request)
        return response
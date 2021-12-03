from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response

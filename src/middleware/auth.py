from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from src.utils.auth import firebase_app
from firebase_admin import auth


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        self.app = firebase_app

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        id_token = request.headers.get('Authorization')
        if not id_token:
            return JSONResponse(
                {'error': 'No token provided'}, status_code=401
            )

        decoded_token = auth.verify_id_token(id_token, app=self.app)
        uid = decoded_token['uid']
        if not uid:
            return JSONResponse(
                {'error': 'Invalid token'}, status_code=401
            )
        return response

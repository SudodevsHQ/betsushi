from src.utils.auth import firebase_app
from firebase_admin import auth
from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    AuthCredentials,
    SimpleUser,
)


class AuthMiddleware(AuthenticationBackend):
    async def authenticate(self, request):
        whitelist = ["/", "/webhook/do", "/webhook/get"]
        if request.url.path in whitelist:
            return
            
        try:
            id_token = request.headers["Authorization"]
            decoded_token = auth.verify_id_token(id_token, app=firebase_app)
            return AuthCredentials(["authenticated"]), \
                SimpleUser(decoded_token["uid"])
        except Exception as e:
            raise AuthenticationError(e)

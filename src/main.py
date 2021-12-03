from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, WebSocketRoute
from src.database.database import async_db_session
from src.routes.websocket import ClientWebsocketEndpoint

from src.utils.http import close_aiohttp_session

from src.routes.create_user import create_user
from src.routes.create_virtual_account import create_account

async def init_database():
    await async_db_session.init()
    await async_db_session.create_all()


async def homepage(request):
    return JSONResponse({"hello": "world"})


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/create_user", create_user, methods=["POST"]),
        Route("/create_virtual_account", create_account, methods=["POST"]),
        WebSocketRoute("/ws", ClientWebsocketEndpoint),
    ],
    on_startup=[init_database],
    on_shutdown=[close_aiohttp_session],
)

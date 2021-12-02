import aiohttp
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from src.models.request.razorpayx import CreateContactRequest
from src.extensions import create_contact
from src.database.database import async_db_session
session: aiohttp.ClientSession = aiohttp.ClientSession()


async def init_database():
    await async_db_session.init()
    await async_db_session.create_all()


async def close_aiohttp_session():
    global session
    session = await session.close()


async def homepage(request):
    return JSONResponse({"hello": "world"})


async def create_contact_route(request):
    json = await request.json()
    request = CreateContactRequest(
        name=json["name"],
        contact=json["contact"],
        email=json["email"],
        type=json["type"],
        reference_id=json["reference_id"],
        notes=json["notes"],
    )
    response = await create_contact(session=session, data=request)
    return JSONResponse(response.__dict__)


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/create_contact", create_contact_route, methods=["POST"]),
    ],
    on_startup=[init_database],
    on_shutdown=[close_aiohttp_session],
)

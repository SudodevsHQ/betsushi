from starlette.responses import JSONResponse
from src.database.models.users import User


async def create_user(request):
    json = await request.json()
    await User.create(
        id=json.get('id'),
        full_name=json.get("name"),
        currency=json.get("currency", "USD"),
    )
    response = {
        "id": json.get('id'),
        "full_name": json.get("name"),
        "currency": json.get("currency", "USD"),
    }
    return JSONResponse(response)

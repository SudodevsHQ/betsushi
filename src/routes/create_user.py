from starlette.responses import JSONResponse
from src.database.models.users import User


async def create_user(request):
    json = await request.json()
    user_id = json.get('id')
    user = await User.get(user_id)
    if user: 
        response = {
            "id": user.id,
            "full_name": user.full_name,
            "currency": user.currency,          
        }
    else:
        await User.create(
            id=user_id,
            full_name=json.get("name"),
            currency=json.get("currency", "USD"),
        )
        response = {
            "id": json.get('id'),
            "full_name": json.get("name"),
            "currency": json.get("currency", "USD"),
        }
    return JSONResponse(response)

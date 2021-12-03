from src.models.request.razorpayx import CreateContactRequest
from starlette.responses import JSONResponse

from src.extensions import create_contact
from src.utils.http import session
from src.database.models.users import User


async def create_virtual_account(request):
    json = await request.json()
    request = CreateContactRequest(
        name=json.get("name"),
        contact=json.get("contact"),
        email=json.get("email"),
        type=json.get("type"),
        reference_id=json.get("reference_id"),
        notes=json.get("notes"),
    )
    contact = await create_contact(session=session, data=request)
    await User.create(full_name=contact.name, currency="USD")
    
    return JSONResponse(contact.__dict__)

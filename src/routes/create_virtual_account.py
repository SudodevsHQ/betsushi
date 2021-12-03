from starlette.responses import JSONResponse
from src.extensions import create_virtual_account
from src.extensions import create_contact

from src.utils.http import session

from src.models.request.razorpay import VirtualAccoutRequest
from src.models.request.razorpayx import CreateContactRequest

from src.database.models.users import User
from src.database.models.account import Account


async def create_account(request):
    json = await request.json()
    user_id = json.get("user_id")

    if not user_id:
        return JSONResponse({"message": "user_id is required"}, status_code=400)

    else:
        try:
            user: User = await User.get(user_id)

            contact_request = CreateContactRequest(
                name=user.full_name,
                contact=json.get("contact"),
                email=json.get("email"),
                type=json.get("type"),
                reference_id=json.get("reference_id"),
                notes=json.get("notes"),
            )
            contact = await create_contact(session=session, data=contact_request)
        except Exception as e:
            return JSONResponse(
                {"message": str(e), "error": "Could not create Contact"},
                status_code=400,
            )

        receivers = {
            "types": ["bank_account"]
        }
        try:
            account_request = VirtualAccoutRequest(
                receivers=receivers,
                close_by=None,
                notes=json.get("notes"),
                description=json.get("description"),
                customer_id=contact.id,
            )
            virtual_account = await create_virtual_account(
                session=session, data=account_request
            )
            print(account_request, "\n\n")
            print(virtual_account)
            await Account.create(balance=0, contact_id=contact.id, user_id=user_id)
        except Exception as e:
            return JSONResponse(
                {"message": str(e), "error": "Could not create Account"},
                status_code=400,
            )

        return JSONResponse(virtual_account.__dict__)

from starlette.responses import JSONResponse
from uuid import uuid4
from src.extensions import create_virtual_account
from src.extensions import create_contact

from src.utils.http import session

from src.models.request.razorpay import VirtualAccoutRequest
from src.models.request.razorpayx import CreateContactRequest

from src.database.models.users import User
from src.database.models.account import Account
from src.database.models.upi import UPI


async def create_account(request):
    json = await request.json()
    user_id = json.get("user_id")

    if not user_id:
        return JSONResponse({"message": "user_id is required"}, status_code=400)

    else:
        try:
            user: User = await User.get(user_id)
            print(user)
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
            print(str(e))
            return JSONResponse(
                {"message": str(e), "error": "Could not create Contact"},
                status_code=400,
            )

        # receivers = {
        #     "types": ["vpa"],
        #     "vpa": {
        #         "descriptor": user.full_name.replace(" ", "-"),
        #     },
        # }
        try:
            # account_request = VirtualAccoutRequest(
            #     receivers=receivers,
            #     close_by=None,
            #     notes=json.get("notes"),
            #     description=json.get("description"),
            #     customer_id=contact.id,
            # )
            # virtual_account = await create_virtual_account(
            #     session=session, data=account_request
            # )
            # MOCK ACCOUNT CREATION
            upi_id = ''
            
            upi_id = await UPI.get_by_user_id(user_id)
            if upi_id:
                account = await Account.get_by_user_id(user_id)
                return JSONResponse({
                    "user_id": user_id,
                    "account_id": account.id,
                    "balance": int(account.balance),
                    "upi_id": upi_id.id,
                })
            else:
                account_id = str(uuid4())
                upi_id = f"{user.full_name.lower().replace(' ', '-')}@okicici"
                
                await Account.create(id=account_id, balance=0, contact_id=contact.id, user_id=user_id)
                await UPI.create(id=upi_id, user_id=user_id)
    
        except Exception as e:
            print('2')
            return JSONResponse(
                {"message": str(e), "error": "Could not create Account"},
                status_code=400,
            )

        return JSONResponse({
            "user_id": user_id,
            "account_id": account_id,
            "balance": 0,
            "upi_id": upi_id,
        })

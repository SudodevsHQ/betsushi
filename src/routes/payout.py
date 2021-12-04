from starlette.responses import JSONResponse
from src.database.models.account import Account
from src.models.request.razorpayx import (
    CreateFundAccountRequest,
    CreatePayoutRequest,
    Vpa,
)
from src.extensions.razorpayx import create_fund_account, create_payout
from src.utils.http import session

async def payout(request):
    """
    Create a new payout
    """

    json = await request.json()
    account: Account = await Account.get_by_user_id(json["user_id"])
    fund_account_request = CreateFundAccountRequest(
        account_type="vpa", contact_id=account.contact_id, vpa=Vpa(address=json["upi"]).__dict__
    )
    print(account.contact_id)
    fund_account_response = await create_fund_account(session, fund_account_request)
    

    data = CreatePayoutRequest(
        account_number="2323230077200976",
        fund_account_id=fund_account_response.id,
        amount=json["amount"],
        currency="INR",
        mode="UPI",
        purpose="vendor bill",
        queue_if_low_balance=True,
        reference_id=f"{fund_account_response.vpa.address}",
        narration=f"UPI transfer",
        notes={
            "user_id": account.user_id,
            "upi_id": fund_account_response.vpa.address
        }
    )
    response = await create_payout(session, data)
    return JSONResponse(response.__dict__)

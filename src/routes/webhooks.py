from dacite import from_dict
from sqlalchemy.sql.functions import user
from src.database.models.account import Account
from src.database.models.transaction import Transaction
from src.models.response.razorpayx import PayoutsPayload
from src.models.response.razorpay import PaymentsPayload
from src.database.models.transaction import Transaction
from src.utils.transactions import get_all_transactions

from src.routes.websocket import ClientWebsocketEndpoint
from starlette.websockets import WebSocket, WebSocketState
from starlette.responses import JSONResponse


async def razorpayx_webhook(request):
    response = await request.json()
    print(response, "do")
    data = from_dict(data_class=PayoutsPayload, data=response)
    user_id = data.payload.payout.entity.notes["user_id"]
    upi = data.payload.payout.entity.notes["upi_id"]
    status = data.event.split(".")[1]
    await Transaction.create(
        razorpay_tid=data.payload.payout.entity.id,
        amount=data.payload.payout.entity.amount,
        user_id=user_id,
        type="send",
        fund_account_id=data.payload.payout.entity.fund_account_id,
        upi=upi,
        status=status,
    )
    if status == "processed":
        account = await Account.get_by_user_id(user_id)
        await Account.update_by_user_id(
            user_id, balance=account.balance - data.payload.payout.entity.amount
        )
        print(f"Deducted {data.payload.payout.entity.amount} from {user_id}")
    # send to websocket here
    websocket = ClientWebsocketEndpoint.user_socket_map.get(user_id)

    if websocket and websocket.client_state == WebSocketState.CONNECTED:
        transactions = await get_all_transactions(user_id)
        account = await Account.get_by_user_id(user_id)
   
        websocket_response = {
            "user_id": user_id,
            "transactions": transactions,
            "balance": float(account.balance)
        }
        await websocket.send_json(websocket_response)
        return JSONResponse({"Success": "Success"}, status_code=200)

    else:
        return JSONResponse({"Error": "Websocket is already closed"}, status_code=500)


async def razorpay_webhook(request):
    
    response = await request.json()
    print(response, "get")
    data: PaymentsPayload = from_dict(data_class=PaymentsPayload, data=response)
    
    user_id = data.payload.payment.entity.notes.user_id
    upi = data.payload.payment.entity.notes.upi_id
    status = data.event.split(".")[1]
    await Transaction.create(
        razorpay_tid=data.payload.payment.entity.id,
        amount=data.payload.payment.entity.amount / 100,
        user_id=user_id,
        type="receive",
        fund_account_id=None,
        upi=upi,
        status=data.event.split(".")[1],
    )

    if status == "authorized":
        account = await Account.get_by_user_id(user_id)
        await Account.update_by_user_id(
            user_id, balance=float(account.balance) + data.payload.payment.entity.amount / 100
        )
        print(f"Credited {data.payload.payment.entity.amount // 100} to {user_id}")

    # send to websocket here
    websocket = ClientWebsocketEndpoint.user_socket_map.get(user_id)

    if websocket and websocket.client_state == WebSocketState.CONNECTED:
        transactions = await get_all_transactions(user_id)
        account = await Account.get_by_user_id(user_id)
   
        websocket_response = {
            "user_id": user_id,
            "transactions": transactions,
            "balance": float(account.balance)
        }
        await websocket.send_json(websocket_response)
        return JSONResponse({"Success": "Success"}, status_code=200)

    else:
        return JSONResponse({"Error": "Websocket is already closed"}, status_code=500)

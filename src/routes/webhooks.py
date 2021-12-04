from dacite import from_dict
from sqlalchemy.sql.functions import user
from src.database.models.account import Account
from src.database.models.transaction import Transaction
from src.models.response.razorpayx import PayoutsPayload
from src.routes.websocket import ClientWebsocketEndpoint
from starlette.websockets import WebSocket, WebSocketState
from starlette.responses import JSONResponse


async def razorpayx_webhook(request):
    response = await request.json()
    data = from_dict(data_class=PayoutsPayload, data=response)
    thing = data.payload.payout.entity.reference_id.split(" ")
    user_id = thing[0]
    upi = thing[1]
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
        account = Account.get_by_user_id(user_id)
        await Account.update_by_user_id(
            user_id, balance=account.balance - data.payload.payout.entity.amount
        )
        print(f"Deducted {data.payload.payout.entity.amount} from {user_id}")
    # send to websocket here
    websocket = ClientWebsocketEndpoint.user_socket_map.get(user_id)

    if websocket and websocket.client_state == WebSocketState.CONNECTED:
        await websocket.send_json(response)
        return JSONResponse({"Success": "Success"}, status_code=200)

    else:
        return JSONResponse({"Error": "Websocket is already closed"}, status_code=500)


async def razorpay_webhook(request):
    response = await request.json()
    data = from_dict(data_class=PayoutsPayload, data=response)
    thing = data.payload.payout.entity.reference_id.split(" ")
    user_id = thing[0]
    upi = thing[1]
    await Transaction.create(
        razorpay_tid=data.payload.payout.entity.id,
        amount=data.payload.payout.entity.amount,
        user_id=user_id,
        type="receive",
        fund_account_id=data.payload.payout.entity.fund_account_id,
        upi=upi,
        status=data.event.split(".")[1],
    )

    # send to websocket here
    websocket = ClientWebsocketEndpoint.user_socket_map.get(user_id)

    if websocket and websocket.client_state == WebSocketState.CONNECTED:
        await websocket.send_json(response)
        return JSONResponse({"Success": "Success"}, status_code=200)

    else:
        return JSONResponse({"Error": "Websocket is already closed"}, status_code=500)

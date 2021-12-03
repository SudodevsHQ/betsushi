from dacite import from_dict
from database.models.transaction import Transaction
from src.models.response.razorpayx import PayoutsPayload


async def razorpayx_webhook(request):
    response = await request.json()
    data = from_dict(data_class=PayoutsPayload, data=response)
    thing = data.payload.payout.entity.reference_id.split(" ")
    user_id = thing[0]
    upi = thing[1]
    await Transaction.create(
        razorpay_tid=data.payload.entity.id,
        amount=data.payload.entity.amount,
        user_id=user_id,
        type="send",
        fund_account_id=data.payload.payout.entity.fund_account_id,
        upi=upi,
        status=data.event.split(".")[1],
    )
    # send to websocket here


async def razorpay_webhook(request):
    response = await request.json()
    data = from_dict(data_class=PayoutsPayload, data=response)
    thing = data.payload.payout.entity.reference_id.split(" ")
    user_id = thing[0]
    upi = thing[1]
    await Transaction.create(
        razorpay_tid=data.payload.entity.id,
        amount=data.payload.entity.amount,
        user_id=user_id,
        type="receive",
        fund_account_id=data.payload.payout.entity.fund_account_id,
        upi=upi,
        status=data.event.split(".")[1],
    )
    # send to websocket here


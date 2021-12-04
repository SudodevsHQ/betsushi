from typing import Any
from dacite import data
from sqlalchemy.sql.sqltypes import DateTime
from src.database.models.transaction import Transaction
from starlette.responses import JSONResponse
from dataclasses import dataclass

def transaction_to_dict(transaction: Transaction) -> dict:
    """
    Converts a transaction object to a dictionary.
    """
    return {
        "razorpay_tid": transaction.razorpay_tid,
        "user_id": transaction.user_id,
        "amount": int(transaction.amount),
        "type": str(transaction.type).split(".")[1],
        "created_at": transaction.created_at,
        "fund_account_id": transaction.fund_account_id,
        "upi": transaction.upi,
        "status": str(transaction.status).split(".")[1],
        "created_at": str(transaction.created_at),
    }

async def fetch_latest_transactions(request):
    """
    Returns the latest transactions from the database.
    """
    user_id = request.query_params.get('user_id')
    transactions = await Transaction.fetch_transactions(user_id)
    print(transactions)
    results = []
    tids = []
    for transaction in transactions:
        if transaction[0].razorpay_tid not in tids:
            results.append(transaction_to_dict(transaction[0]))
            tids.append(transaction[0].razorpay_tid)
    return JSONResponse({"status": results})
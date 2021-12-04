from src.database.models.transaction import Transaction
from src.database.models.transaction import Transaction


def transaction_to_dict(transaction: Transaction) -> dict:
    """
    Converts a transaction object to a dictionary.
    """
    return {
        "razorpay_tid": transaction.razorpay_tid,
        "user_id": transaction.user_id,
        "amount": float(transaction.amount),
        "type": str(transaction.type).split(".")[1],
        "created_at": transaction.created_at,
        "fund_account_id": transaction.fund_account_id,
        "upi": transaction.upi,
        "status": str(transaction.status).split(".")[1],
        "created_at": str(transaction.created_at),
    }


async def get_all_transactions(user_id: str):
    transactions = await Transaction.fetch_transactions(user_id)
    results = []
    tids = []
    for transaction in transactions:
        if transaction[0].razorpay_tid not in tids:
            results.append(transaction_to_dict(transaction[0]))
            tids.append(transaction[0].razorpay_tid)
    return results

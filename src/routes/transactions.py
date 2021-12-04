from typing import Any
from dacite import data
from sqlalchemy.sql.sqltypes import DateTime
from src.database.models.transaction import Transaction
from starlette.responses import JSONResponse
from dataclasses import dataclass
from src.utils.transactions import transaction_to_dict
from src.utils.transactions import get_all_transactions


async def fetch_latest_transactions(request):
    """
    Returns the latest transactions from the database.
    """
    user_id = request.query_params.get('user_id')
    transactions = await Transaction.fetch_transactions(user_id)
    print(transactions)
    results = await get_all_transactions(user_id)
    return JSONResponse({"status": results})
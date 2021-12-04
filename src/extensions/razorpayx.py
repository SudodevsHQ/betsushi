import aiohttp
from src.utils.constants import \
    RAZORPAY_BASE_URL, RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

from src.models.request.razorpayx import \
    CreateContactRequest, CreateFundAccountRequest, CreatePayoutRequest
from src.models.response.razorpayx import (
    CreateContactResponse,
    CreateFundAccountResponse, CreatePayoutResponse
)
from dacite import from_dict

from aiohttp import ClientSession


async def create_contact(
    session: ClientSession, data: CreateContactRequest
) -> CreateContactResponse:
    """
    Create a contact.
    """
    url = RAZORPAY_BASE_URL + "/contacts"

    async with session.post(
        url,
        json=data.__dict__,
        auth=aiohttp.BasicAuth(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET),
    ) as resp:
        response = await resp.json()
        return from_dict(data_class=CreateContactResponse, data=response)


async def create_fund_account(
    session: ClientSession, data: CreateFundAccountRequest
) -> CreateFundAccountResponse:
    """
    Create a fund account.
    """
    url = RAZORPAY_BASE_URL + "/fund_accounts"

    async with session.post(
        url,
        json=data.__dict__,
        auth=aiohttp.BasicAuth(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET),
    ) as resp:
        response = await resp.json()
        print(response, resp.status)
        return from_dict(data_class=CreateFundAccountResponse, data=response)


async def create_payout(
    session: ClientSession, data: CreatePayoutRequest
) -> CreatePayoutResponse:
    """
    Create a payout.
    """
    url = RAZORPAY_BASE_URL + "/payouts"

    async with session.post(
        url,
        json=data.__dict__,
        auth=aiohttp.BasicAuth(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET),
    ) as resp:
        response = await resp.json()
        print(response, resp.status)
        return from_dict(data_class=CreatePayoutResponse, data=response)

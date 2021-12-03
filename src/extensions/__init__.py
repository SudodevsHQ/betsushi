from aiohttp.client import ClientSession
from src.models.request.razorpayx import CreateContactRequest
from src.models.request.razorpay import VirtualAccoutRequest
from src.extensions import razorpayx
from src.extensions import razorpay


async def create_contact(session: ClientSession, data: CreateContactRequest):
    contact = await razorpayx.create_contact(session, data)
    return contact


async def create_virtual_account(session: ClientSession, data: VirtualAccoutRequest):
    account = await razorpay.create_virtual_account(session, data)
    return account
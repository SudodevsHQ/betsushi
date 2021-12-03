from aiohttp.client import ClientSession
from src.models.request.razorpayx import CreateContactRequest
from src.extensions import razorpayx


async def create_contact(session: ClientSession, data: CreateContactRequest):
    contact = await razorpayx.create_contact(session, data)
    return contact

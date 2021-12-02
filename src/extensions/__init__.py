from aiohttp.client import ClientSession
from src.models.request.razorpayx import CreateContactRequest
from src.extensions import razorpayx

from src.database.models.users import User


async def create_contact(session: ClientSession, data: CreateContactRequest):
    contact = await razorpayx.create_contact(session, data)
    await User.create(full_name=contact.name, currency="USD")
    return contact

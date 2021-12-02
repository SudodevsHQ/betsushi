import aiohttp
from src.utils.constants import RAZORPAY_BASE_URL, RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

from src.models.request.razorpayx import CreateContactRequest
from src.models.response.razorpayx import CreateContactResponse
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

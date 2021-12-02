import aiohttp
from src.utils.constants import RAZORPAY_BASE_URL
from src.models.request.razorpayx import CreateContactRequest
from src.models.response.razorpayx import CreateContactResponse
from dacite import from_dict

from aiohttp import ClientSession

async def create_contact(session: ClientSession, data: CreateContactRequest) -> CreateContactResponse:
    """
    Create a contact.
    """
    url = RAZORPAY_BASE_URL + "/contacts"
    
    async with session.post(url, json=data.__dict__, auth=aiohttp.BasicAuth('rzp_test_CqopUr55ZgFmQ9', 'v4WeOs3JuDnnmyIvoSf7PFMF')) as resp:
        response =  await resp.json()
        return from_dict(data_class=CreateContactResponse, data=response)
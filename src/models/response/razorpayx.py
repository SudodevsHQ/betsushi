from dataclasses import dataclass
from typing import Dict

from src.models.request.razorpayx import Vpa


@dataclass
class CreateContactResponse:
    id: str
    entity: str
    name: str
    contact: str
    email: str
    type: str
    reference_id: str
    batch_id: str
    active: bool
    notes: Dict[str, str]
    created_at: int


@dataclass
class CreateFundAccountResponse:
    id: str
    entity: str
    contact_id: str
    account_type: str
    vpa: Vpa
    active: bool
    batch_id: str
    created_at: int


@dataclass
class CreatePayoutResponse:
    id: str
    entity: str
    fund_account_id: str
    amount: int
    currency: str
    notes: Dict[str, str]
    fees: int
    tax: int
    status: str
    utr: str
    mode: str
    purpose: str
    reference_id: str
    narration: str
    batch_id: str
    failure_reason: str
    created_at: int

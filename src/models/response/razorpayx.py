from dataclasses import dataclass
from typing import Dict, Optional

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
    active: bool
    notes: Dict[str, str]
    created_at: int
    batch_id: Optional[str] = None


@dataclass
class CreateFundAccountResponse:
    id: str
    entity: str
    contact_id: str
    account_type: str
    vpa: Vpa
    active: bool
    created_at: int
    batch_id: Optional[str] = None


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
    failure_reason: str
    created_at: int
    batch_id: Optional[str] = None

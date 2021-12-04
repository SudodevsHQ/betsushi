from dataclasses import dataclass
from typing import Dict, Optional, List

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
    created_at: int
    notes: Optional[list]
    batch_id: Optional[str] = None


@dataclass
class CreateFundAccountResponse:
    active: Optional[bool] = None
    created_at: Optional[int] = None
    vpa: Optional[Vpa] = None
    batch_id: Optional[str] = None
    id: Optional[str] = None
    entity: Optional[str] = None
    contact_id: Optional[str] = None
    account_type: Optional[str] = None


@dataclass
class CreatePayoutResponse:
    id: Optional[str] = None
    entity: Optional[str] = None
    fund_account_id: Optional[str] = None
    amount: Optional[int] = None
    currency: Optional[str] = None
    fees: Optional[int] = None
    tax: Optional[int] = None
    status: Optional[str] = None
    utr: Optional[str] = None
    mode: Optional[str] = None
    purpose: Optional[str] = None
    reference_id: Optional[str] = None
    narration: Optional[str] = None
    failure_reason: Optional[str] = None
    created_at: Optional[int] = None
    batch_id: Optional[str] = None


@dataclass
class Error:
    description: None
    source: None
    reason: None


@dataclass
class Entity:
    batch_id: None
    reference_id: Optional[str] = None
    id: Optional[str] = None
    entity: Optional[str] = None
    fund_account_id: Optional[str] = None
    amount: Optional[int] = None
    currency: Optional[str] = None
    notes: Optional[Dict[str, str]] = None
    fees: Optional[int] = None
    tax: Optional[int] = None
    status: Optional[str] = None
    purpose: Optional[str] = None
    utr: Optional[str] = None
    mode: Optional[str] = None
    narration: Optional[str] = None
    failure_reason: Optional[str] = None
    created_at: Optional[int] = None
    fee_type: Optional[str] = None
    error: Optional[Error] = None


@dataclass
class Payout:
    entity: Optional[Entity] = None


@dataclass
class Payload:
    payout: Optional[Payout] = None


@dataclass
class PayoutsPayload:
    entity: Optional[str] = None
    account_id: Optional[str] = None
    event: Optional[str] = None
    contains: Optional[List[str]] = None
    payload: Optional[Payload] = None
    created_at: Optional[int] = None

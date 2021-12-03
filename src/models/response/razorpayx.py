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


@dataclass
class Error:
    description: None
    source: None
    reason: None


@dataclass
class Entity:
    reference_id: None
    batch_id: None
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

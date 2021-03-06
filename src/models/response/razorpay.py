from dataclasses import dataclass
from typing import Optional, List, Any, Dict



@dataclass
class Receiver:
    id: Optional[str] = None
    entity: Optional[str] = None
    username: Optional[str] = None
    handle: Optional[str] = None
    address: Optional[str] = None


@dataclass
class VirtualAccoutResponse:
    amount_expected: Optional[str] = None
    closed_at: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    entity: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[List[Any]] = None
    amount_paid: Optional[int] = None
    customer_id: Optional[str] = None
    receivers: Optional[List[Receiver]] = None
    close_by: Optional[int] = None
    created_at: Optional[int] = None



@dataclass
class AcquirerData:
    auth_code: Optional[int] = None


@dataclass
class Notes:
    user_id: Optional[str] = None
    upi_id: Optional[str] = None


@dataclass
class Entity:
    order_id: None
    invoice_id: None
    refund_status: None
    bank: None
    wallet: None
    vpa: None
    tax: None
    error_code: None
    error_description: None
    error_source: None
    error_step: None
    error_reason: None
    id: Optional[str] = None
    entity: Optional[str] = None
    amount: Optional[int] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    international: Optional[bool] = None
    method: Optional[str] = None
    amount_refunded: Optional[int] = None
    captured: Optional[bool] = None
    description: Optional[str] = None
    card_id: Optional[str] = None
    email: Optional[str] = None
    contact: Optional[str] = None
    notes: Optional[Notes] = None
    fee: Optional[int] = None
    created_at: Optional[int] = None


@dataclass
class Payment:
    entity: Optional[Entity] = None


@dataclass
class Payload:
    payment: Optional[Payment] = None


@dataclass
class PaymentsPayload:
    entity: Optional[str] = None
    account_id: Optional[str] = None
    event: Optional[str] = None
    contains: Optional[List[str]] = None
    payload: Optional[Payload] = None
    created_at: Optional[int] = None

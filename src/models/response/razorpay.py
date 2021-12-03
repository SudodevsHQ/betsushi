from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass
class Receiver:
    id: Optional[str] = None
    entity: Optional[str] = None
    username: Optional[str] = None
    handle: Optional[str] = None
    address: Optional[str] = None


@dataclass
class VirtualAccoutResponse:
    amount_expected: None
    closed_at: None
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

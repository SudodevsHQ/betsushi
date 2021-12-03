from dataclasses import dataclass
from typing import Dict


@dataclass
class CreateContactRequest:
    name: str
    email: str
    contact: str
    type: str
    reference_id: str
    notes: Dict[str, str]


@dataclass
class Vpa:
    address: str


@dataclass
class CreateFundAccountRequest:
    accounttype: str
    contactid: str
    vpa: Vpa


@dataclass
class CreatePayoutRequest:
    account_number: str
    fund_account_id: str
    amount: int
    currency: str
    mode: str
    purpose: str
    queue_if_low_balance: bool
    reference_id: str
    narration: str
    notes: Dict[str, str]

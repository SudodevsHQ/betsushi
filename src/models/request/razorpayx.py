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
from dataclasses import dataclass
from typing import Dict

@dataclass
class CreateContactResponse:
    id: str
    entity: str
    name: str
    contact: str
    email: str
    type: str
    reference_id: str
    batch_id: None
    active: bool
    notes: Dict[str, str]
    created_at: int

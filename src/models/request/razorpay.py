from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Receiver:
    types: List[str]
    vpa: Dict[str, str]


@dataclass
class VirtualAccoutRequest:
    receivers: Dict[str, Receiver]
    close_by: Optional[str] = None
    notes: Optional[Dict[str, str]] = None
    customer_id: Optional[str] = None
    description: Optional[str] = None

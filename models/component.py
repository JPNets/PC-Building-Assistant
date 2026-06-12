from pydantic import BaseModel
from typing import Optional, List

class Component(BaseModel):
    id: str
    name: str
    brand: Optional[str]
    price: float
    performance_score: Optional[float]
    power_draw: Optional[float]
    # Additional fields are kept dynamic
    extra: Optional[dict] = None

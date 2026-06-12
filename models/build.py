from pydantic import BaseModel
from typing import Dict, Any, List

class Build(BaseModel):
    name: str
    components: Dict[str, Any]
    total_price: float
    total_power: float
    scores: Dict[str, float]
    compatibility: Dict[str, str]

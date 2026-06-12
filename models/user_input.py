from pydantic import BaseModel
from typing import Optional, List

class UserInput(BaseModel):
    budget: float
    country: Optional[str] = "US"
    use_case: str
    resolution: str
    target_fps: Optional[int] = 60
    preferred_cpu: Optional[str]
    preferred_gpu: Optional[str]
    existing_components: Optional[List[str]] = []
    form_factor: Optional[str] = "ATX"
    ram_gb: Optional[int] = 16
    storage_gb: Optional[int] = 1000
    rgb: Optional[bool] = False
    noise_sensitive: Optional[bool] = False
    upgrade_priority: Optional[int] = 3
    power_efficiency_priority: Optional[int] = 3

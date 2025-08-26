from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalyticsResponse(BaseModel):
    id: int
    ip_address: Optional['str'] = None
    user_agent: Optional['str'] = None
    timestamp: datetime

    class Config:
        orm_mode = True
from pydantic import BaseModel
from typing import Optional, List
from schemas.link import LinkResponse

class PageCreate(BaseModel):
    name: str               # slug for URL
    title: str              # display title
    description: Optional[str] = None

class PageUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class PageResponse(BaseModel):
    id: int
    name: str
    title: str
    description: Optional[str]
    user_id: int
    links: List[LinkResponse] = []

    class Config:
        orm_mode = True

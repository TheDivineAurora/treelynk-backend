from pydantic import BaseModel, HttpUrl
from typing import Optional


class LinkCreate(BaseModel):
    title: str
    url: HttpUrl
    category: Optional[str] = None
    page_id: int

class LinkUpdate(BaseModel):
    title: str
    url: HttpUrl
    category: Optional[str] = None
    page_id: int

class LinkResponse(BaseModel):
    id: int
    title: str
    url: HttpUrl
    category: Optional[str] = None
    short_code: str
    page_id: int

    class Config:
        orm_mode = True

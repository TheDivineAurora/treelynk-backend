from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from core.deps import get_db, get_current_user
from models.link import Link
from models.analytics import Analytics
from schemas.analytics import AnalyticsResponse
from typing import List

router = APIRouter(
    prefix = "/analytics",
    tags = ["Analytics"],
    dependencies = [Depends(get_current_user)]
)

@router.get("/link/{link_id}", response_model=List[AnalyticsResponse])
def get_analytics(link_id: int, db: Session = Depends(get_db)):
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(404, "Link not found")

    return link.analytics

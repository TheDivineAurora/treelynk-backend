from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from core.deps import get_db, get_current_user
from models.link import Link
from models.analytics import Analytics

router = APIRouter(
    prefix = "/l",
    tags = ["redirect"],
    dependencies = [Depends(get_current_user)]
)

@router.get("/{short_code}")
def redirect_link(short_code: str, request: Request, db: Session = Depends(get_db)):
    link = db.query(Link).filter(Link.short_code == short_code).first()
    if not link:
        raise HTTPException(404, "Link not found")

    analytics = Analytics(
        link_id=link.id,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    db.add(analytics)
    db.commit()

    return RedirectResponse(url=link.url)
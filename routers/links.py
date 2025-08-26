from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.deps import get_db, get_current_user
from models.link import Link
from schemas.link import LinkCreate, LinkUpdate, LinkResponse
from utils.shortener import generate_short_code
from typing import List

router = APIRouter(
    prefix = "/links",
    tags = ["Links"],
    dependencies = [Depends(get_current_user)]
)

@router.post("/", response_model = LinkResponse)
def create_link(link: LinkCreate, db: Session = Depends(get_db)):
    short_code = generate_short_code()
    # print(link)
    new_link = Link(
        title = link.title,
        url = str(link.url),
        category = link.category,
        page_id = link.page_id,
        short_code = short_code
    )
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link

@router.get("/page/{page_id}", response_model = List[LinkResponse])
def get_links_for_page(page_id: int, db: Session = Depends(get_db)):
    return db.query(Link).filter(Link.page_id == page_id).all()

@router.put("/{link_id}", response_model = LinkResponse)
def update_link(link_id: int, link: LinkUpdate, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.id == link_id).first()
    if not db_link:
        raise HTTPException(404, "Link not found")
    
    for key, value in link.model_dump(exclude_unset=True).items():
        if key == "url" and value is not None:
            value = str(value)
        setattr(db_link, key, value)

    db.commit()
    db.refresh(db_link)
    return db_link

@router.delete("/{link_id}")
def delete_link(link_id: int, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.id == link_id).first()
    if not db_link:
        raise HTTPException(404, "Link not found")

    db.delete(db_link)
    db.commit()
    return {"message": "Link deleted"}

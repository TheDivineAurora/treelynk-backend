from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core.deps import get_db, get_current_user
from models.page import Page
from models.user import User
from schemas.page import PageCreate, PageUpdate, PageResponse

router = APIRouter(
    prefix="/pages",
    tags=["Pages"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model = PageResponse)
def create_page(page: PageCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing = db.query(Page).filter(Page.user_id == current_user.id, Page.name == page.name).first()
    if existing:
        raise HTTPException(400, "Page with this name already exists")

    new_page = Page(
        name=page.name,
        title=page.title,
        description=page.description,
        user_id=current_user.id
    )
    db.add(new_page)
    db.commit()
    db.refresh(new_page)
    return new_page

@router.get("/", response_model=List[PageResponse])
def get_user_pages(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Page).filter(Page.user_id == current_user.id).all()

@router.get("/{page_id}", response_model=PageResponse)
def get_page(page_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    page = db.query(Page).filter(Page.id == page_id, Page.user_id == current_user.id).first()
    if not page:
        raise HTTPException(404, "Page not found")
    return page

@router.put("/{page_id}", response_model=PageResponse)
def update_page(page_id: int, page_update: PageUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    page = db.query(Page).filter(Page.id == page_id, Page.user_id == current_user.id).first()
    if not page:
        raise HTTPException(404, "Page not found")

    for key, value in page_update.model_dump(exclude_unset=True).items():
        setattr(page, key, value)

    db.commit()
    db.refresh(page)
    return page

@router.delete("/{page_id}")
def delete_page(page_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    page = db.query(Page).filter(Page.id == page_id, Page.user_id == current_user.id).first()
    if not page:
        raise HTTPException(404, "Page not found")

    db.delete(page)
    db.commit()
    return {"message": "Page deleted successfully"}

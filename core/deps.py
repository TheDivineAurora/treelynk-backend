from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from core.database import SessionLocal
from core.security import decode_access_token
from models.user import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    # httpOnly cookie is there, decode jwt from cookie, validate user id in payload, then query user from db and return
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(401, "Not authenticated")

    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(401, "Invalid or expired token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(401, "Invalid token payload")
    
    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(404, "User not found")
    
    return user
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
from core.database import SessionLocal
from core.security import (
    hash_password, verify_password,
    create_access_token, create_refresh_token,
    decode_access_token
)
from core.deps import get_db
from models.user import User
from schemas.user import UserSignUp, UserSignIn, TokenResponse, UserResponse
from datetime import timedelta

router = APIRouter(prefix = "/auth", tags = ["Auth"])

@router.post("/signup", response_model = UserResponse)
def signup(user: UserSignUp, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(400, "Email already registered")
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(400, "Username already taken")

    hashed_pw = hash_password(user.password)

    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(user: UserSignIn, db: Session = Depends(get_db), response: Response = None):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(401, "Invalid credentials")

    access_token = create_access_token({"sub": str(db_user.id)})
    refresh_token = create_refresh_token({"sub": str(db_user.id)})

    response.set_cookie("access_token", value = access_token, httponly=True, secure = True, max_age=1800, samesite="lax")
    response.set_cookie("refresh_token", value = refresh_token, httponly=True, secure = True, max_age=604800, samesite="lax")

    return {"message": "Login successful"}

@router.get("/me", response_model=UserResponse)
def read_me(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(401, "Not authenticated")

    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(401, "Invalid or expired token")

    user_id = int(payload.get("sub"))
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")

    return user

@router.post("/refresh")
def refresh(request: Request, response: Response):
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(401, "Refresh token missing")

    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(401, "Invalid refresh token")

    new_access = create_access_token({"sub": payload.get("sub")})
    response.set_cookie("access_token", value = new_access, httponly=True, secure = True, max_age=1800, samesite="lax")

    return {"message": "Access token refreshed"}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Logged out successfully"}

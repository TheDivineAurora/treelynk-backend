from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str

    class Config:
        orm_mode = True

class TokenResponse(BaseModel): 
    access_token : str
    token_type : str = "bearer"
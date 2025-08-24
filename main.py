from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine, Base
from sqlalchemy import text
from routers import auth
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("Connection to Database is Successful")
    except Exception as e:
        print("Database Connection Failed: ", e)
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(auth.router, prefix = "/auth", tags = ["Auth"])

@app.get("/")
def root():
    return {"message": "Treelynk backend is running"}
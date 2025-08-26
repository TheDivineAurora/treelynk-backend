from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine, Base
from sqlalchemy import text
from routers import auth, pages, links, analytics, redirect

Base.metadata.create_all(bind = engine)

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

app.include_router(auth.router)
app.include_router(pages.router)
app.include_router(links.router)
app.include_router(analytics.router)
app.include_router(redirect.router)

@app.get("/")
def root():
    return {"message": "Treelynk backend is running"}
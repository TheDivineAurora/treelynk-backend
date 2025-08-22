from fastapi import FastAPI

app = FastAPI(title="Treelynk API")

@app.get("/")
def root():
    return {"message": "Treelynk backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload = True)
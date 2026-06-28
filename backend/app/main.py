from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Apex-OS API",
    description="API for the Apex-OS application",
    version="0.1.0",
)

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"status": "ok"}

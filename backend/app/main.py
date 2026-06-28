from fastapi import FastAPI

app = FastAPI(
    title="Apex-OS API",
    description="API for the Apex-OS application",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"status": "ok"}

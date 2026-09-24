from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(title="MTG Pack Return API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "MTG Pack Return API"}


@app.get("/health")
def health():
    return {"status": "ok"}
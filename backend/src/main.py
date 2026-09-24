from fastapi import FastAPI

app = FastAPI(title="MTG Pack Return API")


@app.get("/")
def root():
    return {"message": "MTG Pack Return API"}


@app.get("/health")
def health():
    return {"status": "ok"}
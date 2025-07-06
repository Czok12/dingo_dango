"""Hauptanwendung für die dango-dingo API."""

from fastapi import FastAPI

from dango_ki.api import router as api_router

app = FastAPI(
    title="dango-dingo API",
    description="API für den juristischen Präzisions-Recherche-Assistenten.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Gibt eine Willkommensnachricht zurück."""
    return {"message": "Willkommen zur dango-dingo API"}


app.include_router(api_router, prefix="/api")

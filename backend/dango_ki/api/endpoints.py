"""API-Endpunkte für dango-dingo."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SearchQuery(BaseModel):
    """Modell für eine Suchanfrage."""

    query: str


@router.get("/health", tags=["Monitoring"])
async def health_check() -> dict[str, str]:
    """Überprüft den Zustand des Dienstes."""
    return {"status": "ok"}


@router.post("/search", tags=["Search"])
async def search(query: SearchQuery) -> dict:
    """Nimmt eine Suchanfrage entgegen und gibt eine Dummy-Antwort zurück."""
    # Hier kommt die Logik für die Vektorsuche hin
    return {"query": query.query, "results": []}

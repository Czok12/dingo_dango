from fastapi import FastAPI

app = FastAPI(
    title="dango-dingo API",
    description="API für den juristischen Präzisions-Recherche-Assistenten.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Willkommen zur dango-dingo API"}

# Hier werden später die Endpunkte aus dango_ki.api.endpoints importiert
# from dango_ki.api import endpoints
# app.include_router(endpoints.router)

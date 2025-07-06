# Konfigurationsmodul für zentrale Konstanten und Pfade.
"""Konfigurationsmodul für zentrale Konstanten und Pfade.

Liest NAS-Pfad aus .env (JURA_KI_DATA_PATH) oder nutzt lokalen Fallback.
Definiert Modellnamen und weitere zentrale Einstellungen.
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# .env laden, falls vorhanden
load_dotenv()

# NAS-Pfad aus Umgebungsvariable, sonst Fallback
JURA_KI_DATA_PATH: Optional[str] = os.getenv("JURA_KI_DATA_PATH")

# Lokaler Fallback-Pfad
LOCAL_DATA_PATH = Path(__file__).parent.parent.parent / "data"

# Effektiver Datenpfad
DATA_PATH = Path(JURA_KI_DATA_PATH) if JURA_KI_DATA_PATH else LOCAL_DATA_PATH

# Modellnamen und zentrale Konstanten
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
RETRIEVAL_MODEL_NAME = "faiss-cpu"
CACHE_DIR = DATA_PATH / "cache"

# Weitere zentrale Konfigurationswerte
MAX_CONTEXT_LENGTH = 4096
DEFAULT_MODE = "default"

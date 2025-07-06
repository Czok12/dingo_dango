# 🏛️ Systemarchitektur: dango-dingo

Dieses Dokument beschreibt die Architektur und den Datenfluss des `dango-dingo` Systems. Die Architektur ist als **"Local First" mit zentraler Datenhaltung** konzipiert.

## 1. Komponenten-Diagramm

Das System besteht aus den folgenden Hauptkomponenten, die lokal auf dem Client-Rechner ausgeführt werden, aber auf eine zentrale Datenquelle zugreifen.

```mermaid
graph TD
    subgraph Client["Client-Rechner (macOS/Windows)"]
        A[Frontend React/TS]
        B[Backend Python/FastAPI Sidecar]
        E[Ollama LLM]
    end

    subgraph Network["Heimnetzwerk"]
        NAS[NAS / Zentraler Speicher]
    end

    subgraph Storage["Zentrale Wissensbasis auf NAS"]
        C[FAISS Vektordatenbank]
        D[SQLite Metadatenbank]
        F[PDF-Originale]
    end

    A -->|"1. User-Anfrage (HTTP)"| B
    B -->|"2. Vektorsuche"| C
    C -->|"3. Vektor-IDs"| B
    B -->|"4. Metadaten-Abfrage"| D
    D -->|"5. Text-Chunks & Metadaten"| B
    B -->|"6. LLM-Anfrage"| E
    E -->|"7. Generierte Antwort"| B
    B -->|"8. Finale Antwort (HTTP)"| A
  
    B -->|"Lese-/Schreibzugriff"| NAS
    NAS -.->|"enthält"| C
    NAS -.->|"enthält"| D
    NAS -.->|"enthält"| F

    classDef frontend fill:#cde4ff
    classDef backend fill:#d5e8d4
    classDef llm fill:#e1d5e7
    classDef storage fill:#f8cecc
  
    class A frontend
    class B backend
    class E llm
    class NAS,C,D,F storage
```

## 2. Datenfluss-Beschreibung

### Typischer Query-Ablauf

1. **User-Anfrage:** Der Nutzer stellt eine Frage über das React-Frontend
2. **Vektorsuche:** Das Backend führt eine semantische Suche in FAISS durch
3. **Metadaten-Abruf:** Zu den gefundenen Vektor-IDs werden die zugehörigen Text-Chunks aus SQLite geladen
4. **LLM-Generierung:** Der lokale Ollama-Server generiert eine Antwort basierend auf dem Kontext
5. **Antwort-Rückgabe:** Die finale Antwort wird über das Backend an das Frontend zurückgegeben

### Daten-Synchronisation

- Alle Daten werden zentral auf dem NAS gespeichert
- Clients greifen direkt über Netzwerk-Shares auf die Datenbank-Dateien zu
- SQLite und FAISS sind dateibasiert und unterstützen gleichzeitigen Lesezugriff
- Schreibvorgänge werden durch Application-Level-Locking koordiniert

Absolut. Jetzt, da die philosophischen und dokumentarischen Grundlagen gelegt sind, gehen wir zur konkreten Umsetzung über. Wir definieren die technische Struktur und den Entwicklungsprozess, speziell zugeschnitten auf eine KI-gestützte Entwicklung mit Tools wie GitHub Copilot.

Hier ist der umfassende Plan, den Sie als Blaupause für die Implementierung von "dango-dingo" verwenden können.

---

### **1. Finale Projektstruktur**

Basierend auf unseren Entscheidungen (Tauri, Sidecar, NAS) schlage ich folgende, klar getrennte Monorepo-Struktur vor. Ein Monorepo (ein Git-Repository für mehrere Teilprojekte) ist hier ideal, da Backend und Frontend eng zusammengehören.

```
dango-dingo/
│
├── .github/                  # (Optional) Für GitHub Actions (CI/CD)
│   └── workflows/
│       └── python-ci.yml
│
├── backend/                  # Das Python-Backend-Projekt
│   ├── .venv/                # Virtuelle Umgebung (in .gitignore)
│   ├── dango_ki/             # Das installierbare Python-Paket
│   │   ├── __init__.py
│   │   ├── api/              # FastAPI-spezifischer Code
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py  # Definition der API-Routen
│   │   │   └── schemas.py    # Pydantic-Modelle für Requests/Responses
│   │   │
│   │   ├── core/             # Die KI-Kernlogik
│   │   │   ├── __init__.py
│   │   │   ├── retrieval.py
│   │   │   ├── quality.py
│   │   │   └── ... (alle anderen Kernmodule)
│   │   │
│   │   └── utils/            # Hilfsfunktionen und Tools
│   │       ├── __init__.py
│   │       ├── data_processing.py
│   │       ├── library_manager.py
│   │       └── config.py     # Zentrale Konfiguration (Pfade, etc.)
│   │
│   ├── tests/                # Alle Python-Tests
│   │   ├── __init__.py
│   │   ├── core/             # Unit-Tests für Kernmodule
│   │   └── api/              # Integrationstests für API-Endpunkte
│   │
│   ├── main.py               # Startpunkt für den uvicorn-Server
│   ├── requirements.txt      # Produktions-Abhängigkeiten
│   ├── requirements-dev.txt  # Entwicklungs-Abhängigkeiten
│   └── pyproject.toml        # Konfiguration für Black, Ruff, Mypy
│
└── frontend/                 # Das Tauri/TypeScript-Frontend-Projekt
    ├── src/
    │   ├── api/              # Funktionen für API-Aufrufe ans Backend
    │   ├── assets/
    │   ├── components/       # Wiederverwendbare UI-Komponenten
    │   ├── hooks/            # Benutzerdefinierte React-Hooks
    │   ├── pages/            # Seiten/Ansichten der Anwendung
    │   └── App.tsx
    ├── src-tauri/            # Tauri-spezifischer Rust-Code
    │   └── ...
    ├── package.json
    ├── tsconfig.json
    └── ...
```

---

### **2. Best Practices & Code-Konventionen**

Diese Regeln sind entscheidend, damit die KI-generierte Code-Qualität hoch bleibt.

1. **Strikte Typisierung (Python & TypeScript):**

   * **Python:** Verwenden Sie überall Type Hints. Mypy wird dies erzwingen. Dies ist die wichtigste Anweisung für Copilot, um korrekten und robusten Code zu generieren.
   * **TypeScript:** Nutzen Sie die Stärke von TS. Definieren Sie `interface` oder `type` für alle API-Antworten und komplexen Objekte.
2. **Konfiguration zentralisieren (`config.py`):**

   * Keine "magischen Strings" oder harten Pfade im Code. Alles (Pfade, Modellnamen, API-Keys) wird aus `dango_ki/utils/config.py` importiert.
   * Nutzen Sie Umgebungsvariablen (`.env`-Datei), um sensible oder benutzerspezifische Werte (wie den NAS-Pfad) zu laden.
3. **Modularität und "Single Responsibility Principle":**

   * Jede Datei und jede Funktion sollte genau eine Aufgabe haben. Fragen Sie Copilot: "Refaktoriere diese Funktion in kleinere, spezialisierte Helper-Funktionen."
   * Die `core`-Module sollten nichts über FastAPI oder die API wissen. Sie nehmen einfache Datentypen entgegen und geben sie zurück. Die `api/endpoints.py` ist der "Übersetzer" zwischen der HTTP-Welt und der Python-Logik.
4. **Backend-Konfiguration (`pyproject.toml`):**

   * Konfigurieren Sie Black, Ruff und Mypy in einer zentralen `pyproject.toml`-Datei im `backend`-Verzeichnis. Das stellt sicher, dass die Tools konsistent arbeiten.

   ```toml
   # pyproject.toml
   [tool.black]
   line-length = 88

   [tool.ruff]
   line-length = 88
   select = ["E", "W", "F", "I", "C", "B"] # Standard-Regeln + flake8-bugbear etc.
   ignore = ["E501"] # wird von Black gehandhabt

   [tool.mypy]
   python_version = "3.10"
   warn_return_any = true
   warn_unused_configs = true
   ```

---

### **3. Roadmap mit Phasen**

Dies ist ein agiler Plan, um das Projekt schrittweise aufzubauen. Jede Phase liefert ein funktionierendes, testbares Inkrement.

**Phase 1: Das Backend-Rückgrat (ohne UI)**

* **Ziel:** Eine funktionierende API, die man z.B. mit `curl` oder der Swagger-UI testen kann.
* **Schritte:**
  1. Projektstruktur anlegen.
  2. `pyproject.toml` und `requirements.txt` erstellen.
  3. Die Kernmodule (`retrieval.py`, `quality.py` etc.) aus dem alten Code in `dango_ki/core/` refaktorisieren. **Fokus:** Strikte Typisierung und Docstrings hinzufügen.
  4. `config.py` erstellen und Pfade zentralisieren.
  5. Den FastAPI-Server in `main.py` und die Endpunkte in `api/endpoints.py` aufsetzen.
  6. Einen ersten Endpunkt `/answer` implementieren, der die Kernlogik aufruft.
  7. Unit-Tests für die wichtigsten Kernfunktionen schreiben.
* **Ergebnis dieser Phase:** Ein lokal lauffähiger API-Server, der Fragen beantworten kann.

**Phase 2: Das Frontend-Skelett & die Brücke**

* **Ziel:** Eine minimale Tauri-App, die erfolgreich mit dem Backend kommunizieren kann.
* **Schritte:**
  1. Tauri-Projekt im `frontend`-Ordner initialisieren.
  2. Ein einfaches UI-Layout erstellen: ein Texteingabefeld und ein Button.
  3. Eine Funktion in `frontend/src/api/` schreiben, die eine `fetch`-Anfrage an den lokalen FastAPI-Endpunkt (`http://localhost:8000/answer`) sendet.
  4. Die Antwort des Backends loggen oder in einem einfachen Textfeld anzeigen.
  5. Das Python-Backend mit `PyInstaller` paketieren und als Sidecar in `tauri.conf.json` konfigurieren.
* **Ergebnis dieser Phase:** Eine installierbare Desktop-App, die eine Anfrage an das Backend senden und eine Antwort empfangen kann.

**Phase 3: Feature-Implementierung & UI-Ausbau**

* **Ziel:** Die volle Funktionalität in einer ansprechenden UI umsetzen.
* **Schritte:**
  1. Die UI für die Frage-Antwort-Funktion ausbauen (Markdown-Rendering, Quellenanzeige, etc.).
  2. Weitere API-Endpunkte und zugehörige UI-Komponenten für die anderen Features implementieren (Bibliotheksverwaltung, System-Status etc.).
  3. Das XAI-Dashboard mit einer Charting-Bibliothek (z.B. `recharts`) im Frontend umsetzen.
  4. Styling und Design der Anwendung verfeinern.
* **Ergebnis dieser Phase:** Eine voll funktionsfähige, gut aussehende `dango-dingo` v1.0.

**Phase 4: Optimierung & Stabilisierung**

* **Ziel:** Performance-Analyse, Bugfixing und Verfeinerung.
* **Schritte:**

  1. Performance-Profiling der Backend-Routen.
  2. Optimierung langsamer Datenbankabfragen.
  3. Verbesserung des Caching-Verhaltens.
  4. Umfassende manuelle Tests.
* **Ergebnis dieser Phase:** Eine stabile, schnelle und zuverlässige Anwendung.
*

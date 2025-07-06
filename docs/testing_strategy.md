# 🧪 Test-Strategie für "dango-dingo"

Dieses Dokument beschreibt die Test-Philosophie, die Werkzeuge und die Prozesse, um die Qualität und Stabilität von `dango-dingo` sicherzustellen.

## 1. Test-Philosophie

- **Vertrauen durch Automatisierung:** Wir verlassen uns auf automatisierte Tests, um Regressionen zu vermeiden und die Korrektheit der Kernlogik zu gewährleisten.
- **Testen, was wichtig ist:** Der Fokus der Tests liegt auf der komplexen KI- und Datenverarbeitungslogik im Python-Backend. Das UI-Frontend wird primär durch manuelle Nutzungstests und optional durch End-to-End-Tests abgedeckt.
- **Tests als Dokumentation:** Gut geschriebene Tests dienen auch als lebendige Dokumentation und zeigen, wie eine Funktion oder ein Modul verwendet werden soll.
- **Pragmatismus:** Wir streben eine hohe Testabdeckung für kritische Pfade an, nicht zwangsläufig 100% für jede Codezeile.

## 2. Test-Ebenen

Wir unterscheiden zwischen den folgenden Test-Ebenen:

### a) Unit-Tests (Höchste Priorität)

- **Zweck:** Testen einer einzelnen, isolierten Funktion oder Klasse. Sie sind schnell, einfach zu schreiben und bilden das Fundament unserer Qualitätssicherung.
- **Ort:** Im `dango-dingo-backend/tests/` Verzeichnis. Die Dateinamen folgen der Konvention `test_*.py` (z.B. `test_query_enhancer.py` testet die Logik in `query_enhancer.py`).
- **Beispiele:**
  - `test_synonym_expansion()`: Prüft, ob für "Vertrag" korrekt "Vereinbarung" gefunden wird.
  - `test_cache_hit_and_miss()`: Stellt sicher, dass das Caching-System wie erwartet funktioniert.
  - `test_citation_formatting()`: Überprüft, ob die Zitations-Engine für einen gegebenen Stil das korrekte Format ausgibt.
- **Prinzipien:**
  - Externe Abhängigkeiten wie LLM-Aufrufe oder Datenbankzugriffe werden **gemockt** (simuliert), um die Tests schnell und unabhängig zu machen.
  - Jeder Testfall sollte eine spezifische Annahme (Assertion) überprüfen.

### b) Integrationstests (Mittlere Priorität)

- **Zweck:** Testen das Zusammenspiel mehrerer Module, um sicherzustellen, dass die "Verkabelung" korrekt ist.
- **Ort:** Ebenfalls im `dango-dingo-backend/tests/`, oft in einer separaten Datei wie `test_integration.py`.
- **Beispiele:**
  - `test_full_rag_pipeline()`: Simuliert eine Anfrage, die durch Query Enhancement, Retrieval, und Answer Generation läuft, und prüft, ob ein valides Ergebnisformat zurückgegeben wird.
  - `test_api_endpoints()`: Startet eine Test-Instanz der FastAPI-Anwendung und sendet HTTP-Anfragen an die Endpunkte, um die Korrektheit der Request/Response-Zyklen zu validieren.
- **Prinzipien:**
  - Es werden weniger Abhängigkeiten gemockt. Oft wird eine temporäre In-Memory-SQLite-Datenbank oder ein kleiner, temporärer FAISS-Index für den Test erstellt.

### c) End-to-End (E2E) Tests (Optional / Manuell)

- **Zweck:** Testen die gesamte Anwendung aus der Perspektive des Nutzers, vom Klick im UI bis zur angezeigten Antwort.
- **Umsetzung:**
  - **Manuell:** Die primäre Methode für dieses Projekt. Nach größeren Änderungen wird die Anwendung gebaut und ein vordefinierter Testplan durchgeklickt.
  - **Automatisiert (Optional):** Könnte später mit Frameworks wie **Playwright** oder **Cypress** implementiert werden. Dies ist für den aktuellen Projektumfang jedoch nicht priorisiert.

## 3. Werkzeuge und Frameworks

- **Backend (Python):**
  - **Test-Runner:** `pytest`
  - **Mocking:** `unittest.mock` (Standardbibliothek) und `pytest-mock`
  - **Testabdeckung:** `pytest-cov`
  - **Asynchrone Tests:** `pytest-asyncio` (wichtig für FastAPI)
- **Frontend (TypeScript):**
  - **Unit-Tests:** `Vitest` oder `Jest` mit `React Testing Library`.
  - **E2E-Tests (Optional):** `Playwright`.

## 4. Ausführung der Tests

1.  Stellen Sie sicher, dass Sie die Entwicklungs-Abhängigkeiten installiert haben:
    ```bash
    # Im Backend-Verzeichnis
    pip install -r requirements-dev.txt
    ```
2.  Führen Sie alle Backend-Tests vom Hauptverzeichnis des Backends aus:
    ```bash
    pytest
    ```
3.  Um einen Report zur Testabdeckung zu erhalten:
    ```bash
    pytest --cov=jura_ki
    ```
    Das Ziel ist eine Abdeckung von **> 80%** für die Module im `jura_ki/core`-Verzeichnis.

## 5. Testdaten

- Für Tests, die Daten benötigen, werden kleine, repräsentative Beispieldaten in einem `tests/fixtures`-Ordner abgelegt (z.B. eine Mini-Version der SQLite-DB, ein paar Beispiel-Text-Chunks).
- Sensible oder große Daten gehören nicht ins Git-Repository.

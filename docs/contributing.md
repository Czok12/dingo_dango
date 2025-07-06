Perfekt. Die `CONTRIBUTING.md` ist das Handbuch für jeden, der am Code arbeiten will – in diesem Fall also für Sie und Ihre Schwester. Sie stellt sicher, dass Sie beide auf die gleiche Weise arbeiten, was zukünftige Probleme vermeidet.

Hier ist eine umfassende Vorlage. Sie ist absichtlich detailliert, um professionellen Standards zu entsprechen, aber bleibt pragmatisch für Ihr Zwei-Personen-Team.

---

### **Aktion 4: `CONTRIBUTING.md` erstellen**

Kopieren Sie den folgenden Inhalt und speichern Sie ihn als `CONTRIBUTING.md` im Hauptverzeichnis Ihres Projekts.

```markdown
# 🛠️ Entwickler-Leitfaden für "dango-dingo"

Herzlich willkommen, Entwickler! Dieses Dokument ist unser gemeinsamer Leitfaden, um die Arbeit an `dango-dingo` konsistent, effizient und nachvollziehbar zu gestalten.

## 📜 Grundprinzipien

1.  **Struktur bewahren:** Halten Sie sich an die definierte Projektstruktur. Neue Module gehören an den dafür vorgesehenen Ort.
2.  **Dokumentation ist Code:** Jede neue Funktion oder signifikante Änderung erfordert eine Aktualisierung der relevanten Dokumentation (Docstrings, README, ADRs).
3.  **Tests sind nicht optional:** Jede Kernfunktion sollte durch Unit-Tests abgedeckt sein.
4.  **Commits sind Geschichten:** Schreiben Sie aussagekräftige Commit-Nachrichten, die erklären, *warum* eine Änderung gemacht wurde.

## 1. Voraussetzungen

Stellen Sie sicher, dass die folgenden Werkzeuge auf Ihrem System installiert sind:

- **Python:** Version 3.10 oder höher.
  - Empfehlung: Verwenden Sie `pyenv` zur Verwaltung von Python-Versionen.
- **Node.js:** Version 18 oder höher.
  - Empfehlung: Verwenden Sie `nvm` (Node Version Manager).
- **Rust & Cargo:** Wird von Tauri benötigt. Folgen Sie der offiziellen [Installationsanleitung](https://www.rust-lang.org/tools/install).
- **Ollama:** Muss lokal installiert sein. Laden Sie das benötigte Modell herunter:
  ```bash
  ollama pull llama3.2
  ```

- **Git:** Für die Versionskontrolle.

## 2. Setup der Entwicklungsumgebung

Das Projekt ist in ein Backend und ein Frontend aufgeteilt. Beide müssen für die Entwicklung eingerichtet werden.

### Backend (Python/FastAPI)

1. **Verzeichnis:** `cd backend`
2. **Virtuelle Umgebung aktivieren:**
    Die virtuelle Umgebung (`dangovenv`) befindet sich im übergeordneten Verzeichnis (`../`).

    ```bash
    source ../dangovenv/bin/activate  # macOS/Linux
    # ..\dangovenv\Scripts\activate   # Windows
    ```

3. **Abhängigkeiten installieren:**

    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt # Entwicklungs-Tools installieren
    ```

4. **Datenbank-Pfad konfigurieren:**
    - Erstellen Sie eine `.env`-Datei im `backend`-Verzeichnis.
    - Fügen Sie den Pfad zu Ihrem NAS-Datenordner hinzu:

      ```
      JURA_KI_DATA_PATH="/Volumes/IhrNAS/Pfad/zu/dango-dingo-data"
      ```

    - Die `dango_ki/utils/config.py` lädt diese Variable automatisch.
5. **Entwicklungsserver starten:**

    ```bash
    uvicorn api:app --reload --port 8000
    ```

    Der Server ist nun unter `http://127.0.0.1:8000` erreichbar.

### Frontend (Tauri/TypeScript)

1. **Verzeichnis:** `cd frontend`
2. **Abhängigkeiten installieren:**

    ```bash
    npm install
    ```

3. **Anwendung im Entwicklungsmodus starten:**
    Dieser Befehl startet die Desktop-Anwendung mit Hot-Reloading für das Frontend. Das Python-Backend muss **separat** wie oben beschrieben gestartet werden, um eine schnelle Entwicklungs-Loop zu gewährleisten.

    ```bash
    npm run tauri dev
    ```

## 3. Typischer Entwicklungs-Workflow

1. **Neuen Branch erstellen:** Beginnen Sie jede neue Funktion oder jeden Bugfix in einem eigenen Branch.

    ```bash
    git checkout main
    git pull
    git checkout -b feat/neue-zitations-engine  # oder fix/cache-problem
    ```

2. **Code schreiben:** Implementieren Sie Ihre Änderungen.
3. **Tests hinzufügen/anpassen:** Schreiben Sie Unit-Tests für Ihre neue Logik im `/tests`-Verzeichnis.
4. **Tests ausführen:**

    ```bash
    # Im Backend-Verzeichnis
    pytest
    ```

5. **Code formatieren & linten:** Stellen Sie sicher, dass der Code unseren Standards entspricht.

    ```bash
    # Im backend-Verzeichnis
    black .
    ruff .

    # Im frontend-Verzeichnis
    npm run format
    npm run lint
    ```

6. **Änderungen committen:** Verwenden Sie aussagekräftige Commit-Nachrichten.

    ```bash
    git add .
    git commit -m "feat(citation): Implement new APA citation style"
    ```

7. **Pull Request (PR) erstellen:** Pushen Sie Ihren Branch und erstellen Sie einen Pull Request auf GitHub/GitLab. So kann die zweite Person die Änderungen überprüfen (Code Review), bevor sie in den `main`-Branch übernommen werden.

## 4. Wichtige Skripte und Befehle

- **Datenbank neu erstellen (Ingest):**

  ```bash
  # Im backend-Verzeichnis
  python -m dango_ki.utils.data_processing ingest
  ```

- **Finale Desktop-App bauen:**

  ```bash
  # Im frontend-Verzeichnis
  npm run tauri build
  ```

  Die fertige Installationsdatei befindet sich dann in `frontend/src-tauri/target/release/bundle/`.

## 5. Architektur-Entscheidungen (ADRs)

Wichtige architektonische Entscheidungen werden in `/docs/adr` festgehalten. Bevor Sie eine grundlegende Änderung am Tech-Stack oder der Architektur vornehmen, erstellen Sie bitte ein neues ADR, um die Entscheidung zu dokumentieren.

```

---

### **Aktion 5: `requirements-dev.txt` erstellen**

Es ist eine bewährte Methode, Entwicklungs-Abhängigkeiten (wie `pytest` oder `black`) von den Produktions-Abhängigkeiten zu trennen.

Erstellen Sie eine neue Datei namens `requirements-dev.txt` im `dango-dingo-backend`-Verzeichnis:

```

# Entwicklungs-Abhängigkeiten für dango-dingo

pytest
pytest-cov
pytest-asyncio
black
flake8
mypy

```

Ihre `requirements.txt` sollte dann nur die Pakete enthalten, die für den Betrieb der Anwendung notwendig sind (langchain, fastapi, etc.). Der Befehl `pip install -r requirements-dev.txt` im Entwickler-Guide sorgt dafür, dass diese zusätzlichen Werkzeuge installiert werden.

---

### **Zusammenfassung und Nächste Schritte**

Sehr gut. Mit der `README.md` und `CONTRIBUTING.md` haben Sie die zwei wichtigsten Dokumente für den Einstieg und die Zusammenarbeit geschaffen. Jeder (Sie, Ihre Schwester, Ihr zukünftiges Ich) weiß nun, was das Projekt ist und wie man daran arbeitet.

Als Nächstes empfehle ich, die **Architecture Decision Records (ADRs)** zu erstellen. Sie sind kurz, aber extrem wertvoll, um die "Warum"-Fragen zu beantworten.

**Sollen wir mit der Vorlage für die ADRs weitermachen?**

**"dango-dingo"**

####  **`README.md` (Überarbeitet)**

```markdown
# 🏛️ dango-dingo: Der juristische Präzisions-Recherche-Assistent

**Ein privater, hochspezialisierter Wissensassistent zur Analyse und Abfrage von juristischen Fachtexten. `dango-dingo` ist als transparenter und validierbarer Helfer für das wissenschaftliche juristische Arbeiten konzipiert.**

---

## 🧭 Projektphilosophie

`dango-dingo` folgt strikten Leitprinzipien, die seine Funktion und seinen Zweck definieren:

1.  **Korrektheit vor Kreativität:** Jede Aussage ist direkt auf die zugrundeliegende, kuratierte Wissensbasis zurückführbar. Das System erfindet keine Informationen.
2.  **Transparenz als Vertrauensgrundlage:** Der Weg von der Nutzeranfrage zur finalen Antwort ist vollständig nachvollziehbar. Alle Retrieval- und Analyseschritte sind einsehbar.
3.  **Assistent, nicht Autor:** Die Software ist ein Werkzeug zur Beschleunigung und Absicherung der Recherche, nicht zur Erstellung eigener juristischer Meinungen. Die Verantwortung verbleibt beim Nutzer.
4.  **Objektivität und Neutralität:** Das System ist darauf ausgelegt, juristische Meinungsstreite (z.B. h.M. vs. Mindermeinung) neutral und gewichtet darzustellen, basierend auf den Quellen.

## ✨ Kern-Features

- **Multi-Stage-Retrieval:** Eine Kombination aus semantischer, Keyword- und Entitäten-basierter Suche für höchste Relevanz.
- **Answer Quality & Confidence Scoring:** Jede Antwort wird automatisch auf ihre Verlässlichkeit, Konsistenz und Quellenabdeckung bewertet.
- **Explainable AI (XAI) Dashboard:** Ein Dashboard zur Visualisierung des gesamten RAG-Prozesses, von der Query-Analyse bis zur Antwortsynthese.
- **Zentrale Wissensbasis:** Synchronisation der Datenbanken (FAISS & SQLite) über ein lokales NAS für die Nutzung durch mehrere Personen im selben Netzwerk.
- **Native Desktop-Anwendung:** Eine performante und sichere Anwendung, gebaut mit Tauri, die lokal auf dem Client-Rechner läuft.
- **Intelligente Zitations-Engine:** Automatische Generierung von korrekten Quellenangaben und Validierung von Rechtsnormen.

## 🚀 Tech-Stack

- **Backend:** Python 3.10+, FastAPI (als lokaler Sidecar-Prozess)
- **Frontend:** Tauri, TypeScript, React (oder ein alternatives modernes Framework)
- **Vektordatenbank:** FAISS
- **Metadatenbank:** SQLite
- **Sprachmodell (LLM):** Ollama (lokal ausgeführt)
- **KI-Framework:** LangChain

## 🛠️ Quick Start: Setup & Installation

Eine detaillierte Anleitung für Entwickler findet sich in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

1.  **Voraussetzungen prüfen:** Python, Node.js, Rust und Ollama müssen installiert sein.
2.  **Repository klonen:** `git clone [URL_IHRES_REPOSITORIES]`
3.  **Backend aufsetzen:** `cd dango-dingo-backend && pip install -r requirements.txt`
4.  **Frontend aufsetzen:** `cd ../dango-dingo-frontend && npm install`
5.  **Datenbank initialisieren:** Konfigurieren Sie den NAS-Pfad und führen Sie das Ingest-Skript aus.
6.  **Anwendung starten:** `npm run tauri dev`

## 📄 Architektur-Überblick

Eine detaillierte Beschreibung und ein Diagramm der Systemarchitektur finden Sie in [`docs/architecture.md`](./docs/architecture.md).

## 🤝 Mitwirken

Richtlinien für die Weiterentwicklung von `dango-dingo` sind in [`CONTRIBUTING.md`](./CONTRIBUTING.md) dokumentiert.

## 📝 Lizenz

[TODO: Fügen Sie hier eine Lizenz hinzu, z.B. "Privat, keine Weitergabe".]
```

---

#### **2. `docs/architecture.md` (Überarbeitet)**

```markdown
# 🏛️ Systemarchitektur: dango-dingo

Dieses Dokument beschreibt die Architektur und den Datenfluss des `dango-dingo` Systems. Die Architektur ist als **"Local First" mit zentraler Datenhaltung** konzipiert.

## 1. Komponenten-Diagramm

Das System besteht aus den folgenden Hauptkomponenten, die lokal auf dem Client-Rechner ausgeführt werden, aber auf eine zentrale Datenquelle zugreifen.

```mermaid
graph TD
    subgraph "Client-Rechner (macOS/Windows)"
        direction LR
        subgraph "Tauri Desktop-Anwendung (dango-dingo)"
            A[Frontend (React/TS)]
        end
        subgraph "Lokale Prozesse"
            B[Backend (Python/FastAPI Sidecar)]
            E[Ollama LLM]
        end
    end

    subgraph "Heimnetzwerk"
        NAS[NAS / Zentraler Speicher]
    end

    subgraph "Zentrale Wissensbasis auf NAS"
        C[FAISS Vektordatenbank]
        D[SQLite Metadatenbank]
        F[PDF-Originale]
    end

    A -- "1. User-Anfrage (HTTP)" --> B
    B -- "2. Vektorsuche" --> C
    C -- "3. Vektor-IDs" --> B
    B -- "4. Metadaten-Abfrage" --> D
    D -- "5. Text-Chunks & Metadaten" --> B
    B -- "6. LLM-Anfrage" --> E
    E -- "7. Generierte Antwort" --> B
    B -- "8. Finale Antwort (HTTP)" --> A
  
    B -- "Lese-/Schreibzugriff" --> NAS
    NAS -- "enthält" --> C
    NAS -- "enthält" --> D
    NAS -- "enthält" --> F

    style A fill:#cde4ff
    style B fill:#d5e8d4
    style E fill:#e1d5e7
    style NAS fill:#f8cecc
```

## 2. Detaillierter Datenfluss einer Anfrage

1. **User-Anfrage:** Der Nutzer gibt eine Frage in die **`dango-dingo` Tauri-App (A)** ein. Das in TypeScript geschriebene Frontend sendet die Anfrage als HTTP-Request an den lokalen FastAPI-Server.
2. **Backend-Verarbeitung:** Das **FastAPI-Backend (B)**, das als Sidecar-Prozess von Tauri gestartet wurde, empfängt die Anfrage. Es nutzt die KI-Kernmodule (z.B. `QueryEnhancer`), um die Anfrage zu analysieren.
3. **Vektorsuche:** Das Backend erstellt ein Embedding für die (verbesserte) Anfrage und führt eine Ähnlichkeitssuche in der **FAISS-Vektordatenbank (C)** durch. Diese liegt physisch auf dem NAS und wird über das Netzwerk angesprochen. FAISS gibt eine Liste der relevantesten Vektor-IDs zurück.
4. **Metadaten-Retrieval:** Mit den Vektor-IDs fragt das Backend die **SQLite-Datenbank (D)** auf dem NAS ab, um die zugehörigen Volltexte der Chunks sowie deren Metadaten (Buch, Seite, etc.) zu erhalten.
5. **Kontext-Erstellung & LLM-Aufruf:** Das Backend assembliert die erhaltenen Texte zu einem Kontext und formuliert einen präzisen Prompt, der an das lokal laufende **Ollama LLM (E)** gesendet wird.
6. **Antwort-Synthese & Qualitätsprüfung:** Die Roh-Antwort des LLM wird vom Backend entgegengenommen. Das `AnswerQualitySystem` prüft die Antwort, berechnet einen Confidence Score und formatiert das Ergebnis.
7. **Rückgabe an Frontend:** Die finale, strukturierte Antwort wird an das **Tauri-Frontend (A)** zurückgesendet und dem Nutzer angezeigt.

## 3. Ingest-Prozess (Datenaufnahme)

1. Ein neues PDF-Dokument wird im Verzeichnis für **Originale (F)** auf dem NAS abgelegt.
2. Ein separates Skript (`jura_ki/utils/data_processing.py`) wird manuell ausgeführt.
3. Das Skript liest das PDF, zerlegt es in Text-Chunks und fügt die Buch-Metadaten zur **SQLite-DB (D)** hinzu.
4. Für jeden Chunk wird ein Embedding berechnet und zusammen mit einer ID in der **FAISS-DB (C)** gespeichert.

Diese entkoppelte Architektur gewährleistet, dass die rechenintensiven Aufgaben lokal ausgeführt werden, während die Daten zentral und für beide Nutzer synchron gehalten werden.

```

---

Die `CONTRIBUTING.md`, die ADRs und die anderen Dokumente können ebenfalls entsprechend angepasst werden, indem "Jura-KI" oder "das Projekt" durch "dango-dingo" ersetzt wird.

Sehr gut. Mit einem konkreten Namen fühlt sich das Projekt sofort greifbarer an.

**Sollen wir jetzt mit der `CONTRIBUTING.md` (dem Entwickler-Guide) fortfahren?** Dieses Dokument ist entscheidend, damit Sie und Ihre Schwester eine konsistente und reibungslose Entwicklungsumgebung haben.
```

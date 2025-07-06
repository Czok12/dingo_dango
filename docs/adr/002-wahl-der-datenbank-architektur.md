# ADR 002: Wahl der Datenbank-Architektur

- **Status:** Akzeptiert
- **Datum:** 2024-05-23
- **Projekt:** dango-dingo

## Kontext

Das System benötigt eine persistente Speicherschicht für zwei grundlegend unterschiedliche Arten von Daten:

1. **Semantische Vektoren:** Numerische Repräsentationen von Text-Chunks für die Ähnlichkeitssuche.
2. **Strukturierte Metadaten:** Informationen über Bücher, Text-Chunks, Cache-Einträge, Nutzer-Feedback und Beziehungen zwischen Entitäten.

Die Daten sollen zentral auf einem NAS im Heimnetzwerk gespeichert werden, um sie zwischen den Nutzern zu synchronisieren.

## Entscheidung

Wir setzen auf eine **hybride Datenbank-Architektur**, die zwei spezialisierte, dateibasierte Systeme kombiniert:

1. **FAISS (Facebook AI Similarity Search):** Wird als **Vektordatenbank** zur Speicherung und Abfrage der Text-Embeddings verwendet.
2. **SQLite:** Wird als **relationale Datenbank** zur Verwaltung aller strukturierten Metadaten genutzt.

Beide Datenbanksysteme (der FAISS-Index-Ordner und die SQLite-`.db`-Datei) werden im zentralen Datenverzeichnis auf dem NAS abgelegt.

## Begründung und Konsequenzen

### Positiv

- **"Best-of-Breed"-Ansatz:** Jede Datenbank wird für den Zweck eingesetzt, für den sie optimiert ist. FAISS ist unschlagbar schnell für Vektorsuchen, SQLite ist der Standard für leichtgewichtige, strukturierte Datenabfragen.
- **Serverlos & Lokal:** Beide Systeme sind dateibasiert und erfordern keinen separaten Datenbank-Server. Dies passt perfekt zur "Local First"-Philosophie der Tauri-Anwendung.
- **Effiziente Synchronisation:** Die Synchronisation der gesamten Wissensbasis erfolgt einfach durch den gemeinsamen Zugriff auf die Dateien auf dem NAS.
- **Industriestandard:** Diese Kombination ist ein etabliertes Muster in der Entwicklung von RAG-Systemen.

### Negativ

- **Zwei Systeme zu verwalten:** Es müssen zwei unterschiedliche Datenbank-Interfaces im Code angesprochen werden.
- **Concurrency-Limitierung von SQLite:** SQLite ist nicht für hohen gleichzeitigen Schreibzugriff optimiert. Für den Anwendungsfall mit 1-2 Nutzern, die selten gleichzeitig schreibend zugreifen (z.B. beim Ingest neuer Bücher), ist dieses Risiko jedoch vernachlässigbar und wird als akzeptabel eingestuft. Ein "database is locked"-Fehler ist im schlimmsten Fall möglich, aber unwahrscheinlich.

# ADR 003: Architektur des Python-Backends

- **Status:** Akzeptiert
- **Datum:** 2024-05-23
- **Projekt:** dango-dingo

## Kontext

Die Python-basierte KI-Logik muss eine Schnittstelle für das Tauri/TypeScript-Frontend bereitstellen. Es muss eine klare Trennung zwischen der Benutzeroberfläche (Frontend) und der Verarbeitungslogik (Backend) geben.

## Entscheidung

Das Python-Backend wird als **lokaler API-Server mit FastAPI** implementiert. Dieser Server wird nicht im Internet gehostet, sondern von der Tauri-Anwendung bei jedem Start als **Sidecar-Prozess** im Hintergrund gestartet.

Die Kommunikation zwischen Frontend und Backend erfolgt über Standard-HTTP-Anfragen an `localhost`.

## Begründung und Konsequenzen

### Positiv

- **Klare Trennung (Decoupling):** Die Frontend-Logik (UI, State Management) ist sauber von der Backend-Logik (KI, Datenzugriff) getrennt. Dies erleichtert die Wartung und parallele Entwicklung.
- **Standardisierte Kommunikation:** Die Verwendung von HTTP und einer REST-API ist ein robuster und gut verstandener Industriestandard.
- **Automatische API-Dokumentation:** FastAPI generiert automatisch eine interaktive Swagger-UI, was die Entwicklung des Frontends erheblich vereinfacht, da die Schnittstellen klar definiert und testbar sind.
- **Zukunftssicherheit:** Sollte das Projekt jemals eine Web-Version benötigen, kann dieselbe FastAPI-Anwendung mit minimalen Änderungen in der Cloud gehostet werden. Die Umstellung wäre unkompliziert.
- **Stabilität:** Das Backend läuft in einem eigenen Prozess. Ein Absturz im Python-Code führt nicht zwangsläufig zum Absturz der gesamten Desktop-Anwendung.

### Negativ

- **Leichter Performance-Overhead:** Die Kommunikation über HTTP ist geringfügig langsamer als ein direkter Funktionsaufruf. Für diesen Anwendungsfall ist dieser Overhead im Vergleich zur Dauer der KI-Berechnungen vernachlässigbar.
- **Komplexität des Sidecar-Managements:** Der Start und die Überwachung des Python-Prozesses müssen von Tauri verwaltet werden. Dies erfordert eine sorgfältige Konfiguration in der `tauri.conf.json`.

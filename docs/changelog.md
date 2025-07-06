# Changelog

Alle nennenswerten Änderungen an `dango-dingo` werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- [TODO: Tragen Sie hier neue Features ein, die noch nicht Teil eines Releases sind]

### Changed

- [TODO: Tragen Sie hier Änderungen ein]

### Fixed

- [TODO: Tragen Sie hier Bugfixes ein]

---

## [0.1.0] - 2024-05-23

### Added

- **Initiales Projekt-Setup:** Erstellung der Grundstruktur für Backend und Frontend.
- **Dokumentation v1.0:** Erstellung der Kerndokumente (`README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `architecture.md`, ADRs, `testing_strategy.md`, `user_manual.md`).
- **Architektur-Entscheidungen:**
  - ADR 001: Festlegung auf Tauri als Frontend-Framework.
  - ADR 002: Definition der hybriden Datenbank-Architektur (FAISS + SQLite).
  - ADR 003: Entscheidung für ein FastAPI-Backend als Sidecar-Prozess.
- **Erste Test-Strategie:** Definition von Unit-, Integrations- und E2E-Tests mit `pytest`.

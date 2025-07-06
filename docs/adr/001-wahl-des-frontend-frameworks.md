# ADR 001: Wahl des Frontend-Frameworks

- **Status:** Akzeptiert
- **Datum:** 2024-05-23
- **Projekt:** dango-dingo

## Kontext

Das Projekt benötigt eine Benutzeroberfläche (Frontend) für eine private, lokale Anwendung, die von 1-2 Personen genutzt wird. Die primären Anforderungen sind eine hohe Performance für eine flüssige User Experience, einfache Verteilung und Installation, maximaler Datenschutz (Daten verlassen das lokale Netzwerk nicht) und die Möglichkeit zur Offline-Nutzung von Kernfunktionen.

Folgende Alternativen wurden evaluiert:
1.  **Streamlit:** Schnelles Prototyping, rein Python-basiert.
2.  **TypeScript-Web-Anwendung (z.B. Next.js):** Maximale UI-Flexibilität, aber erfordert Hosting und komplexe Infrastruktur.
3.  **Tauri (Desktop-Anwendung):** Kombiniert ein Web-Technologie-Frontend mit einem nativen Anwendungs-Wrapper.

## Entscheidung

Wir haben uns für **Tauri** entschieden, um eine native Desktop-Anwendung zu erstellen. Das Frontend wird mit **TypeScript** und einem modernen UI-Framework (wie React) entwickelt.

Das Python-Backend wird als **Sidecar**-Prozess implementiert. Das bedeutet, Tauri startet beim Öffnen der Desktop-App automatisch den Python-Server im Hintergrund.

## Begründung und Konsequenzen

### Positiv:
- **Erfüllt alle Kernanforderungen:**
  - **Einfaches Deployment:** Die gesamte Anwendung wird in eine einzige Installationsdatei (`.dmg`/`.exe`) gebündelt. Es sind keine Webserver oder Cloud-Dienste erforderlich.
  - **Performance:** Die KI-Logik läuft direkt auf dem Client-Rechner, was Netzwerk-Latenzen eliminiert und die Rechenleistung des jeweiligen Nutzers voll ausnutzt.
  - **Datenschutz & Offline-Fähigkeit:** Alle Berechnungen und Daten bleiben auf dem lokalen Rechner bzw. im Heimnetzwerk (NAS).
- **Professionelle UI/UX:** Im Gegensatz zu Streamlit ermöglicht dieser Ansatz eine vollständig benutzerdefinierte und hochgradig interaktive Benutzeroberfläche.
- **Keine CORS-Problematik:** Die Kommunikation zwischen dem Tauri-Frontend und dem lokalen Sidecar-Backend ist unkompliziert und erfordert keine komplexe Cross-Origin-Konfiguration.

### Negativ:
- **Zusätzlicher Build-Schritt:** Das Python-Backend muss in eine eigenständige ausführbare Datei paketiert werden (z.B. mit PyInstaller oder Nuitka), damit Tauri es als Sidecar einbinden kann.
- **Kein direkter Web-Zugriff:** Die Anwendung muss auf jedem Rechner installiert werden und kann nicht einfach über einen Browser-Link geteilt werden. Dies ist für den definierten Anwendungsfall jedoch ein akzeptabler Kompromiss.

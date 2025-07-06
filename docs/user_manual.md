# 📖 dango-dingo - Benutzerhandbuch

Willkommen bei `dango-dingo`, Ihrem persönlichen Assistenten für die juristische Recherche!

## 1. Installation

1. Laden Sie die neueste Installationsdatei (`dango-dingo-vx.x.x.dmg` oder `.msi`) herunter.
2. Öffnen Sie die Datei und folgen Sie den Installationsanweisungen Ihres Betriebssystems.
3. **Wichtig beim ersten Start:** Die Anwendung wird Sie bitten, den Ordner auszuwählen, in dem Ihre `dango-dingo`-Daten (Datenbanken, PDFs) liegen. Navigieren Sie zu dem entsprechenden Ordner auf Ihrem NAS und bestätigen Sie. Dieser Schritt ist nur einmal notwendig.

## 2. Die Benutzeroberfläche

Die Anwendung ist in mehrere Bereiche aufgeteilt, die Sie über die Seitenleiste erreichen können.

### a) Frage & Antwort (Hauptbereich)

Dies ist das Herzstück der Anwendung.

1. **Frage eingeben:** Nutzen Sie das große Textfeld, um Ihre Frage zu formulieren.
   - **Tipp:** Spezifische Fragen mit Paragraphen (z.B. "Welche Rechtsfolgen hat ein Sachmangel nach § 437 BGB?") liefern die besten Ergebnisse.
2. **Antwort generieren:** Klicken Sie auf den Button, um die Suche zu starten.
3. **Ergebnis:** Sie erhalten eine strukturierte Antwort, die mit einem **Confidence Score** versehen ist. Darunter finden Sie die genauen **Quellen** aus Ihren Lehrbüchern, die zur Beantwortung herangezogen wurden.

### b) Bibliotheksverwaltung

Hier verwalten Sie Ihre Wissensbasis.

- **Übersicht:** Sehen Sie alle Bücher, die sich bereits im System befinden.
- **Buch hinzufügen:**
  1. Stellen Sie sicher, dass die PDF-Datei Ihres neuen Buches im `originale`-Ordner auf Ihrem NAS liegt.
  2. Klicken Sie auf "Buch hinzufügen" und füllen Sie die Metadaten (Autor, Titel, etc.) aus.
  3. Starten Sie den **Ingest-Prozess**. Die App wird das neue Buch analysieren und in die Datenbank aufnehmen. Dies kann je nach Buchgröße einige Minuten dauern.

### c) System-Status & Analyse

Dieser Bereich ist für fortgeschrittene Nutzer gedacht, um die Funktionsweise der KI zu verstehen.

- **Letzte Anfrage im Detail:** Sehen Sie sich an, wie `dango-dingo` Ihre letzte Anfrage verarbeitet hat (Query-Analyse, gefundene Dokumente, Ranking-Scores).
- **System-Performance:** Überwachen Sie die Antwortzeiten und die Effizienz des Caches.

## 3. Tipps für die optimale Nutzung

- **Qualität der Quellen:** Die Qualität der Antworten hängt direkt von der Qualität der eingelesenen PDFs ab. Gut strukturierte, durchsuchbare PDFs sind ideal.
- **Geduld beim Ingest:** Das Hinzufügen eines neuen Buches ist ein rechenintensiver Prozess. Führen Sie ihn am besten aus, wenn Sie den Computer eine Weile nicht aktiv benötigen.
- **Feedback geben (zukünftiges Feature):** [TODO: Beschreiben, wie das geplante Feedback-System funktioniert, sobald es implementiert ist].

## 4. Fehlerbehebung (Troubleshooting)

- **Problem: Die Anwendung startet nicht oder zeigt einen Fehler.**
  - **Lösung:** Stellen Sie sicher, dass Ollama auf Ihrem Computer läuft. Öffnen Sie dazu die "Terminal"-App und geben Sie `ollama list` ein. Wenn dies einen Fehler gibt, starten Sie Ollama neu.
- **Problem: Die Anwendung findet keine Antworten, obwohl das Buch vorhanden ist.**
  - **Lösung 1:** Überprüfen Sie, ob Ihr NAS im Netzwerk erreichbar und der Datenordner korrekt gemountet ist.
  - **Lösung 2:** Führen Sie den Ingest-Prozess für das betreffende Buch erneut über die Bibliotheksverwaltung durch.

---

*Handbuch Version 0.1, Stand: 2024-05-23*

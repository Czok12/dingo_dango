"""HierarchicalCacheManager: Hierarchisches Caching für dango-dingo.

Dieses Modul stellt eine Klasse bereit, die ein mehrstufiges Cache-System verwaltet.
Die Implementierung ist ein Platzhalter und muss mit echter Logik gefüllt werden.
"""

import hashlib
import pickle
from contextlib import suppress
from pathlib import Path
from typing import Any, Optional

from dango_ki.utils import config


class HierarchicalCacheManager:
    """Verwaltet ein hierarchisches Cache-System (z.B. RAM, Disk, NAS).

    Args:
        cache_dir (Path): Basisverzeichnis für den Cache.

    """

    def __init__(self, cache_dir: Optional[Path] = None) -> None:
        """Initialisiert den Cache-Manager.

        Args:
            cache_dir (Optional[Path]):
                Pfad zum Cache-Verzeichnis. Default: config.CACHE_DIR

        """
        self.cache_dir = cache_dir or config.CACHE_DIR
        self.memory_cache: dict[str, Any] = {}
        # Stellt sicher, dass das Cache-Verzeichnis existiert
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_filepath(self, key: str) -> Path:
        """Erzeugt den Dateipfad für einen gegebenen Schlüssel."""
        # Hash des Schlüssels als Dateinamen verwenden,
        # um ungültige Zeichen zu vermeiden
        key_hash = hashlib.sha256(key.encode()).hexdigest()
        return self.cache_dir / key_hash

    def get(self, key: str) -> Optional[Any]:
        """Liefert den Wert für den Schlüssel, falls im Cache vorhanden.

        Sucht zuerst im In-Memory-Cache, dann auf der Festplatte.
        Wenn auf der Festplatte gefunden, wird der Wert in den
        In-Memory-Cache geladen.

        Args:
            key (str): Der Schlüssel.

        Returns:
            Optional[Any]: Der Wert oder None, falls nicht gefunden.

        """
        # 1. Im In-Memory-Cache suchen
        if key in self.memory_cache:
            return self.memory_cache[key]

        # 2. Im Festplatten-Cache suchen
        filepath = self._get_filepath(key)
        if filepath.exists():
            try:
                with open(filepath, "rb") as f:
                    value = pickle.load(f)
            except (pickle.UnpicklingError, OSError):
                # Bei Fehlern den Eintrag als nicht gefunden behandeln
                return None
            else:
                # In den In-Memory-Cache für schnelleren zukünftigen Zugriff laden
                self.memory_cache[key] = value
                return value

        return None

    def set(self, key: str, value: Any) -> None:
        """Speichert einen Wert im Cache (RAM und Festplatte).

        Args:
            key (str): Der Schlüssel.
            value (Any): Der zu speichernde Wert.

        """
        # 1. Im In-Memory-Cache speichern
        self.memory_cache[key] = value

        # 2. Auf der Festplatte speichern
        filepath = self._get_filepath(key)
        try:
            with open(filepath, "wb") as f:
                pickle.dump(value, f)
        except OSError:
            # Fehler beim Schreiben auf die Festplatte behandeln
            # (z.B. kein Speicherplatz)
            # Hier könnte man Logging hinzufügen
            pass

    def clear(self) -> None:
        """Leert den gesamten Cache (RAM und Festplatte)."""
        # 1. In-Memory-Cache leeren
        self.memory_cache.clear()

        # 2. Festplatten-Cache leeren
        for filepath in self.cache_dir.glob("*"):
            if filepath.is_file():
                with suppress(OSError):
                    filepath.unlink()

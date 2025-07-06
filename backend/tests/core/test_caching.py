"""Tests für den HierarchicalCacheManager."""

from pathlib import Path
from unittest.mock import patch

from dango_ki.core.caching import HierarchicalCacheManager


def test_set_and_get(tmp_path: Path) -> None:
    """Testet das Setzen und Abrufen eines Werts."""
    cache = HierarchicalCacheManager(cache_dir=tmp_path)
    cache.set("key1", "value1")

    # Aus dem Speicher-Cache abrufen
    assert cache.get("key1") == "value1"

    # Speicher-Cache leeren, um den Festplatten-Cache zu testen
    cache.memory_cache.clear()
    assert cache.get("key1") == "value1"


def test_get_from_disk(tmp_path: Path) -> None:
    """Testet, dass ein Wert von der Festplatte geladen wird."""
    cache = HierarchicalCacheManager(cache_dir=tmp_path)
    cache.set("key2", {"a": 1, "b": 2})

    # Neuen Cache-Manager erstellen, um einen leeren Speicher-Cache zu simulieren
    new_cache = HierarchicalCacheManager(cache_dir=tmp_path)
    assert new_cache.get("key2") == {"a": 1, "b": 2}


def test_clear(tmp_path: Path) -> None:
    """Testet das Leeren des Caches."""
    cache = HierarchicalCacheManager(cache_dir=tmp_path)
    cache.set("key3", "value3")
    cache.clear()

    assert cache.get("key3") is None
    assert not any(tmp_path.iterdir())


def test_corrupted_cache_file(tmp_path: Path) -> None:
    """Testet den Umgang mit einer korrupten Cache-Datei."""
    cache = HierarchicalCacheManager(cache_dir=tmp_path)
    cache.set("key4", "value4")

    # Datei mit ungültigen Daten überschreiben
    filepath = cache._get_filepath("key4")
    with open(filepath, "wb") as f:
        f.write(b"corrupted data")

    # Der Abruf sollte None zurückgeben und keinen Fehler auslösen
    assert cache.get("key4") is None


def test_os_error_on_set(tmp_path: Path) -> None:
    """Testet das Verhalten bei einem OSError während des Schreibens."""
    cache = HierarchicalCacheManager(cache_dir=tmp_path)

    with patch("builtins.open", side_effect=OSError):
        # Das Setzen sollte fehlschlagen, aber keine Ausnahme auslösen
        cache.set("key5", "value5")

    # Der Wert sollte nur im Speicher-Cache sein
    assert "key5" in cache.memory_cache
    # Es sollten keine Dateien auf der Festplatte sein
    assert not list(tmp_path.glob("*"))

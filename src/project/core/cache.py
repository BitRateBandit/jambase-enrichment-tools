import json
from pathlib import Path
from typing import Any

CACHE_DIR = Path("cache")

def cache_path(key: str) -> Path:
    CACHE_DIR.mkdir(exist_ok=True)
    return CACHE_DIR / f"{key}.json"

def load_cache(key: str) -> Any | None:
    path = cache_path(key)
    if path.exists():
        return json.loads(path.read_text())
    return None

def save_cache(key: str, data: Any):
    path = cache_path(key)
    path.write_text(json.dumps(data, indent=2))

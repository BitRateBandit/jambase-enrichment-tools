import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List


def write_manifest(
    script_name: str,
    outputs: List[str],
    config_path: str | None = None,
    notes: str | None = None,
):
    """
    Write a manifest describing what this script produced.

    Manifests are memory anchors. They answer:
    - what ran
    - when
    - with what config
    - what it produced
    """

    manifest = {
        "script": script_name,
        "timestamp_utc": datetime.utcnow().isoformat(),
        "git_commit": _git_commit(),
        "config": config_path,
        "outputs": outputs,
        "notes": notes,
    }

    Path("manifests").mkdir(exist_ok=True)

    path = Path("manifests") / f"{script_name}.json"
    path.write_text(json.dumps(manifest, indent=2))

    return path


def _git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return None

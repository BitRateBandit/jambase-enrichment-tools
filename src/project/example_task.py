"""
script: example_task.py
purpose: Demonstrate logging, retry, caching, and manifest writing
inputs: configs/example.yaml
outputs: artifacts/example_task/<timestamp>/output.json
"""

import json
from pathlib import Path
from project.core.logging import setup_logging
from project.core.retry import default_retry
from project.core.cache import load_cache, save_cache
from project.utils.time import utc_timestamp
from project.core.manifest import write_manifest

@default_retry()
def expensive_operation(x: int) -> int:
    return x * 2

def main():
    log = setup_logging("configs/logging.yaml")
    cache_key = "example_result"

    cached = load_cache(cache_key)
    if cached:
        log.info("Using cached result")
        result = cached
    else:
        log.info("Computing fresh result")
        result = expensive_operation(21)
        save_cache(cache_key, result)

    ts = utc_timestamp()
    out_dir = Path(f"artifacts/example_task/{ts}")
    out_dir.mkdir(parents=True)

    out_file = out_dir / "output.json"
    out_file.write_text(json.dumps({"result": result}, indent=2))

    log.success(f"Wrote {out_file}")
    
    write_manifest(
        script_name="example_task",
        outputs=[str(out_file)],
        config_path="configs/example.yaml",
        notes="Example task run with caching enabled"
    )

if __name__ == "__main__":
    main()

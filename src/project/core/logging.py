from loguru import logger
import sys
import yaml


def setup_logging(config_path: str | None = None):
    logger.remove()
    level = "INFO"

    if config_path:
        with open(config_path) as f:
            cfg = yaml.safe_load(f) or {}
            level = cfg.get("level", "INFO")

    logger.add(
        sys.stdout,
        level=level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan> | {message}"
        ),
    )

    return logger

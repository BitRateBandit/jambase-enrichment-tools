from datetime import datetime, timezone


def utc_timestamp() -> str:
    """
    Return a filesystem-safe UTC timestamp.
    Example: 20260209T231455Z
    """
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

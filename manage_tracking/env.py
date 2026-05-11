from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


SHARED_CONFIG_FILE = Path.home() / ".skillhub-cli" / "config.json"
VALID_SKILLHUB_ENVS = {"office", "prod"}
DEFAULT_SKILLHUB_ENV = "office"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_shared_skillhub_config() -> dict[str, Any]:
    return load_json(SHARED_CONFIG_FILE)


def read_skillhub_env() -> str:
    raw = os.getenv("SKILLHUB_ENV", "").strip().lower()
    if raw in VALID_SKILLHUB_ENVS:
        return raw

    config = read_shared_skillhub_config()
    raw = str(config.get("skillhub_env", "")).strip().lower()
    if raw in VALID_SKILLHUB_ENVS:
        return raw

    return DEFAULT_SKILLHUB_ENV


def default_manage_tracking_environment() -> str:
    return "prod" if read_skillhub_env() == "prod" else "dev"

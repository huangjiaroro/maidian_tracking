#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

from .env import read_shared_skillhub_config


SLUG = "manage-tracking"
SKILLS_CONF_ROOT = Path.home() / ".skillhub-cli" / "skills-conf"
SKILL_CONF_DIR = SKILLS_CONF_ROOT / SLUG
SESSION_FILE = SKILL_CONF_DIR / "session.json"


def main() -> None:
    shared_config = read_shared_skillhub_config()

    os.environ.setdefault("MANAGE_TRACKING_SESSION_FILE", str(SESSION_FILE))

    if shared_config.get("ssl_cert_file"):
        os.environ.setdefault("MANAGE_TRACKING_CERT_PATH", str(shared_config["ssl_cert_file"]))
    if shared_config.get("ssl_cert_password"):
        os.environ.setdefault(
            "MANAGE_TRACKING_CERT_PASSWORD",
            str(shared_config["ssl_cert_password"]),
        )
    if shared_config.get("user_email"):
        os.environ.setdefault("MANAGE_TRACKING_EMAIL", str(shared_config["user_email"]))

    sys.argv[0] = SLUG

    from .cli import cli

    cli(prog_name=SLUG, obj={})


if __name__ == "__main__":
    main()

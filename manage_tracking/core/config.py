"""Configuration helpers for the manage-tracking CLI."""

from __future__ import annotations

import base64
import hashlib
import json
import os
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

from manage_tracking.env import (
    default_manage_tracking_environment,
    read_skillhub_env,
)


DEFAULT_ENVIRONMENTS = {
    "dev": "http://localhost:9854",
    "test": "http://localhost:9854",
    "prod": "https://phonestat.hexin.cn/maidian/server",
    "dreamface": "https://115.236.100.148:7553/maidian/server",
    "ainvest": "https://cbas-gateway.ainvest.com:1443/maidian/server",
}
SKILLHUB_PROD_BASE_URL = "http://172.21.54.74:28000"

SKILLS_CONF_ROOT = Path.home() / ".skillhub-cli" / "skills-conf"
DEFAULT_SESSION_FILE = SKILLS_CONF_ROOT / "manage-tracking" / "session.json"
SESSION_FILE = Path(
    os.environ.get("MANAGE_TRACKING_SESSION_FILE", str(DEFAULT_SESSION_FILE))
).expanduser()


def _default_environment() -> str:
    return default_manage_tracking_environment()


def resolve_initialized_base_url(environment: Optional[str] = None) -> str:
    """Centralized base URL initialization.

    - skillhub_env=prod: always use the fixed prod gateway
    - skillhub_env=office: use the business environment mapping
    """

    if read_skillhub_env() == "prod":
        return SKILLHUB_PROD_BASE_URL

    env_name = (environment or _default_environment()).strip().lower()
    if env_name in DEFAULT_ENVIRONMENTS:
        return DEFAULT_ENVIRONMENTS[env_name]

    return DEFAULT_ENVIRONMENTS[_default_environment()]


def _default_base_url() -> str:
    return resolve_initialized_base_url(_default_environment()).rstrip("/")


@dataclass
class SessionConfig:
    """Session configuration stored on disk."""

    environment: str = field(default_factory=_default_environment)
    base_url: str = field(default_factory=_default_base_url)
    cert_path: Optional[str] = None
    cert_password: Optional[str] = None
    token: Optional[str] = None
    email: Optional[str] = None

    def save(self, path: Path = SESSION_FILE) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path = SESSION_FILE) -> "SessionConfig":
        if not path.exists():
            return cls()

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return cls()

        return cls(**{key: value for key, value in data.items() if value is not None})


@dataclass
class CliConfig:
    """CLI runtime configuration."""

    base_url: str
    cert_path: Optional[str] = None
    cert_password: Optional[str] = None
    token: Optional[str] = None
    json_output: bool = False
    debug: bool = False

    def to_session_config(self, environment: str) -> SessionConfig:
        return SessionConfig(
            environment=environment,
            base_url=self.base_url,
            cert_path=self.cert_path,
            cert_password=self.cert_password,
            token=self.token,
        )


def get_p12_cert_fingerprint(cert_path: str, password: str) -> str:
    """Extract the MD5 fingerprint from a P12 certificate."""

    try:
        result = subprocess.run(
            [
                "openssl",
                "pkcs12",
                "-in",
                cert_path,
                "-nokeys",
                "-passin",
                f"pass:{password}",
                "-clcerts",
                "-out",
                "/dev/stdout",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"Failed to extract certificate: {exc.stderr}") from exc
    except FileNotFoundError as exc:
        raise RuntimeError("openssl not found. Please install OpenSSL.") from exc

    cert_pem = result.stdout
    lines = cert_pem.strip().splitlines()
    cert_lines: list[str] = []
    in_cert = False
    for line in lines:
        if "-----BEGIN CERTIFICATE-----" in line:
            in_cert = True
        if in_cert:
            cert_lines.append(line)
        if "-----END CERTIFICATE-----" in line:
            break

    cert_body = "".join(cert_lines)
    cert_body = cert_body.replace("-----BEGIN CERTIFICATE-----", "")
    cert_body = cert_body.replace("-----END CERTIFICATE-----", "")
    cert_body = cert_body.replace("\n", "").replace(" ", "")

    try:
        cert_der = base64.b64decode(cert_body)
    except Exception as exc:
        raise RuntimeError(f"Failed to decode certificate: {exc}") from exc

    return hashlib.md5(cert_der).hexdigest().upper()


def resolve_base_url(url: Optional[str], env: Optional[str], session: SessionConfig) -> str:
    """Resolve the runtime base URL."""

    if url:
        return url.rstrip("/")

    if session.base_url:
        return session.base_url.rstrip("/")

    return resolve_initialized_base_url(env or session.environment).rstrip("/")


def resolve_cert(
    cert_path: Optional[str],
    cert_password: Optional[str],
    session: SessionConfig,
) -> tuple[Optional[str], Optional[str]]:
    """Resolve certificate configuration."""

    path = cert_path or session.cert_path or os.environ.get("MANAGE_TRACKING_CERT_PATH")
    password = (
        cert_password
        or session.cert_password
        or os.environ.get("MANAGE_TRACKING_CERT_PASSWORD")
    )
    return path, password

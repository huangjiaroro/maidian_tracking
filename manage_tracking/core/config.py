"""Configuration helpers for the manage-tracking CLI."""

from __future__ import annotations

import base64
import hashlib
import subprocess
from dataclasses import dataclass
from typing import Optional

from manage_tracking.env import (
    read_shared_skillhub_config,
    read_skillhub_env,
    resolve_shared_skillhub_config_file,
)


SKILLHUB_BASE_URLS = {
    "office": "https://cbas-gateway.ainvest.com:1443/maidian/server",
    "prod": "http://10.217.201.33:9854",
}


@dataclass
class RuntimeConfig:
    """SkillHub-derived runtime configuration."""

    skillhub_env: str
    base_url: str
    config_path: str
    cert_path: Optional[str] = None
    cert_password: Optional[str] = None
    email: Optional[str] = None

    def status(self) -> dict[str, object]:
        return {
            "skillhub_env": self.skillhub_env,
            "config_path": self.config_path,
            "base_url": self.base_url,
            "has_cert": bool(self.cert_path and self.cert_password),
            "email": self.email,
        }


@dataclass
class CliConfig:
    """CLI runtime configuration."""

    base_url: str
    cert_path: Optional[str] = None
    cert_password: Optional[str] = None
    email: Optional[str] = None
    json_output: bool = False
    debug: bool = False


def _optional_str(value: object) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def resolve_skillhub_base_url(skillhub_env: Optional[str] = None) -> str:
    """Resolve the management API base URL from SkillHub environment only."""

    env_name = (skillhub_env or read_skillhub_env()).strip().lower()
    return SKILLHUB_BASE_URLS.get(env_name, SKILLHUB_BASE_URLS["prod"]).rstrip("/")


def load_runtime_config() -> RuntimeConfig:
    """Load runtime configuration from SkillHub shared config without persistence."""

    shared_config = read_shared_skillhub_config()
    skillhub_env = read_skillhub_env()
    return RuntimeConfig(
        skillhub_env=skillhub_env,
        base_url=resolve_skillhub_base_url(skillhub_env),
        config_path=str(resolve_shared_skillhub_config_file()),
        cert_path=_optional_str(shared_config.get("ssl_cert_file")),
        cert_password=_optional_str(shared_config.get("ssl_cert_password")),
        email=_optional_str(shared_config.get("user_email")),
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

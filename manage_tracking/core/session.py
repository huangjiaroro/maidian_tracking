"""Persistent session helpers for the manage-tracking CLI."""

from __future__ import annotations

from typing import Any, Optional

from manage_tracking.env import read_skillhub_env

from .config import (
    DEFAULT_ENVIRONMENTS,
    SESSION_FILE,
    SessionConfig,
    resolve_initialized_base_url,
)


class Session:
    """Manages CLI session state."""

    def __init__(self, config: Optional[SessionConfig] = None):
        self._config = config or SessionConfig.load()
        self._dirty = False

    @property
    def config(self) -> SessionConfig:
        return self._config

    @property
    def environment(self) -> str:
        return self._config.environment

    @property
    def base_url(self) -> str:
        return self._config.base_url

    @property
    def cert_path(self) -> Optional[str]:
        return self._config.cert_path

    @property
    def cert_password(self) -> Optional[str]:
        return self._config.cert_password

    @property
    def token(self) -> Optional[str]:
        return self._config.token

    @property
    def email(self) -> Optional[str]:
        return self._config.email

    def set_environment(self, env: str) -> None:
        env = env.lower()
        if env not in DEFAULT_ENVIRONMENTS:
            raise ValueError(f"Unknown environment: {env}. Valid: {list(DEFAULT_ENVIRONMENTS.keys())}")

        self._config.environment = env
        self._config.base_url = resolve_initialized_base_url(env)
        self._dirty = True

    def set_base_url(self, url: str) -> None:
        self._config.base_url = url.rstrip("/")
        for name, default_url in DEFAULT_ENVIRONMENTS.items():
            if default_url.rstrip("/") == self._config.base_url:
                self._config.environment = name
                break
        self._dirty = True

    def set_cert(self, path: str, password: str) -> None:
        self._config.cert_path = path
        self._config.cert_password = password
        self._dirty = True

    def set_token(self, token: str) -> None:
        self._config.token = token
        self._dirty = True

    def set_email(self, email: str) -> None:
        self._config.email = email
        self._dirty = True

    def clear_cert(self) -> None:
        self._config.cert_path = None
        self._config.cert_password = None
        self._dirty = True

    def save(self) -> None:
        if self._dirty:
            self._config.save()
            self._dirty = False

    def reset(self) -> None:
        self._config = SessionConfig()
        if SESSION_FILE.exists():
            SESSION_FILE.unlink()
        self._dirty = False

    def status(self) -> dict[str, Any]:
        return {
            "skillhub_env": read_skillhub_env(),
            "environment": self._config.environment,
            "base_url": self._config.base_url,
            "has_cert": self._config.cert_path is not None,
            "has_token": self._config.token is not None,
            "email": self._config.email,
        }


def create_session() -> Session:
    return Session()

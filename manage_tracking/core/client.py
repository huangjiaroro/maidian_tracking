"""HTTP client for the manage-tracking API."""

from __future__ import annotations

import json
import os
import ssl
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional

from .config import CliConfig


class CertP12HTTPSHandler(urllib.request.HTTPSHandler):
    """Custom HTTPS handler that supports P12 certificate authentication."""

    def __init__(self, cert_path: str, cert_password: str, debug: bool = False):
        super().__init__(debuglevel=1 if debug else 0)
        self.cert_path = cert_path
        self.cert_password = cert_password
        self.debug = debug
        self.temp_cert_file: Optional[str] = None

    def https_open(self, req):  # type: ignore[override]
        ctx = self._make_ssl_context()
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
        return opener.open(req)

    def _make_ssl_context(self) -> ssl.SSLContext:
        from cryptography.hazmat.primitives.serialization import (
            Encoding,
            NoEncryption,
            PrivateFormat,
            pkcs12,
        )

        cert_path_obj = Path(self.cert_path)
        if not cert_path_obj.exists():
            raise FileNotFoundError(f"Certificate file not found: {self.cert_path}")

        try:
            with cert_path_obj.open("rb") as file_obj:
                p12_data = file_obj.read()

            private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
                p12_data,
                self.cert_password.encode(),
            )
            if private_key is None or certificate is None:
                raise RuntimeError("P12 file does not contain a private key and certificate.")

            cert_pem = certificate.public_bytes(Encoding.PEM)
            key_pem = private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.PKCS8,
                encryption_algorithm=NoEncryption(),
            )

            fd, temp_path = tempfile.mkstemp(suffix=".pem", prefix="cert_")
            os.write(fd, key_pem)
            os.write(fd, cert_pem)
            if additional_certs:
                for cert in additional_certs:
                    os.write(fd, cert.public_bytes(Encoding.PEM))
            os.close(fd)
            self.temp_cert_file = temp_path
        except Exception as exc:
            raise RuntimeError(f"Failed to load P12 certificate: {exc}") from exc

        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        try:
            ctx.set_ciphers("DEFAULT@SECLEVEL=0")
        except Exception:
            try:
                ctx.set_ciphers("DEFAULT")
            except Exception:
                pass

        try:
            ctx.load_cert_chain(certfile=self.temp_cert_file)
        except Exception as exc:
            raise RuntimeError(f"Failed to load certificate chain: {exc}") from exc

        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def __del__(self) -> None:
        if self.temp_cert_file and os.path.exists(self.temp_cert_file):
            try:
                os.remove(self.temp_cert_file)
            except Exception:
                pass


class ApiError(Exception):
    """API request error."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        error: Optional[Any] = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error = error


class ApiClient:
    """HTTP client for manage-tracking API."""

    def __init__(self, config: CliConfig):
        self.config = config
        self.base_url = config.base_url.rstrip("/")

    def _build_url(self, path: str) -> str:
        if path.startswith("http"):
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def _build_headers(self, extra_headers: Optional[dict[str, str]] = None) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if self.config.email:
            headers["cbas_email"] = self.config.email

        if extra_headers:
            headers.update(extra_headers)

        return headers

    def _create_ssl_context(self) -> ssl.SSLContext:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            ctx.set_ciphers("DEFAULT@SECLEVEL=0")
        except Exception:
            try:
                ctx.set_ciphers("DEFAULT")
            except Exception:
                pass
        return ctx

    def request(
        self,
        method: str,
        path: str,
        data: Optional[dict[str, Any] | list[Any]] = None,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> dict[str, Any] | list[Any]:
        url = self._build_url(path)

        if params:
            query_string = urllib.parse.urlencode(
                {key: value for key, value in params.items() if value is not None},
                doseq=True,
            )
            if query_string:
                url = f"{url}?{query_string}"

        body = json.dumps(data).encode("utf-8") if data is not None else None
        request = urllib.request.Request(
            url,
            data=body,
            headers=self._build_headers(headers),
            method=method,
        )

        if self.config.cert_path and self.config.cert_password:
            opener = urllib.request.build_opener(
                CertP12HTTPSHandler(
                    self.config.cert_path,
                    self.config.cert_password,
                    debug=self.config.debug,
                )
            )
        else:
            ctx = self._create_ssl_context()
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))

        try:
            with opener.open(request, timeout=30) as response:
                response_body = response.read().decode("utf-8")
                if not response_body:
                    return {"_status_code": response.status}
                return json.loads(response_body)
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8") if exc.fp else ""
            try:
                error_json = json.loads(error_body)
            except json.JSONDecodeError:
                raise ApiError(status_code=exc.code, message=error_body or str(exc)) from exc
            raise ApiError(
                status_code=exc.code,
                message=error_json.get("message", str(error_json)),
                error=error_json,
            ) from exc
        except urllib.error.URLError as exc:
            raise ApiError(message=f"Connection error: {exc.reason}") from exc
        except json.JSONDecodeError as exc:
            raise ApiError(message=f"Invalid JSON response: {exc}") from exc

    def get(self, path: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> dict[str, Any] | list[Any]:
        return self.request("GET", path, params=params, **kwargs)

    def post(self, path: str, data: Optional[dict[str, Any]] = None, **kwargs: Any) -> dict[str, Any] | list[Any]:
        return self.request("POST", path, data=data, **kwargs)

    def put(self, path: str, data: Optional[dict[str, Any]] = None, **kwargs: Any) -> dict[str, Any] | list[Any]:
        return self.request("PUT", path, data=data, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        return self.request("DELETE", path, **kwargs)

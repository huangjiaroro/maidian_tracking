"""EasyFetch SQL execution helpers."""

from __future__ import annotations

import json
import os
import ssl
import tempfile
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, pkcs12


DEFAULT_EASY_FETCH_BASE_URLS = {
    "office": "https://cbas-gateway.ainvest.com:1443/sdmp/easyfetch",
    "prod": "http://10.217.201.17:9596/easyfetch",
}
DEFAULT_TIMEOUT_SECONDS = 300


class SqlFetchError(RuntimeError):
    """Raised when SQL execution cannot be completed."""


@dataclass
class SqlFetchConfig:
    """Runtime configuration for EasyFetch SQL calls."""

    base_url: str
    skillhub_env: str = "prod"
    cert_path: Optional[str] = None
    cert_password: Optional[str] = None
    email: Optional[str] = None
    timeout: int = DEFAULT_TIMEOUT_SECONDS

    @classmethod
    def from_runtime(cls, runtime: Any, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> "SqlFetchConfig":
        skillhub_env = str(getattr(runtime, "skillhub_env", "prod")).strip().lower()
        default_base_url = DEFAULT_EASY_FETCH_BASE_URLS.get(
            skillhub_env,
            DEFAULT_EASY_FETCH_BASE_URLS["prod"],
        )

        return cls(
            base_url=default_base_url.rstrip("/"),
            skillhub_env=skillhub_env,
            cert_path=getattr(runtime, "cert_path", None),
            cert_password=getattr(runtime, "cert_password", None),
            email=getattr(runtime, "email", None),
            timeout=timeout,
        )


def sanitize_sql(sql: str) -> str:
    """Clean common shell escaping artifacts from SQL text."""

    return sql.replace("\\'", "'").replace('\\"', '"').strip()


def get_catalog_name(catalog_name: str, skillhub_env: str) -> str:
    """Match the catalog aliasing used by the source Claudable tools."""

    if catalog_name == "starrocks" and skillhub_env in {"office", "prod"}:
        return "starrocks-claude"
    return catalog_name


def format_size(size_bytes: int) -> str:
    """Format byte size for CLI output."""

    if size_bytes == 0:
        return "0B"
    size_names = ["B", "KB", "MB", "GB"]
    index = 0
    value = float(size_bytes)
    while value >= 1024 and index < len(size_names) - 1:
        value /= 1024.0
        index += 1
    return f"{value:.2f}{size_names[index]}"


class EasyFetchSqlClient:
    """Small stdlib HTTP client for EasyFetch SQL endpoints."""

    def __init__(self, config: SqlFetchConfig):
        self.config = config
        self._temp_cert_file: Optional[str] = None

    def _build_headers(self, content_type: str = "application/json") -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "Content-Type": content_type,
        }
        if self.config.email:
            headers["CBAS_EMAIL"] = self.config.email
        return headers

    def _make_ssl_context(self) -> ssl.SSLContext:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        try:
            ctx.set_ciphers("DEFAULT@SECLEVEL=0")
        except Exception:
            try:
                ctx.set_ciphers("DEFAULT")
            except Exception:
                pass

        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        if self.config.cert_path:
            cert_path = Path(self.config.cert_path).expanduser()
            if not cert_path.exists():
                raise SqlFetchError(f"Certificate file not found: {cert_path}")

            if cert_path.suffix.lower() in {".p12", ".pfx"}:
                with cert_path.open("rb") as file_obj:
                    p12_data = file_obj.read()
                private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
                    p12_data,
                    (self.config.cert_password or "").encode(),
                )
                if private_key is None or certificate is None:
                    raise SqlFetchError("P12 file does not contain a private key and certificate.")

                fd, temp_path = tempfile.mkstemp(suffix=".pem", prefix="easyfetch_cert_")
                try:
                    os.write(
                        fd,
                        private_key.private_bytes(
                            encoding=Encoding.PEM,
                            format=PrivateFormat.PKCS8,
                            encryption_algorithm=NoEncryption(),
                        ),
                    )
                    os.write(fd, certificate.public_bytes(Encoding.PEM))
                    if additional_certs:
                        for cert in additional_certs:
                            os.write(fd, cert.public_bytes(Encoding.PEM))
                finally:
                    os.close(fd)
                self._temp_cert_file = temp_path
                ctx.load_cert_chain(certfile=temp_path)
            else:
                ctx.load_cert_chain(certfile=str(cert_path), password=self.config.cert_password or None)

        return ctx

    def _make_opener(self) -> urllib.request.OpenerDirector:
        if self.config.base_url.startswith("https://"):
            return urllib.request.build_opener(urllib.request.HTTPSHandler(context=self._make_ssl_context()))
        return urllib.request.build_opener()

    def close(self) -> None:
        if self._temp_cert_file and os.path.exists(self._temp_cert_file):
            try:
                os.remove(self._temp_cert_file)
            except Exception:
                pass
        self._temp_cert_file = None

    def post_json(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.config.base_url}{endpoint}"
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=body,
            headers=self._build_headers(),
            method="POST",
        )
        opener = self._make_opener()
        try:
            with opener.open(request, timeout=self.config.timeout) as response:
                response_body = response.read().decode("utf-8", errors="replace")
                return _parse_response(response.status, dict(response.headers), response_body)
        except urllib.error.HTTPError as exc:
            body_text = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
            return _parse_response(exc.code, dict(exc.headers), body_text)
        except urllib.error.URLError as exc:
            raise SqlFetchError(f"Connection error: {exc.reason}") from exc
        finally:
            self.close()

    def download_json(self, endpoint: str, payload: dict[str, Any], file_path: Path) -> int:
        url = f"{self.config.base_url}{endpoint}"
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=body,
            headers=self._build_headers(),
            method="POST",
        )
        opener = self._make_opener()
        size = 0
        try:
            with opener.open(request, timeout=self.config.timeout) as response:
                first_chunk = response.read(1024 * 64)
                content_type = response.headers.get("Content-Type", "").lower()
                if "application/json" in content_type or first_chunk.lstrip().startswith(b"{"):
                    body = first_chunk + response.read()
                    body_text = body.decode("utf-8", errors="replace")
                    try:
                        error_payload = json.loads(body_text)
                    except json.JSONDecodeError:
                        raise SqlFetchError(body_text or "Download endpoint returned a JSON-like non-CSV response")
                    status_msg = error_payload.get("status_msg") or error_payload.get("message") or body_text
                    raise SqlFetchError(str(status_msg))

                file_path.parent.mkdir(parents=True, exist_ok=True)
                with file_path.open("wb") as file_obj:
                    if first_chunk:
                        file_obj.write(first_chunk)
                        size += len(first_chunk)
                    while True:
                        chunk = response.read(1024 * 64)
                        if not chunk:
                            break
                        file_obj.write(chunk)
                        size += len(chunk)
            return size
        except urllib.error.HTTPError as exc:
            body_text = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
            raise SqlFetchError(f"HTTP {exc.code}: {body_text or exc.reason}") from exc
        except urllib.error.URLError as exc:
            raise SqlFetchError(f"Connection error: {exc.reason}") from exc
        finally:
            self.close()


def _parse_response(status: int, headers: dict[str, str], body: str) -> dict[str, Any]:
    result: dict[str, Any] = {"status": status, "headers": headers}
    try:
        result["json"] = json.loads(body) if body else None
    except json.JSONDecodeError:
        result["body"] = body
    return result


def _fetch_payload(sql: str, datasource_name: str, config: SqlFetchConfig) -> dict[str, Any]:
    return {
        "sql": sanitize_sql(sql),
        "catalog_name": get_catalog_name(datasource_name, config.skillhub_env),
        "timeout_in_second": config.timeout,
    }


def _result_summary(result: dict[str, Any]) -> dict[str, Any]:
    data = result.get("data") if isinstance(result, dict) else None
    if not isinstance(data, dict):
        return {}

    query_result = data.get("result")
    if isinstance(query_result, dict):
        rows = query_result.get("row_list") or []
        columns = query_result.get("column_list") or query_result.get("columns") or []
        return {
            "preview_rows": len(rows) if isinstance(rows, list) else None,
            "columns_count": len(columns) if isinstance(columns, list) else None,
        }

    body = data.get("body")
    title = data.get("title")
    if isinstance(body, list) or isinstance(title, list):
        return {
            "preview_rows": len(body) if isinstance(body, list) else None,
            "columns_count": len(title) if isinstance(title, list) else None,
            "total_rows": data.get("total"),
        }
    return {}


def preview_sql_result(sql: str, datasource_name: str, config: SqlFetchConfig) -> dict[str, Any]:
    """Run a preview SQL query through EasyFetch."""

    client = EasyFetchSqlClient(config)
    response = client.post_json("/v2/tool/data/fetch", _fetch_payload(sql, datasource_name, config))
    if response.get("status") != 200:
        return {
            "success": False,
            "message": "SQL preview failed",
            "error": f"HTTP {response.get('status')}: {response.get('body', '')}",
        }

    result = response.get("json")
    if not isinstance(result, dict):
        return {"success": False, "message": "SQL preview failed", "error": "Non-JSON response"}
    if result.get("status_code") != 0:
        return {
            "success": False,
            "message": "SQL preview failed",
            "error": result.get("status_msg", "Unknown error"),
            "status_code": result.get("status_code"),
        }

    return {
        "success": True,
        "message": "SQL preview succeeded",
        **_result_summary(result),
        "data": result,
    }


def explain_sql(sql: str, datasource_name: str, config: SqlFetchConfig) -> dict[str, Any]:
    """Run EXPLAIN for a SQL query through EasyFetch."""

    response = preview_sql_result(f"EXPLAIN {sanitize_sql(sql)}", datasource_name, config)
    if not response.get("success"):
        response["message"] = "SQL explain failed"
        return response

    result = response.get("data", {})
    data = result.get("data", {}) if isinstance(result, dict) else {}
    query_result = data.get("result", {}) if isinstance(data, dict) else {}
    row_list = query_result.get("row_list", []) if isinstance(query_result, dict) else []
    plan_lines = []
    if isinstance(row_list, list):
        for row in row_list:
            if isinstance(row, (list, tuple)) and row:
                plan_lines.append(str(row[0]))
            else:
                plan_lines.append(str(row))

    return {
        "success": True,
        "message": "SQL explain succeeded",
        "plan": "\n".join(plan_lines) if plan_lines else "(empty plan)",
    }


def download_sql_result(
    sql: str,
    datasource_name: str,
    project_path: str,
    config: SqlFetchConfig,
) -> dict[str, Any]:
    """Run SQL and save the returned CSV stream under data_file/intermediate."""

    if not project_path:
        return {"success": False, "message": "project_path is required"}

    output_dir = Path(project_path).expanduser() / "data_file" / "intermediate"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"tracking_query_result_{timestamp}.csv"

    client = EasyFetchSqlClient(config)
    try:
        file_size = client.download_json(
            "/v2/tool/data/fetch_presto_download",
            _fetch_payload(sql, datasource_name, config),
            file_path,
        )
    except SqlFetchError as exc:
        return {"success": False, "message": "SQL download failed", "error": str(exc)}

    return {
        "success": True,
        "message": "SQL download succeeded",
        "file_path": str(file_path),
        "file_size": format_size(file_size),
    }

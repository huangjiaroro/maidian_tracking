#!/usr/bin/env python3
"""manage-tracking CLI."""

from __future__ import annotations

import json
import sys
from typing import Any, Optional

import click

from .core.api import ManageTrackingApi
from .core.client import ApiClient, ApiError
from .core.config import CliConfig, RuntimeConfig, load_runtime_config
from .core.sql_fetch import (
    SqlFetchConfig,
    download_sql_result,
    explain_sql,
    get_catalog_name,
    preview_sql_result,
)


_api: Optional[ManageTrackingApi] = None
_json_output = False


def output(result: Any, json_only: bool = False) -> None:
    if _json_output or json_only:
        if hasattr(result, "__dict__"):
            print(json.dumps(result.__dict__, indent=2, default=str))
        else:
            print(json.dumps(result, indent=2, default=str))
        return

    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    elif isinstance(result, list):
        for item in result:
            print(item)
    else:
        print(result)


def handle_api_error(exc: ApiError) -> None:
    if _json_output:
        print(json.dumps({"error": exc.message, "status_code": exc.status_code}, indent=2))
    else:
        print(f"Error: {exc.message}", file=sys.stderr)
    raise SystemExit(1)


def handle_cli_error(message: str) -> None:
    if _json_output:
        print(json.dumps({"error": message}, indent=2))
    else:
        print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_sql_input(sql: Optional[str], sql_file: Optional[str]) -> str:
    if bool(sql) == bool(sql_file):
        handle_cli_error("Provide exactly one of --sql or --sql-file")
    if sql_file:
        try:
            return open(sql_file, encoding="utf-8").read()
        except OSError as exc:
            handle_cli_error(f"Failed to read SQL file: {exc}")
    return sql or ""


def make_sql_fetch_config(
    ctx: click.Context,
    *,
    timeout: int,
) -> SqlFetchConfig:
    runtime: RuntimeConfig = ctx.obj["runtime"]
    return SqlFetchConfig.from_runtime(runtime, timeout=timeout)


@click.group()
@click.option("--json", "json_output", is_flag=True, help="Output as JSON")
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.pass_context
def cli(
    ctx: click.Context,
    json_output: bool,
    debug: bool,
) -> None:
    """manage-tracking - CLI for tracking point management."""

    global _json_output, _api

    _json_output = json_output
    _api = None
    runtime = load_runtime_config()

    config = CliConfig(
        base_url=runtime.base_url,
        cert_path=runtime.cert_path,
        cert_password=runtime.cert_password,
        email=runtime.email,
        json_output=json_output,
        debug=debug,
    )
    client = ApiClient(config)
    _api = ManageTrackingApi(client)

    ctx.ensure_object(dict)
    ctx.obj["runtime"] = runtime
    ctx.obj["api"] = _api


@cli.command("ping")
@click.pass_context
def ping(ctx: click.Context) -> None:
    """Return a local health payload without calling the API."""

    runtime: RuntimeConfig = ctx.obj["runtime"]
    output(
        {
            "status": "ok",
            "entrypoint": "manage-tracking",
            **runtime.status(),
        }
    )


@cli.group("auth")
def auth_group() -> None:
    """Authentication and user commands."""


@auth_group.command("whoami")
@click.pass_context
def auth_whoami(ctx: click.Context) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_current_user())
    except ApiError as exc:
        handle_api_error(exc)


@auth_group.command("query")
@click.argument("email")
@click.pass_context
def auth_query(ctx: click.Context, email: str) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.query_user(email))
    except ApiError as exc:
        handle_api_error(exc)


@cli.group("app")
def app_group() -> None:
    """App management commands."""


@app_group.command("list")
@click.option("--page", default=1, help="Page number")
@click.option("--size", default=20, help="Page size")
@click.pass_context
def app_list(ctx: click.Context, page: int, size: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.list_apps(page=page, size=size))
    except ApiError as exc:
        handle_api_error(exc)


@app_group.command("get")
@click.argument("id", type=int)
@click.pass_context
def app_get(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_app(id))
    except ApiError as exc:
        handle_api_error(exc)


@app_group.command("create")
@click.option("--name", required=True, help="App name")
@click.option("--key", help="App key")
@click.pass_context
def app_create(ctx: click.Context, name: str, key: Optional[str]) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    data = {"name": name}
    if key:
        data["appKey"] = key
    try:
        output(api.create_app(data))
    except ApiError as exc:
        handle_api_error(exc)


@app_group.command("delete")
@click.argument("id", type=int)
@click.pass_context
def app_delete(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.delete_app(id))
    except ApiError as exc:
        handle_api_error(exc)


@cli.group("page")
def page_group() -> None:
    """Page management commands."""


@page_group.command("list")
@click.option("--app-id", type=int, help="Filter by app ID")
@click.option("--page", default=1, help="Page number")
@click.option("--size", default=20, help="Page size")
@click.pass_context
def page_list(ctx: click.Context, app_id: Optional[int], page: int, size: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.list_pages(app_id=app_id, page=page, size=size))
    except ApiError as exc:
        handle_api_error(exc)


@page_group.command("get")
@click.argument("id", type=int)
@click.pass_context
def page_get(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_page(id))
    except ApiError as exc:
        handle_api_error(exc)


@page_group.command("create")
@click.option("--name", required=True, help="Page name")
@click.option("--app-id", "app_id", type=int, required=True, help="App ID")
@click.pass_context
def page_create(ctx: click.Context, name: str, app_id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.create_page({"name": name, "appId": app_id}))
    except ApiError as exc:
        handle_api_error(exc)


@page_group.command("delete")
@click.argument("id", type=int)
@click.pass_context
def page_delete(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.delete_page(id))
    except ApiError as exc:
        handle_api_error(exc)


@cli.group("section")
def section_group() -> None:
    """Section management commands."""


@section_group.command("list")
@click.option("--page", default=1, help="Page number")
@click.option("--size", default=20, help="Page size")
@click.option("--name", help="Filter by section name")
@click.pass_context
def section_list(ctx: click.Context, page: int, size: int, name: Optional[str]) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    params: dict[str, Any] = {"page": page, "size": size}
    if name:
        params["name"] = name
    try:
        output(api.list_functions(**params))
    except ApiError as exc:
        handle_api_error(exc)


@section_group.command("get")
@click.argument("id", type=int)
@click.pass_context
def section_get(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_function(id))
    except ApiError as exc:
        handle_api_error(exc)


@section_group.command("create")
@click.option("--name", required=True, help="Section name")
@click.option("--page-id", "page_id", type=int, required=True, help="Page ID")
@click.pass_context
def section_create(ctx: click.Context, name: str, page_id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.create_function({"name": name, "pageId": page_id}))
    except ApiError as exc:
        handle_api_error(exc)


@section_group.command("delete")
@click.argument("id", type=int)
@click.pass_context
def section_delete(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.delete_function(id))
    except ApiError as exc:
        handle_api_error(exc)


@cli.group("element")
def element_group() -> None:
    """Element management commands."""


@element_group.command("list")
@click.option("--page", default=1, help="Page number")
@click.option("--size", default=20, help="Page size")
@click.option("--section-id", "section_id", type=int, help="Filter by section ID")
@click.pass_context
def element_list(
    ctx: click.Context,
    page: int,
    size: int,
    section_id: Optional[int],
) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    params: dict[str, Any] = {"page": page, "size": size}
    if section_id:
        params["functionId"] = section_id
    try:
        output(api.list_controls(**params))
    except ApiError as exc:
        handle_api_error(exc)


@element_group.command("create")
@click.option("--name", required=True, help="Element name")
@click.option("--section-id", "section_id", type=int, required=True, help="Section ID")
@click.pass_context
def element_create(ctx: click.Context, name: str, section_id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.create_control({"name": name, "functionId": section_id}))
    except ApiError as exc:
        handle_api_error(exc)


@element_group.command("delete")
@click.argument("id", type=int)
@click.pass_context
def element_delete(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.delete_control(id))
    except ApiError as exc:
        handle_api_error(exc)


@cli.group("track")
def track_group() -> None:
    """Track management commands."""


@track_group.command("list")
@click.option("--page", default=1, help="Page number")
@click.option("--size", default=20, help="Page size")
@click.option("--app-id", "app_id", type=int, help="Filter by app ID")
@click.option("--page-id", "page_id", type=int, help="Filter by page ID")
@click.option("--function-id", "function_id", type=int, help="Filter by function ID")
@click.pass_context
def track_list(
    ctx: click.Context,
    page: int,
    size: int,
    app_id: Optional[int],
    page_id: Optional[int],
    function_id: Optional[int],
) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    params: dict[str, Any] = {"page": page, "size": size}
    if app_id:
        params["appId"] = app_id
    if page_id:
        params["pageId"] = page_id
    if function_id:
        params["functionId"] = function_id
    try:
        output(api.list_tracks(**params))
    except ApiError as exc:
        handle_api_error(exc)


@track_group.command("get")
@click.argument("id", type=int)
@click.pass_context
def track_get(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_track(id))
    except ApiError as exc:
        handle_api_error(exc)


@track_group.command("get-by-key")
@click.option("--key", "track_key", required=True, help="Track key")
@click.pass_context
def track_get_by_key(ctx: click.Context, track_key: str) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_track_by_key(track_key))
    except ApiError as exc:
        handle_api_error(exc)


@track_group.command("search")
@click.argument("key")
@click.pass_context
def track_search(ctx: click.Context, key: str) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.search_tracks(key))
    except ApiError as exc:
        handle_api_error(exc)


@track_group.command("all")
@click.pass_context
def track_all(ctx: click.Context) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.get_all_tracks())
    except ApiError as exc:
        handle_api_error(exc)


@track_group.command("create")
@click.option("--name", required=True, help="Track name")
@click.option("--event-code", "event_code", help="Event code")
@click.option("--page-id", "page_id", type=int, help="Page ID")
@click.option("--function-id", "function_id", type=int, help="Function ID")
@click.pass_context
def track_create(
    ctx: click.Context,
    name: str,
    event_code: Optional[str],
    page_id: Optional[int],
    function_id: Optional[int],
) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    data: dict[str, Any] = {"name": name}
    if event_code:
        data["eventCode"] = event_code
    if page_id:
        data["pageId"] = page_id
    if function_id:
        data["functionId"] = function_id
    try:
        output(api.create_track(data))
    except ApiError as exc:
        handle_api_error(exc)


@track_group.command("delete")
@click.argument("id", type=int)
@click.pass_context
def track_delete(ctx: click.Context, id: int) -> None:
    api: ManageTrackingApi = ctx.obj["api"]
    try:
        output(api.delete_track(id))
    except ApiError as exc:
        handle_api_error(exc)


@cli.group("data")
def data_group() -> None:
    """Tracking data SQL execution commands."""


@data_group.command("preview")
@click.option("--sql", help="SQL text to execute")
@click.option("--sql-file", help="Path to a SQL file to execute")
@click.option(
    "--datasource-name",
    type=click.Choice(["presto-hive", "starrocks"]),
    default="presto-hive",
    show_default=True,
)
@click.option("--timeout", default=300, show_default=True, help="Request timeout in seconds")
@click.pass_context
def data_preview(
    ctx: click.Context,
    sql: Optional[str],
    sql_file: Optional[str],
    datasource_name: str,
    timeout: int,
) -> None:
    """Preview SQL result through EasyFetch."""

    query_sql = read_sql_input(sql, sql_file)
    config = make_sql_fetch_config(
        ctx,
        timeout=timeout,
    )
    output(preview_sql_result(query_sql, datasource_name, config))


@data_group.command("download")
@click.option("--sql", help="SQL text to execute")
@click.option("--sql-file", help="Path to a SQL file to execute")
@click.option(
    "--datasource-name",
    type=click.Choice(["presto-hive", "starrocks"]),
    default="presto-hive",
    show_default=True,
)
@click.option("--project-path", default=".", show_default=True, help="Project root for data_file/intermediate output")
@click.option("--timeout", default=300, show_default=True, help="Request timeout in seconds")
@click.pass_context
def data_download(
    ctx: click.Context,
    sql: Optional[str],
    sql_file: Optional[str],
    datasource_name: str,
    project_path: str,
    timeout: int,
) -> None:
    """Download full SQL result to data_file/intermediate as CSV."""

    query_sql = read_sql_input(sql, sql_file)
    config = make_sql_fetch_config(
        ctx,
        timeout=timeout,
    )
    output(download_sql_result(query_sql, datasource_name, project_path, config))


@data_group.command("explain")
@click.option("--sql", help="SQL text to explain")
@click.option("--sql-file", help="Path to a SQL file to explain")
@click.option(
    "--datasource-name",
    type=click.Choice(["presto-hive", "starrocks"]),
    default="presto-hive",
    show_default=True,
)
@click.option("--timeout", default=300, show_default=True, help="Request timeout in seconds")
@click.pass_context
def data_explain(
    ctx: click.Context,
    sql: Optional[str],
    sql_file: Optional[str],
    datasource_name: str,
    timeout: int,
) -> None:
    """Explain SQL through EasyFetch."""

    query_sql = read_sql_input(sql, sql_file)
    config = make_sql_fetch_config(
        ctx,
        timeout=timeout,
    )
    output(explain_sql(query_sql, datasource_name, config))


@data_group.command("config")
@click.option("--timeout", default=300, show_default=True, help="Request timeout in seconds")
@click.pass_context
def data_config(
    ctx: click.Context,
    timeout: int,
) -> None:
    """Show SQL execution configuration without secrets."""

    config = make_sql_fetch_config(
        ctx,
        timeout=timeout,
    )
    output(
        {
            "easy_fetch_base_url": config.base_url,
            "skillhub_env": config.skillhub_env,
            "has_cert": bool(config.cert_path and config.cert_password),
            "email": config.email,
            "starrocks_catalog": get_catalog_name("starrocks", config.skillhub_env),
            "timeout": config.timeout,
        }
    )


@cli.group("config")
def config_group() -> None:
    """Configuration management commands."""


@config_group.command("show")
@click.pass_context
def config_show(ctx: click.Context) -> None:
    runtime: RuntimeConfig = ctx.obj["runtime"]
    output(runtime.status())


@cli.command("repl")
@click.pass_context
def repl(ctx: click.Context) -> None:
    """Enter interactive REPL mode."""

    import code

    api: ManageTrackingApi = ctx.obj["api"]
    runtime: RuntimeConfig = ctx.obj["runtime"]
    console_locals = {
        "api": api,
        "runtime": runtime,
        "output": output,
        "json": lambda value: print(json.dumps(value, indent=2)),
    }
    banner = """
manage-tracking REPL
Available objects:
  api     - ManageTrackingApi instance
  runtime - RuntimeConfig instance
  output  - Print formatted output
  json    - Print as JSON
"""
    code.interact(banner=banner, local=console_locals)


def main() -> None:
    cli(obj={})


if __name__ == "__main__":
    main()

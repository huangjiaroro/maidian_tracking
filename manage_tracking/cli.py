#!/usr/bin/env python3
"""manage-tracking CLI."""

from __future__ import annotations

import json
import os
import sys
from typing import Any, Optional

import click

from .core.api import ManageTrackingApi
from .core.client import ApiClient, ApiError
from .core.config import CliConfig, resolve_base_url, resolve_cert
from .core.session import Session, create_session
from .env import read_skillhub_env


_session: Optional[Session] = None
_api: Optional[ManageTrackingApi] = None
_json_output = False


def get_session() -> Session:
    global _session
    if _session is None:
        _session = create_session()
    return _session


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


@click.group()
@click.option("--url", help="Base URL for the API")
@click.option("--cert-path", help="Path to P12 certificate file")
@click.option("--cert-password", help="P12 certificate password")
@click.option("--token", help="Auth token")
@click.option(
    "--env",
    type=click.Choice(["dev", "test", "prod", "dreamface", "ainvest"]),
    help="Environment name",
)
@click.option("--json", "json_output", is_flag=True, help="Output as JSON")
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.pass_context
def cli(
    ctx: click.Context,
    url: Optional[str],
    cert_path: Optional[str],
    cert_password: Optional[str],
    token: Optional[str],
    env: Optional[str],
    json_output: bool,
    debug: bool,
) -> None:
    """manage-tracking - CLI for tracking point management."""

    global _json_output, _api, _session

    _json_output = json_output
    _session = None
    _api = None

    session = get_session()

    if env:
        session.set_environment(env)

    resolved_url = resolve_base_url(url, env, session.config)
    if resolved_url and resolved_url != session.base_url:
        session.set_base_url(resolved_url)

    resolved_cert_path, resolved_cert_password = resolve_cert(
        cert_path,
        cert_password,
        session.config,
    )
    if resolved_cert_path and resolved_cert_password:
        session.set_cert(resolved_cert_path, resolved_cert_password)

    resolved_token = token or os.environ.get("MANAGE_TRACKING_TOKEN") or session.token
    if resolved_token:
        session.set_token(resolved_token)

    resolved_email = os.environ.get("MANAGE_TRACKING_EMAIL") or session.email
    if resolved_email:
        session.set_email(resolved_email)

    config = CliConfig(
        base_url=session.base_url,
        cert_path=session.cert_path,
        cert_password=session.cert_password,
        token=session.token,
        json_output=json_output,
        debug=debug,
    )
    client = ApiClient(config)
    client.session = session.config
    _api = ManageTrackingApi(client)

    ctx.ensure_object(dict)
    ctx.obj["session"] = session
    ctx.obj["api"] = _api


@cli.command("ping")
@click.pass_context
def ping(ctx: click.Context) -> None:
    """Return a local health payload without calling the API."""

    session: Session = ctx.obj["session"]
    output(
        {
            "status": "ok",
            "entrypoint": "manage-tracking",
            "skillhub_env": read_skillhub_env(),
            "environment": session.environment,
            "base_url": session.base_url,
            "has_cert": session.cert_path is not None,
            "has_token": session.token is not None,
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


@cli.group("config")
def config_group() -> None:
    """Configuration management commands."""


@config_group.command("show")
@click.pass_context
def config_show(ctx: click.Context) -> None:
    session: Session = ctx.obj["session"]
    output(session.status())


@config_group.command("set-url")
@click.argument("url")
@click.pass_context
def config_set_url(ctx: click.Context, url: str) -> None:
    session: Session = ctx.obj["session"]
    session.set_base_url(url)
    session.save()
    output({"message": f"URL set to {url}"})


@config_group.command("set-env")
@click.argument("env", type=click.Choice(["dev", "test", "prod", "dreamface", "ainvest"]))
@click.pass_context
def config_set_env(ctx: click.Context, env: str) -> None:
    session: Session = ctx.obj["session"]
    session.set_environment(env)
    session.save()
    output({"message": f"Environment set to {env}", "url": session.base_url})


@config_group.command("set-cert")
@click.argument("cert_path")
@click.argument("cert_password")
@click.pass_context
def config_set_cert(ctx: click.Context, cert_path: str, cert_password: str) -> None:
    session: Session = ctx.obj["session"]
    session.set_cert(cert_path, cert_password)
    session.save()
    output({"message": "Certificate configured"})


@config_group.command("clear-cert")
@click.pass_context
def config_clear_cert(ctx: click.Context) -> None:
    session: Session = ctx.obj["session"]
    session.clear_cert()
    session.save()
    output({"message": "Certificate cleared"})


@config_group.command("reset")
@click.pass_context
def config_reset(ctx: click.Context) -> None:
    session: Session = ctx.obj["session"]
    session.reset()
    output({"message": "Configuration reset to defaults"})


@cli.command("repl")
@click.pass_context
def repl(ctx: click.Context) -> None:
    """Enter interactive REPL mode."""

    import code

    api: ManageTrackingApi = ctx.obj["api"]
    session: Session = ctx.obj["session"]
    console_locals = {
        "api": api,
        "session": session,
        "output": output,
        "json": lambda value: print(json.dumps(value, indent=2)),
    }
    banner = """
manage-tracking REPL
Available objects:
  api     - ManageTrackingApi instance
  session - Session instance
  output  - Print formatted output
  json    - Print as JSON
"""
    code.interact(banner=banner, local=console_locals)


def main() -> None:
    cli(obj={})


if __name__ == "__main__":
    main()

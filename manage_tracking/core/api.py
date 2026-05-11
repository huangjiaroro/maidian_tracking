"""Typed API wrapper for the manage-tracking CLI."""

from __future__ import annotations

from typing import Any, Optional

from .client import ApiClient, ApiError


class ManageTrackingApi:
    """API wrapper for manage-tracking endpoints."""

    API_PREFIX = "maidian"
    PROXY_SUFFIX = "/maidian/server"

    def __init__(self, client: ApiClient):
        self._client = client

    def _path(self, endpoint: str) -> str:
        if self._client.base_url.endswith(self.PROXY_SUFFIX):
            return endpoint.lstrip("/")
        return f"{self.API_PREFIX}/{endpoint.lstrip('/')}"

    def get_current_user(self) -> dict[str, Any]:
        return self._client.get(self._path("/auth/getuser"))

    def query_user(self, email: str) -> list[str]:
        result = self._client.get(self._path("/query"), params={"email": email})
        return result if isinstance(result, list) else []

    def get_app(self, id: int) -> dict[str, Any]:
        return self._client.get(self._path(f"/appInfo/{id}"))

    def list_apps(self, page: int = 1, size: int = 20, **kwargs: Any) -> dict[str, Any]:
        return self._client.get(self._path("/appInfo/page"), params={"page": page, "size": size, **kwargs})

    def create_app(self, app_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/appInfo"), data=app_data)

    def delete_app(self, id: int) -> dict[str, Any]:
        return self._client.delete(self._path(f"/appInfo/{id}"))

    def generate_app_key(self, id: int) -> dict[str, Any]:
        return self._client.get(self._path(f"/appInfo/createAppKey/{id}"))

    def get_page(self, id: int) -> dict[str, Any]:
        return self._client.get(self._path(f"/pageInfo/{id}"))

    def list_pages(
        self,
        app_id: Optional[int] = None,
        page: int = 1,
        size: int = 20,
        **kwargs: Any,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"page": page, "size": size}
        if app_id:
            params["appId"] = app_id
        params.update(kwargs)
        return self._client.get(self._path("/pageInfo/page"), params=params)

    def create_page(self, page_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/pageInfo"), data=page_data)

    def delete_page(self, id: int) -> dict[str, Any]:
        return self._client.delete(self._path(f"/pageInfo/{id}"))

    def get_page_directory(self, app_id: int) -> dict[str, Any]:
        return self._client.get(self._path("/pageInfo/page_dir"), params={"app_id": app_id})

    def list_functions(self, page: int = 1, size: int = 20, **kwargs: Any) -> dict[str, Any]:
        return self._client.get(self._path("/functionInfo/page"), params={"page": page, "size": size, **kwargs})

    def get_function(self, id: int) -> dict[str, Any]:
        return self._client.get(self._path("/functionInfo/page"), params={"id": id})

    def create_function(self, func_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/functionInfo"), data=func_data)

    def update_function(self, func_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/functionInfo"), data=func_data)

    def delete_function(self, id: int) -> dict[str, Any]:
        return self._client.delete(self._path(f"/functionInfo/{id}"))

    def list_controls(self, page: int = 1, size: int = 20, **kwargs: Any) -> dict[str, Any]:
        return self._client.get(self._path("/controlInfo/page"), params={"page": page, "size": size, **kwargs})

    def create_control(self, control_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/controlInfo"), data=control_data)

    def update_control(self, control_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/controlInfo"), data=control_data)

    def delete_control(self, id: int) -> dict[str, Any]:
        return self._client.delete(self._path(f"/controlInfo/{id}"))

    def list_tracks(self, page: int = 1, size: int = 20, **kwargs: Any) -> dict[str, Any]:
        return self._client.post(self._path("/trackInfo/page"), data={"page": page, "size": size, **kwargs})

    def get_track(self, id: int) -> dict[str, Any]:
        return self._client.get(self._path(f"/trackInfo/{id}"))

    def get_track_by_key(self, track_key: str) -> dict[str, Any]:
        return self._client.get(
            self._path("/trackInfo/getTrackInfoByTrackKey"),
            params={"trackKey": track_key},
        )

    def create_track(self, track_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/trackInfo"), data=track_data)

    def update_track(self, track_data: dict[str, Any]) -> dict[str, Any]:
        return self._client.post(self._path("/trackInfo"), data=track_data)

    def delete_track(self, id: int) -> dict[str, Any]:
        return self._client.delete(self._path(f"/trackInfo/{id}"))

    def search_tracks(self, track_key: str) -> list[dict[str, Any]]:
        result = self._client.get(
            self._path("/trackInfo/fuzzySearchTrackList"),
            params={"trackKey": track_key},
        )
        return result if isinstance(result, list) else []

    def get_all_tracks(self) -> list[dict[str, Any]]:
        result = self._client.get(self._path("/trackInfo/all"))
        return result if isinstance(result, list) else []

    def batch_copy_tracks(self, track_ids: list[int], target_app_id: int) -> dict[str, Any]:
        return self._client.post(
            self._path("/trackInfo/batchCopyTrackInfo"),
            data={"trackIds": track_ids, "targetAppId": target_app_id},
        )

    def list_track_fields(self, track_id: int) -> list[dict[str, Any]]:
        result = self._client.get(self._path("/trackField/list"), params={"trackId": track_id})
        return result if isinstance(result, list) else []

    def list_templates(self, page: int = 1, size: int = 20) -> dict[str, Any]:
        return self._client.get(self._path("/trackTemplate/page"), params={"page": page, "size": size})

    def get_template(self, id: int) -> dict[str, Any]:
        return self._client.get(self._path(f"/trackTemplate/{id}"))

    def list_businesses(self, page: int = 1, size: int = 20, **kwargs: Any) -> dict[str, Any]:
        return self._client.get(
            self._path("/businessProcess/page"),
            params={"page": page, "size": size, **kwargs},
        )

    def get_business_tree(self, app_id: int) -> dict[str, Any]:
        return self._client.get(self._path("/businessProcess/tree"), params={"appId": app_id})

    def list_operations(self, page: int = 1, size: int = 20, **kwargs: Any) -> dict[str, Any]:
        return self._client.get(self._path("/operation/page"), params={"page": page, "size": size, **kwargs})


def create_api(client: ApiClient) -> ManageTrackingApi:
    return ManageTrackingApi(client)

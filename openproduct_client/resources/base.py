from __future__ import annotations

import logging
from collections.abc import Mapping
from typing import TYPE_CHECKING

import msgspec
import requests

if TYPE_CHECKING:
    from ..clients import OpenProductClient


logger = logging.getLogger(__name__)


class BaseResource:
    http_client: OpenProductClient

    def __init__(self, http_client: OpenProductClient):
        self.http_client = http_client

    @staticmethod
    def process_response[T](
        response: requests.Response,
        struct_type: type[T],
    ) -> T:
        response_data = response.json()
        # for now: assume no errors :)
        return msgspec.convert(response_data, type=struct_type)

    def _get(
        self,
        path: str,
        headers: Mapping | None = None,
        params: msgspec.Struct | None = None,
    ) -> requests.Response:
        query_params = msgspec.to_builtins(params)
        response = self.http_client.request(
            "get", path, headers=headers, params=query_params
        )
        response.raise_for_status()
        return response

    def _post(
        self,
        path: str,
        headers: Mapping | None = None,
        params: msgspec.Struct | None = None,
        data: object = None,
    ) -> requests.Response:
        query_params = msgspec.to_builtins(params)
        response = self.http_client.request(
            "post",
            path,
            headers=headers,
            json=data,
            params=query_params,
        )
        response.raise_for_status()
        return response

    def _put(
        self,
        path: str,
        headers: Mapping | None = None,
        params: msgspec.Struct | None = None,
        data: object = None,
    ) -> requests.Response:
        query_params = msgspec.to_builtins(params)
        response = self.http_client.request(
            "put", path, headers=headers, json=data, params=query_params
        )
        response.raise_for_status()
        return response

    def _delete(
        self,
        path: str,
        headers: Mapping | None = None,
        params: msgspec.Struct | None = None,
    ) -> requests.Response:
        query_params = msgspec.to_builtins(params)
        response = self.http_client.request(
            "delete",
            path,
            headers=headers,
            params=query_params,
        )
        response.raise_for_status()
        return response

    def _patch(
        self,
        path: str,
        headers: Mapping | None = None,
        params: msgspec.Struct | None = None,
        data: object = None,
    ) -> requests.Response:
        query_params = msgspec.to_builtins(params)
        response = self.http_client.request(
            "patch",
            path,
            headers=headers,
            params=query_params,
            json=data,
        )
        response.raise_for_status()
        return response

    def _options(
        self,
        path: str,
        headers: Mapping | None = None,
        params: msgspec.Struct | None = None,
    ) -> requests.Response:
        query_params = msgspec.to_builtins(params)
        response = self.http_client.request(
            "delete",
            path,
            headers=headers,
            params=query_params,
        )
        response.raise_for_status()
        return response

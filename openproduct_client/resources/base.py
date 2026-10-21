from __future__ import annotations

import logging
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

import msgspec
import requests

from ..structs.base import BaseSchemaStruct, PaginatedResponseBody

if TYPE_CHECKING:
    from ..clients import OpenProductClient


logger = logging.getLogger(__name__)


class BaseResource[T: BaseSchemaStruct]:
    http_client: OpenProductClient

    def __init__(self, http_client: OpenProductClient):
        self.http_client = http_client

    @staticmethod
    def process_response(
        response: requests.Response,
        struct_type: type[T],
    ) -> T | PaginatedResponseBody[T] | Sequence[T]:
        response_data = response.json()

        if isinstance(response_data, list):
            return msgspec.convert(response_data, type=list[struct_type])

        return msgspec.json.decode(
            response.content,
            type=PaginatedResponseBody[struct_type]
            if "next" in response_data
            else struct_type,
        )

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

from __future__ import annotations

import logging
from collections.abc import Callable, Iterator, Mapping
from typing import TYPE_CHECKING, Concatenate, ParamSpec, Self, overload

import msgspec
import requests

from ..structs.base import BaseSchemaStruct, PaginatedResponseBody

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

    def _paginator[T: BaseSchemaStruct](
        self,
        paginated_data: PaginatedResponseBody[T],
        item_type: type[T],
        max_requests: int | None = None,
    ) -> Iterator[T]:
        page_type = PaginatedResponseBody[item_type]

        def row_iterator(
            _data: PaginatedResponseBody[T],
            # at least one request has been made to have a response body -> default 1
            num_requests=1,
        ) -> Iterator[T]:
            yield from _data.results

            if next_url := _data.next:
                if max_requests and num_requests >= max_requests:
                    logger.info(
                        "paginator_max_requests_reached",
                        extra={
                            "max_requests": max_requests,
                            "next_url": next_url,
                        },
                    )
                    return

                response = self.http_client.get(next_url)
                num_requests += 1
                response.raise_for_status()
                data = self.process_response(response, struct_type=page_type)
                yield from row_iterator(data, num_requests)

        return row_iterator(paginated_data)

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


P = ParamSpec("P")


class ListIter[T: BaseSchemaStruct, **P]:
    def __init__(
        self,
        resource: BaseResource,
        fetch_first: Callable[P, PaginatedResponseBody[T]],
        item_type: type[T],
        max_requests: int | None = None,
    ) -> None:
        self._resource = resource
        self._fetch_first = fetch_first
        self._item_type = item_type
        self._max_requests = max_requests

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> Iterator[T]:
        # Generator: the first request happens lazily, on first iteration.
        yield from self._resource._paginator(
            self._fetch_first(*args, **kwargs),
            item_type=self._item_type,
            max_requests=self._max_requests,
        )

    def limit(self, max_requests: int) -> ListIter[T, P]:
        return ListIter(
            self._resource, self._fetch_first, self._item_type, max_requests
        )


class make_list_iter[R: BaseResource, T: BaseSchemaStruct, **P]:
    def __init__(
        self,
        list_method: Callable[Concatenate[R, P], PaginatedResponseBody[T]],
        item_type: type[T],
    ):
        self.list_method = list_method
        self.item_type = item_type

    def __set_name__(self, owner: type[R], name: str):
        self._name = name

    @overload
    def __get__(self, resource: None, owner: type[R]) -> Self: ...

    @overload
    def __get__(self, resource: R, owner: type[R]) -> ListIter[T, P]: ...

    def __get__(self, resource: R | None, owner: type[R]) -> Self | ListIter[T, P]:
        # class attribute access
        if resource is None:
            return self

        def fetch_first(*args: P.args, **kwargs: P.kwargs) -> PaginatedResponseBody[T]:
            return self.list_method(resource, *args, **kwargs)

        return ListIter(resource, fetch_first, self.item_type)

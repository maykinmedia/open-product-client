import uuid
from collections.abc import Sequence
from typing import ClassVar

from ...structs.base import PaginatedResponseBody
from ...structs.product_type import (
    ContentParams,
    NestedContentElement,
    ProductType,
    ProductTypeCreateData,
    ProductTypeParams,
    ProductTypePartialUpdateData,
)
from ..base import BaseResource


class ProductTypeResource(BaseResource):
    base_path: ClassVar[str] = "producttypen"

    def list(
        self, *, params: ProductTypeParams | None = None
    ) -> PaginatedResponseBody[ProductType]:
        """
        Get all the available product types (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        return self.process_response(response, PaginatedResponseBody[ProductType])

    def retrieve(self, /, uuid: str | uuid.UUID) -> ProductType:
        """
        Get a specific product type based on its uuid.
        """
        response = self._get(f"{self.base_path}/{uuid!s}")
        return self.process_response(response, ProductType)

    def create(self, *, data: ProductTypeCreateData) -> ProductType:
        """
        Create a new product type.
        """
        response = self._post(self.base_path, data=data)
        return self.process_response(response, ProductType)

    def partial_update(
        self, /, uuid: str, *, data: ProductTypePartialUpdateData
    ) -> ProductType:
        """
        Partially update a specific product type.
        """
        response = self._patch(f"{self.base_path}/{uuid!s}", data=data)
        return self.process_response(response, ProductType)

    def delete(self, /, uuid: str):
        """
        Delete a specific product type.
        """
        return self._delete(f"{self.base_path}/{uuid!s}")

    def list_content(
        self, uuid: str | uuid.UUID, *, params: ContentParams | None = None
    ) -> Sequence[NestedContentElement]:
        """
        Get the content of a specific product type (based on query parameters).
        """
        response = self._get(f"{self.base_path}/{uuid!s}/content", params=params)
        return self.process_response(response, Sequence[NestedContentElement])

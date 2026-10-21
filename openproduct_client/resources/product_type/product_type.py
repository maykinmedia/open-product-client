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


class ProductTypeResource(BaseResource[ProductType]):
    base_path: ClassVar[str] = "producttypen"

    def list(
        self, *, params: ProductTypeParams | None = None
    ) -> PaginatedResponseBody[ProductType]:
        """
        Get all the available product types (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        result = self.process_response(response, ProductType)

        assert isinstance(result, PaginatedResponseBody)

        return result

    def retrieve(self, /, uuid: str | uuid.UUID) -> ProductType:
        """
        Get a specific product type based on its uuid.
        """
        response = self._get(f"{self.base_path}/{uuid!s}")
        result = self.process_response(response, ProductType)

        assert isinstance(result, ProductType)

        return result

    def create(self, *, data: ProductTypeCreateData) -> ProductType:
        """
        Create a new product type.
        """
        response = self._post(self.base_path, data=data)
        result = self.process_response(response, ProductType)

        assert isinstance(result, ProductType)

        return result

    def partial_update(
        self, /, uuid: str, *, data: ProductTypePartialUpdateData
    ) -> ProductType:
        """
        Partially update a specific product type.
        """
        response = self._patch(f"{self.base_path}/{uuid!s}", data=data)
        result = self.process_response(response, ProductType)

        assert isinstance(result, ProductType)

        return result

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

        # TODO
        # See if there is another way to get rid of the ignore type statement
        result = self.process_response(response, NestedContentElement)  # pyright: ignore[reportArgumentType]

        assert isinstance(result, Sequence)

        # TODO
        # See if there is another way to get rid of the ignore type statement
        return result  # pyright: ignore[reportReturnType]

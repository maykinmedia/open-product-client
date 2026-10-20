from typing import ClassVar

from ...structs.product_type import Price, PriceParams
from ...types.base_resources import PaginatedResponseBody
from ..base import BaseResource


class PriceResource(BaseResource[Price]):
    base_path: ClassVar[str] = "prijzen"

    def list(
        self, *, params: PriceParams | None = None
    ) -> PaginatedResponseBody[Price]:
        """
        Get all the available prices (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        result = self.process_response(response, Price)

        assert isinstance(result, PaginatedResponseBody)

        return result

from typing import ClassVar

from ...structs.base import PaginatedResponseBody
from ...structs.product_type import Price, PriceParams
from ..base import BaseResource


class PriceResource(BaseResource):
    base_path: ClassVar[str] = "prijzen"

    def list(
        self, *, params: PriceParams | None = None
    ) -> PaginatedResponseBody[Price]:
        """
        Get all the available prices (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        return self.process_response(response, PaginatedResponseBody[Price])

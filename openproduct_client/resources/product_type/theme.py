from typing import ClassVar

from ...structs.base import PaginatedResponseBody
from ...structs.product_type import (
    Theme,
    ThemeParams,
)
from ..base import BaseResource


class ThemeResource(BaseResource):
    base_path: ClassVar[str] = "producttypen/api/v1/themas"

    def list(
        self, *, params: ThemeParams | None = None
    ) -> PaginatedResponseBody[Theme]:
        """
        Get all the available themes (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        return self.process_response(response, PaginatedResponseBody[Theme])

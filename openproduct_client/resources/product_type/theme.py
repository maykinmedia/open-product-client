from typing import ClassVar

from ...structs.base import PaginatedResponseBody
from ...structs.product_type import (
    Theme,
    ThemeParams,
)
from ..base import BaseResource


class ThemeResource(BaseResource[Theme]):
    base_path: ClassVar[str] = "themas"

    def list(
        self, *, params: ThemeParams | None = None
    ) -> PaginatedResponseBody[Theme]:
        """
        Get all the available themes (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        result = self.process_response(response, Theme)

        assert isinstance(result, PaginatedResponseBody)

        return result

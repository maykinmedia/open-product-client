from typing import ClassVar

from ...structs.base import PaginatedResponseBody, PaginationParams
from ...structs.product_type import ContentLabel
from ..base import BaseResource


class ContentLabelResource(BaseResource):
    base_path: ClassVar[str] = "producttypen/api/v1/contentlabels"

    def list(
        self, *, params: PaginationParams | None = None
    ) -> PaginatedResponseBody[ContentLabel]:
        """
        Get all the available content labels (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        return self.process_response(response, PaginatedResponseBody[ContentLabel])

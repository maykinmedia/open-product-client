from typing import ClassVar

from ...structs.product_type import ContentLabel
from ...types.base_resources import PaginatedResponseBody, PaginationParams
from ..base import BaseResource


class ContentLabelResource(BaseResource[ContentLabel]):
    base_path: ClassVar[str] = "contentlabels"

    def list(
        self, *, params: PaginationParams | None = None
    ) -> PaginatedResponseBody[ContentLabel]:
        """
        Get all the available content labels (based on query parameters).
        """
        response = self._get(self.base_path, params=params)
        result = self.process_response(response, ContentLabel)

        assert isinstance(result, PaginatedResponseBody)

        return result

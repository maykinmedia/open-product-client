from collections.abc import MutableMapping
from typing import Literal

from ape_pie import APIClient
from ape_pie.typing import ConfigAdapter

from .resources.product_type import (
    ContentLabelResource,
    PriceResource,
    ProductTypeResource,
    ThemeResource,
)


class OpenProductClient(APIClient):
    product_type: ProductTypeResource
    theme: ThemeResource
    content_label: ContentLabelResource
    price: PriceResource

    def __init__(
        self,
        base_url: str,
        *,
        token: str = "",
        language_code: Literal["nl", "en"] = "nl",
        request_kwargs: MutableMapping[str, object] | None = None,
        **kwargs,
    ):
        if request_kwargs is None:
            request_kwargs = {}
        if "headers" not in request_kwargs:
            request_kwargs["headers"] = {}

        assert isinstance(request_kwargs["headers"], MutableMapping)

        if token:
            request_kwargs["headers"]["Authorization"] = f"Token {token}"

        request_kwargs["headers"]["Accept-Language"] = language_code

        super().__init__(base_url=base_url, request_kwargs=request_kwargs)  # pyright: ignore[reportArgumentType]

        self.theme = ThemeResource(self)
        self.content_label = ContentLabelResource(self)
        self.product_type = ProductTypeResource(self)
        self.price = PriceResource(self)

    @classmethod
    def configure_from(cls, adapter: ConfigAdapter, **kwargs):
        base_url = adapter.get_client_base_url()
        session_kwargs = adapter.get_client_session_kwargs()
        return cls(base_url, request_kwargs=session_kwargs, **kwargs)

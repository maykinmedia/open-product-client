import pytest

from openproduct_client.clients import OpenProductClient
from openproduct_client.structs.product_type import PriceParams


@pytest.mark.vcr
def test_list_prices(client: OpenProductClient):
    response = client.price.list()
    prices = response.results

    assert len(prices) == 2
    assert prices[0].uuid == "d71a7ff5-32e4-4bb8-8293-44728ba60933"
    assert prices[1].uuid == "55ed7060-0f46-4f04-9cb2-8dc494c83a92"


@pytest.mark.vcr
def test_list_prices_with_params(client: OpenProductClient):
    response = client.price.list(
        params=PriceParams(producttype__uuid="5d42a943-065a-46e7-8f17-54a5edbc88eb")
    )
    prices = response.results

    assert len(prices) == 1
    assert prices[0].uuid == "55ed7060-0f46-4f04-9cb2-8dc494c83a92"

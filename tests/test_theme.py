import pytest

from openproduct_client.clients import OpenProductClient
from openproduct_client.structs.product_type import ThemeParams


@pytest.mark.vcr
def test_list_themes(client: OpenProductClient):
    response = client.theme.list()
    themes = response.results

    assert len(themes) == 3
    assert themes[0].uuid == "619b8102-c476-4c38-af10-990990e6cf8f"
    assert themes[1].uuid == "ce3132cc-1c8f-4476-9ea6-1ff93e0ea9e4"
    assert themes[2].uuid == "cfac32d8-9ced-4b90-aa5c-46ea1cbfe04f"


@pytest.mark.vcr
def test_list_themes_with_params(client: OpenProductClient):
    response = client.theme.list(
        params=ThemeParams(producttypen__uuid="9903945d-b639-49da-85ed-7305817f47ad")
    )
    themes = response.results

    assert len(themes) == 1
    assert themes[0].uuid == "ce3132cc-1c8f-4476-9ea6-1ff93e0ea9e4"

import pytest

from openproduct_client.clients import OpenProductClient


@pytest.mark.vcr
def test_list_content_labels(client: OpenProductClient):
    response = client.content_label.list()
    content_labels = response.results

    assert len(content_labels) == 2
    assert content_labels[0].naam == "Voorwaarden"
    assert content_labels[1].naam == "Eisen"

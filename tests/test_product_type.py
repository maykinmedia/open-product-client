import msgspec
import pytest
import requests

from openproduct_client.clients import OpenProductClient
from openproduct_client.structs.product_type import (
    ContentParams,
    ProductTypeCreateData,
    ProductTypeParams,
    ProductTypePartialUpdateData,
)


@pytest.mark.vcr
def test_list_product_types(client: OpenProductClient):
    response = client.product_type.list()
    product_types = response.results

    assert len(product_types) == 2
    assert product_types[0].uuid == "5d42a943-065a-46e7-8f17-54a5edbc88eb"
    assert product_types[1].uuid == "9903945d-b639-49da-85ed-7305817f47ad"


@pytest.mark.vcr
def test_list_product_types_with_params(client: OpenProductClient):
    response = client.product_type.list(params=ProductTypeParams(code="PARKVER"))
    product_types = response.results

    assert len(product_types) == 1
    assert product_types[0].uuid == "9903945d-b639-49da-85ed-7305817f47ad"


@pytest.mark.vcr
def test_retrieve_product_type(client: OpenProductClient):
    product_type = client.product_type.retrieve("5d42a943-065a-46e7-8f17-54a5edbc88eb")

    assert product_type.uuid == "5d42a943-065a-46e7-8f17-54a5edbc88eb"


@pytest.mark.vcr
def test_create_product_type(client: OpenProductClient):
    data = ProductTypeCreateData(
        doelgroep="interne_organisatie",
        thema_uuids=["ce3132cc-1c8f-4476-9ea6-1ff93e0ea9e4"],
        naam="test-product-type",
        code="ACODE",
        samenvatting="test",
    )

    product_type = client.product_type.create(data=msgspec.to_builtins(data))

    assert product_type.uuid is not None
    assert product_type.doelgroep == "interne_organisatie"
    assert product_type.naam == "test-product-type"
    assert product_type.code == "ACODE"
    assert product_type.samenvatting == "test"
    assert product_type.themas[0].uuid == "ce3132cc-1c8f-4476-9ea6-1ff93e0ea9e4"


@pytest.mark.vcr
def test_partial_update_product_type(client: OpenProductClient):
    data = ProductTypePartialUpdateData(keywords=["akeyword"])

    product_type = client.product_type.partial_update(
        "5d42a943-065a-46e7-8f17-54a5edbc88eb", data=msgspec.to_builtins(data)
    )

    assert product_type.keywords == ["akeyword"]


@pytest.mark.vcr
def test_delete_product_type(client: OpenProductClient):
    # create a product type
    data = ProductTypeCreateData(
        doelgroep="interne_organisatie",
        thema_uuids=["ce3132cc-1c8f-4476-9ea6-1ff93e0ea9e4"],
        naam="product-type-to-delete",
        code="DELETE",
        samenvatting="test-delete",
    )

    created_product_type = client.product_type.create(data=msgspec.to_builtins(data))

    assert created_product_type.uuid is not None

    # delete the product type
    delete_response = client.product_type.delete(created_product_type.uuid)

    assert delete_response.status_code == 204

    # make sure it's deleted
    with pytest.raises(requests.exceptions.HTTPError):
        client.product_type.retrieve(created_product_type.uuid)


@pytest.mark.vcr
def test_list_content(client: OpenProductClient):
    # without params
    content = client.product_type.list_content("9903945d-b639-49da-85ed-7305817f47ad")

    assert len(content) == 2
    assert content[0].uuid == "a34f4e7c-026e-40eb-91a4-0540a6682519"
    assert content[0].labels == ["Eisen"]
    assert content[1].uuid == "017aa485-b56f-444b-a29f-39026edc3436"
    assert content[1].labels == ["Voorwaarden"]

    # with filtering on labels
    params = ContentParams(labels=["Voorwaarden"])
    content_with_params = client.product_type.list_content(
        "9903945d-b639-49da-85ed-7305817f47ad", params=params
    )

    assert len(content_with_params) == 1
    assert content_with_params[0].uuid == "017aa485-b56f-444b-a29f-39026edc3436"
    assert content_with_params[0].labels == ["Voorwaarden"]

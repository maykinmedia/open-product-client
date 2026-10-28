==========
Quickstart
==========

Installation
============

* Install from PyPI using ``uv``:

   .. code-block:: bash

      uv pip install open-product-client

Requirements
============

* API root URL where Open Product is running
* An API token for Open product with read/write permissions

Usage
=====

To use the client, instantiate it with the connection parameters and call the methods on
the provided resources:

.. code-block:: python

    from openproduct_client import OpenProductClient

    client = OpenProductClient(
        base_url="https://open-product.example.com",
        token="3955bbce-a9ba-48b9-9c76-fddc09e40ea9"
    )

    with client:
        product_types = client.list_product_types()
    
    print(product_types.results)
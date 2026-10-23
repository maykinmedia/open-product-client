Quickstart
==========

Installation
------------

**Requirements**

* Python 3.12 or newer

* Install from PyPI using ``uv``:

   .. code-block:: bash

      uv pip install open-product-client

.. note::

    This library has some dependencies, ``ape-pie`` and ``msgspec``.

**Dependencies**

- `ape-pie <https://ape-pie.readthedocs.io/en/latest/>`_
- `msgspec <https://msgspec.dev/>`_


Usage
-----

In your application you can create/build a client and this should be based on the 
``OpenProductClient`` class. Then you can access the desired resource and its method, 
which will return the results. The example below shows how we can retrieve and access a 
list of all the product_types:

.. code-block:: python

    from openproduct_client.clients import OpenProductClient

    class A(OpenProductClient):
        def list_product_types(self)-> PaginatedResponseBody[ProductType]:
            response = self.product_type.list()
            return response.results

    # a function that builds the client (based on A) is needed
    with build_client as client:
        product_types = client.list_product_types()
        uuids = [pt.uuid for pt in product_types]

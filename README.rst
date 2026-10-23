===================
Open Product Client
===================

:Version: 0.3.0
:Source: https://github.com/maykinmedia/open-product-client
:Keywords: Open Product API, Client, producten, producttypen

Currently compatible with Open Product 1.9.0

|build-status| |coverage| |python-versions| |pypi-version|

About
=====

A Python client library for interacting with the `Open Product API <https://github.com/maykinmedia/open-product>`_.

Introduction
============

The main goal of this library is to talk to ``producten`` and ``producttypen`` APIs via
the ``OpenProductClient`` and its resources. Using `msgspec <https://msgspec.dev/>`_
all the resources can be safe regarding their types while at the same time we can take 
advantage of the runtime validation in external data.

Requirements
============

* Python 3.12 or newer

Dependencies
============

* ape-pie
* msgspec

Installation
============

.. code-block:: bash

    uv pip install open-product-client


Usage
=====

In your application, you can build the client based on the ``OpenProductClient`` and then
access any resource and its methods. The return type will always be a ``msgspec.Struct``.
In order to get all the product types you have to do:

.. code-block:: python

    client.product_type.list()


See `Usage` in :doc:`Quickstart <quickstart>` for the complete guide.

Licence
=======

Licensed under the `MIT`_.

.. _`Maykin Media B.V.`: https://www.maykin.nl
.. _`MIT`: LICENSE
.. _`Open Product API`: https://github.com/maykinmedia/open-product

.. |build-status| image:: https://github.com/maykinmedia/open-product-client/actions/workflows/ci.yml/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/open-product-client/actions/workflows/ci.yml

.. |coverage| image:: https://codecov.io/gh/maykinmedia/open-product-client/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/open-product-client
    :alt: Coverage status

.. |python-versions| image:: https://img.shields.io/badge/python-3.12-blue.svg
    :alt: Supported Python versions

.. |pypi-version| image:: https://img.shields.io/pypi/v/open_product_client.svg
    :target: https://pypi.org/project/open-product-client/

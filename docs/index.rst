Welcome to Open Product Client's documentation!
===============================================

|build-status| |code-quality| |ruff| |coverage| |docs|

|python-versions| |pypi-version|

Open Product Client is a strongly typed HTTP client library for the `Open Product <https://github.com/maykinmedia/open-product>`_ 
API.

Features
========

* Resource-driven Python API, e.g. `client.product_type.list()`
* Fully type-annotated for type safety and editor autocomplete support
* Built on top of requests and `msgspec <https://msgspec.dev/>`_

.. toctree::
   :maxdepth: 2

   quickstart
   developers
   testing
   changelog


.. |build-status| image:: https://github.com/maykinmedia/open-product-client/actions/workflows/ci.yml/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/open-product-client/actions/workflows/ci.yml

.. |code-quality| image:: https://github.com/maykinmedia/open-product-client/actions/workflows/code-quality.yml/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/open-product-client/actions/workflows/code-quality.yml

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. |coverage| image:: https://codecov.io/gh/maykinmedia/open-product-client/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/open-product-client
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/open-product-client/badge/?version=latest
    :target: https://open-product-client.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/open-product-client.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/open-product-client.svg
    :target: https://pypi.org/project/open-product-client/

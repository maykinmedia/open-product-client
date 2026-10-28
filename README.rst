Welcome to Open Product Client's documentation
==============================================

:Version: 0.3.0
:Source: https://github.com/maykinmedia/open-product-client
:Keywords: Open Product API, Client, producten, producttypen

Currently compatible with Open Product 1.9.0

|build-status| |code-quality| |ruff| |coverage| |docs|

|python-versions| |pypi-version|

About
=====

A Python client library for interacting with the `Open Product API <https://github.com/maykinmedia/open-product>`_.

Introduction
============

Open Product Client is a strongly typed HTTP client library for the `Open Product <https://github.com/maykinmedia/open-product>`_ 
API. For installation and usage instructions, see the `documentation <https://open-product-client.readthedocs.io/en/latest/?badge=latest>`_.

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

.. |code-quality| image:: https://github.com/maykinmedia/open-product-client/workflows/Code quality checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/open-product-client/actions?query=workflow%3A%22Code+quality+checks%22

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

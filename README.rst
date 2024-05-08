========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |github-actions|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|

.. |github-actions| image:: https://github.com/ionelmc/python-su/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/python-su/actions

.. |version| image:: https://img.shields.io/pypi/v/pysu.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pysu

.. |wheel| image:: https://img.shields.io/pypi/wheel/pysu.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pysu

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pysu.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pysu

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pysu.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pysu

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-su/v1.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-su/compare/v1.0.1...master



.. end-badges

Simple Python-based setuid+setgid+setgroups+exec. A port of https://github.com/tianon/gosu

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pysu

You can also install the in-development version with::

    pip install https://github.com/ionelmc/python-su/archive/master.zip


Documentation
=============

Usage: pysu [-h] user[:group] command

Change user and exec command.

positional arguments:
  user
  command

optional arguments:
  -h, --help  show this help message and exit

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

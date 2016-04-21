========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |requires|
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-su/badge/?style=flat
    :target: https://readthedocs.org/projects/python-su
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-su.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-su

.. |requires| image:: https://requires.io/github/ionelmc/python-su/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-su/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pysu.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pysu

.. |downloads| image:: https://img.shields.io/pypi/dm/pysu.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pysu

.. |wheel| image:: https://img.shields.io/pypi/wheel/pysu.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pysu

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pysu.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pysu

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pysu.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pysu


.. end-badges

Simple Python-based setuid+setgid+setgroups+exec. A port of https://github.com/tianon/gosu

* Free software: BSD license

Installation
============

::

    pip install pysu

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

To run the all tests run::

    tox

###############################################################################
                     PYTHON TRAINING COURSE - EXAM BASICS
###############################################################################

This repository contains exam challenges for the first block of the curriculum.

.. todo: add link https://edu-python-corse.github.io/exam/basics.html

For developers
==============

This project implements :abbr:`TDD (Test-Driven Development)` approach.

Tests in this repository should be marked as ``expected failed`` for
the development environment. Use ``xfail`` marker to do this. The ``ENV``
environment variable should be set to ``dev`` to activate the developer's
mode.

.. code-block:: python

    import pytest

    def sum(x, y):
        """Return sum of two numbers"""

    # next test will be skipped in development environment
    # and it will fail in normal environment until function isn't implemented

    @pytest.mark.xfail(os.environ.get("ENV") == "dev",
                       reason="development environment")
    def test_something():
        assert sum(1, 2) == 3


.. code-block:: shell

    ENV=dev pytest


Challenge preparation
---------------------

#.  Create a dummy function in **src/exam** directory.
    Added documentation with usage examples.
    You type hinting to declare the function's signature.
#.  Create ``<module>_test.py`` in **tests** directory and write test cases.
    Fill free to adjust *conftest.py* in case you need some fixture data.

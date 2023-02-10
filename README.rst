###############################################################################
                     PYTHON TRAINING COURSE - EXAM BASICS
###############################################################################

This repository contains exam challenges for the first block of the curriculum.

.. todo: add link to exam document once is available
         https://edu-python-corse.github.io/exam/basics.html ???

For developers
==============

This project implements :abbr:`TDD (Test-Driven Development)` approach.

Tests in this repository should be marked as ``expected failed`` for
the development environment. Use ``xfail`` marker to do this.

.. code-block:: python

    import pytest

    def sum(x, y):
        """Return sum of two numbers"""

    # next test will be skipped in development environment
    # and it will fail in normal environment until function isn't implemented

    @pytest.mark.xfail(os.environ.get("DEV"), reason="development environment")
    def test_something():
        assert sum(1, 2) == 3

To mark environment as *development* just define ``DEV`` variable in it.
The value of this variables **doesn't** matter, the fact of its presence do.

.. code-block:: shell

    DEV=something pytest


Challenge preparation
---------------------

#.  Create a dummy function in **src/exam** directory.
    Added documentation with usage examples.
    You type hinting to declare the function's signature.
#.  Create ``function_test.py`` in **tests** directory and write test cases.
    Fill free to adjust *conftest.py* in case you need some fixture data.

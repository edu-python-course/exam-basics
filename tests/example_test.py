import pytest

from exam.example import example


@pytest.mark.example
def test_example():
    assert example("1", "2") == "3"

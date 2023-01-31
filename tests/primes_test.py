import os
import timeit

import pytest

from exam import primes


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="development environment")
def test_is_prime():
    assert primes.is_prime(10) is False
    assert primes.is_prime(1) is False
    assert primes.is_prime(2) is True
    assert primes.is_prime(3) is True
    assert primes.is_prime(547) is True


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="development environment")
@pytest.mark.dependency()
def test_get_primes(limit, primes_under_1k):
    assert primes.get_primes(limit) == primes_under_1k


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="development environment")
@pytest.mark.dependency(depends=["test_get_primes"])
def test_benchmark(limit, primes_under_1k):
    time_limit = 0.5
    setup = "from exam.primes import get_primes"
    stmt = "get_primes(1_000)"
    benchmark = timeit.timeit(stmt, setup, number=1_000)
    assert benchmark <= time_limit, \
        f"execution time exceeded time limit: {time_limit}"

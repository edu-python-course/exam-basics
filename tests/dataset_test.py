import os
import timeit

import pytest

from exam.dataset import filter_by_values


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
@pytest.mark.level_2
@pytest.mark.level_3
@pytest.mark.dependency()
def test_dataset_f1(dataset, filter_1):
    filtered, *keys = filter_1
    assert filter_by_values(dataset, keys) == filtered


@pytest.mark.level_3
@pytest.mark.dependency(depends=["test_dataset_f1"])
def test_dataset_f1_benchmark():
    time_limit = 0.5
    timeit_num = 3
    setup = "from exam.dataset import filter_by_values; " \
            "from tests.conftest import DATASET, KEYS_1"
    stmt = "filter_by_values(DATASET, KEYS_1)"
    benchmark = timeit.timeit(stmt, setup, number=timeit_num)
    assert benchmark <= time_limit, \
        f"execution time exceeded time limit: {time_limit}"


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
@pytest.mark.level_2
@pytest.mark.level_3
@pytest.mark.dependency()
def test_dataset_f2(dataset, filter_2):
    filtered, *keys = filter_2
    assert filter_by_values(dataset, keys) == filtered


@pytest.mark.level_3
@pytest.mark.dependency(depends=["test_dataset_f2"])
def test_dataset_f2_benchmark():
    time_limit = 0.5
    timeit_num = 3
    setup = "from exam.dataset import filter_by_values; " \
            "from tests.conftest import DATASET, KEYS_2"
    stmt = "filter_by_values(DATASET, KEYS_2)"
    benchmark = timeit.timeit(stmt, setup, number=timeit_num)
    assert benchmark <= time_limit, \
        f"execution time exceeded time limit: {time_limit}"

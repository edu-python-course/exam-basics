import csv
from pathlib import Path

import pytest


@pytest.fixture
def small_fixture():
    """Provide a brick wall structure and bricks count"""

    return [[1], [1], [1]]


@pytest.fixture
def small_fixture_count():
    return 3


@pytest.fixture
def regular_fixture():
    """Provide a brick wall structure and bricks count"""

    return [
        [5, 5, 3, 4, 1],
        [3, 2, 1, 4, 2, 1, 5],
        [2, 3, 1, 5, 5, 2],
        [3, 4, 3, 4, 3, 1],
        [5, 5, 3, 2, 3],
    ]


@pytest.fixture
def regular_fixture_count():
    return 29


@pytest.fixture
def position():
    return 5


@pytest.fixture()
def limit():
    return 1000


@pytest.fixture()
def primes_under_1k():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
            281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
            367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
            443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
            523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
            613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
            691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
            787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
            877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
            971, 977, 983, 991, 997]


def dict_from_csv(filepath):
    with open(filepath) as csv_file_handler:
        return [row for row in csv.DictReader(csv_file_handler)]


DATASET = dict_from_csv(
    Path(__file__).resolve().parent.joinpath("fixtures", "dataset.csv")
)


@pytest.fixture
def dataset():
    return DATASET


FILTER_1 = dict_from_csv(
    Path(__file__).resolve().parent.joinpath("fixtures", "filter_1.csv")
)
KEYS_1 = "city",


@pytest.fixture
def filter_1():
    return FILTER_1, *KEYS_1


FILTER_2 = dict_from_csv(
    Path(__file__).resolve().parent.joinpath("fixtures", "filter_2.csv")
)
KEYS_2 = "last_name", "city"


@pytest.fixture
def filter_2():
    return FILTER_2, *KEYS_2

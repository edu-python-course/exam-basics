import os

import pytest

from exam import brick_wall


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
def test_small_brick_counter(small_fixture):
    structure, number_of_bricks = small_fixture
    assert brick_wall.get_bricks_count(structure) == number_of_bricks


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
def test_brick_counter(regular_fixture):
    structure, number_of_bricks = regular_fixture
    assert brick_wall.get_bricks_count(regular_fixture) == number_of_bricks


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
def test_get_least_bricks_position(regular_fixture, position):
    assert brick_wall.get_least_bricks_position(regular_fixture) == position

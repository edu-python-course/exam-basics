import os

import pytest

from exam import brick_wall


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
@pytest.mark.level_1
def test_small_brick_counter(small_fixture, small_fixture_count):
    assert brick_wall.get_bricks_count(small_fixture) == small_fixture_count


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
@pytest.mark.level_1
def test_brick_counter(regular_fixture, regular_fixture_count):
    assert brick_wall.get_bricks_count(regular_fixture) == regular_fixture_count


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
@pytest.mark.level_2
@pytest.mark.dependency()
def test_get_least_bricks_position(regular_fixture, position):
    assert brick_wall.get_least_bricks_position(regular_fixture) == position


@pytest.mark.xfail(os.environ.get("ENV") == "dev",
                   reason="development environment")
@pytest.mark.level_2
@pytest.mark.dependency(depends=["test_get_least_bricks_position"])
def test_least_bricks(regular_fixture, small_fixture):
    assert brick_wall.get_least_bricks_count(regular_fixture) == 1
    assert brick_wall.get_least_bricks_count(small_fixture) == 3

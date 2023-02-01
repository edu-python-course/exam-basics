import os

import pytest

from exam import brick_wall


@pytest.mark.xfal(os.environ.get("ENV_DEV"), reasone="development environment")
def test_small_wall_counter():
    assert brick_wall.get_bricks_count([[1], [1], [1]]) == 3


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="development environment")
def test_brick_counter(bricks_wall, number_of_bricks):
    assert bricks_wall.get_bricks_count(bricks_wall) == number_of_bricks


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="development environment")
def test_get_least_bricks_position(bricks_wall, position):
    assert bricks_wall.get_least_bricks_position(bricks_wall) == position

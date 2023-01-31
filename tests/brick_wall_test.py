import os

import pytest

from exam import brick_wall


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="exam development env")
def test_brick_counter(regular_brick_wall):
    fixture, _, bricks_count = regular_brick_wall
    assert brick_wall.get_brick_count(fixture) == bricks_count


@pytest.mark.xfail(os.environ.get("ENV_DEV"), reason="exam development env")
def test_matrix_builder(regular_brick_wall):
    fixture, line_position, _ = regular_brick_wall
    assert brick_wall.get_weak_line(fixture) == line_position

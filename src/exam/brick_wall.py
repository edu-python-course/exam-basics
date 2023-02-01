"""
Brick wall challenge
====================

"""

import random
from typing import List


# noinspection PyUnusedLocal
def get_bricks_count(structure: List[list[int]]) -> int:
    """Return number of bricks in the wall structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: total number of bricks in the entire wall structure
    :rtype: int

    """


# noinspection PyUnusedLocal
def get_least_bricks_position(structure: List[List[int]]) -> int:
    """Return a pointer to the weakest line in the structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: the distance from the left edge to the weakest line location
    :rtype: int

    """


# noinspection PyUnusedLocal
def get_least_bricks_count(structure: List[List[int]]) -> int:
    """Return the least number of bricks in a line

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: the least number of bricks crossed by a vertical line
    :rtype: int

    """


def generate_wall(rows: int = 5, min_row_length: int = 15) -> List[List[int]]:
    """Generates a wall structure for a challenge

    :param rows: number of rows in a wall structure to generate.
        Defaults to 5.
    :param min_row_length: minimum desired length of a single row in a wall
        structure. Defaults to 15.
    :return: a generated wall structure

    """

    structure: List[List[int]] = []
    max_row_length: int = 0
    for row in range(rows):
        structure_row: List[int] = []
        structure_row_length: int = 0

        while structure_row_length < min_row_length:
            brick_length = random.randint(1, 5)
            structure_row.append(brick_length)
            structure_row_length += brick_length

        max_row_length = max(structure_row_length, max_row_length)
        structure.append(structure_row)

    # adjust rows length
    for structure_row in structure:
        structure_row_length = sum(structure_row)
        if structure_row_length < max_row_length:
            structure_row.append(max_row_length - structure_row_length)

    return structure

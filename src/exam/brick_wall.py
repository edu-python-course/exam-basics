"""
Brick wall challenge
====================

"""

from typing import List


# noinspection PyUnusedLocal
def get_bricks_count(structure: List[List[int]]) -> int:
    """Return number of bricks in the wall structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: total number of bricks in the entire wall structure
    :rtype: int

    The general algorithm is to walk through all collections of the given
    structure and to sum number of its elements.

    Usage example:

    >>> assert get_bricks_count([[1], [1], [1]]) == 3
    >>> assert get_bricks_count([[1, 1], [2], [1, 1]]) == 5
    >>> assert get_bricks_count([[6], [2, 2, 2], [3, 1, 1, 1], [2, 3, 1]]) == 11

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

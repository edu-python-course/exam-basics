"""
*******
Helpers
*******

Some helper functions were provided for this exam:

.. autofunction:: generate_wall

"""

import random
from typing import List


def generate_wall(rows: int = 5, min_row_length: int = 15) -> List[List[int]]:
    """Generates a wall structure for a challenge

    :param rows: number of rows in a wall structure to generate.
        Defaults to 5.
    :type rows: int
    :param min_row_length: minimum desired length of a single row in a wall
        structure. Defaults to 15.
    :type min_row_length: int

    :return: a generated wall structure
    :rtype: list[list[int]]

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

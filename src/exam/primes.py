"""
Prime Lookup Functions

"""

from typing import List


# noinspection PyUnusedLocal
def is_prime(number: int) -> bool:
    """Return prime check result for a specified number

    :param number: number to check
    :type number: int

    :return: prime check result
    :rtype: bool

    The result of this function is True if a number is prime, otherwise
    False.

    Usage examples:

    >>> assert not is_prime(0)
    >>> assert not is_prime(1)
    >>> assert is_prime(2)
    >>> assert is_prime(3)
    >>> assert not is_prime(4)
    >>> assert is_prime(5)

    """


# noinspection PyUnusedLocal
def get_primes(limit: int) -> List[int]:
    """Return a list of prime numbers within specified range

    :param limit: a range limit to look for prime numbers
    :type limit: int

    :return: the list of prime numbers within a specified range
    :rtype: list[int]

    Usage examples:

    >>> assert get_primes(10) == [2, 3, 5, 7]
    >>> assert get_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    """

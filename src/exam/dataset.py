"""
Datasets functions implementation

"""

from typing import Any, Dict, List, Optional


# noinspection PyUnusedLocal
def filter_by_values(origin: List[Dict[str, Any]],
                     keys: Optional[List[str]] = ...) -> List[Dict[str, Any]]:
    """Return a filtered dataset using unique values in given keys

    :param origin: origin dataset
    :type origin: list

    :param keys: a list of keys
    :type keys: list, optional

    :return: filtered dataset
    :rtype: list[dict]

    The original dataset is a list that contains dictionaries.
    All the dictionaries have the same keys of a string type.

    The function will filter the original dataset using values in a given
    set of keys. If some set of values has been seen before, the entire
    dictionary should be filtered (excluded from the result list).

    Example:

    >>> filter_by_values([{"x": 1, "y": "A"}, {"x": 1, "y":"AB"}], ["x"])
    [{"x": 1, "y": "A"}]
    >>> filter_by_values([{"x": 1, "y": "A"}, {"x": 1, "y":"AB"}], ["x", "y"])
    [{"x": 1, "y": "A"}, {"x": 2, "y": "AB"}]

    In case ``key`` parameter has been omitted, all the available keys are
    to be used to filter values.

    Example:

    >>> filter_by_values([{"x": 1, "y": "A"}, {"x": 1, "y":"AB"}])
    [{"x": 1, "y": "A"}, {"x": 2, "y": "AB"}]

    """

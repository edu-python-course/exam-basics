"""
Datasets functions implementation

"""

from typing import Any, Dict, List, Optional


# noinspection PyUnusedLocal
def filter_by_values(origin: List[Dict[str, Any]],
                     keys: Optional[List[str]] = ...) -> List[Dict[str, Any]]:
    """Return a filtered datasets by unique values in a given keys sets

    :param origin: an original dataset with entries to filter
    :type origin: list
    :param keys: a collection of keys to use for filtering
    :type keys: list, optional

    :return: a filtered dataset
    :rtype: list

    The origin dataset is a list of dictionaries. All the dictionaries have
    the same set of keys of a string type. At least one entry with at least
    one key is granted.

    The keys parameter is used to set the dictionary keys to filter unique
    values. Keys list is considered to be validated before passing to this
    function, all values (if any) are valid. In case this parameter is
    omitted - all available keys should be used.

    Usage:

    >>> ds = [{"x": 1, "y": 2, "z": 3}, {"x": 0, "y": 2, "z": 3}]
    >>> assert filter_by_values(ds, ["x"]) == ds       # the same as origin
    >>> assert filter_by_values(ds, ["x", "z"]) == ds  # the same as origin
    >>> assert filter_by_values(ds, ["y"]) == [{"x": 1, "y": 2, "z": 3}]
    >>> assert filter_by_values(ds, ["y", "z"]) == [{"x": 1, "y": 2, "z": 3}]

    """


#!/usr/bin/env python3

"""
Module with decorator for caching
results of some expensive operations
and function calls
"""

from functools import wraps
from typing import Callable


def cache(function: callable) -> Callable:
    """
    Cache expensive function's return values
    Args:
        function (Callable): function to cache return value
    """

    cached_items = {}

    @wraps(function)
    def wrapper(*args: list) -> object:
        """The wrapper function"""
        if args in cached_items.keys():
            return {"cached": cached_items[args]}

        return_value = function(*args)
        cached_items[args] = return_value

        return return_value

    return wrapper

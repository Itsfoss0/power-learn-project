#!/usr/bin/env python3


"""
Module to test out the functionality
of the repeat function decorator
And practice some decorator chaining too
"""


from decorators.repeat import repeat
from decorators.logging import function_logger
from decorators.caching import cache


@cache
@function_logger
@repeat(5)
def add(num_a, num_b):
    """Add num_a and num_b"""
    return (num_a + num_b)


if __name__ == "__main__":
    print(add(12, 14))
    print(add(12, 14))
